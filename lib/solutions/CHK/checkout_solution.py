

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
        

        for item in skus:
            if not item in item_base_prices.keys():
                return -1
            
            item_counts[item] = item_counts.get(item, 0) + 1
        print(item_counts)
        total += triple_offers(item_counts, item_triple_offers, item_base_prices)
        print(item_counts)
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


def triple_offers(item_counts, item_triple_offers, item_base_prices):
    total = 0
    triple_items = []

    for item in item_triple_offers:
        if item in item_counts:
            triple_items.extend([item] * item_counts[item])
    
    while len(triple_items) >=3:
        triple_items.sort(key=lambda x: item_base_prices[x], reverse=True)

        total += 45
        for i in range(3):
            item = triple_items[i]
            item_counts[item] -= 1
            if item_counts[item] == 0:
                del item_counts[item]

        triple_items = triple_items[3::]
   
    return total




def calculate_checkout(item_counts,item_base_prices):
    total = 0
    for item, count in item_counts.items():
        total += count * item_base_prices[item]

    return total
               
    


         





