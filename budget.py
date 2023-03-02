class Category:
    ledger = []
    name = "" 
    
    def __init__(self, cat_name):
        self.name = cat_name  
        self.ledger = []          

    def get_balance(self):          
        total = 0.00        
        for item in self.ledger:
            total+=float(item.get("amount"))
        total = round(total,2)   
        return total    
        
    
    def check_funds(self, amount):
        total = self.get_balance()        
        if total - amount < 0:            
            return False        
        return True
    
    def deposit(self, amount, description=""):
        amount = float(amount)
        self.ledger.append({"amount": round(amount,2), "description": description})  
    
    def withdraw(self, amount, description=""):
        amount = round(amount,2)
        if self.check_funds(amount):
            amount = float(0 - amount)
            self.ledger.append({"amount": round(amount,2), "description": description})
            return True
        else:
            return False  
    
    def transfer(self, amount, other_cat): 
        funds_ok = self.check_funds(amount)         
        if funds_ok:
            descrip_other = "Transfer from " + self.name
            descrip = "Transfer to " + other_cat.name 
            self.withdraw(amount, descrip)  
            other_cat.deposit(amount, descrip_other)  
            return True
        return False
    
    def __repr__(self):
        string = ""
        #Category Name
        asterisks = ""
        cant_asterisks = int (15 - (len(self.name)/2))
        for i in range(0,cant_asterisks):
            asterisks += '*'
        title = asterisks + self.name + asterisks
        string = string + title + "\n"
        #Items description
        for item in self.ledger:
            desc = item.get("description")
            amount = item.get("amount") 
            amount = f"{amount:.2f}" 
            if len(desc)>23:
                desc = desc[:23]
            if len(desc)<23:
                desc_spaces = ""
                cant_desc_spaces = int(23 - len(desc))
                for i in range(0,cant_desc_spaces):
                    desc_spaces+=" "
                desc = desc+desc_spaces
            if len(amount)<7:        
                amount_spaces = ""
                cant_amount_spaces = int(7 - len(amount))
                for i in range(0,cant_amount_spaces):
                    amount_spaces+=" "
                amount = amount_spaces+amount     
            
            string = string + desc + amount +"\n"
        #Total
        total = "Total: "
        monto = str(self.get_balance())
        total = total + monto
        string = string + total        
        return string    
      
#Chart function:
import budget
def create_spend_chart(list: 'budget.Category'):  
    chart = "Percentage spent by category\n"    
    withdrawals = []
    percentages = []
    names = []

    for category in list:
        name = category.name
        names.append(name)
        withdrawal = 0
        ledger = category.ledger
        for item in ledger:
            amount = item.get('amount')            
            if amount < 0:
                withdrawal += (amount*(-1))             
        withdrawals.append(withdrawal)

    withdrawal_sum  = sum(withdrawals)
    
    for value in withdrawals:
        percentages.append(int(value * 100 / withdrawal_sum))
        
    percentage = 100
    for i in range (11):
        if percentage == 100:
            chart += str(percentage) + "| "
        elif percentage >= 10:
            chart += " " +str(percentage) + "| "
        else:
            chart += "  " +str(percentage) + "| "
        for value in percentages:
            if value >= (percentage):
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
        percentage -= 10
    chart += "    -"
    for category in list:
        chart += "---"
    chart += "\n"

    max_name_len = 0
    for name in names:
        if len(name) > max_name_len:
            max_name_len = len(name)
    
    for x in range(max_name_len): 
        chart += "     "       
        for name in names:
            if len(name) > x:
                chart += name[x] + "  "
            else:
                chart += "   "
        if x < (max_name_len - 1):
            chart += "\n"    

    return chart

        



              
              