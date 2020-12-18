
check_address_name = []
map_change_address = []
map_change_name = []
map_read_split_x_name = 0
name_no = 0

#ini = open('ini_test.txt', 'r')
ini = open('test2.ini', 'r')
ini_read = ini.readline()

while ini_read :
    ini_read = ini.readline()
    ini_read_split = ini_read.split(',')
    if len(ini_read_split) == 13 :
        check_address_name.append(ini_read_split[7]) # ini file address name

ini.close()

#map = open('map_test.txt', 'r')
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
                #print (map_read_split_x[i])
                break
            i+=1

    #if len(map_read_split_x) == 2 :

        i=0
        while i < len(check_address_name) :

            if check_address_name[i] == map_read_split_x_name :
                if map_read_split_x_name in map_change_name :
                    pass
                    if len(map_read_split_x[name_no-1]) == 6 :
                        map_add_print = map_read_split_x[name_no-1][1:5]
                        map_change_address.append(map_add_print) # map file address
                        map_change_name.append(map_read_split_x_name) # map file name

            i+=1
        
map.close()



print("Match %d MAP addresses of %d INI addresses."%(len(map_change_name),len(check_address_name)))

# write
ini_new = open('write1.ini', 'w')
#ini = open('ini_test.txt', 'r')
ini = open('test2.ini', 'r')

ini_read = ini.readline()
while ini_read :

    ini_read = ini.readline()
    ini_read_split = ini_read.split(',')
    
    if len(ini_read_split) == 13 :
        i=0
        flag = 0
        #print(ini_read_split[7])
        while i < len(map_change_name) :

            if ini_read_split[7] == map_change_name[i] : 
                ini_write = ini_read_split[0][0:4]+map_change_address[i]
                ini_read_split[0] = ini_write
                
                for out in ini_read_split :
                    if out != ini_read_split[len(ini_read_split)-1] :                    

                        ini_new.write(out+',')        
                    else :
                        ini_new.write(out) 
                flag = 1 # find map_change_name
                break
            i+=1

        if flag == 0  : #not find map_change_name : Outputs just like "ini file"
            ini_new.write(ini_read)

    else :
        ini_new.write(ini_read)

ini.close()
ini_new.close()

print("ini addres name: ")
print(check_address_name)
print(len(check_address_name))
print("map addres name: ")
print(map_change_name)
print(len(map_change_name))
print("map addres: ")
print(map_change_address)
#print(len(map_change_address))

