def arithmetic_arranger(problems: list, solve: bool = False) -> str:
    if len(problems) > 5:
        return "Error: Too many problems."
        
    pproblems = []
    for a in problems:
        e = a.split()
        if not any([e[1] == "-", e[1] == "+"]):
            return "Error: Operator must be '+' or '-'."
        if not all([e[0].isnumeric(), e[-1].isnumeric()]):
            return "Error: Numbers must only contain digits."
        if not all([len(e[0]) <= 4, len(e[-1]) <= 4]):
            return "Error: Numbers cannot be more than four digits."
        pproblems.append((e, len(max(e, key=len))))
        
    first_line = []
    second_line = []
    dashes_line = []
    results_line = []
    
    for p in pproblems:
        first_line.append(" " * (2 + p[1] - len(p[0][0])) + p[0][0])
        second_line.append(p[0][1] + " " * (1 + p[1] - len(p[0][2])) + p[0][2])
        dashes_line.append("-" * len(second_line[-1]))
        if solve is True:
            result = str(eval("".join(p[0])))
            results_line.append(" " * (len(second_line[-1]) - len(result)) + result)
    single = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes_line)
    print(pproblems)
    #print("    ".join(first_line))
    #print("    ".join(second_line))
    #print("    ".join(dashes_line))
    if solve is True:
        # print("    ".join(results_line))
        single += "\n" + "    ".join(results_line)
    return single