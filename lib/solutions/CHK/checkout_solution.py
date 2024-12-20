

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
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21
        }

        item_triple_offers = {'S','T','X','Y','Z'}
        
        item_special_offers = {
             'A': {3: 130, 5: 200},
             'B': {2: 45},
             'H': {5: 45, 10: 80},
             'K': {2: 120},
             'P': {5: 200},
             'Q': {3: 80},
             'V': {2: 90, 3: 130},
        }

        item_bogof_offers = {
             'E': {'letter': 'B', 'needed': 2, 'free': 1},
             'F': {'letter':'F', 'needed':3, 'free': 1 },
             'N': {'letter':'M', 'needed':3, 'free': 1 },
             'R': {'letter':'Q', 'needed':3, 'free': 1},
             'U': {'letter': 'U', 'needed': 4, 'free': 1}
        }
        

        item_counts = {}

        triple_sets = {}
 

        total = 0
        set_counter=0

        totalSets=0

        for item in skus:
            if not item in item_base_prices.keys():
                return -1
            
            item_counts[item] = item_counts.get(item, 0) + 1
            

            if item in item_triple_offers:
                triple_sets[item] = triple_sets.get(item, 0 ) + 1
                set_counter +=1
        
        if set_counter > 2:
            #a set exists and we need to find the highest value set of 3 keys
            #i.e remove all keys with the highest value first and then the next highest value
            for item in sorted(triple_sets, key=triple_sets.get, reverse=True):
                if triple_sets[item] > 0:
                    triple_sets[item] -= 1
                    set_counter -= 1
                    totalSets +=1 
                    if set_counter == 2:
                        break
                
        total += totalSets * 45

        


        

        bogof_offer(item_counts, item_bogof_offers)
        total += special_offer(item_counts,item_special_offers)

        total += calculate_checkout(item_counts, item_base_prices)


        return total

def special_offer(item_counts, item_special_offers):
    total = 0
    for item, deals in item_special_offers.items():
        if item not in item_counts.keys():
            continue
          #iterate backwarsd through the deals as they are sorted
        for deals in sorted(deals.keys(), reverse=True):
            count = item_counts[item] // deals
            if count > 0:
                total += count * item_special_offers[item][deals]
                item_counts[item] -= count * deals

               
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
    def test_checkout_13H(self):
        assert checkout('HHHHHHHHHHHHH') == 110
    def test_checkout_3U(self):
        assert checkout('UUU') == 120
    def test_checkout_3R_1Q(self):
        assert checkout('RRRQ') == 150
    def test_checkout_6R_2Q(self):
        assert checkout('RRRRRRQQ') == 300
    def test_checkout_3R_1Q_1R_1Q_2R(self):
        assert checkout('RRRQRQRR') == 300
    def test_checkout_3N_1M(self):
        assert checkout('NNNM') == 120
    def test_checkout_6N_2M(self):
        assert checkout('NNNNNNMM') == 240
    def test_checkout_3N_1M_1N_1M_2N(self):
        assert checkout('NNNMNMNN') == 240
    def test_checkout_3V(self):
        assert checkout('VVV') == 130   
    def test_checkout_2V(self):
        assert checkout('VV') == 90
    def test_checkout_3V_2V(self):
        assert checkout('VVVVV') == 220
    def test_checkout_3V_3V_1V(self):
        assert checkout('VVVVVVV') == 310
    def test_checkout_3S(self):
        assert checkout('SSS') == 45
    def test_checkout_4S(self):
        assert checkout('SSSS') == 65
    def test_checkout_5S(self):
        assert checkout('SSSSS') == 85
    def test_checkout_6S(self):
        assert checkout('SSSSSS') == 90
    def test_checkout_1T_1S_1Y(self):
        assert checkout('TSY') == 45
    def test_checkout_1T(self):
        assert checkout('T') == 20
    def test_checkout_1K(self):
        assert checkout('K') == 70
    def test_checkout_alphabet(self):
        assert checkout('ABCDEFGHIJKLMNOPQRSTUVW') == 795
    def test_checkout_1S_1T_1X(self):
        assert checkout('STX') == 45
    def test_checkout_1S_1T_1X_1S_1T_1X(self):
        assert checkout('STXSTX') == 90
    def test_checkout_3S_1Z(self):
        assert checkout('SSSZ') == 65
