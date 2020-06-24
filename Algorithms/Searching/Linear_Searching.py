# Time Complexity: O(n)
class Linear_Searching:
    def __init__(self):
        self.num=0
        self.arr=[]

    def accept(self):
        n= int (input("Enter the size of array: "))
        print('Enter the Array Elements')
        while n!=0:
            n-=1
            self.arr.append(int(input()))

        self.num=int(input("Enter the number to be searched: "))

    def l_search(self):
        num=self.num
        arr=self.arr
        res=-1
        for i,j in enumerate(arr):
            if j==num:
                res=i

        if res==-1:
            print('Not Found')
        else:
            print(f'Number Found at Index {res}')

if __name__ == "__main__":
    ls=Linear_Searching()
    ls.accept()
    ls.l_search()


