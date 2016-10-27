System Information
==================

These bash scripts gather system information and the python script parses it to HTML accessible output.

Author
------

- [TTJ](https://gitlab.com/u/ThomasTJ)
- License MIT

License
-------

* MIT

Credit
------

* Bash files origin from Linux Dash, (c) 2014 afaqurk (slightly modified)

Requirements
------------

Flask
Shlex
Python (only tested on python >= 3)

Installation
------------

- Clone folder with git

OR

- Copy content to folder (no specific name is required)

Use
---

The purpose of the software is to generate HTML output from system information to use on a HTML webpage. It's developed and tested on a Raspberry Pi 3.

1. Run the **app.py**
2. The python scripts executes the bash files in the **bash** folder and grabs the output
3. The python scripts formats the output to html
4. **app.py** then serves this data using flask

Features
--------

Please check out the folder **bash** to view the different system information scripts.

How to
------

Run: 
python app.py

Browse:
127.0.0.1:5003/system_info

Todo
----

* Remove HTML formatting from script and change output to list []. The HTML formatting should be done more generic in another function.

