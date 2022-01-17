import json 

class Anagram:
    def __init__(self, a_type="country"):
        self.type = a_type
        self.__load_database()

    def __load_database(self):
        import json
        with open("./{}-database.json".format(self.type),"r") as fp:
            li = json.loads(fp.read())
        self.database = li

    def match(self, inputword):
        for con in self.database:
            if sorted(str(con).lower()) == sorted(inputword.lower()):
                return True, con
        return False, "No match!"

    def pro_match(self, inputword):
        sameli = [str(con).lower() for con in self.database if len(con) == len(inputword)]
        n_li = []
        for con_name in sameli:
            c_name = con_name
            percentage = 0
            length = len(con_name)
            con_name = list(con_name) 
            for y in inputword:
                if y in con_name:
                    con_name.remove(y)
                    percentage += 1
            percentage = (percentage/length)*100
            n_li.append((c_name,percentage))
            #print(percentage)
        return sorted(n_li, key = lambda x: x[1],reverse=True)

    def pro_match_max(self, inputword):
        lista:list = self.pro_match(inputword)
        maximum_matched = lista[0][1]
        n_list = []
        n_list.append(lista.pop(0))
        for x in lista:
            if x[1] != maximum_matched:
                break
            else:
                n_list.append(x[0])
        return(n_list)

    def similarity_match(self,inputword):
        raise RuntimeError("under development")


solver = Anagram()
x = solver.pro_match_max('bgaladshne')
print(x)

"""solver = Anagram()
print(solver.match("Bnladshage"))
print(solver.pro_match("artinagen"))
print(solver.pro_match_max("madasagcar"))
print("\n\n\n\n")
solver_for_capital = Anagram("capital")
print(solver_for_capital.pro_match("hakad"))"""

