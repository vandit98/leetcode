class Solution:
    def __init__(self):
        self.dictt={"I":1,
                    "II":2,
                    "III":3,
              "IV":4,
              "V":5,
                    "VI":6,
                    "VII":7,
                "VIII":8,
                    # "IX":9,
              "X":10,
                "XX":20,
                "XXX":30,
                   
                    
              "L":50,
                     "LX":60,
                    "LXX":70,
                    "LXXX":80,
              "C":100,
                "CC":200,
                    "CCC":300,
              "D":500,
                    "DC":600,
                    "DCC":700,
                    "DCCC":800,
              "M":1000,
                "MM":2000,
                    "MMM":3000
              
                    
                
             }
    def find_roman(self,no) -> int:
        # print(" i m called and no is ",no)
        ans=""
        while(no>0):
            for i,j in self.dictt.items():
                if j>=no:
                    ans=i+ans
                    no=j-no
                    break
        # print("i m returning",ans)
        return ans
                    
            
    def intToRoman(self, num: int) -> str:
#         we will iterate form left to right
        ans=""
      
        x=len(str(num))
        # print("len is ",x)
        # print(len(str(num)))
        for i in range(0,len(str(num))):
            place=x-i-1
            # print("place is",place)
            quotient=num/pow(10,place)
            no=int(floor(quotient)*pow(10,place))
            # print("no is ",no)
            ans+=self.find_roman(no)
            num-=no
            
        return ans
            
            
            
        