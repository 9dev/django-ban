from ._base import BaseTestCase

from datetime import datetime, timedelta, timezone
from selenium.webdriver.support.ui import Select

from django.conf import settings
from django.contrib.auth.models import User

from ban.models import Ban


class TestBan(BaseTestCase):

    def setUp(self):
        super(TestBan, self).setUp()
        self.harriet = User.objects.get(pk=1)
        self.florence = User.objects.get(pk=2)

    def test_can_ban_user_permanently(self):
        # Harriet logs in as an admin.
        self.login_as_admin()

        # She hits the admin panel for users.
        self.get('/admin/auth/user')

        # She bans user with pk=2 permanently.
        self.browser.find_element_by_css_selector('input.action-select[value="2"]').click()
        select = Select(self.browser.find_element_by_css_selector('select[name="action"]'))
        select.select_by_visible_text('Ban selected users permanently')
        self.browser.find_element_by_css_selector('button[name="index"]').click()

        # She goes to the admin panel for bans.
        self.get('/admin/ban/ban')

        # She sees a ban for this user with no end date.
        self.assertEqual(
            self.browser.find_element_by_class_name('row1').text,
            'test_user1 (None) admin',
        )

    def test_can_ban_user_for_month(self):
        self.fail()

    def test_can_ban_user_for_week(self):
        self.fail()

    def test_can_ban_user_for_day(self):
        self.fail()

    def test_can_warn_user(self):
        self.fail()

    def test_banned_user_cannot_log_in(self):
        # Florence was banned some time ago.
        Ban.objects.create(creator=self.harriet, receiver=self.florence)

        # She tries to log in.
        self.login_as_test_user()

        # She is redirected to the login page.
        self.assertEqual(self.browser.current_url, '{}{}'.format(self.live_server_url, settings.LOGIN_URL))

        # She sees a message that she was banned.
        self.assertIn('This account has been banned.', self.get_text())

    def test_banned_user_can_log_in_after_ban_period(self):
        # Florence was banned some time ago, but is active now.
        end_date = datetime.now(timezone.utc) - timedelta(days=1)
        Ban.objects.create(creator=self.harriet, receiver=self.florence, end_date=end_date)

        # She logs in.
        self.login_as_test_user()

        # She is redirected to the login redirect url.
        self.assertEqual(self.browser.current_url, '{}{}'.format(self.live_server_url, settings.LOGIN_REDIRECT_URL))

        # She doesn't see a message that she was banned.
        self.assertNotIn('This account has been banned.', self.get_text())

    def test_user_gets_banned_after_too_many_warnings(self):
        self.fail()

    def test_multiple_bans_merge_into_one(self):
        self.fail()
