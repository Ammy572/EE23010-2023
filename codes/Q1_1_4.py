import numpy as np 

def direction_vector (point_1 , point_2):
    return point_2 - point_1
def parametric_form (A,B,k):
    direction_vector_AB = direction_vector(A,B)
    x = A + k * direction_vector_AB
    return x    

if __name__ == "__main__":
    # Given points A,B,C
    A = np.array (([1,-1]))
    B = np.array (([-4,6]))
    C = np.array (([-3,-5]))

    k_values = np.linspace(0,1,10)  #Given range and number of points
    
    print("parametric form of line AB:")
    for k in k_values:
        parametric_point_AB = parametric_form(A,B,k)
        print (f"(k) = {k},Parametric_form_AB:",parametric_point_AB)
    

    print("\nparametric form of line BC:")
    for k in k_values:
        parametric_point_BC = parametric_form(B,C,k)
        print (f"(k) = {k},Parametric_form_BC:",parametric_point_BC)

    print ("\nparametric form of line CA:")
    for k in k_values:
        parametric_point_CA = parametric_form(C,A,k)
        print (f"(k) = {k},Parametric_form_CA:",parametric_point_CA)

