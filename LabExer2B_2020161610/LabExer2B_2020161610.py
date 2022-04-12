import os

#Use to clear some codes on output
def bura():  
    os.system( 'cls' )

#Represent a node of doubly linked list 
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class SearchList:    
    #Represent the head and tail of the doubly linked list    
    def __init__(self):    
        self.head = None;    
        self.tail = None;    
            
    #addNode() will add a node to the list    
    def addNode(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):    
            #Both head and tail will point to newNode    
            self.head = self.tail = newNode;    
            #head's previous will point to None    
            self.head.previous = None;    
            #tail's next will point to None, as it is the last node of the list    
            self.tail.next = None;    
        else:    
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = newNode;    
            #newNode's previous will point to tail    
            newNode.previous = self.tail;    
            #newNode will become new tail    
            self.tail = newNode;    
            #As it is last node, tail's next will point to None    
            self.tail.next = None;    
                
    #searchNode() will search a given node in the list    
    def searchNode(self, value):    
        i = 1;    
        flag = False;    
        #Node current will point to head    
        current = self.head;    
            
        #Checks whether the list is empty    
        if(self.head == None):    
            print("List is empty");    
            return;    
                
        while(current != None):    
            #Compare value to be searched with each node in the list    
            if(current.data == value):    
                flag = True;    
                break;    
            current = current.next;    
            i = i + 1;    
                
        if(flag):
            print("\nTrue\n")
            print(Search + " is present in the list at the position : " + str(i));    
        else:    
            print("\nFalse\n")
            print(Search + " is not present in the list");   
            
dList = SearchList();
count = 0
print("Note: Write [Exit] if you want to search\n")
while (count < 1): 
    value = input("Enter Node:")
    dList.addNode(value);
    if(value == "Exit"):
        count = count + 1

Search = input("\nEnter what Item you're searching:\n")
dList.searchNode(Search);         
bura()
