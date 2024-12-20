

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
        item_base_prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
        }
        
        item_special_offers = {
             'A': {3: 130, 5: 200},
             'B': {2: 45},
             'H': {5: 45, 10: 80},
             'K': {2: 150},
             'P': {5: 200},
             'Q': {3: 80},
             'V': {2: 90, 3: 130},
             'W': {3: 130}
        }

        item_bogof_offers = {
             'E': {'letter': 'B', 'needed': 2, 'free': 1},
             'F': {'letter':'F', 'needed':3, 'free': 1 },
             'N': {'letter':'M', 'needed':3, 'free': 1 },
             'R': {'letter':'Q', 'needed':3, 'free': 1},
             'U': {'letter': 'U', 'needed': 3, 'free': 1}
        }
        

        item_counts = {}
        total = 0

        for item in skus:
            if not item in item_base_prices.keys():
                return -1
            
            item_counts[item] = item_counts.get(item, 0) + 1

        bogof_offer(item_counts, item_bogof_offers)
        special_offer(item_counts,)
        
        total = calculate_checkout(item_counts, item_base_prices)


        return total

def special_offer(item_counts, item_special_offers):
     total =0
     for item, deals in item_special_offers.items():
          #iterate backwarsd through the deals as they are sorted
          for deals in sorted(deals.keys(), reverse=True):
               #lower count until below the amount needed for the deal
               
    return total
               
               
            

          
        

def bogof_offer(item_counts, item_bogof_offers):
    for item, deal in item_bogof_offers.items():
        if item in item_counts.keys() and deal['letter'] in item_counts.keys():
            count = item_counts[item] // deal['needed']
            if item_counts[deal['letter']] - count > 0:
                item_counts[deal['letter']] -= count
            else:
                item_counts[deal['letter']] = 0


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
    def test_checkout_2F(self):
        assert checkout('FF') == 20
    def test_checkout_3F(self):
        assert checkout('FFF') == 20
    def test_checkout_4F(self):
        assert checkout('FFFF') == 30
    def test_checkout_5F(self):
        assert checkout('FFFFF') == 40
    def test_checkout_6F(self):
        assert checkout('FFFFFF') == 40

         


