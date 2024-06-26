from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask(__name__) # flask application initialize

db = {}

@app.route("/") # decorator, routing
def home(): # decorating home() function
    return render_template('home.html') # render with variable 'name'

@app.route("/search")
def search():
    keyword = request.args.get('keyword')
    if keyword == None:
        return redirect("/")
    
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
        
    return render_template('search.html', keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get('keyword')
    if keyword == None:
        return redirect("/")
    
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run(port=5000, debug=True)