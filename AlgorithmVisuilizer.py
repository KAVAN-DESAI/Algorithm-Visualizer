from numpy.lib.utils import _info
import pygame
import random

import numpy as np
from queue import PriorityQueue

from pygame import surface
from pygame.constants import K_d
from collections import defaultdict


pygame.font.init()

screen = pygame.display.set_mode((900, 810))

# Title and Icon 
pygame.display.set_caption("SORTING VISUALISER")
  
# Boolean variable to run the program in while loop
run = True
  
# Window size
width = 1000
length = 7000
sz = 50000
array = [0]*(sz+1)
arr_clr = [(0, 204, 102)]*(sz+1)
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0),
       (0, 0, 153), (255, 102, 0),(230,230,250), (250,250,250)]
matrix_clr=[[(250,250,250)]*101]*101
matrix=[[0]*101]*101

#Graph edges
edges=[]
removed_edges=[]
path=[]


npMatrix_clr = np.array([[x for x in y] for y in matrix_clr])
        

fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 30)
fnt2 = pygame.font.SysFont("comicsans", 20)


base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(600, 10, 140, 32)
toggle_circle_graph=pygame.Rect(650, 50, 16, 16)
toggle_circle_sort=pygame.Rect(500, 50, 16, 16)

source_rect = pygame.Rect(600, 5, 18, 18)
destination_rect = pygame.Rect(600, 27, 18, 18)

# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color1 = (0,0,0)
color2=(0,0,0)

  
active = False

# window toggle circle
# window = pygame.display.set_mode((300, 300))

#Graph Details
width=660
rows=60
gap = width // rows


def build_graph(edges):
    graph = defaultdict(list)
     
    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
         
        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph


# Function to find the shortest
# path between two nodes of a graph
def BFS_ShortestPath(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
        npMatrix_clr[node[0]][node[1]]=clr[4]
        npMatrix_clr[source_tile[0]][source_tile[1]]=clr[0]
        draw_graph(0)
        pygame.display.update()
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return new_path
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return



def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr_clr[i] = clr[2]
        arr_clr[largest] = clr[2]
        refill(4)
        arr_clr[i] = clr[0]
        arr_clr[largest] = clr[0]
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
# Sorting Algo:Heap sort
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        arr_clr[i] = clr[1]
        refill(4)
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr_clr[i] = clr[2]
        arr_clr[0] = clr[2]
        refill(4)
        arr_clr[i] = clr[3]
        arr_clr[0] = clr[0]
        refill(4)
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    for i in range(n):
        arr_clr[i]=clr[3]


def quickSortPartition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
    arr_clr[pivot_index] = clr[4]
      
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            arr_clr[start] = clr[1]
            refill(3)
            arr_clr[start] = clr[0]
            start += 1
              
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            arr_clr[end] = clr[2]
            refill(3)
            arr_clr[end] = clr[0]
            end -= 1
          
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
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
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    arr_clr[end] = clr[2]
    refill(3)
    array[end], array[pivot_index] = array[pivot_index], array[end]
    arr_clr[end] = clr[2]
    arr_clr[pivot_index] = clr[4]
    refill(3)
    arr_clr[end] = clr[0]
    arr_clr[pivot_index] = clr[0]
     
    # Returning end pointer to divide the array into 2
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

source=False
destination_set=False
source_set=False
destination=False


# Draw the 2d matrix
def draw_graph(x):
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
        txt = fnt2.render("PRESS 'd' to perform Dijkstra's Algorithm", 1, (0, 0, 0))
        # Position where text is placed
        screen.blit(txt, (20, 20))
        txt = fnt2.render("PRESS 'r' Reset", 1, (0, 0, 0))
        screen.blit(txt, (20, 40))
        txt = fnt2.render("PRESS 'c' to perform Quick Sort", 1, (0, 0, 0))
        screen.blit(txt, (20, 60))
        txt = fnt2.render("PRESS 'd' to perform Heap Sort", 1, (0, 0, 0))
        screen.blit(txt, (20, 80))
        txt1 = fnt2.render("PRESS 'R' FOR NEW ARRAY.",1, (0, 0, 0))
        screen.blit(txt1, (20, 100))
        txt = fnt1.render("Source", 1, (0, 0, 0))
        screen.blit(txt, (360, 5))
        txt = fnt1.render("Destination", 1, (0, 0, 0))
        screen.blit(txt, (360, 32))
    
    pygame.draw.line(screen, (0, 0, 0), (120, 120), (790, 120), 5)
    pygame.draw.line(screen, (0, 0, 0), (120, 120), (120, 790), 5)
    pygame.draw.line(screen, (0, 0, 0), (120, 790), (790, 790), 5)
    pygame.draw.line(screen, (0, 0, 0), (790,120), (790,790), 5)
    for i in range(rows):
        for j in range(rows):
            pygame.draw.rect(screen, npMatrix_clr[i][j],pygame.Rect((i*gap)+125, (j*gap)+125, gap, gap))
            # pygame.draw.line(screen, matrix_clr[i][j],(i+125,j+125),(i*gap + 125,j*gap +125),gap)
            
    for i in range(rows):
        pygame.draw.line(screen,  (224, 224, 224), (125, i * gap +125), (width+125, i * gap+ 125))
        pygame.draw.line(screen,  (224, 224, 224), (i * gap+125, 125), (i * gap+125, width+125))

    
    pygame.draw.rect(screen, color1, source_rect)
    # pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 50, 50, 32))

    pygame.draw.rect(screen, color2, destination_rect)
    # pygame.draw.rect(screen, (0,0,0), pygame.Rect(600, 50, 50, 32))

    pygame.draw.circle(screen,(0,0,0),(650, 66),16)
    pygame.draw.circle(screen,(230,230,230),(600, 66),16)

    pygame.draw.circle(screen,(0,0,0),(650, 66),16)
    pygame.draw.circle(screen,(230,230,230),(600, 66),16 )

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(600, 50, 50, 32))
    pygame.draw.circle(screen,(230,230,230),(650, 66),16)
    pygame.draw.circle(screen,(0,0,0),(600, 66),16)

    

def getClickedPostition(position):
    x, y = position
    x-=125
    y-=125
    rowx, columny = x // gap, y // gap
    return (rowx, columny)


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
    
    if active:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(screen, color, input_rect)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(600, 50, 50, 32))
    pygame.draw.circle(screen,(0,0,0),(650, 66),16)
    pygame.draw.circle(screen,(230,230,230),(600, 66),16)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
    # display.flip() will update only a portion of the
    # screen to updated, not full area


done=False
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
        if pygame.mouse.get_pressed()[0]:
            x,y=getClickedPostition(pos)
            if not source and not destination and x >= 0 and x <= 59 and y >= 0 and y <= 59:
                if (x,y) not in removed_edges:
                    npMatrix_clr[x][y]=(0,0,0)
                    removed_edges.append((x,y))
                    print(x,y)
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
                        ok=True
                        ok1=True
                        ok2=True
                        ok3=True
                        ok4=True
                        for k in removed_edges:
                            if k==(i,j):
                                ok1=False
                            if k==(i,j+1):
                                ok1=False
                            if k==(i,j-1):
                                ok2=False
                            if k==(i+1,j):
                                ok3=False
                            if k==(i-1,j):
                                ok4=False
                        if ok and ok1:
                            edges.append([(i,j),(i,j+1)])
                        if ok and ok2:
                            edges.append([(i,j),(i,j-1)])
                        if ok and ok3:
                            edges.append([(i,j),(i+1,j)])
                        if ok and ok4:
                            edges.append([(i,j),(i-1,j)])
                print("X")
                newEdges=[]
                for j in edges:
                    if j[0] not in removed_edges:
                        if j[1] not in removed_edges:
                            newEdges.append(j)

                graph=build_graph(newEdges)
                path=BFS_ShortestPath(graph, source_tile, destination_tile)
                print(path)
                for i in path:
                    npMatrix_clr[i[0]][i[1]]=clr[1]
                # npMatrix_clr[source_tile[0]][source_tile[1]]=clr[0]
                npMatrix_clr[destination_tile[0]][destination_tile[1]]=clr[2]
                npMatrix_clr[source_tile[0]][source_tile[1]]=clr[0]

                draw_graph(0)
        if event.type == pygame.MOUSEBUTTONDOWN and toggle:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN and toggle:
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                if(len(user_text)==1):
                    user_text = user_text[:-1]
                    sz =1
                elif(len(user_text)>1):
                    user_text = user_text[:-1]
                    sz = int(user_text)
                array = [0]*(sz+1)
                arr_clr = [(0, 204, 102)]*(sz+1)
                generate_arr()
            elif event.key == pygame.K_a:
                    active=False
                    mergesort(array, 1, len(array)-1)
            elif (event.key == pygame.K_b):
                    active=False
                    bubblesort(array)
            elif(event.key == pygame.K_c):
                active=False
                quickSort(0, len(array) - 1, array)
            elif(event.key == pygame.K_d):
                active=False
                heapSort(array)
            elif(event.key == pygame.K_r):
                generate_arr()
            elif(active):
                user_text += event.unicode
                sz = int(user_text)
                array = [0]*(sz+1)
                arr_clr = [(0, 204, 102)]*(sz+1)
                generate_arr()
            # Unicode standard is used for string
            # formation
    # print(toggle,"here")
    pygame.display.update()
