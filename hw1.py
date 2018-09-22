# Matthew Pham - mdpham2
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

def histogram_times(filename):
    crashTimes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    isFirstLine = False
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')    
        for row in csv_reader:
            if(not isFirstLine):
                isFirstLine = True
                continue
            hour = ((f'{row[1]}')).replace('c:', '')
            hour = hour.replace('c', '')
            hour = hour[0:2]
            if(':' in hour):
                hour = hour.replace(':','')
                hour = '0'+hour
            if(hour == ''):
                continue
            crashTimes[int(hour)] = crashTimes[int(hour)] + 1
        return crashTimes
            
def weigh_pokemons(filename, weight):
    pokemonNames = []
    with open(filename) as json_data:
        pokemonJson = json.load(json_data)
        for pokemon in pokemonJson['pokemon']:
            pokemonWeight = pokemon['weight'].replace(' kg', '')
            if(float(pokemonWeight) == weight):
                pokemonNames.append(pokemon['name'])
    return pokemonNames
         
def single_type_candy_count(filename):
    numCandies = 0
    with open(filename) as json_data:
        pokemonJson = json.load(json_data)
        for pokemon in pokemonJson['pokemon']:
            pokemonType = pokemon['type']
            if(len(pokemonType) == 1):
                if('candy_count' in pokemon.keys()):
                    numCandies = numCandies + pokemon['candy_count']
        return numCandies     

def reflections_and_projections(points):
    print(math.e)
    def rotateX(point):
        x, y = point
        angle = math.radians(90)
        fx = math.sin(angle) * (y)
        return fx
    def rotateY(point):
        x, y = point
        angle = math.radians(90)
        fy = -math.sin(angle) * (x)
        return fy;
    def dotProduct(point1, point2):
        x, y = point1
        x1, y1 = point2
        return (x* x1) + (y * y1)
    def magnitude(vector):
        x,y = vector
        return math.sqrt(math.pow(x,2) + math.pow(y, 2))
    reflect = list(map(lambda y: -1*(y-1)+1, points[1]))
    points[1] = reflect
  
    for i in range(points[0].size):
        xvalue = points[0][i]
        yvalue = points[1][i]
        points[0][i] = rotateX((points[0][i], points[1][i]))
        points[1][i] = rotateY((xvalue, yvalue))
    for i in range(points[0].size):
        xvalue = points[0][i]
        yvalue = points[1][i]
        points[0][i] = round(xvalue*(dotProduct((xvalue, yvalue), (1,3)))/(math.pow(magnitude((xvalue, yvalue)),2)))
        points[1][i] = round(yvalue*(dotProduct((xvalue, yvalue), (1,3)))/(math.pow(magnitude((xvalue, yvalue)),2)))
    return points   
        

def normalize(image):
    max = image[0][0]
    min = image[0][0]
    for i in range(32):
        for j in range(32):
            if(image[i][j] > max):
                max = image[i][j]
            if(image[i][j] < min):
                min = image[i][j]
    for i in range(32):
        for j in range(32):
            p = image[i][j]
            image[i][j] = (255/(max-min)) * (p - min)
    return image
            
def sigmoid_normalize(image, a):
    for i in range(32):
        for j in range(32):
            p = image[i][j]
            image[i][j] = 255 * math.pow((1 + math.pow(math.e, math.pow(a, -1) * (p-128))), -1)
    return image

