title: "Python's ftp library"
tags: [for loop, python, sqlalchemy]
date: 2016-05-14
lastmod: 2016-05-14
description: "Downloading a file using Python's built in ftp library"

I recently worked on a project where I needed to download a csv file from a remote ftp server periodically so I could use the file in the rest of the project. After doing some digging, I found out that python has a built in library to do some ftp operations. Here is a function I'm using to download a file using python's ftplib library.

    from ftplib import FTP

    def download_file_from_ftp_server(filename):
        """Download file from ftp server."""
        ftp = FTP()
        ftp.connect("websitename.com", 5000)
        ftp.login("username", "very_secure_password")
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        ftp.quit()
        localfile.close()

If the file is at the root of the webserver, then you can pass in the exact file name you want to grab. If the file is in another directory, you can pass in the directory structure to the file and the file name such as `reports/monday/logs.csv`.

This function connects and logs in to the ftp server, reads the file on the server and writes it to the local file system. It also handles closing the ftp connection and the local file after it has been created.
