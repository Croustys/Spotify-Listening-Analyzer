import json

def loadData(filename):
  with open(filename, encoding="utf8") as f:
    data = json.load(f)
    return data

def main():
  totalData = []
  totalData.append(loadData("./StreamingHistory0.json"))
  totalData.append(loadData("./StreamingHistory1.json"))
  totalData.append(loadData("./StreamingHistory2.json"))

  totalMsListenedTo = 0
  for i in totalData:
    for j in i:
      totalMsListenedTo += j["msPlayed"]
  totalHours = totalMsListenedTo / 3600000
  print(f"{totalHours} hours listened to.")

if __name__ == "__main__":
  main()