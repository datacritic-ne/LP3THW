def cryptos(bitcoins, bcashs, ethers):
    crypto_value = 66000 * bitcoins + 500 * bcashs + 3400 * ethers
    print(f"So, you have {bitcoins} Bitcoin, {bcashs} Bitcoin Cash units, and {ethers} Ether.")
    print(f"By my math, that's worth ${crypto_value}.")
    print("Dang, you're rich!")

# Ancillary function
def portfolio(dollars):
    portfolio_bitcoin = dollars * 0.8
    portfolio_bcash = dollars * 0.1
    portfolio_ether = dollars * 0.1
    cryptos(portfolio_bitcoin, portfolio_bcash, portfolio_ether)

# Call #1: Just give it values
cryptos(3, 20, 10)

# Call #2: Make it do a little math
cryptos(1 + 11, 50 + 35, 10 + 9)

# Call #3: Give it global variable inputs
amt_bitcoin = 5
amt_bcash = 100
amt_ether = 17
cryptos(amt_bitcoin, amt_bcash, amt_ether)

# Call #4: Combine global variable and math inputs
cryptos(amt_bitcoin + 2, amt_bcash + 32, amt_ether + 21)

# Call #5: Use user inputs
bitcoin_input = input("How many Bitcoin do you own? ")
bcash_input = input("How many Bitcoin Cash do you own? ")
ether_input = input("How many Ether do you own? ")
cryptos(int(bitcoin_input), int(bcash_input), int(ether_input))

# Call #6: Combine user inputs and math
cryptos(int(bitcoin_input) + 2, int(bcash_input) + 25, int(ether_input) + 1)

# Call #7: Use the ancillary function to feed the crypto function arguments, with a specified dollar value
portfolio(100000)

# Call #8: Use the ancillary function to feed the crypto function arguments, giving it a global variable input
amt_dollars = 5000
portfolio(amt_dollars)

# Call #9: Use the ancillary function to feed the crypto function arguments, combining a global variable and math
portfolio(amt_dollars + 1000)

# Call #10: Use the ancillary function to feed the crypto function arguments, with user input
dollar_input = input("How many dollars do you have to invest? ")
portfolio(int(dollar_input))

