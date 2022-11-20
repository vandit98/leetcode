class Solution:
    def preorderTraversal(self, root,lst=None):
        #first travelling to left
        if not lst: 
            lst = []
        if root!=None:
            # print("trying to append t list")
            # print(root.val)
            lst.append(root.val)
            # print("lst is",lst)
            self.preorderTraversal(root.left,lst)
            self.preorderTraversal(root.right,lst)
        return lst
    def binary_search(self,arr,x):
        low=0
        high=len(arr)-1
        
        while(low<high):
            mid=int(low+ (high-low)/2)
            # print("mid is",mid)
            if arr[mid]>=x:
                high=mid
            else:
                low=mid+1
        # print("low pos is",arr[low])
        # print("high pos is",arr[high])
        if arr[low]>=x:
            pass
        else:
            return -1
        return high
    def closestNodes(self, root, queries):
        lst=self.preorderTraversal(root)
        print(lst)
        out=[]
        # lst.sort()
        a=set(lst)
        a=list(a)
        a.sort()
        for i in queries:
            high_index=self.binary_search(a,i)
            if a[high_index]==i:
                out.append([i,i])
                continue
            if high_index!=-1:
                max=a[high_index]
            else:
                max=-1
            if high_index==-1:
                min=a[high_index]
            elif high_index==0:
                min=-1
            else:
                min=a[high_index-1]
            out.append([min,max])
        return out