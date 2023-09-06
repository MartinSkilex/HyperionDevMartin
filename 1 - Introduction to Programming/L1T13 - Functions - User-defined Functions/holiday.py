
#Asking user for holiday details
city_flight = input("Choose destiantion (Cape Town, Durban, Johannesburg, Harare):")

num_nights = int(input("Please enter number of nights you staying at a hotel:"))

rental_days = int(input("The numnber of days you will rent the car for: "))

#function for total hotel cost
def hotel_cost(num_nights):
    #price per night cost
    price_per_night = 400

    #total price for number of nights stayed at hotel calculation 
    total_cost = num_nights * price_per_night

    return total_cost

#function for plane cost
def plane_cost(city_flight):
    # Flight prices for different cities
    if city_flight == "Cape Town":
        flight_price = 1500

    elif city_flight == "Durban":
        flight_price = 2000

    elif city_flight == "Johannesburg":
        flight_price = 1000

    else:
        flight_price = 4500

    return flight_price

#function for total car rental cost
def car_rental(rental_days):

    #daily rental cost for the car
    daily_rental_price = 800

    #total price for number of days of car rental calculation
    total_rental = daily_rental_price * rental_days

    return total_rental

#function for total holiday costs
def holiday_cost (num_nights,city_flight,rental_days):
    
    # Calculating the total holiday cost by calling the other functions
    total_holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

    return total_holiday_cost


# Calculating the holiday cost
total_cost = holiday_cost(num_nights,city_flight,rental_days)

#Displaying holiday details
print("\nHoliday Details")
print("City: " + city_flight)
print("Number of nights at the hotel: " + str(num_nights))
print("Number of days for car rental: " + str(rental_days))

print("The holiday total cost is R" + str(total_cost))