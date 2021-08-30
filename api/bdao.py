import pymysql
from default import DEFAULT_DB_CONFIG

def get_bd_connection():
    connection_bd = pymysql.connect(**DEFAULT_DB_CONFIG)
    return connection_bd

    
def execute_query(query):
    connection_bd = get_bd_connection()
    cursor = connection_bd.cursor()
    sql_table_created = query
    cursor.execute(sql_table_created)
    connection_bd.commit()
    cursor.close()
    connection_bd.close()


def create_events_table():
    sql_table_created = """ 
        CREATE TABLE IF NOT EXISTS `event` (
  `id` varchar(250) NOT NULL,
  `evt_name` varchar(200) DEFAULT NULL,
  `evt_short_name` varchar(30) DEFAULT NULL,
  `evt_url` varchar(150) DEFAULT NULL,
  `evt_qr_code_location` varchar(250) DEFAULT NULL,
  `evt_doc_url` varchar(150) DEFAULT NULL,
  `evt_doc_qr_code_location` varchar(150) DEFAULT NULL,
  `evt_date_label` varchar(10) NOT NULL,
  `evt_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    """
    execute_query(sql_table_created)

def build_insert_event_query(event):
    sql_insert = """INSERT INTO event (id, evt_name, evt_short_name, 
    evt_url, evt_qr_code_location, evt_doc_url, evt_doc_qr_code_location,
     evt_date_label, evt_datetime) VALUES """ 
    sql_insert += """ ( "{}", "{}", "{}" , "{}" , "{}" , "{}" , "{}" , "{}", "{}")""".format(
        event['id'] ,
        event['evt_name'] ,
        event['evt_short_name'] , 
        event['evt_url'],
        event['evt_qr_code_location'] , 
        event['evt_doc_url'] , 
        event['evt_doc_qr_code_location'] , 
        event['evt_date_label'] , 
        event['evt_datetime'])
    return sql_insert

    
def insert_bulk_event(events):
    connection_bd = get_bd_connection()
    cursor = connection_bd.cursor()
    for event in events:
        sql_insert = build_insert_event_query(event)
        cursor.execute(sql_insert)
    connection_bd.commit()
    cursor.close()
    connection_bd.close()