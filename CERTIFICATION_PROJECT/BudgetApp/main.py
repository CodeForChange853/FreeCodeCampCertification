class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            lines.append(f"{desc}{amt}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    spendings = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spendings.append(spent)

    total_spent = sum(spendings)
    if total_spent == 0:
        percentages = [0 for _ in categories]
    else:
        percentages = [int((spent / total_spent) * 10) * 10 for spent in spendings]

    chart = "Percentage spent by category"
    for i in range(100, -1, -10):
        chart += f"\n{i:3}|"
        for pct in percentages:
            if pct >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " "

    chart += "\n    " + "-" * (len(categories) * 3 + 1)

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "\n     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "

    return chart
