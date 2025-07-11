from bs4 import BeautifulSoup

with open(f"jee/{input('Enter your exam date:-')}april_shift_{input('Enter your shift:-')}.html") as f:
    htmlcontent = f.read()

soup = BeautifulSoup(htmlcontent, 'html.parser')

divs = soup.body.contents[1].find_all('div')
div = list(divs)[20]
all_td = div.find_all('td')

list =[]

for td in all_td:
    try:
        if type(int(td.span.string)) == int:
            list.append(td.span.string)
    except Exception as e:
        pass

question = list[0::2]

answer = list[1::2]
dict = dict(zip(question,answer))
