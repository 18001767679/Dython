# Dython Moclude
#You need a self param for every
# Oprations
class math():
    '''def expon(num, root): You can use math.pow(num,root) for this.
        ji = float(num)
        for j in range(root - 1):
            ji = float(float(ji) * float(num))
        return ji'''
    def itemsAdd(s,var):
        num = 0
        for i in list(var):
            num += float(i)
        return num
    '''def itemsSub(var):
        num = float(list(var)[0] * 2)
        for i in list(var):
            num -= float(i) You should not combine non-associative functions.
        return num'''
    def itemsMulti(s,var):
        num = 1
        for i in list(var):
            num = float(float(num) * float(i))
        return num
    '''def itemsDivd(var):
        num = float(list(var)[0])
        for i in range(int(len(list(var))) - 1):
            num = float(float(num) / float(var[i + 1]))
        return num'''
    def joinStrs(s,strings):
        string = ""
        for i in list(strings):
            string += str(i)
        return str(string)
    '''def itemCount(var, item):
        count = 0
        for i in list(var): list.count is enough.
            if i is item: count += 1
        return int(count)'''
    def rangeLimit(s,num, MIN, MAX):
        if int(num) > int(MAX): return int(MAX)
        elif int(num) < int(MIN): return int(MIN)
        else: return int(num)
    def feturn(s,con, true, false):#Inline if exp
        return true if con else false
    '''def listInit(var, item):
        for j in range(len(list(var))):list.index is the same
            if list(var)[j] is item: return int(j)
        return None'''
    def listInits(s,var, item):
        items = []
        for j in range(len(list(var))):
            if list(var)[j] is item: items.append(j)
        if items != []: return list(items) 
        else: return None
    def filterList(s,var, item):
        items = []
        for j in list(var):
            if not j is item: items.append(j)
        return items
    def map(funct,dt):
        for i in dt:
            funct(dt)
        
# Temp Variables
#temps = []
# [ [name, value] ]

class temp():
    def __init__(self):
        self.temps=[]
    def define(s,name, start):
        b = True
        for i in list(s.temps):
            if list(i)[0] is str(name):
                b = False
                break
        if bool(b): s.temps.append([str(name), start])
    def get(s,name):
        for i in list(s.temps):
            if list(i)[0] is str(name):
                return list(i)[1]
        return None
    def set(s,name, value):
        count = 0
        for i in s.temps:
            if list(i)[0] is str(name):
                s.temps[int(count)] = [str(name), value]
            count += 1
    def remove(s,name):
        for i in range(int(len(s.temps))):
            j = list(temps)[i]
            if list(j)[0] is str(name): s.temps.pop(i)

# Console
class console():
    def menu(s,caption, options, noAnwser):
        print('')
        if caption != "" and caption != None: print(str(caption))
        if int(len(options)) <= 1:
            print("error in a menu() function")
            exit
        for optionCount in range(len(options)):
            print(str(optionCount) + ": " + str(options[optionCount]))
        while True:
            optionAnwser = input("└> ")
            try:
                testAnwser = int(optionAnwser)
                mest = "int"
            except ValueError:
                try:
                    testAnwser = float(optionAnwser)
                    mest = "float"
                except ValueError:
                    try:
                        testAnwser = str(optionAnwser)
                        mest = "str"
                    except:
                        print("error in a menu() function")
                        exit
            if mest == "int" or mest == "float":
                if mest == "float": testAnwser = int(round(float(testAnwser)))
                optionAnswer = testAnwser
                if int(optionAnswer) >= 0 and int(optionAnswer) < int(len(options)): return int(optionAnswer)
            elif mest == "str":
                if bool(noAnwser) and str(optionAnwser) == "": return None
