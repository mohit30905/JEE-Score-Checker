import requests
url = "https://cdn3.digialm.com//per/g28/pub/2083/touchstone/AssessmentQPHTMLMode1//2083O2353/2083O2353S1D12997/16815367317841340/DL01034196_2083O2353S1D12997E1.html"
r = requests.get(url).content
print(r)
with open("jee/janardhan.html", "wb") as f:
    f.write(r)