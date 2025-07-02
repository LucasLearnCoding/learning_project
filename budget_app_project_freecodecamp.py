class Category:
    all_spending_categories = {}

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0.0

    def __str__(self): 
        title = self.category.center(30, '*') + '\n'
        content = ""
        for item in self.ledger:
            content += f'{item["description"][:23]:23}{item["amount"]:>7.2f}\n'
        total = f'Total: {self.get_balance():.2f}'
        return title + content + total

    def deposit(self, amount, description=''):
        self.balance += amount
        if amount == 0:
            self.ledger.append({'amount': amount, 'description': 'initial deposit'})
        else:
            self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            if self.category in __class__.all_spending_categories:
                __class__.all_spending_categories[self.category] += amount
            else:   
                __class__.all_spending_categories[self.category] = amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.balance -= amount
            category.balance += amount 
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {category.category}'})
            category.ledger.append({'amount': amount, 'description': f'Transfer from {self.category}'})
            if self.category in __class__.all_spending_categories:
                __class__.all_spending_categories[self.category] += amount
            else:   
                __class__.all_spending_categories[self.category] = amount
            return True
        return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    result = "Percentage spent by category\n"
    
    spending = []
    for cat in categories:
        spent = sum(item['amount'] for item in cat.ledger if item['amount'] < 0)
        spending.append(abs(spent))
    
    total = sum(spending)
    
    for i in range(0,11):
        percentage = (100 - i*10)
        result += f"{percentage:>3}| "
        for spent in spending:
            if total > 0:
                cat_percentage = ((spent / total) * 100)
                cat_percentage = (cat_percentage // 10) * 10
            else:
                cat_percentage = 0
            if cat_percentage >= percentage:
                result += "o  "
            else:
                result += "   "
        result += "\n"
    result += "    " + "-" + "---" * len(categories) + "\n"
    max_length = max(len(cat.category) for cat in categories)
    for i in range(max_length):
        result += "     "
        for cat in categories:
            if i < len(cat.category):
                result += cat.category[i] + "  "
            else:
                result += "   "
        result += "\n"
    result = result.rstrip("\n")
    
    return result

def main():
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    auto = Category("Auto")
    food.transfer(50, clothing)
    food.transfer(100, auto)
    clothing.withdraw(30.50, 't-shirt')
    auto.withdraw(70.30, "engine")

    print(food)
    print(create_spend_chart([food, clothing, auto]))
main()
