from itemadapter import ItemAdapter


class MiniProjectPipeline:
    def process_item(self, item, spider):
        return item

class BookscraperPipeline:
    def process_item(self, item, spider):
        item['title'] = item['title'].strip() if item['title'] else 'NA'

        price = item.get('price', '').replace('£', '').replace('$', '').strip()
        try:
            item['price'] = float(price) if price else None
        except ValueError:
            item['price'] = None

        rating_map = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        rating_val = item.get('rating', '')
        rating = rating_val.split()[-1] if rating_val else 'NA'
        item['rating'] = rating_map.get(rating, None)

        return item