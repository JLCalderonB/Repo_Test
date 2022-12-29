import numpy as np

def new_feature():
    a = np.random.randint(10, size=1)
    b = np.random.randint(10, size=1)
    print(a,b)
    return(a-b)

if __name__=="__main__":
    print(new_feature())
