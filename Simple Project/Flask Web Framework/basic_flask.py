from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# saved in DB actually
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

@app.route('/')
def index():
    li_tags = ''
    for topic in topics:
        li_tags = li_tags + f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
        
    return f'''
    <!DOCTYPE html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {li_tags}
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''
            
    """ return render_template(
        'home.html', 
        topic_0_id = topics[0]['id'],
        topic_0_title = topics[0]['title'],
        topic_1_id = topics[1]['id'],
        topic_1_title = topics[1]['title'],
        topic_2_id = topics[2]['id'],
        topic_2_title = topics[2]['title'],
    ) """

@app.route('/create')
def create():
    return 'Create'

@app.route('/read/<id>')
def read(id):

    return f'Read {id}'


app.run(port=5001, debug=True) # flask default port=5000