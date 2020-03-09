from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client


def get_github_projects():
    list = []
    url = "https://github.com/NMan1?tab=repositories"
    desc = []
    name = []
    giturl = []

    uClient = uReq(url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    for container in page_soup.find_all("li", {"class": "col-12 d-flex width-full py-4 border-bottom public source"}):
        name_html = container.find("h3", attrs={"class": "wb-break-all"})
        desc_html = container.find("p", attrs={"class": "col-9 d-inline-block text-gray mb-2 pr-4"})
        url_html = container.div.div.h3.a["href"]

        if desc_html is not None:
            desc.append(desc_html.text.strip())
        else:
            desc.append("none")

        if name_html is not None:
            name.append(name_html.text.strip())
        else:
            name.append("none")

        if url_html is not None:
            giturl.append(url_html)
        else:
            giturl.append("none")

    for i in range(len(name)):
        dict = {'title': '', 'description': '', 'link': ''}
        dict['title'] = name[i].replace(",", " |")
        dict['description'] = desc[i]
        dict['link'] = giturl[i]

        list.append(dict)

    return list
