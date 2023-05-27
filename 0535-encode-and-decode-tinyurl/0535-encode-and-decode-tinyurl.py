class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        b=longUrl.split("://")
        # print(b)
        right=b[1]
        ans=""
        # print("longUrl is",longUrl)
        a=right.split("/")
        # print(a)
        x=len(a)
        ans+=f"{x+1}"
        ans+=f"#{len(b[0])+3}#{b[0]}://"
        for i in a:
            ans+="#"
            ans+=f"{len(i)+1}"
            ans+="#"
            ans+=i
            if i==a[-1]:
                continue
            ans+="/"
        return ans
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s=shortUrl 
        # print("we got input as",s)
        i=0
        x=""
        while(s[i]!="#"):
            x+=s[i]
            i+=1
        # print("x is",x)
        ans=""
        x=int(x)
        s=s[i:]
        # print("we got input as",s)
        i=0
        for t in range(x):
            if s[i]=="#":
                # print("in if")
                i+=1
                l=""
                while(s[i]!="#"):
                    l+=s[i]
                    i+=1
                i+=1
                l=int(l)
                # print("length is ",l)
                ans+=s[i:i+l]
                i+=l
                
        return ans
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))