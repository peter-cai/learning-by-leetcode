# solution by Python3

class Solution:    
    def isMatch(self, s: str, p: str) -> bool:         
        # 当s不存在，则p须全为“*”才能进行匹配
        if not s:
            return not p.replace("*","") 
        # 构建一个指示矩阵，以s为行，p为列，
        # 指示矩阵多出一行一列，最左上角元素为True 
        # 进行元素匹配，传导True   
        m, n = len(p)+1, len(s)+1
        jdg = [[False]*n for i in range(m)]
        jdg[0][0] = True

        # 按行、列进行双重循环
        for i in range(1,m):
            for j in range(0,n):
                # 当某行p的元素为“*”，则可传递其正上方的True，意为“*”可匹配0个
                # 同时，可传递其左上方的True，该True向所在行进行贯穿传递，意为“*”可匹配多个
                if p[i-1] == "*":           
                    jdg[i][j] = jdg[i-1][j] or jdg[i][j]
                    if j>0 and jdg[i-1][j-1] == True:
                        jdg[i][j:] = [True] * (n-j) 
                # 当某行p的元素为“？”或p与s对应元素相同，则可传递其左上方的True
                elif j>0 and (p[i-1] == "?" or p[i-1] == s[j-1]):
                        jdg[i][j] = jdg[i-1][j-1] or jdg[i][j]  
        return jdg[-1][-1]        
