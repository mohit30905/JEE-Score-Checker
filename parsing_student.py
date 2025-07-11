from bs4 import BeautifulSoup

with open(f"jee/{input('Enter your name:-')}.html") as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
divs = soup.body.div.find_all('td')
td_list = []
for td in divs:
    try:
        tds = str(td.string)
        if tds != "None":
            td_list.append(tds)
    except Exception as e:
        pass
td_list = td_list[12:]
listoflists = []
ll2 = []
realdict = {}
i,k=18,0
j = 1
while j<=90:
    td_list2 = td_list[k:i]
    listoflists.append(td_list2)
    if 1 <= j <= 19:
        i, k = i + 18, k + 18
    elif j == 20 :
        i, k = i + 9, k + 18
    elif 21 <= j <= 29:
        i, k = i + 9, k + 9
        td_list2.insert(0,"ques no")
    elif j == 30:
        i, k = i + 18, k + 9
    elif 31 <= j <= 49:
        i, k = i + 18, k + 18
    elif j == 50 :
        i, k = i + 9, k + 18
    elif 51 <= j <= 59:
        i, k = i + 9, k + 9
        td_list2.insert(0, "ques no")
    elif j == 60:
        i, k = i + 18, k + 9
    elif 61 <= j <= 79:
        i, k = i + 18, k + 18
    elif j == 80:
        i, k = i + 9, k + 18
    elif 81 <= j <= 89:
        i, k = i + 9, k + 9
        td_list2.insert(0, "ques no")
    j = j + 1
for list in listoflists:
    if 'Answered' in list :
        ll2.append(list)
    elif 'Marked For Review' in list :
        ll2.append(list)

try:
    for lst in ll2:
        res_dct = {lst[i]: lst[i + 1] for i in range(0,len(lst),2)}
        if res_dct["Question Type :"] =="SA":
            realdict[res_dct['Question ID :']]=res_dct['Given Answer :']
        elif res_dct["Question Type :"] =="MCQ":
            realdict[res_dct['Question ID :']]= res_dct[f'Option {res_dct["Chosen Option :"]} ID :']
except Exception as e:
    print(e)