from datetime import datetime

birthday = datetime(1971,6,28,11, 30)
birthday.year
birthday.weekday()
datetime.now()

datetime.now() - datetime(1946,4,2)
datetime(2023,5,2) - datetime(1971,6,28,11, 30)


parsed_date = datetime.strptime('31/01/22 23:59:59.999999','%d/%m/%y %H:%M:%S.%f')


parsed_date2 = datetime.strptime('31/01/22 23:59:59.999999','%d/%m/%y %H:%M:%S.%f')


date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
date_string
