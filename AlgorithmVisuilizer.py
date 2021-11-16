import pygame
import random
pygame.font.init()


screen = pygame.display.set_mode((900, 650))
  
pygame.display.set_caption("SORTING VISUALISER")

run = True

width = 900
length = 600
sz = 50000
array = [0]*(sz+1)
arr_clr = [(0, 204, 102)]*(sz+1)
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0),
       (0, 0, 153), (255, 102, 0),(230,230,250)]


fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 30)
fnt2 = pygame.font.SysFont("comicsans", 20)


base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(600, 10, 140, 32)
  

color_active = pygame.Color('lightskyblue3')
  

color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = False


def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
    
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
      
    if largest != i:
        arr_clr[i] = clr[2]
        arr_clr[largest] = clr[2]
        refill(4)
        arr_clr[i] = clr[0]
        arr_clr[largest] = clr[0]
        arr[i], arr[largest] = arr[largest], arr[i]
        
        heapify(arr, n, largest)

        
        
# Sorting Algo:Heap sort
def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2 - 1, -1, -1):
        arr_clr[i] = clr[1]
        refill(4)
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr_clr[i] = clr[2]
        arr_clr[0] = clr[2]
        refill(4)
        arr_clr[i] = clr[3]
        arr_clr[0] = clr[0]
        refill(4)
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    for i in range(n):
        arr_clr[i]=clr[3]
        
        
        
        

def quickSortPartition(start, end, array):
      
    
    pivot_index = start 
    pivot = array[pivot_index]
    arr_clr[pivot_index] = clr[4]
      
    
    while start < end:
        while start < len(array) and array[start] <= pivot:
            arr_clr[start] = clr[1]
            refill(3)
            arr_clr[start] = clr[0]
            start += 1
              
        
        while array[end] > pivot:
            arr_clr[end] = clr[2]
            refill(3)
            arr_clr[end] = clr[0]
            end -= 1
          
        
        if(start < end):
            arr_clr[start] = clr[1]
            arr_clr[end] = clr[2]
            refill(3)
            array[start], array[end] = array[end], array[start]
            arr_clr[start] = clr[2]
            arr_clr[end] = clr[1]
            refill(3)
            arr_clr[start] = clr[0]
            arr_clr[end] = clr[0]
    
    arr_clr[end] = clr[2]
    refill(3)
    array[end], array[pivot_index] = array[pivot_index], array[end]
    arr_clr[end] = clr[2]
    arr_clr[pivot_index] = clr[4]
    refill(3)
    arr_clr[end] = clr[0]
    arr_clr[pivot_index] = clr[0]
     
    
    return end

  
# Sorting Algo:Quick sort
def quickSort(start, end, array):
    if (start < end):
        p = quickSortPartition(start, end, array)
        quickSort(start, p - 1, array)
        quickSort(p + 1, end, array)
    for i in range(end+1):
        arr_clr[i]=clr[3]
        
# Sorting Algo:Bubble sort
def bubblesort(array):
    pygame.event.pump()
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
          if array[j] > array[j+1]:
                arr_clr[j] = clr[1]
                arr_clr[j+1] = clr[2]
                refill(2)
                arr_clr[j] = clr[0]
                arr_clr[j+1] = clr[0]
                array[j], array[j+1] = array[j+1], array[j]
    for i in range(n):
        arr_clr[i]=clr[3]
        
# Generate new Array
def generate_arr():
    for i in range(1, sz+1):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 90)


# Refill
def refill(x):
    screen.fill((255, 255, 255))
    draw(x)
    pygame.display.update()
    pygame.time.delay(50)
    
# Sorting Algo:Merge sort
def mergesort(array, l, r):
    mid = (l + r)//2
    if l < r:
      mergesort(array, l, mid)
      mergesort(array, mid + 1, r)
      merge(array, l, mid,mid + 1, r)

def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        arr_clr[i] = clr[1]
        arr_clr[j] = clr[1]
        refill(1)
        arr_clr[i] = clr[0]
        arr_clr[j] = clr[0]
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        arr_clr[i] = clr[1]
        refill(1)
        arr_clr[i] = clr[0]
        temp.append(array[i])
        i += 1
    while j <= y2:
        arr_clr[j] = clr[1]
        refill(1)
        arr_clr[j] = clr[0]
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        arr_clr[i] = clr[2]
        refill(1)
        if y2-x1 == len(array)-2:
            arr_clr[i] = clr[3]
        else:
            arr_clr[i] = clr[0]

# Draw the array values
def draw(x):
    # x : number of sort tochange heading
    if(x==1):
        txt2 = fnt1.render("ALGORITHM USED: Merge Sort", 1, (0, 0, 0))
        screen.blit(txt2, (300, 60))
    elif(x==2):
        txt2 = fnt1.render("ALGORITHM USED: Bubble Sort", 1, (0, 0, 0))
        screen.blit(txt2, (300, 60))
    elif(x==3):
        txt2 = fnt1.render("ALGORITHM USED: Quick Sort", 1, (0, 0, 0))
        screen.blit(txt2, (300, 60))
    elif(x==4):
        txt2 = fnt1.render("ALGORITHM USED: Heap Sort", 1, (0, 0, 0))
        screen.blit(txt2, (300, 60))
    else:
         # Text should be rendered
        txt = fnt2.render("PRESS 'a' to perform Merge Sort", 1, (0, 0, 0))
        # Position where text is placed
        screen.blit(txt, (20, 20))
        txt = fnt2.render("PRESS 'b' to perform Bubble Sort", 1, (0, 0, 0))
        screen.blit(txt, (20, 40))
        txt = fnt2.render("PRESS 'c' to perform Quick Sort", 1, (0, 0, 0))
        screen.blit(txt, (20, 60))
        txt = fnt2.render("PRESS 'd' to perform Heap Sort", 1, (0, 0, 0))
        screen.blit(txt, (20, 80))
        txt1 = fnt2.render("PRESS 'R' FOR NEW ARRAY.",1, (0, 0, 0))
        screen.blit(txt1, (20, 100))
        txt = fnt1.render("Enter the size of Array :-", 1, (0, 0, 0))
        screen.blit(txt, (360, 17))

    element_width =(width-(sz+1))//(sz+1)
    boundry_arr = 900 / (sz+1)
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 120), (900, 120), 6)
    for i in range(1, 100):
        # pygame.draw.line(surface, color, start_pos, end_pos, width=1)
        pygame.draw.line(screen, 
                        (224, 224, 224), 
                        (0, boundry_grp * i + 125), 
                        (900, boundry_grp * i + 125), 1)
      
    # Drawing the array values as lines
    for i in range(1, sz+1):
        pygame.draw.line(screen, arr_clr[i],\
            (boundry_arr * i-3, 125),\
            (boundry_arr * i-3, array[i]*boundry_grp + 125),\
            element_width)            

toggle=True# sorting window
# Infinite loop to keep the window open
while run:
    # background
    screen.fill((255, 255, 255))
    if toggle:
        draw(0)
    else:
        draw_graph(0)        
    # pygame.display.updat()
    # Event handler stores all event
    for event in pygame.event.get():
        # If we click Close button in window
        if event.type == pygame.QUIT:
            run = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and not toggle:
            x,y=getClickedPostition(pos)
            if source:
                npMatrix_clr[x][y]=clr[0]
                source_set=True
                source=False
                source_tile=(x,y)
                pygame.draw.rect(screen, clr[0],source_rect)
                draw_graph(0)
                continue
            if destination:
                npMatrix_clr[x][y]=clr[2]
                destination_set=True
                destination=False
                destination_tile=(x,y)
                pygame.draw.rect(screen, clr[0],destination_rect)
                draw_graph(0)
                continue
            if not source and not destination and x >= 0 and x <= 59 and y >= 0 and y <= 59:
                npMatrix_clr[x][y]=(0,0,0)
                removed_edges.append((x,y))
                print(x,y)
            if pos[1]<=20 and pos[1]>=7 and pos[0]>=600 and pos[0]<=615 and not source_set:
                source=True
                color1=clr[0]
                pygame.draw.rect(screen, clr[3],source_rect)
                draw_graph(0)
            if pos[1]<=42 and pos[1]>=27 and pos[0]>=600 and pos[0]<=615 and not destination_set:
                print("Destination")
                destination=True
                color2=clr[2]
                pygame.draw.rect(screen, clr[4],destination_rect)
                draw_graph(0)
            draw_graph(0)
            if destination_set:
                destination_set=True
                destination=False
         if event.type == pygame.MOUSEBUTTONDOWN:
            if (pos[1]<=79 and pos[0]>=580 and pos[1]>=48 and pos[0]<=616) or (pos[1]>=48 and pos[0]>=640 and pos[1]<=78 and pos[0]<=664):
                toggle=not toggle
         if event.type == pygame.KEYDOWN and not toggle:
            if event.key == pygame.K_r:
              for i in range(61):
                    for j in range(61):
                        npMatrix_clr[i][j]=(250,250,250)
              source=False
              destination_set=False
              source_set=False
              destination=False
              color1=(0,0,0)
              color2=(0,0,0)
              removed_edges=[]
              edges=[]
          elif event.key == pygame.K_d:
                print(removed_edges)
                for i in range(61):
                    for j in range(61):


