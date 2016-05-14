title: "For Loop or None"
tags: [for loop, python, sqlalchemy]
date: 2016-05-14
lastmod: 2016-05-14
description: "Handling when a variable is None instead of a list in a for loop in Python"

### `TypeError: 'NoneType' object is not iterable`

Have you ever received the error: `TypeError: 'NoneType' object is not iterable` when trying to iterate over a variable. Well that's because you're trying to iterate over a variable that is set to None instead of a list.

This is a solution I found when trying to loop over a variable that could either be a list of items or the variable could be set to None. It feels a lot more pythonic than having to check if the variable is a list before looping over it. This was specifically happing when getting back data from sqlalchemy queries. The query can either return a list of items it found in the database or it can return None if nothing is found.


This is an sqlalchemy query, it will either return a list of people with the first_name of 'Justin' or if there is no person with that first name it will return None. This is just an example of when a variable might be a list with list items or None.

    people = Person.query.filter_by(first_name='Justin').all()

I'm going to specifically set `people` to None here to show that `people` is actually None instead of having to look into what the above query actually returns.

    people = None

If `people` was a list that contained items, the print statements in the for loop would be called. Since `people` is set to None, nothing will be printed because the empty list in the 'or []' section is what gets evaluated.

    for person in people or []:
        print(person.first_name)
        print(person.last_name)



### Unlrelated comprehension equivalent but same concept

    result = [do_something(item) for item in a_list() or []]
