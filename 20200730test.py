data_str = 'J0RB8BMRQU@gmail.com,4699\nLEKUUWH7QG@gmail.com,3443\nED61NHVAKH@gmail.com,2436\nBLNJKE6MOT@gmail.com,700\nWX79DJ3GBX@gmail.com,4585\n89RNWHB29T@gmail.com,3502\nDBSDKRY0M5@gmail.com,5704\n1VCSTNN5DT@gmail.com,8859\nQJ5GSY0Y7O@gmail.com,5676\n8LI30OUMNO@gmail.com,2375\nZWRZ4E4QN8@gmail.com,3783\n2R2001VJRH@gmail.com,5272\nXR4Q2992I2@gmail.com,6403\nQ7S1VG75BQ@gmail.com,5316\nIBSNP0S0KG@gmail.com,320\nVCBMQ40FNN@gmail.com,7738\nQSHRIT977Q@gmail.com,9183\n5JGZSS2QPB@gmail.com,8964\nRL0U9FCRT9@gmail.com,4093\nJI8F4EY4CA@gmail.com,184\n5XKR544N7Q@gmail.com,5858\nOI278Z7NYZ@gmail.com,8980\nD389NLF4BC@gmail.com,9378\nIVP4KUWQ7U@gmail.com,3759\n1ET6L0BAC9@gmail.com,6997\n0S4QQBJFDL@gmail.com,8143\nGXG5SM11ZX@gmail.com,2580\n7HN1DMLO5B@gmail.com,5483\n5YORL6N7NR@gmail.com,3619\n7PM5UTQP2R@gmail.com,6578'





















































































lines = data_str.split('\n')
times = [int(line.split(',')[1]) for line in lines]
formated_times = [f'{time//60}hrs {time%60}mins' for time in times]
mails = [line.split(',')[0] for line in lines]
accounts = [mail.split('@')[0] for mail in mails]
