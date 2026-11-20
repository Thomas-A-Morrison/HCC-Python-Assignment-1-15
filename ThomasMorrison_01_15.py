# Class: COP-1030-2
# Programmer: Thomas A. Morrison
# Program: Assignment 1.15
# Date: 25 AUG 2026
# Description: This program will print the state sales tax rates for five U.S. states.
# Data: The data was found 25 AUG 2026 on https://taxfoundation.org/data/all/state/sales-tax-rates.

# Declare variables
alabamaSalesTax = 0.04
alaskaSalesTax = 0.00
arizonaSalesTax = 0.056
arkansasSalesTax = 0.065
californiaSalesTax = 0.0725

# Print the sales tax rates
print("Sales Tax Rates by State:")
print("-------------------------")
print(f"Alabama:    {(alabamaSalesTax * 100): .3f}%")
print(f"Alaska:     {(alaskaSalesTax * 100): .3f}%")
print(f"Arizona:    {(arizonaSalesTax * 100): .3f}%")
print(f"Arkansas:   {(arkansasSalesTax * 100): .3f}%")
print(f"California: {(californiaSalesTax * 100): .3f}%")
