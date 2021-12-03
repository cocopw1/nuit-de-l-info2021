from functions import import_csv
def r(recherche):
    listsup3 = [line for line in poi if (str(line[1])==recherche)]
    return sorted(listsup3, key = lambda listsup3:listsup3[1])
	

poi = import_csv("base.csv",";")


