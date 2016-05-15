title: "Reading data from a csv file in python"
tags: [python, csv]
date: 2016-05-14
lastmod: 2016-05-14
description: "Reading data from a csv file in python"

This is a common function that I use in my code when reading in data from a csv file with python.

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import csv

    def get_contacts_from_csv(directory):
        contacts = []
        if directory:
            csv_location = directory + '/contacts.csv'
        else:
            csv_location = 'contacts.csv'

        with open(csv_location, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                contacts.append([row[0], row[1], row[2], row[3].lower()])
        # remove header row if it exists.
        if contacts[0][0] == 'user_login':
            del contacts[0]
        return contacts

    if __name__ == "__main__":
        contacts_from_csv = get_staff_from_csv('home/juzten')

This works really well, I can even update the function to take in a file name if I had the need to read multiple files. In line 19 I'm checking if the first row is a header by checking if the first item is the contacts list is equal to what would normally be in the first row and column of the csv file, in this case it would be 'user_login' so I'm deleting that item in the contacts list. I could also skip the first row while reading in the csv but in this case I did not do that.

On line 17 I'm specifically adding the first 4 rows to a list. I'm also converting the 4th row to lowercase. Just for reference this is what the data from this csv would look like:

    [
        ['Homer', 'Simpson', 'male', '35'],
        ['Bart' , 'Simpson', 'male', '12']
    ]
