import numpy as np

class matrix_playground:

    def __init__(self):
        
        self.m1=np.array([[1,2,3],[4,5,6],[7,8,9]])
        self.m2=np.array([[3,0,9],[2,4,6],[4,0,7]])
        self.menu()

    #choose what you want to do(menu option)
    def menu(self):
        print("-----------------MATRIX PLAYGROUND-----------------")
        print("Enter your choice:")
        choose=input("1.Show matrices\n2.Addition\n3.Subtraction\n4.Multiplication\n5.Division\n6.Transpose\n7.detarminant\n8.exit\n")
        while True:

            if choose=="1":
                self.show_matrices()
            elif choose=="2":
                self.addition()
            elif choose=="3":
                self.subtraction()
            elif choose=="4":
                self.multiplication()
            elif choose=="5":
                self.division()
            elif choose=="6":
                self.Transpose_menu()
            elif choose=="7":
                self.detarminant_menu()
            elif choose=="8":
                self.row_sum()
            elif choose=="9":
                self.column_sum()
            elif choose=="10":
                self.max_element()
            elif choose=="11":
                print("Exited")
                break
            else:
                print("Invalid chooise")

    def show_matrices(self):
        print("\nMatrix1 :\n ",self.m1)
        print("\nMatrix2 :\n ",self.m2)

    def addition(self):
        #add two matrix
        return np.add(self.m1,self.m2)
    
    def subtraction(self):
        #subtract two matrix
        return np.subtract(self.m1,self.m2)
    
    def multiplication(self):
        #multiply two matrix
        return np.dot(self.m1,self.m2)
    
    def division(self):
        #divide two matrix
        return np.divide(self.m1,self.m2)
    
    #----------------------transpose menu-----------------------
    def Transpose_menu(self):
        #transpose the matrix 
        choose = input("Transpose of (1) Matrix1 or (2) Matrix2: ")

        if choose == "1":
            print(np.transpose(self.m1))

        elif choose == "2":
            print(np.transpose(self.m2))

        else:
            print("Invalid Choice")

   #-------------detarminant menu------------------         
    def detarminant_menu(self):
        #determinant of the matrix
        choose = input("Determinant of (1) Matrix1 or (2) Matrix2: ")

        if choose == "1":
            print(np.linalg.det(self.m1))

        elif choose == "2":
            print(np.linalg.det(self.m2))

        else:
            print("Invalid Choice")

    def row_sum(self):
        print("row sum of matrix1:",np.sum(self.m1,axis=1))
        print("row sum of matrix2:",np.sum(self.m2,axis=1))

    def column_sum(self):
        print("column sum of matrix1:",np.sum(self.m1,axis=0))
        print("column sum of matrix2:",np.sum(self.m2,axis=0))

    def max_element(self):
        print("Max in Matrix1:", np.max(self.m1))
        print("Max in Matrix2:", np.max(self.m2))


obj1=matrix_playground()#create an object
