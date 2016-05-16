title: "Converting a list to a string in python"
tags: [python, csv]
date: 2016-05-14
lastmod: 2016-05-14
description: "Convertin a list of strings to a single string in python"

Here I am converting a list of strings to a single string and placing a comma between each item in the new string.

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # convert list to string with removed []
    LIST = ['first', 'second', 'third', 'fourth']
    str_list = (", ".join(LIST))

This is the output:

    print str_list
    >> 'first, second, third, fourth
