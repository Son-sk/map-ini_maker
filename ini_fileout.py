
check_address_name = []
change_address = []
change_name = []
i=0

name_no = 0
map_read = 1
map_read_split_x_name =0
ini = open('test2.ini', 'r')

ini_read = ini.readline()

while ini_read :
    ini_read = ini.readline()
    ini_read_split = ini_read.split(',')
    if len(ini_read_split) == 13 :
        check_address_name.append(ini_read_split[7])

ini.close()

map = open('test1.map', 'r')

map_read = map.readline()

while map_read :

    map_read = map.readline()
    map_read_split = map_read.split(' ')
    map_read_split_x = [x for x in map_read_split if x]
    if len(map_read_split_x) > 1 :
        i=0
        while i < len(map_read_split_x) :
            if map_read_split_x[i][0] == '_' :
                map_read_split_x_name = map_read_split_x[i][1:map_read_split_x[1].find('\n')]  
                name_no = i
                break
            i+=1

    if len(map_read_split_x) == 2 :
  
        i=0
        while i < len(check_address_name) :

            if check_address_name[i] == map_read_split_x_name :

                if len(map_read_split_x[name_no-1]) == 6 :
                    map_add_print = map_read_split_x[name_no-1][1:5]
                    change_address.append(map_add_print)
                    change_name.append(map_read_split_x_name)

            i+=1
        
map.close()

# print(change_address)
# print(len(change_address))
# print(change_name)
# print(check_address_name)
# print(len(change_name))


ini_new = open('write.ini', 'w')

ini = open('test2.ini', 'r')

ini_read = ini.readline()
while ini_read :

    ini_read = ini.readline()
    ini_read_split = ini_read.split(',')
    #print(ini_read_split)
    if len(ini_read_split) == 13 :
        i=0
        while i < len(change_name) :
            print(ini_read_split[7])
            print(change_name[i])
            if ini_read_split[7] == change_name[i] : 
                ini_write = ini_read_split[0][0:4]+change_address[i]
                ini_read_split[0] = ini_write
                
                
                for out in ini_read_split :
                    if out != ini_read_split[len(ini_read_split)-1] :                    

                        ini_new.write(out+',')        
                    else :
                        ini_new.write(out) 
            else :
                ini_new.write(ini_read+'r')
                break        

            i+=1    
    else :
        ini_new.write(ini_read+'x')

ini.close()
ini_new.close()

