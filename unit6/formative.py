class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_url="localhost:5432", debug=False):
        if not self._initialized:
            self.db_url = db_url
            self.debug = debug
            self._initialized = True


config1 = Config("postgresql://localhost/mydb", True)
config2 = Config()

print(config1 is config2)
print(config1.db_url)
print(config1.debug)
print(config2.db_url)
print(config2.debug)


class Notification:
    
    def send(self, message):
        raise NotImplementedError("...")
    
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")
        
        
class SMSNotification(Notification): 
    def send(self, message):
        print(f"Sending SMS: {message}")
        
class NotificationFactory:
    @classmethod
    def create_notification(cls, type_name):
        if type_name == "email":
            return EmailNotification()
        elif type_name == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unknown notification type")
        
email_notification = NotificationFactory.create_notification("email")
email_notification.send("Your order has shipped")
sms_notification = NotificationFactory.create_notification("sms")
sms_notification.send("Your verification code is 02749")



class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Error, payment not processed ")
    
    
class ThirdPartyPayment: 
    def make_transaction(self, value):
        print(f"Third-party processing payment of {value}")
        
        
class ThirdPartyAdapter(PaymentProcessor): 
    def __init__(self, third_party_payment):
        self.third_party_payment = third_party_payment
        
    def process_payment(self, amount):
        self.third_party_payment.make_transaction(amount)
        

third_party_payment = ThirdPartyPayment()
adapter = ThirdPartyAdapter(third_party_payment)
adapter.process_payment(50)
        

class DataService:
    def get_data(self):
        return "Important data"
    
class LoggingDataService:
    def __init__(self, service):
        self.service = service
    
    def get_data(self):
        print("LOG: about to fetch data")
        result = self.service.get_data()
        return result
        
service = DataService()
logged_service = LoggingDataService(service)
data = logged_service.get_data()
print(data)


class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers = []
        
    def attach(self, observer):
            self.observers.append(observer)
            
    def detach(self, observer):
        self.observers.remove(observer)
            
    def notify_observers(self):
        for observer in self.observers:
                observer.update(self)
                
    def set_price(self, new_price):
        self.price = new_price
        self.notify_observers()
            
class MobileApp:
    def update(self, stock):
        print(f"MobileApp: {stock.name} new price is {stock.price}")
        
        
class EmailAlert:
    def update(self, stock):
        print(f"EmailAlert: {stock.name} new price is {stock.price}")
        

stock = Stock("ABC", 100)

mobile = MobileApp()
email = EmailAlert()

stock.attach(mobile)
stock.attach(email)

stock.set_price(120)
stock.set_price(90)





class DiscountStrategy:
    def apply(self, price):
        raise NotImplementedError("Subclasses must implement apply()")
    
class Nodiscount(DiscountStrategy):
    def apply(self, price):
        return price
    
    
class PercentageDiscount(DiscountStrategy): 
    def __init__(self, percentage):
        self.percentage = percentage 
        
    def apply(self, price):
        discount_amount = (price * self.percentage) / 100
        final_price = price - discount_amount
        return final_price
    
    
class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount
        
    def apply(self, price):
        result = price - self.amount 
        return result 


class Checkout:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy
        
    def final_price(self, original_price):
        return self.discount_strategy.apply(original_price) 
    
    
stratergy1 = Nodiscount()
checkout = Checkout(stratergy1)
result = checkout.final_price(100)
print(result)


stratergy2 = PercentageDiscount(10)
checkout = Checkout(stratergy2)
result = checkout.final_price(10)
print(result)


stratergy3 = FixedDiscount(5)
checkout = Checkout(stratergy3)
result = checkout.final_price(100)
print(result)




