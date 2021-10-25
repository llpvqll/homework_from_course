import unittest
import unittest.mock


def average(lst):
    if len(lst) == 0:
        raise ValueError('List is empty!')
    return sum(lst) / len(lst)


def removing_x_from_list(lst: list, x):
    new_lst = []
    for item in lst:
        if item == x:
            continue
        elif item != x:
            new_lst.append(item)
    return new_lst


def creating_user_function(first_name, last_name, birthday):
    user_list = [first_name, last_name, birthday]
    writing_to_console(user_list)


def writing_to_console(user_list):
    print('Creating user...')
    print(f'User {user_list} created successfully!')


class UserTestCase(unittest.TestCase):
    def test_average(self):
        lis = [1, 2, 3, 4, 5, 6, 7]
        result = average(lis)
        self.assertTrue(result, sum(lis) / len(lis))

    def test_removing_x_from_list(self):
        lst = [1, 2, 2, 3, 4, 5, 6]
        value = 2
        result = removing_x_from_list(lst, value)
        new_list = [1, 3, 4, 5, 6]
        self.assertTrue(result, result == new_list)

    @unittest.mock.patch('addition_task.writing_to_console')
    def test_creating_user_function(self, mocked_sum):
        name = 'Vlad'
        last_name = 'Palamarchuk'
        birthday = 26022002
        creating_user_function(name, last_name, birthday)
        self.assertTrue(mocked_sum.called)


# # call average function
# print(average([1, 2, 3, 4, 5]))
# # call removing from list function
# print(removing_x_from_list([1, 2, 2, 3, 4, 5, 6], 2))
# # call creating user function
# creating_user_function('Vlad', 'Palamarchuk', 26022002)


