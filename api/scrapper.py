import requests
from bs4 import BeautifulSoup
from default import DEFAULT_SOURCES_LINKS

def scrap(output_format, output_directory):
    
    rq_response = requests.get(DEFAULT_SOURCES_LINKS['un']).text
    soup = BeautifulSoup(rq_response, 'lxml')
    print(soup.title.text)
    assert "List of International Days and Weeks" in soup.title.text
    events_elements = soup.find_all("div", class_='views-row')
    parse_events(events_elements)


def parse_events(events_elements):
    all_events = []
    for event in events_elements:
        event_obj = get_event_data(event)
        all_events.append(event_obj)


    
def get_event_data(event):
    link = event.find(class_="views-field-title").find("a")
    event_link_url = ""
    event_name = ""
    if(link):
        event_name = link.text
        event_link_url = link.get("href")
    
    link = event.find(class_="views-field-field-url")
    event_doc_link_url = ""
    if(link):
        link = link.find("a")
        event_doc_link_url = link.get("href") if link else ""
        
        
    event_date = event.find(class_="date-display-single")
    date = event_date["content"] if event_date else ""
    date_label = event_date.text if event_date else ""
    """
    print("----------------")
    print(event_name)
    print(event_link_url)
    print(event_doc_link_url)
    print(date_label)
    print("----------------")
    """
    return {'evt_name' : event_name, 'evt_url' : event_link_url, 'evt_doc_url' : event_doc_link_url, 'evt_date' : date, 'evt_date_label' : date_label, 'image_url' : ""}


