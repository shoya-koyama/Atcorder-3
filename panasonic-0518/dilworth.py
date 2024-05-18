from collections import defaultdict

def is_substring(s, t):
    n = len(s)
    m = len(t)
    for i in range(n - m + 1):
        if s[i:i + m] == t:
            return True
    return False

def max_flow(source, sink, graph):
    parent = {}
    max_flow_value = 0
    
    while True:
        visited = set()
        stack = [source]
        while stack:
            u = stack.pop()
            visited.add(u)
            if u == sink:
                break
            for v, capacity in graph[u]:
                if v not in visited and capacity > 0:
                    stack.append(v)
                    parent[v] = u
        
        if sink in visited:
            path_flow = float('inf')
            current = sink
            while current != source:
                path_flow = min(path_flow, graph[parent[current]][current])
                current = parent[current]
            
            max_flow_value += path_flow
            
            v = sink
            while v != source:
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
                v = u
        else:
            break
    
    return max_flow_value

def main():
    n = int(input())
    s = []
    a = []
    
    for _ in range(n):
        s_i = input().strip()
        s.append(s_i)
    
    for _ in range(n):
        a_i = int(input())
        a.append(a_i)
    
    graph = defaultdict(dict)
    
    for i in range(n):
        graph['source'][i] = a[i]
        graph[i + n]['sink'] = a[i]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j]:
                    if i < j:
                        graph[i][j + n] = inf
                elif is_substring(s[i], s[j]):
                    graph[i][j + n] = inf
    
    flow = max_flow('source', 'sink', graph)
    sum_a = sum(a)
    print(sum_a - flow)

if __name__ == "__main__":
    main()
