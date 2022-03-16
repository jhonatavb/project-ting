import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    rows_file = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(rows_file),
        "linhas_do_arquivo": rows_file
    }

    file_already_gone = False

    for index, _item in enumerate(instance.all_queue()):
        curr_file = instance.search(index)
        if curr_file == data:
            file_already_gone = True

    if not file_already_gone:
        instance.enqueue(data)
        print(f"{data}", file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
