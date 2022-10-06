# **Battleship CLI** - Python deployed on Heroku

<a href='https://python-battleship-cli-game.herokuapp.com/'><img src='' alt='Main screen of the website'></a>

### [Live Webiste](https://python-battleship-cli-game.herokuapp.com/)

<br/>

# Table of Contents 
* [Introduction](#introduction)
* [How To Play](#How-To-Play)
* [Features](#features)
* [UX](#ux)
* [Testing](#testing)
* [User Stories](#user-stories)
* [Credits](#credits)
* [Deployment](#deployment)

<br/>

# Introduction  

<img src='' alt='flow of webiste on mobile screen'>


**Time frame to finish this project was about 15-20 hours.** 

# How To Play

# Features 



# UX

## Wire Frames


# Testing


## Manual Testing

Input testing - Placing boats

**Boat size 5 ■■■■■**
| Input      | Expected       | Result
| -----------| -------------  |------------- 
|   1,1      | Pass           | ✓
|   9,9      | Fail           | ✓
|   6,1      | Fail           | ✓
|   a,b      | Fail           | ✓
|   0,1      | Fail           | ✓
|   1,0      | Fail           | ✓
|   11       | Fail           | ✓
|   1,11     | Fail           | ✓
|   asd      | Fail           | ✓

**Boat size 1 ■**
| Input      | Expected       | Result
| -----------| -------------  |------------- 
|   1,1      | Pass           | ✓
|   9,9      | Pass           | ✓
|   6,1      | Pass           | ✓
|   a,b      | Fail           | ✓
|   0,1      | Fail           | ✓
|   1,0      | Fail           | ✓
|   11       | Fail           | ✓
|   1,11     | Fail           | ✓
|   asd      | Fail           | ✓

**Attempt to place boat on already taken up square**
Boat size | Input      | Expected       | Result
----------| -----------| -------------  |------------- 
5 ■■■■■| 1,1      | Pass           | ✓
4 ■■■■| 1,1      | Fail           | ✓
4 ■■■■| 2,1      | Fail           | ✓
4 ■■■■| 3,1      | Fail           | ✓
2 ■■| 6,1      | Pass           | ✓

**Attempt to place boat outside the grid**
Boat size | Input      | Expected       | Result
----------| -----------| -------------  |------------- 
5 ■■■■■| 5,1      | Pass           | ✓
5 ■■■■■| 6,1      | Fail           | ✓
5 ■■■■■| 0,1      | Fail           | ✓
5 ■■■■■| 5,5      | Fail           | ✓
4 ■■■■| 6,1      | Pass           | ✓
4 ■■■■| 7,1      | Fail           | ✓


Input testing - Shooting boats
| Input      | Expected       | Result
| -----------| -------------  |------------- 
|   1,1      | Pass           | ✓
|   9,9      | Pass           | ✓
|   6,1      | Pass           | ✓
|   a,b      | Fail           | ✓
|   0,1      | Fail           | ✓
|   1,0      | Fail           | ✓
|   11       | Fail           | ✓
|   1,11     | Fail           | ✓
|   asd      | Fail           | ✓

Note - Shooting at the same already shoot square is a feature. In real life you can shoot multiple times at the same location so to keep my game realistic I have decided to let the user and the computer shoot at a already shot square if they choose to do so.

##  Validator Testing


## Issues and Fixes 



# User Stories
### Some of user stories that got completed 

| #           | User Story      
| ----------- | ------------- 
| 1           | 
| 2           | 
| 3           | 
| 4           | 
| 5           | 
| 6           | 
| 7           | 
| 8           | 
| 9           |       
| 10          | 

<br/>

### Some of user stories are planned for next sprint

| #           | User Story      
| ----------- | ------------- 
| 1           | 
| 2           | 
| 3           | 
| 4           | 


# Credits


# Deployment


