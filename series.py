def fibonacci(n):
    '''
    function that require value then it keep recal with -1 until it is equal 1 and thats called the 'Recursion':
        input ---> value
        output >> represnt the fibonacci series for the input number
    '''
    series=[0,1]
    i=0
    answer = 0
    while (i<=n):
        if (i==len(series)):
            series.append(series[i-2]+series[i-1])
        answer = series[i]
        i+=1
    return answer
         
    
    
def lucas(n):
    '''
    function that require value then it keep recal with -1 until it is equal 2 and thats called the 'Recursion':
        input ---> value
        output >> represnt the lucas series for the input number
    '''
    series=[2,1]
    i=0
    answer = 0
    while (i<=n):
        if (i==len(series)):
            series.append(series[i-2]+series[i-1])
        answer = series[i]
        i+=1
    return answer

def sum_series(n,f=0,s=1):
    '''
    Calling this function with no optional parameters will produce numbers from the fibonacci series. 
    Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. 
    Other values for the optional parameters will produce other series.
    '''
    series=[f,s]
    i=0
    answer = 0
    while (i<=n):
        if (i==len(series)):
            series.append(series[i-2]+series[i-1])
        answer = series[i]
        i+=1
    return answer
