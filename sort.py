def sort_dictionary(dict_input):
    dictsort = sorted(dict_input.items(), key=lambda x: x[1][1])
    dictoutput = []
    for name, (phone, age) in dictsort:
        dictoutput.append((name, phone))
    return dictoutput