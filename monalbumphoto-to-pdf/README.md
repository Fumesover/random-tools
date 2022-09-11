Mon Album Photo to pdf
======================

Convert an album from monalbumphoto.fr to a pdf

# Setup

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# Usage

When sharing an album, you get the following URL : https://www.monalbumphoto.fr/voir-livre-en-ligne?widgetId=00000000-0000-0000-0000-000000000000

Take the uuid at the end of the url (`00000000-0000-0000-0000-000000000000`) and pass it as an argument to the script.

```bash
$ album-to-pdf.py 00000000-0000-0000-0000-000000000000
Generating 00000000-0000-0000-0000-000000000000.pdf ...
Fetching HPage_front.jpeg ...
[...]
Fetching HPage_back.jpeg ...
File 00000000-0000-0000-0000-000000000000.pdf created.
```
