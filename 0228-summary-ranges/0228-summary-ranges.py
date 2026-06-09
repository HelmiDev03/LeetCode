class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==1:
            nums[0]=str(nums[0])
            return nums 
        s=[]
        a=""
        for i in range(1,len(nums)):
            if a=="":
                a+=str(nums[i-1])

            if abs(nums[i] - nums[i-1] > 1) :
                s.append(a)
                if i != len(nums)-1:
                    a=str(nums[i])
                else:
                    s.append(str(nums[i]))
                    a=""    
               
            elif ">" in a :
                j=0
                new=""
                while a[j]!="-":
                    new+=a[j]
                    j+=1
                a=new+"->"+str((nums[i]))  
            else:
                a+= "->" + str(nums[i])      

        if a!="":
            s.append(a)
        return s        

        