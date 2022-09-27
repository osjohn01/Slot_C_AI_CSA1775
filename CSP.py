def color(mpa, colors=['red', 'green', 'blue']):
    (vars, adjoins)=parse_map(map)
    p=Problem()
    p.addVariables(vars, colors)
    for (v1,v2) in adjoins:
        p.addContraint(lambda x,y:x!=y, [v1, v2])
    solution = p.getSolution()
    if solution:
        for v in vars:
            print("%s:%s"%(v, solution[v]), print)
    else:
        print("NO SOLUTION FOUND --> ")
australia="SA:WA NT Q NSW V;NT:WA Q;NSW:Q V;T:"
