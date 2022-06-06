from utils import select_db_count, show_tables, create_msg_table
from loguru import logger


def get_max_seq() -> str:
    have_data_table = False
    max_seq = '01'
    tables = show_tables()

    for item in tables:
        table = item[0]
        name_list = table.split('_')
        if name_list[0] == 'telegram' and name_list[1] == 'msg' and name_list[-1] >= max_seq:
            max_seq = name_list[-1]
            have_data_table = True

    if not have_data_table:
        create_msg_table('telegram_msg_01')

    return max_seq


def get_table_name():
    try:
        max_seq = get_max_seq()
        count = select_db_count(max_seq)[0][0]
        if count > 9999999:  # 记录条数大于9999999，则新建一个表
            max_seq = '0' + str(int(max_seq) + 1)
            table_name = 'telegram_msg_' + max_seq
            create_msg_table(table_name)
        else:
            table_name = 'telegram_msg_' + max_seq

        return table_name
    except Exception as e:
        logger.error('获取表名失败-----------')
        print(e)
        return None


if __name__ == '__main__':
    get_table_name()