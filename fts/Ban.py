from ._base import BaseTestCase

from django.contrib.auth.models import User

from ban.models import Ban


class TestBan(BaseTestCase):

    def setUp(self):
        super(TestBan, self).setUp()
        self.harriet = User.objects.get(pk=1)
        self.florence = User.objects.get(pk=2)

    def test_can_ban_user_permanently(self):
        self.fail()

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
        # She is redirected to the homepage.
        # She sees a message that she was banned.
        self.fail()

    def test_banned_user_can_log_in_after_ban_period(self):
        self.fail()

    def test_user_gets_banned_after_too_many_warnings(self):
        self.fail()

    def test_multiple_bans_merge_into_one(self):
        self.fail()
