class ShoppingCart():
    # write your code here
    def __init__(self, emp_discount = None, total = 0, items = []):
        self.emp_discount = emp_discount
        self.total=total
        self.items=items
        
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total
    def mean_item_price(self):
        return self.total/len(self.items)

    def median_item_price(self):
        prices = [item["price"] for item in self.items]
        length = len(prices)
        if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        mid = int(length/2)
        return prices[mid]
        
    def apply_discount(self):
        if self.emp_discount:
            discount = self.total - (1-(self.emp_discount/100))
            return discount

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']