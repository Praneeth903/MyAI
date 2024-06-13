                                                                                                Personal AI Assistant


This repository contains the code for "AI assistant" a voice-controlled AI assistant built using Python. AI can perform a variety of tasks, including providing the current time and date, searching Wikipedia, taking screenshots, sending emails, playing YouTube videos, sending WhatsApp messages, and more. Below is an explanation of each function in the code to help you understand its functionality.

Main file is ai.py.

Functions used in this code:
Main Loop 
  The main loop listens for voice commands and performs the corresponding actions.
  Commands include asking for the time or date, searching Wikipedia, taking screenshots, sending emails, playing YouTube videos, sending WhatsApp messages, searching the web, remembering information, playing or controlling songs, shutting down or restarting the PC, and more.
  If a command is not recognized, it sends the query to the AI model for a response.
  
 speak(audio) 
  Converts text to speech using the pyttsx3 library.
  It takes a string audio as input and speaks it out loud.
  
  time() 
  Announces the current time.
  Uses the datetime library to get the current time and the speak function to vocalize it.
  
  date() 
  Announces the current date.
  Uses the datetime library to get the current date and the speak function to vocalize it.
  
  youtube(ele)  
  Plays a YouTube video.
  Uses the pywhatkit library to search for and play the specified video.
  
  chrome(ele)  
  Searches the web using Chrome.
  Uses the pywhatkit library to perform the search.
  
  whatsapp(t, msg)  
  Sends a WhatsApp message.
  Uses the pywhatkit library to send a message instantly to the specified number t with the message msg.
  
  sendmail(to, msg)  
  Sends an email using SMTP.
  Logs in to a Gmail account and sends an email to the recipient to with the message msg.
  
  wish()  
  Greets the user based on the current time of day.
  Uses the datetime library to determine the appropriate greeting and the speak function to vocalize it.
  
  inp() 
  Listens for voice input from the user.
  Uses the speech_recognition library to capture and recognize speech, returning the recognized text.
  
  screenshot() 
  Takes a screenshot of the current screen.
  Uses the pyscreeze library to capture and save the screenshot.
  
  talktoai(query)  
  Sends a query to an AI model for a response.
  Uses the requests library to send a request to an AI service and speaks the response using the speak function.
  
Authorization Header: The headers variable contains an authorization token required to access the AI service.
AI Service URL: The url variable specifies the endpoint for the AI service used in talktoai.
Wikipedia Search: The wikipedia library is used to search for and summarize Wikipedia articles.
Sample Module: The sample module contains functions to play and control songs, which are invoked in the main loop.

Requirements:
Python 3.x
Libraries:
pyttsx3, datetime, speech_recognition, wikipedia, pyautogui, pyscreeze, json, requests, openai, pywhatkit, smtplib, sample, os

                                                                                                        How to Use 
Clone the repository.
Install the required libraries using pip install <library_name>.
Run the script using python script_name.py.
Interact with the AI assistant using voice commands.
This README provides a high-level overview of the functions in the  AI assistant. For more detailed usage and customization, refer to the code comments and documentation within the script.
