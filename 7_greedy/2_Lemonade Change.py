def lemonadeChange( bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)
        five = 0
        ten = 0

        for i in range (0,n):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>=1:
                    five-=1
                    ten +=1
                else:
                    return False
            else:
                if five>=1 and ten>=1:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else: return False
        return True 

# example
print(lemonadeChange([5,5,5,10,20]))