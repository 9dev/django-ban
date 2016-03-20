from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse


CHROMEDRIVER_PATH = '/usr/bin/chromedriver'


class BaseTestCase(StaticLiveServerTestCase):
    fixtures = ['base.json']

    def setUp(self):
        self.browser = webdriver.Chrome(CHROMEDRIVER_PATH)

    def tearDown(self):
        self.browser.close()

    def get(self, url=None, name=None, *args, **kwargs):
        if name:
            url = reverse(name, *args, **kwargs)
        self.browser.get('{}{}'.format(self.live_server_url, url))

