# Summer Projects Collection

Welcome to my 2025 summer programming projects! This repository contains a collection of small but interesting coding challenges and exercises I've worked on during my summer break. Each project demonstrates different programming concepts and problem-solving approaches.

## Table of Contents
FizzBuzz Program

Scrabble Word Finder Program

4 Gallon Water Bucket Problem

## FizzBuzz Program
Description
The classic FizzBuzz programming challenge! This program prints numbers from 1 to a specified limit (100 in my code), but with a twist:

**Fizz** - printed for numbers divisible by 3

**Buzz** - printed for numbers divisible by 5

**FizzBuzz** - printed for numbers divisible by both 3 and 5

## Scrabble Word Finder Program
This is a simple Python program with an interactive artifact that finds all valid Scrabble words that can be formed from a given set of letters. It first generates all possible permutations of the input letters and checks them against a local scrabble dictionary file to produce an alphabetized list of valid words in the Scrabble game. 

In my program, I uses "tabind" as the given combinations of words if one does not provide any word. Of course, you can modify the my_letters variable inside the Python script or type different words on the program to the set of letters you want to check.
This is what the interactive artifact looks like: 
![Screenshot 2025-07-01 at 4 52 36 PM](https://github.com/user-attachments/assets/4371c490-f49f-422e-a38a-2f66945e3ecb)

### Acknowledgments
The words.txt file used in this project is a comprehensive dictionary of Scrabble words sourced from the scrabble repository on GitHub, maintained by user redbo.

You can find the original repository and file here: github.com/redbo/scrabble

## 4 Gallon Water Project
Objective: 
This program solves the classic water measurement problem where two kids need to 
fetch exactly 4 gallons of water from a stream using only two unmarked buckets: 
- One 5-gallon bucket (defined as bucket1 in the code)
- One 3-gallon bucket (defined as bucket2 in the code)

Specifically, I used Breadth-First Search (BFS) to find the optimal solution in 
minimum steps and returns all possible solutions in less than 15 steps.
