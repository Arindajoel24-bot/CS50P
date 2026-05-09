def main():
    while True:
        fuel = input("Fraction: ")
        
        try:
            percentage = convert(fuel)
        except (ValueError, ZeroDivisionError):
             continue
        print(gauge(percentage))
        break
def convert(fraction):           
            fraction = fraction.split("/")
            x = int(fraction[0])
            y = int(fraction[1])

            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                 raise ValueError
                    
            return round(x/y * 100)
            
            
def gauge(percentage):                       
        if percentage <= 1:
            return "E"
            
        elif percentage >= 99:
            return "F"
            
        else:
            return f"{percentage}%"
                
if __name__ == "__main__":
     main()                
            

