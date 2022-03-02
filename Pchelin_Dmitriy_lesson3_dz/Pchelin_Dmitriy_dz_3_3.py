def thesaurus(*args):
    name_dict = {}
    for name in args:
        if not name_dict.get(name[0]):
            name_dict[name[0]] = [name]
        else:
            name_list = name_dict[name[0]]
            name_list.append(name)
            name_dict[name[0]] = name_list
    print(name_dict)

thesaurus("Иван", "Мария", "Петр", "Илья")