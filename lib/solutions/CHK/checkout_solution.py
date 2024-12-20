

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

            # Handle special offers


            #Handle E buy 2 e get one free
            if item_counts.get('E', 0) ==2:
                item_counts['B'] = item_counts.get('B',0) - 1
                 



           

        for item, count in item_counts.items():
            total += count * item_base_prices[item]
        return total



