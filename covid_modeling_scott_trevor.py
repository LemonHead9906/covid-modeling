 # Simple COVID-19 Exponential Growth Simulator Template -- Trevor S -- 5/1/2020 -- 9:46 AM -- 1.0

import time

num_infected_ppl = 0
current_day = 0
days_sim = 0
num_deaths_ppl = 0

print("This program will model potential Covid-19 infections and deaths in the U.S. Right now, the number of infections doubles evry six days.\n")
time.sleep(4)

num_infected_ppl = int(input("How many people are currently infected? Please enter an INTERGER number with no commas. Then press enter.    "))
days_sim = int(input("How many days of infection growth do you want to stimulate? Please enter an INTERGER number with no commas. Then press enter.    "))

print(f"The number of people infected with Covid-19 is {num_infected_ppl:,} and you will stimulate {days_sim} days worth of infection growth.\n")


while Current day <= days_sim:
    
    current_day += 6
    num_infected_ppl += num_infected_ppl 
    num_deaths_ppl = round(num_infected_ppl *0.023)
    print(f"On day {current_day} there will be {num_infected_ppl:,) infections and approximately {num_deaths_ppl:,} people will die from Covid-19.\n") 
    time.sleep(4)

print(f"After the simulation completes there will be {num_infected_ppl:,) infections and approximately {num_deaths_ppl:,} people will die from Covid-19.\n")


I Hope you can see this now.

  
