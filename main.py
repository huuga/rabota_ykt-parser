from bs4 import BeautifulSoup
import requests_cache
import fake_useragent

result = []
user = fake_useragent.UserAgent().random
page = 1
header = {
    'user-agent': user
}
url = 'https://rabota.ykt.ru/jobs?categoriesIds=2081'

session = requests_cache.CachedSession()
file = session.get(url, headers=header)
sp = BeautifulSoup(file.text, "lxml")

while sp.find("i", class_="yui-icon yui-icon-chevron-right"):
    page += 1
    jobs = sp.find_all("span", class_="r-vacancy_title")
    companies = sp.find_all("div", class_="r-vacancy_company")
    salary = sp.find_all("div", class_="r-vacancy_salary ng-binding")
    j = 0
    for i in range(1, len(companies), 2):
        print(jobs[j].text, end=' - ')
        print(salary[j].text.strip(), end=' - ')
        print(companies[i].find("a").text)
        print('----------------------')
        j += 1
    file = session.get(url + '&page=' + str(page), headers=header)
    sp = BeautifulSoup(file.text, "lxml")
