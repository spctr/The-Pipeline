import random,sys
city_size = int(sys.argv[1])
print('City size is: ', city_size)
with open('cityX.txt', 'w') as the_file:
    the_file.write(str(city_size)+'\n')
    for y in range(city_size):
        line=''
        for x in range(city_size-1):
            line+=str(random.randint(1,1000000))+" "
        line+=str(random.randint(1,1000000))    
        the_file.write(line+'\n')