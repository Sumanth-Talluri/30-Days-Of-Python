class Statistics:

    def __init__(self, lst):
        self.lst = lst

    def count(self):
        return len(self.lst)

    def sum(self):
        total = 0
        for item in self.lst:
            total += item
        return total

    def min(self):
        minn = self.lst[0]
        for item in self.lst:
            if item < minn:
                minn = item
        return minn

    def max(self):
        maxx = None
        for item in self.lst:
            if item > maxx:
                maxx = item
        return maxx

    def range(self):
        minn = self.min()
        maxx = self.max()
        return maxx-minn

    def mean(self):
        val = float(self.sum()) / self.count()
        return val

    def median(self):
        new_lst = self.lst
        new_lst.sort()
        length = self.count()
        if length % 2 == 0:
            output = [new_lst[(length/2)-1], new_lst[length/2]]
        else:
            output = [new_lst[length//2]]
        return output

    def mode(self):
        count_dic = {}
        for item in self.lst:
            if item not in count_dic:
                count_dic[item] = 1
            else:
                count_dic[item] += 1
        output = []
        for k, v in count_dic.items():
            tup = (k, v)
            output.append(tup)
        output.sort(key=lambda x: x[1], reverse=True)
        res = {}
        res['mode'] = output[0][0]
        res['count'] = output[0][1]
        return res

    def var(self):
        avg = self.mean()
        n = self.count()
        sq_diff_lst = []
        for item in self.lst:
            diff = item - avg
            sq_diff_lst.append(diff**2)
        total = 0
        for item in sq_diff_lst:
            total += item
        var = float(total)/n
        return var

    def std(self):
        avg = self.mean()
        n = self.count()
        sq_diff_lst = []
        for item in self.lst:
            diff = item - avg
            sq_diff_lst.append(diff**2)
        total = 0
        for item in sq_diff_lst:
            total += item
        var = total/n
        sd = var**0.5
        return sd

    def freq_dist(self):
        count_dic = {}
        for item in self.lst:
            if item not in count_dic:
                count_dic[item] = 1
            else:
                count_dic[item] += 1
        output = []
        for k, v in count_dic.items():
            tup = (k, v)
            output.append(tup)
        output.sort(key=lambda x: x[1], reverse=True)
        return output

    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Variance: ', self.var())
        print('Standard Deviation: ', self.std())
        print('Frequency Distribution: ', self.freq_dist())


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
data.describe()


class PersonalAccount:

    def __init__(self, fname, lname, incomes, expenses, properties):
        self.fname = fname
        self.lname = lname
        self.incomes = incomes
        self.expenses = expenses
        self.properties = properties

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income[0]
        return total

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense[0]
        return total

    def account_info(self):
        print("Firstname:", self.fname)
        print("Lastname:", self.lname)
        print("Income:", self.incomes)
        print("Expenses:", self.expenses)
        print("Properties:", self.properties)

    def add_income(self, income, desc):
        self.incomes.append((income, desc))
        return self.incomes

    def add_expense(self, expense, desc):
        self.expenses.append((expense, desc))
        return self.expenses

    def account_balance(self):
        bal = self.total_income() - self.total_expense()
        return bal


ram = PersonalAccount("Ram", "Binod", [(10000, 'salary'), (5000, 'pension')], [
                      (1000, 'Rent'), (1000, 'Food'), (800, 'Clothes')], "No Properties")
ram.account_info()
print("Account Balance:", ram.account_balance())
