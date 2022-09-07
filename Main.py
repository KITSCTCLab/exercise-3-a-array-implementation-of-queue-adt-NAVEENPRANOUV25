class Solution:
    """This class implements linear queue.
      Attributes:
          stack: A list which maintains the content of stack.
          queue: A list which maintains the content of queue.
          top: An integer which denotes the index of the element at the top of the stack.
          front: An integer which denotes the index of the element at the front of the queue.
          rear: An integer which denotes the index of the element at the rear of the queue.
          size: An integer which represents the size of stack and queue.
      """

    # Write your code here
    def __init__(self, size):
        """Inits Solution with stack, queue, size, top, front and rear.
        Arguments:
          size: An integer to set the size of stack and queue.
        """
        self.stack = []
        self.queue = []
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1

    def is_stack_empty(self):
        """
        Check whether the stack is empty.
        Returns:
          True if it is empty, else returns False.
        """
        return self.top == -1

    def is_queue_empty(self):
        """
        Check whether the queue is empty.
        Returns:
          True if it is empty, else returns False.
        """
        return self.front == -1 or self.front > self.rear

    def is_stack_full(self):
        """
        Check whether the stack is full.
        Returns:
          True if it is full, else returns False.
        """
        return self.top == self.size - 1

    def is_queue_full(self):
        """
        Check whether the queue is full.
        Returns:
          True if it is full, else returns False.
        """
        return self.rear == self.size - 1

    def push_character(self, character):
        """
        Push the character to stack, if stack is not full.
        Arguments:
            character: A character that will be pushed to the stack.
        """
        if not self.is_stack_full():
            self.stack.append(character)
            self.top += 1

    def enqueue_character(self, character):
        """
        Enqueue the character to queue, if queue is not full.
        Arguments:
            character: A character that will be enqueued to queue.
        """
        if not self.is_queue_full():
            if  self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue.append(character)

    def pop_character(self):
        """
        Do pop operation if the stack is not empty.
        Returns:
          The data that is popped out if the stack is not empty.
        """
        if not self.is_stack_empty():
            self.top -= 1
            return self.stack.pop(self.top + 1)

    def dequeue_character(self):
        """
        Do dequeue operation if the queue is not empty.
        Returns:
          The data that is dequeued if the queue is not empty.
        """
        if not self.is_queue_empty():
            self.front += 1
            return self.queue[self.front - 1]
               


# read the string text
text = input()

# find the length of text
length_of_text = len(text)

# Create the Solution class object
solution = Solution(length_of_text)

# push/enqueue all the characters of string text to stack
for index in range(length_of_text):
    solution.push_character(text[index])
    solution.enqueue_character(text[index])

is_palindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both characters
If the comparison fails, set is_palindrome as False.
'''
for index in range(length_of_text):
    if solution.pop_character() != solution.dequeue_character():
        is_palindrome = False


# finally print whether string text is palindrome or not.
if is_palindrome:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")
class MyCircularQueue:
    def _init_(self, size: int):
        self.size=size
        self.queue=[None]*size
        self.rear=-1
        self.front=-1

    def enqueue(self, value: int) -> bool:
       
        if(self.is_full()==False):
            if(self.front==-1):
                self.front=0
                self.rear=0
                self.queue[self.rear]=value
            else:
                self.rear=(self.rear+1)%self.size
                self.queue[self.rear]=value
            return True
        else:
            return False

    def dequeue(self) -> bool:
        if(self.is_empty()==False):
            if(self.front==self.rear):
                self.front=-1
                self.rear=-1
                return True
            else:
                self.front=(self.front+1)%self.size
                return True
        else:
            return False
               

    def get_front(self) -> int:
        if(self.is_empty()==False):
            return self.queue[self.front]
        else:
            return -1

    def get_rear(self):
        if(self.is_empty()==False):
            return self.queue[self.rear]
        else:
            return -1

    def is_empty(self):
        return self.front==-1

    def is_full(self):
        return (self.rear+1)%self.size==self.front
           


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
