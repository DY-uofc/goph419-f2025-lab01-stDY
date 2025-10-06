def factorial(x:int)->int:
    """Description of function.
    returns the discrete factorial of the variable
    Parameters
    x
    Returns
    x!
    """
    if x<0:
        print("Error_Factoral_input_nagetive")
    if x == 0 or x == 1:
        return 1
    return x*factorial(x - 1)

def interger_power(x:float,n:int)->float:
    """Description of function.
    returns x to the interger power
    Parameters
    x,n
    Returns
    x^n
    """
    y=1
    if n==0: #x^0=1 for all x\ne0 so y*x^0=y
        return y
    if n<0: #y*x^(-n)=y*(1/x)^(-(-n))=y*(1/x)^n
        x=1/x
        n=-n
    while (n>=1):# loop the mutiplication
        y*=x
        n-=1
    return y

def sqrt(x:float,iteration:int=10)->float: 
    """Description of function.
    Consider the input domain of the function in this case is 0≤x≤π^2/4<2.5
    so a=0.5,1,1.5,2.0,2.5
    Parameters
    x
    Returns
    sqrt(x)
    """
    if x<0 or x>=2.75:
        print("Value out of range")
        return -1000
    elif x<0.75: #for a=0.5
        a=0.5
        y=0.7071067811865476
        for k in range(1,iteration+1): #counts k from 1 to the 'iteration'
            j=1
            const=0.5
            while j<=k-1:
                const*=-0.5*(2*j-1)
                j+=1
            y+=const*(interger_power(x-a,k))/(factorial(k)*interger_power((0.7071067811865476),2*k-1))
    elif x<1.25: #for a=1
        a=1
        y=1
        for k in range(1,iteration+1): #counts k from 1 to the 'iteration'
            j=1
            const=0.5
            while j<=k-1:
                const*=-0.5*(2*j-1)
                j+=1
            y+=const*(interger_power(x-a,k))/(factorial(k)*interger_power((1),2*k-1))
    elif x<1.75: #for a=1.5
        a=1.5
        y=1.224744871391589
        for k in range(1,iteration+1): #counts k from 1 to the 'iteration'
            j=1
            const=0.5
            while j<=k-1:
                const*=-0.5*(2*j-1)
                j+=1
            y+=const*(interger_power(x-a,k))/(factorial(k)*interger_power((1.224744871391589),2*k-1))
    elif x<2.25: #for a=2
        a=2
        y=1.4142135623730951
        for k in range(1,iteration+1): #counts k from 1 to the 'iteration'
            j=1
            const=0.5
            while j<=k-1:
                const*=-0.5*(2*j-1)
                j+=1
            y+=const*(interger_power(x-a,k))/(factorial(k)*interger_power((1.4142135623730951),2*k-1))
    elif x<2.75: #for a=2.5
        a=2.5
        y=1.5811388300841898
        for k in range(1,iteration+1): #counts k from 1 to the 'iteration'
            j=1
            const=0.5
            while j<=k-1:
                const*=-0.5*(2*j-1)
                j+=1
            y+=const*(interger_power(x-a,k))/(factorial(k)*interger_power((1.5811388300841898),2*k-1))
    return y

def arcsin(x:float,iteration:float=100)->float:
    """Description of function.
    takes an number and spitout the arcsin of that number
    Parameters
    x,iteration
    Returns
    arcsin(x)
    """
    a=0
    for n in range(1,iteration+1):
        a+=0.5*interger_power(2*x,2*n)/(interger_power(n,2)*(factorial(2*n)/interger_power(factorial(n),2)))
        y=sqrt(a)
    return y

def launch_angle(ve_v0:float, alpha:float)->float:
    """Description of function.
    takes ve_V0, the ratio of escape velocity to terminal velocity, and alpha, 
    the designated altitude, return the value of the angle phi
    Parameters
    ve_v0, alpha
    Returns
    phi
    """
    return arcsin((1+alpha)*sqrt(1-(alpha/(1+alpha))*interger_power(ve_v0,2)))

def launch_angle_range(ve_v0:float, alpha:float, tol_alpha:float)->float:
    """Description of function.
    by using ve_v0, alpha, and it's tolorance to find the range of acceptable 
    launch angle phi range in format of ([minimum angle, maximum angle])
    to be in the designated altitude
    Parameters
    ve_v0, alpha, tol_alpha
    Returns
    phi_range
    """
    angle_max=launch_angle(ve_v0,(1-tol_alpha)*alpha)
    angle_min=launch_angle(ve_v0,(1+tol_alpha)*alpha)
    phi_range=([angle_min,angle_max])
    return phi_range


