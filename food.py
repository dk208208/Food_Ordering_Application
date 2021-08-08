from datetime import datetime,timedelta
import time

class food:
    purpose : "TO SERVE FOOD"
    admin_detail = {}    
    first_food_id = 4  
    food_list = {1:
                 {'Quantity': '2 pieces',
                  'Food Name': 'Tandoori Chicken',
                  'Price': 240,
                  'Discount': 10,
                  'Total Price': 240,
                  'Stock': 3
                 },2:
                 {'Quantity': '1 Piece',
                  'Food Name': 'Vegan Burger',
                  'Price': 320,
                  'Discount': 14,
                  'Total Price':  320,
                  'Stock': 3
                 },3:
                 {'Quantity': '500 Gram',
                  'Food Name': 'Truffle Cake',
                  'Price': 900,
                  'Discount': 45,
                  'Total Price':  900 ,
                  'Stock': 3
                 }  
                }
       
    def admin_home(self):
        print("\n-----------------------------Admin Portal----------------------------------\n")
        self.admin_input = input("\nPress>>1.   Sign-Up\nPress>>2.   Sign-In\nPress>>0.   Home        ")
        if self.admin_input == "1":
            self.admin_sign_up()
        elif self.admin_input =="2":
            self.admin_sign_in()
        elif  self.admin_input == "0":
            self.home()
        else:
            print("!!!Enter correct NUmber!!!")
            self.admin_home()
           
    def admin_sign_up(self):
        print("Enter details for sign-up----------------")
        self.name = input("Enter Full-Name:   ").upper()
        self.email = input("Enter Email:   ")
        self.password = input("Create Your Password:   ")
        food.admin_detail[self.email] = self.password
        print("\nSign-up successful")
        self.admin_home()
       
    def admin_sign_in(self):
        print("\n Enter details for log-in-------------")
        self.email0 = input("Enter Email/Username: ")
        if self.email0 in food.admin_detail :
            self.password0 = input("Enter Your Password: ")
            if food.admin_detail[self.email0] == self.password0:
                print("\n Login successful ")
                self.admin_feature()
            else:
                print(" Username or Password does not match!!!")
                self.admin_home()
        else:
            print("Invalid Email !!!")
            self.admin_home()    
       
    def admin_feature(self):
        print('-----------------------------------------------------------------------------------------------------')
        admin_input01 = input("\nPress>>1.   Add Food\n\nPress>>2.   Remove Food\n\nPress>>3.   List of Food\n\nPress>>4.   Update Food\n\nPress>>0.   Home             ")
        print('-----------------------------------------------------------------------------------------------------')  
        if admin_input01 == "1":
            self.add_food()
        elif admin_input01 == "2":
            self.remove_food()
        elif admin_input01 == "3":
            for p_id, p_info in food.food_list.items():
                print("\n---Food ID:", p_id)
                for key in p_info:
                    print(key + ':', p_info[key])
            self.admin_feature()
        elif admin_input01 == "4":
            self.update_food()      
        elif admin_input01 =="0":
            self.home()
           
    def add_food(self):
        self.food_id = food.first_food_id
        print(self.food_id)
        self.food_dict = {}
        self.foodname = input("Food Name:\n").upper()
        self.foodQuantity = input("Enter Quntity")
        self.foodprice = int(input("Price:\n"))
        self.fooddiscount= int(input("Discount:\n"))
        self.foodstock= int(input("Stock:\n"))
        self.food_dict['Food Name'] = self.foodname
        self.food_dict['Quantity'] = self.foodQuantity
        self.food_dict['Price'] = self.foodprice
        self.food_dict['Discount'] = self.fooddiscount
        self.finalprice = (int(self.foodprice)*(100-self.fooddiscount))/100
        self.food_dict['Final Price'] = self.finalprice
        self.food_dict['Stock'] = self.foodstock  
        food.food_list[self.food_id] = self.food_dict  
        food.first_food_id += 1
        print(f"\n{self.foodname} has been added.")
        print("\n\n----Available Food List Given Below\n")
        for p_id, p_info in food.food_list.items():
                print("\n---Food ID:", p_id)
                for key in p_info:
                    print(key + ':', p_info[key])
        self.admin_feature()

    def update_food(self):
        self.admin_input02 = int(input("Enter Food-ID:    "))
        if self.admin_input02 in food.food_list :
            admin_input03 = input("\n   What do you want to update?\n\nPress>>1.   Food Name\nPress>>2.   Quantity\nPress>>3.   Price\nPress>>4.   Discount\nPress>>5.   Stock\nPress>>0.   Back       ")
            print('-----------------------------------------------------------------------------------------------------')  
            if admin_input03 =="1":
                in1 = input("Enter New Food Name: \n")
                food.food_list[self.admin_input02]["Food Name"] = in1
            elif admin_input03 == "2":
                in2 = input("Enter New Quantity: \n")
                food.food_list[self.admin_input02]["Quantity"] = in2
            elif admin_input03 =="3":
                in3 = input("Enter New price: \n")
                food.food_list[self.admin_input02]["Price"] = in3
            elif admin_input03 == "4":
                in4= input("Enter New Discount: \n")
                food.food_list[self.admin_input02]["Discount"] = in4
            elif admin_input03 == "5":
                in5 =input("Enter New Stock: \n")
                food.food_list[self.admin_input02]["Stock"] = in5
            elif admin_input03 == "0":
                self.admin_feature()
            else:
                print("!!!Enter valid number!!!")
                self.update_food()
        else:
            print("Enter correct Food_Id\n")
            self.update_food()
           
           
    def remove_food(self):
        try:
            self.remove_foodid = int(input(" Enter food_id you want to remove: \n"))
            x = food.food_list[self.remove_foodid]['Food Name']
            if self.remove_foodid in food.food_list:
                del food.food_list[self.remove_foodid]
                print(f"\n{x} has been removed.\n")
            else:
                print("Food-Id is not valid ")
            self.admin_feature()
        except:
            print("\n!!!  You Have Entered Invalid Food-Id  !!! ")
            self.admin_feature()

    def food_menu(self):
        print("------------------------------Food List----------------------------------")
        for p_id, p_info in food.food_list.items():
            for i in p_info :
                print(end=' ')
            print(p_id,":",  f"{p_info['Food Name']}({p_info['Quantity']})[INR {p_info['Price']}]  ")
           
           
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44


class customer(food):
    customer_login_detail = {}
    order_history = {}
    customer_order = {}
#     dict1 = {}
   
    def __init__(self):
        print("----------------------Welcome to Food Delivery Application--------------------------\n")
        self.home()

    def home(self):
        print("------------------------------[HOME]----------------------------------\n")
        self.home_input = input("\nPress>>1.  Admin \nPress>>2.  Customer      ")
        if self.home_input == "1":
            self.admin_home()
        elif self.home_input == "2":
            self.customer_home()
        else:
            print("\n!!!Enter correct number!!!")
            self.home
           
    def customer_home(self):
        print("\n-----------------------------Customer Portal----------------------------------\n")
        self.admin_input = input("\nPress>>1.  Sign-Up\nPress>>2.  Sign-In\n")
        if self.admin_input == "1":
            self.customer_sign_up()
        elif self.admin_input =="2":
            self.customer_login()
        else:
            print("!!!Enter correct Number!!!")
            self.customer_home()        
       
    def customer_sign_up(self):
        print("Enter details for sign-up----------------")
        self.c_name = input("\nEnter Full-Name: ").upper()
        self.c_phone = input("\nEnter Phone Number: ")
        self.c_email = input("\nEnter Email: ")
        self.c_address = input("\nEnter Address: ")
        self.c_password = input("\nCreate Your Password: ")
        d_dict = {}
        d_dict["Name"] = self.c_name
        d_dict["Phone No."] = self.c_phone
        d_dict["Password"] = self.c_password
        d_dict["Address"] = self.c_address
        customer.customer_login_detail[self.c_email] = d_dict  
        print(f"\nWelcome {self.c_name} ")
        print(customer.customer_login_detail)
        print("\nSign-up is successfull.")
        time.sleep(1)
        print("\n.")
        time.sleep(1)
        print("\n.")
        self.customer_home()
       
    def customer_login(self):
        print("\n-------Enter Details To Sign-In------- ")
        self.cc_email = input("\nEnter Email: ")
        if self.cc_email in customer.customer_login_detail:
            self.cc_password = input("\nEnter Your Password: ")
            if customer.customer_login_detail[self.cc_email]['Password'] == self.cc_password:
                print("Login successful")
            else:
                print("Email or Password does not match!!!! ")
        else:
            print("Email found error!!!! ")
        self.cumtomer_option()
       
    def cumtomer_option(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
        option1 = input("Press>>1.   Place New Order \n\nPress>>2.   Last Order History \n\nPress>>3.   Update Profile \n\nPress>>0.   Home             \n")
        print("-----------------------------------------------------------------------------------------------------------")
        if option1 == "1":
            self.food_menu()
            self.placed_ordered()
        elif option1 =="2":
            self.history()
            self.cumtomer_option()
        elif option1 == "3":
            self.update_profile()
        elif option1 == "0":
            self.home()
        else:
            print("!!!Enter correct number!!!")
            self.cumtomer_option()
           
    def placed_ordered(self):
        print("\nNote: If you have multiple choice use comma(,) after select the number like 1,2,3 ....so on\n" )
        try:
            self.placed_ord = list(map(int,input("Enter Number:").strip().split(",")))
            self.total = 0
            self.dict1 = {}
            self.dict1['Food Name'] = []
            for i in self.placed_ord:
                self.dict1['Food Name'].append(food.food_list[i]["Food Name"])
                if food.food_list[i]["Stock"] > 0:  
                    print(food.food_list[i]["Food Name"],">>INR:",food.food_list[i]["Total Price"])
                    self.total = self.total + food.food_list[i]["Total Price"]
            print("Total Price : ",self.total)        
            self.placed_ordered_0()
        except:
            self.cumtomer_option()

    def placed_ordered_0(self):
        input_order = input('''If you want to place an order (p/P)
                                    Else Press>> Any Key                                ''').upper()
        if input_order == "P":
            print("To confirm your order please enter your username and password")
            self.confirm_input_u = input("Enter your Email: ")
            if self.confirm_input_u in customer.customer_login_detail:
                self.confirm_input_p = input("Enter your Password: ")
                if customer.customer_login_detail[self.cc_email]['Password'] == self.confirm_input_p:
                    print("Your order has been replaced.")
                    for i in self.placed_ord:
                        food.food_list[i]['Stock'] -= 1
                    self.time = time.asctime(time.localtime(time.time()))
                    self.dict1['Total Amount'] = self.total
                    self.dict1['Order Time'] = self.time
                    customer.order_history[self.confirm_input_u] = {}
                    customer.order_history[self.confirm_input_u][i] = self.dict1
                    self.cumtomer_option()
                else:
                    print("!!! You have entered wrong username or password !!!")
                    self.placed_ordered_0()
            else:
                print("!!! Enter Valid Username !!!")
                self.placed_ordered_0()
        else:
            print("Thank You")
            self.cumtomer_option()
       
    def history(self):
        print("---------Your Last Order History---------")
        s = input("Enter Your Email\n                      ")
        print(customer.order_history[s])
       
    def update_profile(self):
        self.mail = input("Enter Your Email: \n")
        if self.mail in customer.customer_login_detail:
            c_input = input("What do you want to update\nPress>>1.   Name \nPress>>2.   Contact No. \nPress>>3.   Password \nPress>>4.   Address")
            if c_input == "1":
                name = input("Enter Name: \n").upper()
                customer.customer_login_detail[self.mail]['Name'] = name
                print("Name has been updated.\n")
                self.cumtomer_option()
            elif c_input == "2":
                phone = input("Enter phone no.: \n")
                customer.customer_login_detail[self.mail]['Phone No.'] = phone
                print("Phone No. has been updated.\n")
                self.cumtomer_option()
            elif c_input == "3":
                passw = input("Enter Password")
                customer.customer_login_detail[self.mail]['Password'] = passw
                print("Password has been updated.\n")
                self.cumtomer_option()
            elif c_input == "4":
                add = input("Enter Your Address")
                customer.customer_login_detail[self.mail]['Address'] = add
                print("Address has been updated.\n")
                self.cumtomer_option()
        print(customer.customer_login_detail)      
#    =============================  COMPLETED  ==============================================  
       
adams = customer()