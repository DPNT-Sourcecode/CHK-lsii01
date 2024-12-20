

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
        item_base_prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
        }
        item_special_offers = {
             'A' : {3: 130, 5: 200},
             'B' : {2: 45},
        }
        

        item_counts = {}
        running_item_counts = {}
        total = 0

        for item in skus:
            if not item in item_base_prices.keys():
                return -1
            
            item_counts[item] = item_counts.get(item, 0) + 1

            running_item_counts[item] = running_item_counts.get(item, 0) + 1

        
            #Handle E buy 2 e get one free
            if item_counts.get('E', 0) == 2:
                item_counts['B'] = item_counts.get('B', 0) - 1

            #Handle special offers
            if item == 'B':
                if item_counts[item] == 2:
                    total += item_special_offers[item][2]
                    item_counts[item] = 0
            elif item == 'A':
                if item_counts[item] == 3:
                     total += item_special_offers[item][3]
                     item_counts[item] = 0
                     
                if running_item_counts[item] == 5:
                     total += item_special_offers[item][5]
                     total -= item_special_offers[item][3]
                     running_item_counts[item] = 0
                     item_counts[item] = 0



        for item, count in item_counts.items():
            if count > 0:
                total += count * item_base_prices[item]
            
        return total


class TestChk():
    def test_checkout_5A(self):
        assert checkout('AAAAA') == 200
    def test_checkout_3A(self):
         assert checkout('AAA') == 130
    def test_checkout_4A(self):
         assert checkout('AAAA') == 180
    def test_checkout_2B(self):
         assert checkout('BB') == 45
    def test_checkout_2E_0B(self):
         assert checkout('EE') == 80
    def test_checkout_2E_1B(self):
         assert checkout('EEB') == 80
    def test_checkout_2E_2B(self):
         assert checkout('EEBB') == 110

