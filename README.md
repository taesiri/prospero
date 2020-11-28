# Prospero

Prospero crawls `Engadget` and `Twitter` for posts related to `PS5` and show the results in a simple webpage.

## How it works

Prospero consists of different parts for doing various tasks. It uses `Selenium` and `Chrome Driver` for crawling `Engadget`. For `Twitter`, instead of using its official API, or using a similar technique for crawling `Engadget`, I opted to use `Twint`. `Twint` is one of the most advanced Twitter crawlers, yet lots of people don't know about it. Here are different libraries used in building Prospero:

1. [Selenium](https://selenium-python.readthedocs.io/)
1. [Twint](https://github.com/twintproject/twint)
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
1. [Word Cloud](https://github.com/amueller/word_cloud)
1. [Huggingface Transformers](https://github.com/huggingface/transformers)

## Project Structure

* [Crawlers](Crawlers/) - Contains code for Engadget and Twitter
* [Server](Server/) - Contains code for flask app
* [Analysis](Analysis/) - Contains code and notebook for Data Analysis
* [Images](Images/) - Contains images for `README.md` file

## Sentiment Analysis

Sentiment analysis is done with the Huggingface Transformers libraries, without any re-training, transfer learning, or fine-tuning. The results can be very wrong in some cases. Here are a plot showing the sentiment ratio for 100 randomly chosen tweets:

![Sentiment Analysis](Images/sent.png)

More information can be found in [this](Analysis/sentiment_analysis.ipynb) JupyterNotebook.

## How to Run

First modify [this line](https://github.com/taesiri/prospero/blob/main/Crawlers/Engadget/encrawler.py#L10) to the location of Chrome Web Driver.

* To Run Crawlers:

```bash
python twcrawler.py

# or

python encrawler.py
```

* To run the webserver, In Server directory, run the following code

```bash
flask run
```

## Requirements

All dependencies are listed in requirements.txt. You can use pip to install them as follows:

```bash
pip install -r requirements.txt
```

To install Twint, you have to run the following line:

```bash
pip install --user --upgrade "git+https://github.com/twintproject/twint.git@origin/master#egg=twint"
```

* All code tested with Python 3.6.9
