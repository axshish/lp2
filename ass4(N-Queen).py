def isSafe(arr,x,y,n) ->bool:
    
    # Check if there's a queen in the same column above
    for row in range(x):
        if arr[row][y]==1:
            return False
    
    # Check upper left diagonal    
    row, col = x, y
    while row >= 0 and col >= 0:
        if arr[row][col]==1:
            return False
        row -= 1
        col -= 1
        
    # Check upper right diagonal
    row, col = x, y
    while row >= 0 and col < n:
        if arr[row][col]==1:
            return False
        row -= 1
        col += 1
        
    return True


def nqueen(arr,x,n) -> bool:
    if x>=n:
        return True
    
    for col in range(n):
        if isSafe(arr,x,col,n):
            arr[x][col]=1
            
            if nqueen(arr,x+1,n):
                return True
                        
            arr[x][col]=0 #backtracking
            
    return False

if __name__=="__main__":
    n   = int(input("Enter N for N-Queen Problem : "))
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    
    if nqueen(arr,0,n)  :
        print("\n\nHere is Solution for",n,"Queens\n\n")
        for i in range(n)   :
            for j in range(n):
                print(arr[i][j] ,end="\t")
            print("\n")
            
    else:
        print("\n\nSolution does not exist for the given ",n,"\n\n")