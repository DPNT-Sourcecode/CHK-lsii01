

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
        

        item_counts = {}
        total = 0
        for item in skus:
            if not item in item_base_prices.keys():
                return -1
            
            item_counts[item] = item_counts.get(item, 0) + 1


           

        for item, count in item_counts.items():
            total += count * item_base_prices[item]
        return total





