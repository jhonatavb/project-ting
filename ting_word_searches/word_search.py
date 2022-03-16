def exists_word(word, instance):
    all_queue = instance.all_queue()
    data_info = list()
    data_events = list()

    for info in all_queue:
        rows = info["linhas_do_arquivo"]
        name = info['nome_do_arquivo']
        for index, line in enumerate(rows):
            if word in line:
                data_events.append({"linha": index + 1})

        if len(data_events) >= 1:
            new_data_info = dict()
            new_data_info["palavra"] = word
            new_data_info["arquivo"] = name
            new_data_info["ocorrencias"] = data_events

            data_info.append(new_data_info)
    return data_info

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
