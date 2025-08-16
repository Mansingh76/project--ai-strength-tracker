
import streamlit as st
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- Load or initialize data ---
if os.path.exists("users.csv"):
    users = pd.read_csv("users.csv")
else:
    users = pd.DataFrame({"user_id":[1,2],"name":["Aman","Ravi"]})

if os.path.exists("workouts.csv"):
    workouts = pd.read_csv("workouts.csv")
else:
    workouts = pd.DataFrame(columns=["user_id","exercise","sets","reps","weight","rpe","date"])

if os.path.exists("nutrition.csv"):
    nutrition = pd.read_csv("nutrition.csv")
else:
    nutrition = pd.DataFrame(columns=["user_id","date","calories","protein_g","carbs_g","fats_g"])
