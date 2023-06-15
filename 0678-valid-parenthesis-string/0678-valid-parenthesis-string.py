class Solution:
    def checkValidString(self, s: str) -> bool:
        # using a stack to solve it
        stack=[]
        for i in s:
            # print("we got ",i)
            if i=="(" or i=="*":
                stack.append(i)
                # print("our stack is ",stack)
            else:
                # we got ) - iterate to the stack backwardly and see if we got a open bracket associated with it
                flag=0
                for j in range(len(stack)):
                    k=len(stack)-1-j
                    if stack[k]=="(":
                        stack.pop(k)
                        flag=1
                        break
                if flag:
                    pass
                else:
                    # check for * and make it open bracket and pop it
                    for j in range(len(stack)):
                        if stack[j]=="*":
                            stack.pop(j)
                            flag=1
                            break
                if flag:
                    continue
                else:
                    return False
                # print("our stack is ",stack)
        if "(" or ')' in stack:
            pass
        else:
            return True
        ans=[]
        for i in stack:
            # print("ans is ",ans)
            if i=="(":
                ans.append(i)
            else:
                if len(ans):
                    ans.pop()
                    # print("after pop ans is ",ans)
        if "(" in ans:
            return False
        return True
        
                            
                
                        
                    
                
        