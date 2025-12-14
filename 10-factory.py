#%% Import data
with open("input.txt") as file:
    machines = file.readlines()

lights = [line.split('[')[1].split(']')[0] for line in machines]
buttons = [[[int(num) for num in group.strip('()').split(',')] for group in line.split() if group.startswith('(')] for line in machines]

#%% Part 1: Count min steps to turn light pattern
def solve(lights, buttons):
    lights = sum(j << c for c, j in enumerate(lights))
    buttons = [sum((1 << j) for j in i) for i in buttons]
    memo = {}
    
    def rsolve(l, idx=0):
        if l == 0: return 0
        if idx == len(buttons): return len(buttons) + 1
        
        if (l, idx) in memo:
            return memo[(l, idx)]
        
        result = min(rsolve(l, idx + 1), 1 + rsolve(l ^ buttons[idx], idx + 1))
        memo[(l, idx)] = result
        return result
    
    return rsolve(lights)

count = 0 
for light, button in zip(lights, buttons):
    light_pattern = [1 if ch == '#' else 0 for ch in light]
    steps = solve(light_pattern, button)
    count += steps

print(f"Total button presses: {count}")