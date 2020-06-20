from collections import deque

queue = deque()
number = int(input())
for _ in range(number):
    cmd = input()
    if cmd.startswith('ENQUEUE'):
        queue.append(cmd.split(' ')[1])
    elif cmd == 'DEQUEUE':
        queue.popleft()
while len(queue) > 0:
    print(queue.popleft())
