import csv

def import_csv(url_file, delimiter) :
    '''permet d'importer un csv dans une liste de liste Python
    url_file est le nom du fichier plus l'extension
    delimiter est le craractère de délimitation dans le csv
    souvent soit ',' soit ';'
    list_list est la liste de liste retournée'''
    with open(url_file, newline='', encoding='utf-8') as csvfile :
        file = csv.reader(csvfile, delimiter=delimiter)
        #Initialisation de la liste de liste
        list_list = []
        for row in file :
            list_list.append(row)

    return list_list
