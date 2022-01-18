import json


class Anagram:
    def __init__(self, a_type="country"):
        self.type = a_type
        self.__load_database()

    def __load_database(self):
        import json

        with open("./{}-database.json".format(self.type), "r") as fp:
            li = json.loads(fp.read())
        self.database = li

    def match(self, inputword):
        for con in self.database:
            if sorted(str(con).lower()) == sorted(inputword.lower()):
                return True, con
        return False, "No match!"

    def pro_match(self, inputword):
        database = [
            con for con in self.__load_compiled_database() if len(con) == len(inputword)
        ]

        result_list = []
        # print(database)
        for con_name in database:
            points = 0
            list_input = list(inputword.lower())
            for letter in con_name:
                if letter in list_input:
                    points += 1
                    # print(list_input)
                    # print(letter)
                    list_input.remove(letter)
            if len(con_name) > len(inputword):

                result_list.append(((points / len(con_name)) * 100, con_name))
            else:
                result_list.append(((points / len(inputword)) * 100, con_name))
        return sorted(result_list, key=lambda x: x[0], reverse=True)

    def __get_maximum(self, list_of_data):
        lista = list_of_data
        maximum_matched = lista[0][1]
        n_list = []
        n_list.append(lista.pop(0))
        for x in lista:
            if x[1] != maximum_matched:
                break
            else:
                n_list.append(x[0])
        return n_list

    def pro_match_max(self, inputword):
        return self.__get_maximum(self.pro_match(inputword))

    def __load_compiled_database(self):
        return [x.lower() for x in self.database]

    def ultra_pro_match(self, inputword):
        database = self.__load_compiled_database()

        result_list = []
        # print(database)
        for con_name in database:
            points = 0
            list_input = list(inputword.lower())
            for letter in con_name:
                if letter in list_input:
                    points += 1
                    # print(list_input)
                    # print(letter)
                    list_input.remove(letter)
            if len(con_name) > len(inputword):

                result_list.append(((points / len(con_name)) * 100, con_name))
            else:
                result_list.append(((points / len(inputword)) * 100, con_name))
        return sorted(result_list, key=lambda x: x[0], reverse=True)

    def ultra_pro_match_max(self, inputword):
        return self.__get_maximum(self.ultra_pro_match(inputword))

    def similarity_match(self, inputword):
        n_li = []
        for x in self.__load_compiled_database():
            points = 0

            wordforlen = min(len(inputword), len(x))

            for y in range(0, wordforlen):
                # print(y)
                if inputword[y] == x[y]:
                    points += 1
            n_li.append((x, (points / wordforlen) * 100))
        return sorted(n_li, key=lambda x: x[1], reverse=True)


solver = Anagram()
print(solver.match("Bnladshage"))
print(solver.pro_match("artinagen"))
print(solver.pro_match_max("madasagcar"))
solver = Anagram("capital")
print(solver.pro_match("hakad"))
print(solver.ultra_pro_match_max("hakad"))
print(solver.pro_match_max("hakad"))
print(solver.similarity_match("hakad"))
