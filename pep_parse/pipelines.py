import csv
from datetime import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:

    def open_spider(self, spider):
        self.counter = {'Статус': 'Количество'}
        self.total = 0

    def process_item(self, item, spider):
        status = item['status']
        self.counter[status] = self.counter.get(status, 0) + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        self.counter['Total'] = self.total
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.counter.items())
