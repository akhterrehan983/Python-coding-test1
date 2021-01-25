from flask import Flask, request, render_template  

#for payment availaibility, true means available otherwise is false #
avail_cheap = True
avail_expensive = False
avail_premium = True
#..................................................................#


#........... three types of payments ............#
def CheapPaymentGateway(amount):
   if avail_cheap:
      print("CheapPaymentGateway",amount)
      return True
   else:
      return False
   
def ExpensivePaymentGateway(amount):
   if avail_expensive:
      print("ExpensivePaymentGateway",amount)
      return True
   else:
      return False
def PremiumPaymentGateway(amount):
   if avail_premium:
      print("PremiumPaymentGateway ",amount)
      return True
   else:
      return False
#...............................................#


#for response.#
def Success():
   return "Payment is processed: 200 OK"
def Fail():
   return "The request is invalid: 400 bad request"
#.............#


# Flask constructor 
app = Flask(__name__)    
@app.route('/', methods =["GET", "POST"]) 


#....................... 1 method to handle the task....................................#
def gfg(): 
   if request.method == "POST":
      
      card_no = request.form.get("card_no","")
      name = request.form.get("name","")
      date = request.form.get("date","")
      security_code = request.form.get("code","") 
      amount = int(request.form.get("amount",""))
      
      
      if amount<=20:
         if CheapPaymentGateway(amount):
               return Success()
         else:
               return Fail()
         
      elif 21<=amount<=500:
         if ExpensivePaymentGateway(amount):
            return Success()
         elif CheapPaymentGateway(amount):
            return Success()
         else:
            return Fail()
         
      elif amount>500:
         for i in range(3):
            if PremiumPaymentGateway(amount):
               return Success()
         return Fail()     
      else:
         return "Any error: 500 internal server error"
        
      # return (str(card_no)+"  "+str(name)+"  "+str(date)+"  "+str(security_code)+"  "+str(amount))
   return render_template("form.html")
#...............................................................................................# 
  
  
if __name__=='__main__':
   app.debug = True 
   app.run() 