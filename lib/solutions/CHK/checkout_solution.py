

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
        total = 0

        for item in skus:
            if not item in item_base_prices.keys():
                return -1
            
            item_counts[item] = item_counts.get(item, 0) + 1

        #handle e count selection before getting to the checkout calculation
        if 'E' in item_counts.keys() and 'B' in item_counts.keys():
            count = item_counts['E'] // 2
            if item_counts['B'] - count > 0:
                 item_counts['B'] -= count
            else:
                 item_counts['B'] = 0
        
        if 'F' in item_counts.keys() and item_counts.get('F',0) >= 3:
             item_counts['F'] -= item_counts['F'] // 2


        total = calculate_checkout(item_counts, item_base_prices)


        return total

def calculate_checkout(item_counts,item_base_prices):
    total = 0
    
    for item, count in item_counts.items():
        if item == 'A':
            
            if count >=5:
                 total += ((count // 5 * 200) + (count % 5 // 3 * 130) + (count % 5 % 3 * 50))
            elif count >=3:
                 total += (count // 3 * 130) + (count % 3 * 50)
            else:
                 total += count * 50
        elif item =='B':
            #Handle E special offer
            if count >= 2:
                 total += (count //2 * 45) + (count % 2 * 30)
            else:
                 total += count * 30
            
        else:
             total += count * item_base_prices[item]


    return total

               
class TestChk():
    def test_checkout_solution_5A(self):
        assert checkout_solution('AAAAA') == 200
    def test_checkout_solution_3A(self):
         assert checkout_solution('AAA') == 130
    def test_checkout_solution_4A(self):
         assert checkout_solution('AAAA') == 180
    def test_checkout_solution_2B(self):
         assert checkout_solution('BB') == 45
    def test_checkout_solution_2E_0B(self):
         assert checkout_solution('EE') == 80
    def test_checkout_solution_2E_1B(self):
         assert checkout_solution('EEB') == 80
    def test_checkout_solution_2B_2E(self):
         assert checkout_solution('BBEE') == 110
    def test_checkout_solution_2E_2B(self):
         assert checkout_solution('EEBB') == 110
    def test_checkout_solution_BEBEEE(self):
            assert checkout_solution('BEBEEE') == 160
    def test_checkout_solution_ABCDECBAABCABBAAAEEAA(self):
            assert checkout_solution('ABCDECBAABCABBAAAEEAA') == 665
         


