import unittest
from app.models import Article
# from models import article
# Article = article.Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Source Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("BBC News","Theranos founder hit with criminal charges","Elizabeth Holmes is charged with fraud over claims made for blood tests her company developed.", "http://www.bbc.co.uk/news/business-44501631","https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/_102072553_holmes.jpg","2018-06-15T22:25:40Z")
        self.new_article = Article("Adrian Chiles","The secret of happiness? Be more like Ted Lasso | Adrian Chiles","I love the comedy show about a goodhearted football manager so much I decided to emulate him. Then Private Eye, the satirical news magazine, took a swipe at me Ted Lasso has changed my life. It’s a comedy series on Apple TV+ about a coach of an American footb…", "https://amp.theguardian.com/commentisfree/2021/aug/12/the-secret-of-happiness-be-more-like-ted-lasso", "shorturl.at/blFNP", "2021-08-12T06:00:10Z")
    def test_instance(self):
        '''
        test case to test if object instance is created
        '''
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        Test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_article.author,"Adrian Chiles")
        self.assertEqual(self.new_article.title,"The secret of happiness? Be more like Ted Lasso | Adrian Chiles")
        self.assertEqual(self.new_article.description,"I love the comedy show about a goodhearted football manager so much I decided to emulate him. Then Private Eye, the satirical news magazine, took a swipe at me Ted Lasso has changed my life. It’s a comedy series on Apple TV+ about a coach of an American footb…")
        self.assertEqual(self.new_article.url,"https://amp.theguardian.com/commentisfree/2021/aug/12/the-secret-of-happiness-be-more-like-ted-lasso")
        self.assertEqual(self.new_article.urlToImage,"shorturl.at/el145")
        self.assertEqual(self.new_article.publishedAt,"2018-06-15T22:25:40Z")
