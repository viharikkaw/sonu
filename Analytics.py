import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_energy_data(filepath="data\energy_data.csv"):
    df = pd.read_csv(filepath,parse_dates=['timestamp'])
    return df 

def visualize_daily_usage(df):
    df['date'] = df['timestamp'].dt.date
    daily_usage = df.groupby('date')['total_usage'].sum().reset_index()

    fig, ax= plt.subplots(figsize=(12,5))
    sns.lineplot(data=daily_usage, x='date', y='total_usage',ax=ax, marker='o')
    ax.set_title("Dailt Energy Usage Over Time")
    ax.set_xlabel = ("Date")
    ax.set_ylabel = ("KWh")
    plt.xticks(rotation=45)
    return fig

def usage_by_appliance(df):
    avg_usage = df[['ac_usage','fridge_usage','washing_machine_usage','lights_usage']].mean()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(avg_usage, labels=avg_usage.index,autopct='%1.1f%%', startangle=90)
    ax.set_title("Average Energy Use by Appliance")
    return fig

def hourly_pattern(df):
    df['hour'] = df['timestamp'].dt.hour
    hourly_avg = df.groupby('hour')['total_usage'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10,4))
    sns.barplot(data=hourly_avg, x='hour', y='total_usage',ax = ax,  palette='viridis')
    ax.set_title("Average Hourly Energy Usage")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Hour of Day")
    return fig