
from utils import select_db_record
from choice_table import get_max_seq

max_seq = get_max_seq()

sql = f"select link, max(msg_id) from telegram01.telegram_msg_{max_seq} " \
      f"group by link;"

link_list = select_db_record(sql)
print(link_list)

new_links = {}
for tuple_item in link_list:
    new_links[tuple_item[0]] = tuple_item[1]

print(new_links)