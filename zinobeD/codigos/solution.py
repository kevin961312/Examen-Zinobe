def equation(variable):
    (N,t)= variable
    #constans
    mu, mass , gravity, acce = 0.2, 10, 10, 0.012
    w = mass*gravity
    #assignment
    F_r = N*mu
    w_x = w*sin(t) 
    w_y = w*cos(t)
    #Equation system
    system_q = [-F_r+w_x-mass*acce, N-w_y]
    return system_q
solution = opt.fsolve(equation, (0,2*pi) )  