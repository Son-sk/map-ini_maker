with open('test1.map', 'r') as ini:

    with open('test1.map', 'r') as map:
        ini_read = ini.readline()
        map_read = map.readline()
        while ini_read :
            ini_read = ini.readline()
            ini_read_split = ini_read.split(' ')
            ini_read_split_x = [x for x in ini_read_split if x]
            print(ini_read_split_x)
            if len(ini_read_split_x[0]) == 6 :
                ini_print = ini_read_split_x[0][1:5]
                print (ini_print)





            # if len(ini_read_split) == 13 :
            #     print (ini_read_split[7])

            #while map_read :
                #with open('test1.map', 'r') as map:
                    #map_read = map.readline()