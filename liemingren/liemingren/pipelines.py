# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
class LiemingrenPipeline:
    def process_item(self, item, spider):
        item['title'] = item['title'].strip() #；因为字符串不可变，故需要重新赋值。
        item['title'] = item['title'].replace(" ","_")#tiele不是title，拼写错误会导致键不存在。
        print("--------------------------------------------------------")
        print(item['title'])
        print("--------------------------------------------------------")
        with open('G:/scrapy/liemingren/data/%s.txt' % (item['title']), 'w', encoding='utf-8',newline='') as fp:
            item['book'] = [str(item) for item in item['book']]
            fp.write('\n'.join(item['book']))
            #write = csv.writer(fp)
            #write.writerows(item['book'])
        #return item
