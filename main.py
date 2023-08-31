#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/11
#
#Purpose:       The purpose of this is to write a complete Python 
#               program that computes the X and Y coordinates for a parabola 
#               and an elliptical arc, then plots both separately & together.

from time import ctime
import numpy as np
import matplotlib.pyplot as plt

def displayTerminationMessage():
    print(f"""
Programmed by Farjad Tariq
Date: {ctime()}
End of processing.\n""")

def getPositiveFloat(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input, please enter a number.")

def getPositiveInt(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input, please enter a number.")

def computeXcoordinates(maxX, intervals):
    #maxX = the max value along the x-axis
    #intervals = number of intervals
    
    return np.linspace(0, maxX, intervals + 1)

def ellipticArc(a, b, xCoordinates):
    #a = length of the semi-major axis
    #b = length of the semi-minor axis
    #yCoordsArc = list of y Coordinates of the arc
    #xCoordinates = list of x Coordinates
    
    return np.array(b * np.sqrt(1 - (xCoordinates / a)**2))

def parabola(h, k, xCoordinates):
    #h = one half the width of the parabola
    #k = height of the parabola
    #yCoordsParabola = list of y Coordinates of the parabola
    #xCoordinates = list of x Coordinates
    #a = -k / h * h
    
    a = -k / h ** 2
    return np.array(a * (xCoordinates - h) ** 2 + k)

def plotGraph(xCoords1, yCoords1, xCoords2, yCoords2):
    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(xCoords1, yCoords1, 'g-')
    plt.ylabel('F(X)')
    plt.xlabel('X')
    plt.title('Elliptic Arc')

    plt.subplot(3, 1, 2)
    plt.plot(xCoords2, yCoords2, 'r-')
    plt.ylabel('F(X)')
    plt.xlabel('X')
    plt.title('Parabola')

    plt.subplot(3, 1, 3)
    plt.plot(xCoords1, yCoords1, 'g-', xCoords2, yCoords2, 'r-')
    plt.legend(['Elliptic Arc', 'Parabola'], loc='best')
    plt.ylabel('F(X)')
    plt.xlabel('X')
    plt.title('Elliptic Arc vs Parabola')

    plt.tight_layout()
    plt.show()
    
def main():
    print('\n' + '-' * 80)
    
    intervals = getPositiveInt('Enter the number of intervals (>0): ')
    maxX = getPositiveFloat('Enter the maximum X coordinate (>0): ')
    maxY = getPositiveFloat('Enter the maximum Y coordinate (>0): ')

    xCoords = computeXcoordinates(maxX, intervals)
    yCoords1 = ellipticArc(maxX, maxY, xCoords)
    yCoords2 = parabola(maxX/2, maxY, xCoords)
    
    plotGraph(xCoords, yCoords1, xCoords, yCoords2)
    
    displayTerminationMessage()

main()
