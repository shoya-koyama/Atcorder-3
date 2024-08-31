num_events = int(input())
last_position = [-1, -1]   # 0: left hand, 1: right hand
total_distance = 0

for _ in range(num_events):
    position, direction = input().split()
    position = int(position)
    hand_index = (0 if direction == 'L' else 1)
    
    if last_position[hand_index] != -1:
        total_distance += abs(last_position[hand_index] - position)
    
    last_position[hand_index] = position

print(total_distance)
