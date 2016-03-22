from ._base import BaseTestCase

from datetime import datetime, timedelta, timezone
import dateutil.parser

from django.conf import settings
from django.contrib.auth.models import User

from ban.models import Ban


class TestBan(BaseTestCase):

    def setUp(self):
        super(TestBan, self).setUp()
        self.harriet = User.objects.get(pk=1)
        self.florence = User.objects.get(pk=2)

    def assert_can_ban_user_for_period(self, period_name, period_length):
        # Harriet logs in as an admin.
        self.login_as_admin()

        # She hits the admin panel for users.
        self.get('/admin/auth/user')

        # She bans user with pk=2 for requested period of time.
        self.select_admin_object(2)
        self.admin_action('Ban selected users for {}'.format(period_name))

        # She goes to the admin panel for bans.
        self.get('/admin/ban/ban')

        # She sees a ban for this user ending after specified period.
        row = self.browser.find_element_by_class_name('row1').text
        found_end_text = row.replace('test_user1', '').replace('admin', '')
        found_end_ts = dateutil.parser.parse(found_end_text).replace(tzinfo=timezone.utc).timestamp()
        expected_end_ts = (datetime.now(timezone.utc) + timedelta(days=period_length)).timestamp()

        self.assertTrue(row.startswith('test_user1'))
        self.assertTrue(row.endswith('admin'))
        self.assertAlmostEqual(expected_end_ts, found_end_ts, delta=60)

    def test_can_ban_user_permanently(self):
        # Harriet logs in as an admin.
        self.login_as_admin()

        # She hits the admin panel for users.
        self.get('/admin/auth/user')

        # She bans user with pk=2 permanently.
        self.select_admin_object(2)
        self.admin_action('Ban selected users permanently')

        # She goes to the admin panel for bans.
        self.get('/admin/ban/ban')

        # She sees a ban for this user with no end date.
        self.assertEqual(
            self.browser.find_element_by_class_name('row1').text,
            'test_user1 (None) admin',
        )

    def test_can_ban_user_for_month(self):
        self.assert_can_ban_user_for_period('month', 30)

    def test_can_ban_user_for_week(self):
        self.assert_can_ban_user_for_period('week', 7)

    def test_can_ban_user_for_day(self):
        self.assert_can_ban_user_for_period('day', 1)

    def test_can_warn_user(self):
        # Harriet logs in as an admin.
        self.login_as_admin()

        # She hits the admin panel for users.
        self.get('/admin/auth/user')

        # She warns Florence.
        self.select_admin_object(self.florence.pk)
        self.admin_action('Warn selected users')

        # She goes to the admin panel for warns.
        self.get('/admin/ban/warn')

        # She sees a warn for Florence.
        self.assertEqual(
            self.browser.find_element_by_class_name('row1').text,
            'test_user1 admin',
        )

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
        # Florence was banned some time ago.
        end_date = datetime.now(timezone.utc) + timedelta(days=1)
        Ban.objects.create(creator=self.harriet, receiver=self.florence, end_date=end_date)

        # Harriet logs in as an admin.
        self.login_as_admin()

        # She hits the admin panel for users.
        self.get('/admin/auth/user')

        # She bans Florence permanently.
        self.select_admin_object(self.florence.pk)
        self.admin_action('Ban selected users permanently')

        # She goes to the admin panel for bans.
        self.get('/admin/ban/ban')

        # She sees a permanent ban for Florence with no end date.
        self.assertEqual(
            self.browser.find_element_by_class_name('row1').text,
            'test_user1 (None) admin',
        )

        # She does not see any other bans for Florence as they were merged into one.
        self.assertIn('1 ban', self.get_text())
