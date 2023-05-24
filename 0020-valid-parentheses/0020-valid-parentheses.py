class Solution:
   
        
    def isValid(self, s: str) -> bool:
        def issmatch(c1,c2):
            if((c1=='(' and c2==')') or (c1=='{' and c2=='}') or (c1=='[' and c2==']')):
                return True
            else:
                return False
        open=[]
        for i in s:
            if i in ('(','{','['):
                open.append(i)
#             if nothing comes in open it means that str is empty sowe break here
            else:
#         if string is empty
                if not open:
                    return False
                elif issmatch(c1=open[-1],c2=i)==False:
                        return False
                else:
                    open.pop()
#         if no of open bracket still remians
        if open:
            return False
        else:
            return True
    
            
        
            
        