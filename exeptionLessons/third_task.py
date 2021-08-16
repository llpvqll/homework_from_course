
class Employee:
    list_of_employee = [['Vlad', 'Palamarchuk', 'Ukraine', 2020], ['Vladislav', 'Sodolevski', 'Ukraine', 2019]]

    def employee(self):
        lst = []
        try:
            lst.append(str(input('Enter your name: ')))
            lst.append(str(input('Enter your second name: ')))
            lst.append(str(input('Enter your department (country): ')))
            lst.append(int(input('Enter your year hiring: ')))
            self.list_of_employee.append(lst)
            Employee().choose()
        except ValueError:
            print(f'You enter incorrect value, try again!')
            return Employee().employee()

    def filter(self):
        filtered = []
        try:
            year_hiring = int(input('Which year of employment to show: '))
            for item in self.list_of_employee:
                for i in item:
                    if i == year_hiring:
                        filtered.append(item)
            print(filtered)

        except ValueError:
            print('There is no such year of admission to work!')
            return Employee().filter()

    @staticmethod
    def choose():
        while True:
            try:
                action = int(input('For adding new employee enter 1, for find employee enter 2: '))
                if action == 1:
                    Employee().employee()
                elif action == 2:
                    Employee().filter()
                else:
                    return Employee().choose()
            except ValueError:
                print('You enter incorrect value, try again!')
                return Employee().choose()


Employee().choose()
