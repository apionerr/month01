#-- Static variables
time = 30

#-- Define growth of savings account
def savings_rate(income, rate, time):
    savings_as_percent = (int(income) * int(rate))/100      #Dollar ammount of percent to save
    savings_account = [0]                                   #Staring ammount of value to return
    current = savings_account[len(savings_account)-1]       #The value for each year

    for i in range(1, int(time)):                           #Iterate year over year
        adjust = (savings_as_percent + current) * i         #Growth = Years savings + the current * i
        savings_account.append(adjust)                      #Add another year to the list

    return savings_account                                  #Return the list


#-- Define growth if yearly it were invested into stock market

#-- Low growth at 3 percent yearly
def low_growth(savings):
    rate = 3
    first_year = savings[1] +((savings[1] * rate) / 100)
    low_growth_account = [0, first_year]
    for i in range(1, 30):
        save = (((savings[1] + low_growth_account[i]) * rate) / 100) + low_growth_account[i] + savings[1]
        low_growth_account.append(save)

    return low_growth_account

#-- mid growth at 5 percent yearly
def mid_growth(savings):
    rate = 5
    first_year = savings[1] +((savings[1] * rate) / 100)
    mid_growth_account = [0, first_year]
    for i in range(1, 30):
        save = (((savings[1] + mid_growth_account[i]) * rate) / 100) + mid_growth_account[i] + savings[1]
        mid_growth_account.append(save)

    return mid_growth_account

#-- Low growth at 8 percent yearly
def high_growth(savings):
    rate = 8
    first_year = savings[1] +((savings[1] * rate) / 100)
    high_growth_account = [0, first_year]
    for i in range(1, 30):
        save = (((savings[1] + high_growth_account[i]) * rate) / 100) + high_growth_account[i] + savings[1]
        high_growth_account.append(save)

    return high_growth_account

#-- retreive information
income = raw_input("What is your annual income?")
to_save = raw_input("Percent of income to save annualy? Example: 3 is 3%")

#-- Run report

savings = savings_rate(income, to_save, 30)
low = low_growth(savings)
mid = mid_growth(savings)
high = high_growth(savings)


#-- Create document
outlook = open("investment.txt", "w")
information = "Income: ${},  Time to save: {} years.".format(income, time)
outlook.writelines(information)
header = "\nYEAR | SAVINGS |    lOW   |   MID   |   HIGH   |"
outlook.writelines(header)

for i in range(1, time):
    it = "\n{}       {}       {}       {}       {}      ".format(i, savings[i], low[i], mid[i], high[i])
    outlook.writelines(it)
outlook.close()
