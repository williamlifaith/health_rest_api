from django.core.management.base import BaseCommand
from .config import *  # hide config info in separate module for safety measures
import psycopg2, csv

# a list to save error log
error_list = []


def error_log():
    with open('error_list.txt', 'a') as data:
        data.write(str(error_list))


# custom django-admin commands
class Command(BaseCommand):
    def handle(self, *args, **options):
        global conn # required in python
        try:
            conn = psycopg2.connect(host=host, dbname=dbname, user=user, password='',
                                    port='')
        except psycopg2.OperationalError as e:
            # print and write down the error
            error_list.append(e)
            error_log()
            print(e)
        else:
            print('DB Connected successfully!')

        cur = conn.cursor()

        """
       suppose the database is initially empty
       so before loading,'patient_id','patient_name' and 'type_name' should be inserted first
        """
        # insert value as parameters for safety measures
        sql1 = 'INSERT INTO patients_patient (patient_id, patient_name) VALUES '
        values1 = [(1, 'Jane'), (2, 'John')]
        sql1 += '(%s' + ',%s' * (len(values1) - 1) + ') ON CONFLICT DO NOTHING '

        sql2 = 'INSERT INTO patients_event_type (id, type_name) VALUES '
        values2 = [(1, 'HR'), (2, 'RR')]
        sql2 += '(%s' + ',%s' * (len(values2) - 1) + ') ON CONFLICT DO NOTHING'
        try:
            cur.executemany(sql1, values1)
            conn.commit()
            cur.executemany(sql2, values2)
            conn.commit()
        except psycopg2.OperationalError as e:
            # print and write down the error
            error_list.append(e)
            error_log()
            print(e)

        """
        use python csv module read csv file and use csv.DictReader convert file into dict,then insert db
        another option is using COPY        
        """

        with open(r'apps/patients/management/commands/events.csv') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',', quotechar=' ')
            for row in spamreader:
                try:
                    cur.execute(f"""INSERT INTO patients_event (patient_id, event_type_id , event_value ,event_unit, event_time) VALUES
                              ('{row['PATIENT ID']}','{row['EVENT TYPE']}','{row['EVENT VALUE']}',
                               '{row['EVENT UNIT']}','{row['EVENT TIME']}') ON CONFLICT DO NOTHING """)
                except psycopg2.OperationalError as e:
                    # always print and write down the error
                    error_list.append(e)
                    error_log()
                    print(e)
        conn.commit()
        conn.close()  # close the connection or it will make system slower
        print('CSV data loaded successfully!')
