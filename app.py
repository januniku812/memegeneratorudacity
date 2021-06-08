import random
import os
import requests
from flask import Flask, render_template, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
app = Flask(__name__)

meme = MemeEngine('./tmp')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.append(Ingestor.Ingestor.parse(file))

    # image path
    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = imgs[random.randint(0, len(imgs))]
    quote = quotes[random.randint(0, len(quotes))]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    # using requests to save the image from the image_url
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    img = requests.get(image_url, True)
    # form param to a temp local file.
    img_file = f'tmp/{random.randint(0, 100000000)}.jpg'
    open(img_file, 'wb').write(img.content)
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    path = meme.make_meme(img_file, body, author)
    # 3. Remove the temporary saved image.
    os.remove(img_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=False)
