#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 17:37:39 2023

@author: sunyenpeng
"""
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

class JosephSun:
    def info(self,x):
        if x=="Age":
            print_slow("24 years old.")
        elif x=="experience":
            print_slow("I was a research assistant at ITRI for 1.5 years.\nSupport my team to build AI models for companies.")
        elif x=="education":
            print_slow("I majored in business management at National Sun yat-sen University.\nNow, I'm pursuing my Master of Science degree at Warwick Business School.")
        elif x=="name":
            print_slow("I am Joseph Sun from Taiwan.\n")
            print_slow("Do you want to connect me through LinkedIn?\n(y/n)\n")
            x=input()
            if x=="y":
                print_slow("Sure! Let's connect!")
                url = "https://www.linkedin.com/in/yen-peng-sun-50ab6819a/"  
                driver = webdriver.Chrome('/Users/sunyenpeng/Desktop/python/cooperation/chromedriver_mac_arm64 (2)/chromedriver')
                driver.get(url)
            elif x=="n":
                print_slow("Okay!\n")
        elif x=="certification":
            print_slow("I have 15+ Python & R Datacamp certifications.\nSuch as:\n Data Manipulation with pandas,\n Data Visulization with ggplot2,\n and Machine Learning with scikit-learn.")
        elif x=="skill":
            print_slow("R, Python, Microsoft Excel, PowerPoint, MySQL, Minitab")
            time.sleep(0.5)
            print("\nYou may want to know:\n My programming abilities?\n(y/n)")
            r=input()
            if r=="y":
                print_slow("Here you go!")
                time.sleep(1)
                categories = ['Data Cleaning', 'Data Manipulation', 'Data Visualization', 'Building Models', 'Developing']
                categories = [*categories, categories[0]]
                Python = [4.5, 5, 4, 4, 3.5]
                R = [4.5, 5, 4.5, 4.5, 2]
                Python = [*Python, Python[0]]
                R = [*R, R[0]]
                label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(Python))
                plt.figure(figsize=(6, 6))
                plt.subplot(polar=True)
                plt.plot(label_loc, Python, label='Python',color='r')
                plt.fill(label_loc, Python, facecolor='pink',alpha=0.5)
                plt.plot(label_loc, R, label='R')
                plt.fill(label_loc, R, facecolor='skyblue',alpha=0.5)
                plt.title('Skills Radar Plot', size=15)
                lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
                plt.legend()
                plt.show()
            elif r=="n":
                print_slow("Alright!\n")
        elif x=="personality":
            print_slow("My MBTI test result is 'INTJ-A'\nAlso known as 'Architecture personality'\n")
            print_slow("An Architect (INTJ) is a person with the Introverted, Intuitive, Thinking, and Judging personality traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.\n")
                
    def stat(self):
        print_slow("These are my achievements and stats...\n")
        print("Undergrad GPA:\n 3.6/4.0 \n")
        time.sleep(0.5)
        print("GRE:\n Quantitative:168\n Verbal:152\n")
        time.sleep(0.5)
        print_slow("The valedictorian of National Sun Yat-sen University class of 2020.\nDean's awards for 2 times\n2019-Foxconn Scholarships winner (top 5% over 7000+ students)\nMachine Learning competition-Excellent Award\nR programming competition-Excellent Award\n")
        print_slow("2020 Sri Lanka Volunteer Group-Class Manager\n")
        
    def interest(self):
        print_slow("Okay! I have listed some specific questions for you\nWhich one do you want to know...\n")
        time.sleep(0.5)
        print("1. My favorite anime character\n2. My favorite sport\n3. The person I admire the most\n4. Music?\n5. Anything else?\n")
        x=input()
        if x=="1":
            print("The Pokeman Pikachu is my all time favorite anime character!\nIt is so cute!")
            m="00111011001011010010111000100000001000000010000000100000001000000010000000100000001000000010000000100000010111110101111101011111001011000000101000100000001000000110000000101110011000000101110001011111001011100010111000101110001011100101111100101111011000000010111000101101001000100110000000001010001000000010000000100000001000000101110000100000001000000010000000100000001000000010000000100000001000000010111100100000001000000010000000100000001000000010000000101100000010100010000000100000001000000010000000101111001010000010100100100000001000000010000000101000001010010010000001011100001000000010000000100000001000000010111000100111001000000110000000101101001011100101111100001010001000000010000000100000011111000010100100100000001000000010111000100000001000000010000000100000001010000010100101011100001000000010000000101111001000000010000000100000010111110010111000100111000010100010000000100000001000000101110000100000001000000010110100100111001011010010000000100000001000000010000000100000001011000011101100100000001001110010111000100000001111000000101000100000001000000010000000100000001110110010111001011111010111110010000000100000001000000010000000100000001011000011101101111100001000000010000000100000001111100010000001011100000010100010000000100000001000000010111100100000001011000010000000100000001000000010000000101111001000000010110000100000001000000111110000101110001011010010011100101110001011010010011100001010001000000010000000101000010111110010111100100000001000000010000000100000001010000101111100101111001000000010110000111011011111000010111000111100011000000000101000100000001000000010000000100000010111000010000000100000001000000010000000101100001000000010000000100000001000000010000000111011001011010110000000001010001000000010000000100000001000000010000000111110001000000010000000100000010111000010000000100000001000000010000000101111000010100010000000100000001000000010000000101000010111110010110000101101001001110110000000111110001000000010111000100111000010100010000000100000001000000010000000100000001000000010000000100000001000000010100001011111001011000010011100001010"
            a=""
            for i in range(len(m)//8):
                a+=chr(int(m[8*i:8*(i+1)],2))
            print_slow(a)
            print_slow("Do you want to know more about my interests?\n(y/n)\n")
            z=input()
            if z=="y":
                JosephSun().interest()
            elif z=="n":
                print_slow("Okay!\n")
        elif x=="2":
            print_slow("Basketball, I was the captain of my department basketball team.\nI led my team win two championships in University Basketball League.\n")
            print_slow("Do you want to know more about my interests?\n(y/n)\n")
            z=input()
            if z=="y":
                JosephSun().interest()
            elif z=="n":
                print_slow("Okay!\n")
        elif x=="3":
            print_slow("Elon Musk. He is extremely smart and what he is doing is for the whole society but not for personal benefits.\nI also consider him a person with great vision.\nOverall, Elon Musk is my role model.\n")
            print_slow("Do you want to know more about my interests?\n(y/n)\n")
            z=input()
            if z=="y":
                JosephSun().interest()
            elif z=="n":
                print_slow("Okay!\n")
        elif x=="4":
            print_slow("I self-learned guitar and remix music on 'Garageband'.\n")
            time.sleep(1.5)
            print_slow("Oh! I almost forgot that I learned piano for only 2 weeks. I quit because the teacher is too harsh for me as I was only 6 years old then.\n")
            print_slow("Do you want to know more about my interests?\n(y/n)\n")
            z=input()
            if z=="y":
                JosephSun().interest()
            elif z=="n":
                print_slow("Okay!\n")
        elif x=="5":
            print_slow("I built Gunpla model kits and installed LED on them. I mean... every male loves glowing robot, right?\nSo I made for myself.\n")
            print_slow("Do you want to know more about my interests?\n(y/n)\n")
            z=input()
            if z=="y":
                JosephSun().interest()
            elif z=="n":
                print_slow("Okay!\n")
        else:
            print_slow("I have many other interests\nif you want to know more about me\nYou can reach me through LinkedIn:\nhttps://www.linkedin.com/in/yen-peng-sun-50ab6819a/ .\n")
            print_slow("Do you want to know more about my interests?\n(y/n)\n")
            z=input()
            if z=="y":
                JosephSun().interest()
            elif z=="n":
                print_slow("Okay!\n")
if __name__ =="__main__":
    while True:
        time.sleep(0.5)
        print("\nWhat do you want to know about me?")
        print(" 1. What is your name?\n 2. Any achievements or awards?\n 3. What did you do before graduate school?\n 4. What are your interests?\n 5. What certifications do you have?\n 6. What skills do you have?\n 7. How do you consider yourself? Or your personality test?\n(Press 1,2,3...to select your question...)")
        y=input()
        if y == "1":
            JosephSun().info("name")
        elif y == "2":
            JosephSun().stat()
        elif y == "3":
            JosephSun().info("experience")
        elif y == "4":
            JosephSun().interest()
        elif y == "5":
            JosephSun().info("certification")
        elif y == "6":
            JosephSun().info("skill")
        elif y == "7":
            JosephSun().info("personality")
        else:
            print("Please Enter 'Numeric' numbers")
            