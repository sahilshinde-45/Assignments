import csv






object = con_psql.poconn('localhost', 'student', 'postgres', 'Neosoft$22')

with open('laptop.csv', 'r') as temp_1_csv:
    csv_reader = csv.reader(temp_1_csv)

    with open('laptop.csv', 'w') as laptop_csv:
        # field = ['date','prodeuct','price','cardtype','location1','address2','loc2','loc4','datetime','monthtime','lon','lat']

        csv_writer = csv.writer(laptop_csv, delimiter='|')

        # csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

cur = object.createCursor()

with open('Student.csv', 'r') as student_csv:
    next(student_csv)
    cur.copy_from(student_csv, 'student_csv', sep='|')

    object.endConn()
import Con_psql

o
