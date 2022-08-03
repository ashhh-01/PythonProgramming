import pandas

data=pandas.read_csv("./Squirrel Data Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

greySquirrelCount=len(data[data["Primary Fur Color"]=="Gray"])
redSquirrelCount=len(data[data["Primary Fur Color"]=="Cinnamon"])
blackSquirrelCount=len(data[data["Primary Fur Color"]=="Black"])


dataDict={
    "Fur Color":["Grey","cinnamon","Black"],
    "count":[greySquirrelCount,redSquirrelCount,blackSquirrelCount]
}

DataCsv=pandas.DataFrame(dataDict)
DataCsv.to_csv("./Squirrel Data Analysis/Count.csv")