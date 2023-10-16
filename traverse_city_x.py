city_x_file=open('cityX.txt','r')
city_x_lines=city_x_file.readlines()
city_size=int(city_x_lines[0])
matrix = [[int(x) for x in line.split()] for line in city_x_lines[1:city_size+1]]
mat_t = [list(x) for x in zip(*matrix)] #transpose matrix to be able to work column per column


for i in range(1,city_size):
    current_column = mat_t[i]
    previous_column = mat_t[i-1]
   
    distances={}

    for j in range(0, city_size):

        for k in range(j, city_size):
            if j==0:
                distances[(k,k)]=current_column[k]
            else:
                distance=distances[(k-j,k-1)]+current_column[k]
                distances[(k-j,k)]=distance



    for j in range(0, city_size):
        minimum_distance = 1000000000001
        for k in range(0, city_size):
            cost=0
            if (j,k) in distances:
                cost=distances[(j,k)]
            else:
                cost=distances[(k,j)]
            cost+=previous_column[k]
            if cost<minimum_distance:
                minimum_distance=cost
        current_column[j]=minimum_distance

print(min(mat_t[city_size-1]))    