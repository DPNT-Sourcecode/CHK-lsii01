

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

        total = handle_special_offers(item_counts)


        return total

def handle_special_offers(item_counts):
    for item, count in item_counts.items():
        if item == 'A':
            if count >= 3 and count < 5:
                if count % 3 == 0:
                    return count / 3 * 130
            elif count >= 5:  
                if count % 5 == 0:
                    return count / 5 * 200
                else:
                    return (count / 5 * 200) + (count % 5 * 50)
            else:
                return count * 50
            
        elif item =='B':
             #need to handle E special offer
             if item_counts.get('E', 0) % 2 == 0 and item_counts.get('E', 0)!= 0:
                  count -= item_counts.get('E', 0 ) / 2
             if count >= 2:
                  if count % 2 == 0:
                       return count / 2 * 45
                  else:
                       return (count / 2 * 45) + (count % 2 * 30)

               
     


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
    def test_checkout_2B_2E(self):
         assert checkout('BBEE') == 110
    def test_checkout_2E_2B(self):
         assert checkout('EEBB') == 110
    def test_checkout_BEBEEE(self):
            assert checkout('BEBEEE') == 160
    def test_checkout_ABCDECBAABCABBAAAEEAA(self):
            assert checkout('ABCDECBAABCABBAAAEEAA') == 665
         








