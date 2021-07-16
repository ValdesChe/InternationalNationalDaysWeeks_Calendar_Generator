import requests
from bs4 import BeautifulSoup
from requests.sessions import default_hooks
from default import DEFAULT_SOURCES_LINKS, DEFAULT_OUTPUT_COLOR, DEFAULT_OUTPUT_DIR
import qrcode
import uuid
import os

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
    event_link_url = event_name = evt_qr_code_url = ""
    if(link):
        event_name = link.text
        event_link_url = link.get("href")
        evt_qr_code_url = generate_qr_code(event_link_url)

    link = event.find(class_="views-field-field-url")
    doc_qr_code_url = ""
    event_doc_link_url = ""
    if(link):
        link = link.find("a")
        event_doc_link_url = link.get("href") if link else ""
        doc_qr_code_url = generate_qr_code(event_doc_link_url, True)
    
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
    return {'evt_name' : event_name, 'evt_url' : event_link_url, 'evt_doc_url' : event_doc_link_url, 'evt_date' : date, 'evt_date_label' : date_label, 'evt_qr_url' : evt_qr_code_url, 'evt_doc_qr_url' : doc_qr_code_url}



def generate_qr_code(url, is_doc = False):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    fill_color = DEFAULT_OUTPUT_COLOR["evt_doc"] if is_doc else DEFAULT_OUTPUT_COLOR["evt_link"]
    img = qr.make_image(**fill_color)
    if not os.path.exists(DEFAULT_OUTPUT_DIR):
        os.mkdir(DEFAULT_OUTPUT_DIR, 0o666)
    output_name = DEFAULT_OUTPUT_DIR + str(uuid.uuid4()) +'.png'
    img.save(output_name)