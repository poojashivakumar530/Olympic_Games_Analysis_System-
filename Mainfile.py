import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

df = pd.read_csv(r"<paste csv/excel file path here>", encoding="cp1252")

def menu():
    ans = True
    while ans:
        print("""
   :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
   :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    OLYMPICS GAMES ANALYSIS SYSTEM
   :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
   :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
     1-Data Visualisation
     2-Data Analysis
     3-Read CSV/EXCEL file
     4-Data Manipulation
     5-Exit
   :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""")
        inp = int(input("enter your choice:"))
        if inp == 1:
            datavisual()
        elif inp == 2:
            odanalysis()
        elif inp == 3:
            read_csv_excel()
        elif inp == 4:
            manuplt()
        elif inp == 5:
            ex = input("are you sure you want to exit?(y/n)")
            if ex == 'y' or ex == 'Y':
                print("exiting now......Done!\nhave a nice day!!")
                sys.exit()
        else:
            print("\ninvalid input try again")


def datavisual():
    ans = True
    while ans:
        print('''
  =======================================================
  DATA VISUALISATION OF TOP 10 COUNTRIES
  =======================================================
  1-Line Chart-> COUNTRIES VS TOTAL MEDALS
  2-Line Chart-> COUNTRIES VS TOTAL NO.OF TIMES PARTICIPATED(IN SUMMER& WINTER)
  3-Bar Chart->COUNTRIES VS TOTAL NO. OF GOLD MEDALS
  4-Bar Chart->COUNTRIES VS TOTAL NO. OF SILVER MEDALS
  5-Bar Chart->COUNTRIES VS TOTAL NO. OF BRONZE MEDALS
  6-Pie Chart->DISTRIBUTION OF GOLD,SILVER & BRONZE MEDALS
  7-Bar Chart->COUNTRIES VS TOTAL NO. OF MEDALS(IN SUMMER & WINTER)
  8-Exit to Main Menu
  =======================================================
  =======================================================''')
        ans = input("please enter your choice:")
        if ans == '1':
            line_chart1()
        elif ans == '2':
            line_chart2()
        elif ans == '3':
            bar_chart1()
        elif ans == '4':
            bar_chart2()
        elif ans == '5':
            bar_chart3()
        elif ans == '6':
            pie_chart()
        elif ans == '7':
            dbargraph()
        elif ans == '8':
            menu()
        else:
            print("\ninvalid choice try again")
            continue


def line_chart1():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    df = df.sort_values(by="TotalMedal", ascending=False, inplace=True)
    df = df.loc[:, ['Country', 'TotalMedal']]
    df1 = df.head(10)
    Countries = df1["Country"]
    TotalMedal = df1["TotalMedal"]
    pl.plot(Countries, TotalMedal, linestyle=":", color="green", marker=",")
    pl.xlabel("Country ~ ~ ~ ~>", fontsize=12, color="r")
    pl.ylabel("Total Medals~ ~ ~ ~ >", fontsize=12, color="r")
    pl.title("TOTAL MEDALS WON BY TOP 10 COUNTRIES\n", color="blue", fontsize=18)
    pl.show()


def line_chart2():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    df.sort_values(by="TotalTimesPart", ascending=False, inplace=True)
    df = df.loc[:, ["Country", "SummerTimesPart", "WinterTimesPart"]]
    df1 = df.head(10)
    Countries = df1["Country"]
    Stotal = df1["SummerTimesPart"]
    Wtotal = df1["WinterTimesPart"]
    pl.plot(Countries, Stotal, linestyle="dashed", color="orange", label="Summer", marker="+")
    pl.plot(Countries, Wtotal, linestyle="dashed", color="dimgrey", label="Winter", marker="+")
    pl.xlabel("Country~ ~ ~ ~ ~ >", fontsize=12, color="r")
    pl.ylabel("no.of times partipated~ ~ ~ ~ >", fontsize=12, color="r")
    pl.title("TOTAL NO.OF TIMES PARTIPACIPATED BY TOP 10 COUNTRIES\n", color="blue", fontsize=18)
    pl.legend()
    pl.show()


def bar_chart1():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    df = df.sort_values("Tgoldmedal", ascending=False)
    df1 = df.head(n=10)
    x = np.arange(len(df1))
    Countries = df1["Country"]
    Totalgold = df1["Tgoldmedel"]
    pl.bar(x + 0.25, Totalgold, width=.6, label="Total No.of Gold Medal by Top 10 Countries ", color="gold")
    pl.xticks(x, Countries, rotation=30)
    pl.title("Olympics Gold Medal Analysis of Top 10 Countries", color="blue", fontsize=16)
    pl.xlabel("Countries~ ~ ~ ~ ~ >", fontsize=12, color="red")
    pl.grid()
    pl.legend()
    pl.show()


def bar_chart2():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    df = df.sort_values("Tsilvermedal", ascending=False)
    df1 = df.head(n=10)
    x = np.arange(len(df1))
    Countries = df1["Country"]
    Totalsilver = df1["Tsilvermedal"]
    pl.bar(x + 0.25, Totalsilver, width=6, label="Total No.of Silver Medal by Top 10 countries", color="silver")
    pl.xticks(x, Countries, rotation=30)
    pl.title("Olymbics Silver Medal Analysis of Top 10 Countries", color="blue", fontsize=16)
    pl.xlabel("Contries~ ~ ~ ~ ~ >", fontsize=12, color="red")
    pl.ylabel("No.of Silver Medal~ ~ ~ ~ ~ >", fontsize=12, color="red")
    pl.grid()
    pl.legend()
    pl.show()


def bar_chart3():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    df = df.sort_values("Tbronzemedal", ascending=False)
    df1 = df.head(n=10)
    x = np.arange(len(df1))
    Countries = df1["Country"]
    Totalbronze = df1["Tbronzemedal"]
    pl.bar(x + 0.25, Totalbronze, width=.6, label="Total No.of Bronze Medal by Top 10 Countries", color="peru")
    pl.xticks(x, Countries, rotation=30)
    pl.title("Olymbics Bronze Medal Analysis of Top 10 Countries", color="blue", fontsize=16)
    pl.xlabel("Countries~ ~ ~ ~ ~ >", fontsize=12, color="red")
    pl.ylabel("No.of Bronze Medal~ ~ ~ ~ ~ >", fontsize=12, color="red")
    pl.grid()
    pl.legend()
    pl.show()


def pie_chart():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    df.sum(axis=0, skipna=True)
    lst = df.iloc[:, 6:9], sum(axis=0)
    lst.value.tolist()
    clm = ["Bronze", "Silver", "Gold"]
    pl.title("Medal Distribution", color="navy")
    pl.pie(lst, label=clm, autopct="%1.1f%%", color=["brown", "silver", "gold"], shadow=True)
    pl.legend(loc="upper left")
    pl.show()


def dbargraph():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    df.sort_values(by="Totalmedal", ascending=False, inplace=True)
    df1 = df.head(n=10)
    x = np.arange(len(df1))
    Countries = df["Country"]
    SummerMedal = df1["SummerMedal"]
    Wintermedal = df1["WinterMedal"]
    pl.bar(x - 0.25, SummerMedal, label="Total No.of Medals By Top 10 Countries IN Summer", width=0.4, color="oranred")
    pl.bar(+ 0.25, Wintermedal, label="Total No.of Medals By Top 10 Countries IN Winter", width=0.4, color="grey")
    pl.xticks(x, Countries, rotation=20)
    pl.title("Olymbics Medal Analysis by Top 10 Countries", color="navy", fontsize=16)
    pl.xlabel("Countries~ ~ ~ ~ ~ >", fontsize=12, color="r")
    pl.ylabel("No.of Medals~ ~ ~ ~ ~ >", fontsize=12, color="r")
    pl.grid()
    pl.legend()
    pl.show()


def odanalysis():
    while True:
        print(" < -------------------------------- > ")
        print("Data Frame Analysis ")
        print("< --------------------------------- > ")
        mn = '''1)T print Top Records by Total Medals Won
          \n 2) To print Top Records by Total Gold Medals Won
          \n3)  To print Top Records by Total Silver Medals Won
          \n4) To print Top Records by Total Bronze Medals Won
          \n5) To print Bottom Records
          \n6) To print the general information of the dataframe
          \n7) To describe the dataframe
          \n8) To print specified column data
          \n9) to print maximum value for each column
          \n10)To go back to the main menu'''
        print(mn)
        x = int(input("Enter Your choice "))
        print("------------------x-------------------------x--------------------------x----------------------x ")
        df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
        if x == 1:
            df = df.sort_value("TotalMedal", ascending=False)
            nor = int(input("Enter the number of records to be displayed "))
            print("Top", nor, "records from DataFrame ")
            print(df.head(nor))
            print("------------------x-------------------x----------------x------------------x ")
        elif x == 2:
            df = df.sort_values("Tgoldmedal", ascending=False)
            nor = int(input("Enter the number of records to be displayed"))
            print("Top", nor, "records by total no.of gold medals")
            print(df.head(nor))
            print("------------x------------------------x--------------------x---------------------x")
        elif x == 3:
            df = df.sort_values("TSilver", ascending=False)
            nor = int(input("Enter the number of records to be displayed"))
            print("Top", nor, "records by total no. of silver medals")
            print(df.head(nor))
            print("--------------x-----------------------x--------------------x---------------------x")
        elif x == 4:
            df = df.sort_values("Tbronzemedals", ascending=False)
            nor = int(input("Enter the number of records to be displayed"))
            print("Top", nor, "records by total no. of bronze medals")
            print(df.head(nor))
            print("----------------x---------------------x-------------------x-----------------------x")
        elif x == 5:
            df = df.sort_values("Totalmedals", ascending=False)
            nor = int(input("Enter the number of records to br displayed"))
            print("Bottom", nor, "records from the  dataframe")
            print(df.tail(nor))
            print("-----------------x------------------------x---------------------x------------------x")
        elif x == 6:
            print("information of the dataframe")
            print(df.info())
            print("--------------x----------------------x----------------------x---------------------x")
        elif x == 7:
            print("Describing the basic characteristics of the dataframe")
            print(df.describe())
            print("----------------x------------------------x-------------------------x--------------------x")
        elif x == 8:
            print("Name of the columns~ ~ ~ >", df.columns)
            clm = eval(input("Enter the column names in alist"))
            print(df[clm])
            print("----------------x------------------------x----------------------x-------------------------x")
        elif x == 9:
            print("Maxmium value for each column")
            print(df.apply(np.max))
            print("-----------------x--------------------x------------------x--------------------------x")
        elif x == 10:
            menu()
            break


def read_csv_excel():
    ans = True
    while ans:
        print('''1)Read CSV file and display DataFrame
            \n 2) Read Excel File and Display dataframe
            \n 3) Press 3 to go back to main menu''')
        ans = int(input("Enter Your choice:"))
        if ans == 1:
            df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
            print(df)
            print("Done!")
        elif ans == 2:
            frame = input("Enter file name with PATH and EXTENSION(.xls/.xlsx):")
            df = pd.read_excel(frame)
            print(df)
            print("Done!")
        elif ans == 3:
            menu()


def manuplt():
    df = pd.read_csv(r"C:\\Users\\pooja\\OneDrive\\Documents\\ip_project\\ip_Project_2.csv", encoding="cp1252")
    ans = True
    while ans:
        print('''DATA MANIPULATION\n
1.Inserting a Row
2.Deleting a Row
 3.Inserting a Column
 4.Deleting a Column
 5.Renaming a Column
  6.Exit to main menu''')
        ans = int(input("Enter your choice:"))
        if ans == 1:
            col = df.columns
            lst = eval(input("Enter the row values in list:"))
            sr = pd.Series(lst, index=col)
            row_df1 = pd.DataFrame([sr])
            df = pd.concat([row_df1], ignore_index=True)
            print(df)
            print("Row Added Successfully!!")
            print(" ~ " * 30)
        elif ans == 2:
            inp = int(input("Enter the row's index you want to be deleted:"))
            df1 = df.drop(inp, axis=0)
            print("~" * 30)
            print(df1)
            print("~" * 30)
        elif ans == 3:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_cloumn", None)
            clname = input("Enter the column name:")
            inp = int(input("Enter the column  index no.\nWhere You Want to input the column:"))
            df.insert(inp, clname, "Nan")
            print(df)
            print(" ~ " * 30)
        elif ans == 4:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_cloumn", None)
            print("DataFrame before deleting the column")
            print(df)
            print(" ~ " * 30)
        elif ans == 5:
            pd.set_option("display.width", 500)
            pd.set_option("displat.max_columns", None)
            print(" ~ " * 30)
            print("Dataframe before changing the column names/s")
            print(" ~ " * 30)
            print(df)
            oldcm = input("Enter the column name you want to rename:")
            newcm = input("Enter the new column name:")
            df = df.rename(cloumns={oldcm: newcm})
            print(" ~ " * 30)
            print("Dataframe after changing the column names/s")
            print(" ~ " * 30)
            print(df)
            print(" ~ " * 30)
        elif ans == 6:
            print("returning to main menu……..Done!!")
            menu()


menu()
