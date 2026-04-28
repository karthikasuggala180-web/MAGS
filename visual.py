import matplotlib.pyplot as plt
import pandas as pd


def bar_chart(logs):
    df = pd.DataFrame(logs)

    board = df.groupby("player")["score"].sum()

    board.plot(kind="bar")
    plt.title("Leaderboard")
    plt.xlabel("Player")
    plt.ylabel("Score")
    plt.show()


def line_chart(logs):
    df = pd.DataFrame(logs)

    plt.plot(df["score"])
    plt.title("Player Performance")
    plt.xlabel("Game Number")
    plt.ylabel("Score")
    plt.show()


def pie_chart(logs):
    df = pd.DataFrame(logs)

    games = df["game"].value_counts()

    games.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Game Distribution")
    plt.ylabel("")
    plt.show()
