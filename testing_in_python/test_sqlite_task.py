from sqlite_task import User, registry_new_user, sending_message_to_mail, finding_user
import unittest
import unittest.mock
from datetime import datetime


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.test_full_name = 'test1 test2 test3'
        self.test_birthday = '26 02 2002'
        self.year, self.months, self.day = self.test_birthday.split(' ')
        self.test_email = 'llpvo2602ll@gmail.com'
        self.user = User(
            self.test_full_name,
            self.test_birthday,
            self.test_email
        )

    def test_constructor(self):
        self.assertEqual(self.user.full_name, self.test_full_name)
        self.assertEqual(self.user.birthday, self.test_birthday)
        self.assertEqual(self.user.email, self.test_email)

    def test_get_full_name(self):
        expected_result = self.test_full_name
        full_name = self.user.get_full_name()
        self.assertIsInstance(full_name, str)
        self.assertEqual(full_name, expected_result)

    def test_get_short_name(self):
        test_short_name = 'test1 t.t.'
        short_name = self.user.get_short_name()
        self.assertEqual(short_name, test_short_name)

    def test_get_age(self):
        year, months, day = int(self.year), int(self.months), int(self.day)
        birthday = datetime(day, months, year)
        test_get_age = self.user.get_age()
        self.assertEqual(test_get_age, datetime.date(birthday))
        return datetime.date(birthday)

    def test_str__(self):
        test_str = self.test_full_name, self.test_get_age(), self.test_email
        main_str = self.user.__str__()
        self.assertEqual(test_str, main_str)

    @unittest.mock.patch('sqlite_task.registry_new_user')
    def test_registry_new_user(self, mocked_sum):
        self.assertFalse(mocked_sum.called)

    @unittest.mock.patch('sqlite_task.sending_message_to_mail')
    def test_sending_message_to_mail(self, mocked_sum):
        self.assertFalse(mocked_sum.called)

    def test_finding_user(self):
        result = ("['test1',", "'test2',", 'llpvo2602ll@gmail.com')
        called = finding_user()
        self.assertEqual(called, result)


