import pandas as pd
import numpy as np


def build_dataframe(logs):
    df = pd.DataFrame(logs)
    return df


def compute_averages(logs):
    df = pd.DataFrame(logs)

    if df.empty:
        return {}

    result = df.groupby("player")["score"].mean()
    return result.to_dict()


def generate_leaderboard(logs):
    df = pd.DataFrame(logs)

    if df.empty:
        return pd.DataFrame()

    board = df.groupby("player")["score"].sum().reset_index()
    board = board.sort_values(by="score", ascending=False)

    return board
