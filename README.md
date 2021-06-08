**Meme Generator Project**\
Second project of the Intermediate Python Nanodegree, in which there
is a command line and web interface from which we can generate random memes 
with a given quote, author, and image. 

**Main Modules**\
QuoteEngine, MemeEngine

**Packages**\
Flask, pandas, python-docx, Pillow, requests, subprocess, PIL, ABC,
typing, os, argparse

**How to Run Program**
You can either run app.py on flask or from the terminal using a command 
a invoking python3 meme.py and then three other optional CLI arguments: 
* --body: string quote body
* --author: string quote author
* --path: path to image file

**Overview**\
This project is split up into many modules/directories, but the main ones are the QuoteEngine and MemeEngine
modules that handle parsing & extracting data from files and later using it to create memes, respectively. The _data directory
holds all the data for various parts of the project, e.g. the MemeEngine class make_meme method. The tmp directory is responsible for keeping temporary files
created. The static is for static files created (by app.py).

