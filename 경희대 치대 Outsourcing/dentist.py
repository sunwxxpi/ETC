import pandas as pd

test_csv = pd.read_csv("./경희대_치대_Outsourcing/dentist.csv", encoding='cp949')
df = pd.DataFrame(test_csv)
df.index = df.index + 1

file = open("./경희대_치대_Outsourcing/dentist.txt", 'rt', encoding='UTF8')
lines = file.readlines()

name_dict = {} # {'name': 'info'}

with open("./경희대_치대_Outsourcing/text.txt", 'w', encoding='UTF-8') as f:
    for name in df['Name']:
        info_dict = {} # {'info': 'win_or_not'}
        
        for line_num, line in enumerate(lines):
            if name in line:
                info_dict[(lines[line_num - 3]).split('<td>')[1].replace('</td>\n', '')] = lines[line_num + 1].split('>')[1].replace('</td', '')
                    
        name_dict[name] = info_dict
                
        f.write(name + '\n')
        for i in name_dict[name]:
            f.write(str(i) + ' : ' + str(name_dict[name][i]) + '\n')
        f.write('\n')
        
print(name_dict['최민석'])
    
for name, num1 in zip(df['Name'], df['num1']):
    if num1 == '1 회':
        if '4월 4주차 치주수술 주말1차' in list(name_dict[name].keys()) and '4월 4주차 치주수술 주말2차' in list(name_dict[name].keys()) and '취소' not in list(name_dict[name].values()):
            # print(f'{name} 통과')
            pass
        else:
            print(f'{name} 오류')
    elif num1 == '2 회':
        if '4월 4주차 치주수술 주말1차' not in list(name_dict[name].keys()) and '4월 4주차 치주수술 주말2차' not in list(name_dict[name].keys()) and '4월 4주차 치주수술 주말3차' not in list(name_dict[name].keys()) and '취소' not in list(name_dict[name].values()):
            # print(f'{name} 통과')
            pass
        else:
            print(f'{name} 오류')
    else:
        print("Need Code Debug")
        
print('--------------------')
        
for name, num2 in zip(df['Name'], df['num2']):
    if num2 == '0 회':
        if '4월 4주차 소아치과 교수님 TAS 주말1차' in list(name_dict[name].keys()) and '4월 4주차 소아치과 교수님 TAS 주말2차' in list(name_dict[name].keys()) and '취소' not in list(name_dict[name].values()):
            # print(f'{name} 통과')
            pass
        else:
            print(f'{name} 오류')
    elif num2 == '1 회':
        if '4월 4주차 소아치과 교수님 TAS 주말1차' not in list(name_dict[name].keys()) and '4월 4주차 소아치과 교수님 TAS 주말2차' not in list(name_dict[name].keys()) and '취소' not in list(name_dict[name].values()):
            # print(f'{name} 통과')
            pass
        else:
            print(f'{name} 오류')
    else:
        print("Need Code Debug")