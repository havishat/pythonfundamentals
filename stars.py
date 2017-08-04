#part1
def draw_stars(arr):
    for i in arr:
        print "*" * i 
num_arr = [3,4]     
draw_stars(num_arr)

#part 2 

def draw_stars2(arr):
    for i in arr:
        if isinstance(i, int):
            print "*" * i 
        elif isinstance(i, str):
            length = len(i)
            letter = i[0].lower()
            print letter*length
            
num = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]   
draw_stars2(num)
    
