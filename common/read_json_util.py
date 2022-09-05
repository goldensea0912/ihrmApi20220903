import json


# ���庯������ȡ data/xxx.json �ļ�
def read_json_data(path_filename):
    # with open("../data/ihrm_login.json", "r", encoding="utf-8") as f:
    # with open("../data/add_emp.json", "r", encoding="utf-8") as f:
    with open(path_filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        list_data = []
        for item in json_data:
            tmp = tuple(item.values())
            list_data.append(tmp)

    # ��� ���أ���������� for ��
    return list_data


if __name__ == '__main__':
    ret = read_json_data()
    print(ret)