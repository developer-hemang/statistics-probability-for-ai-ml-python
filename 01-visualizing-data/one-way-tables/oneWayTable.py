import pandas as pd


class oneWayTable():

    def __init__(self):
        pass


    def getNiftyHistoricalMarketCondition(self):

        # Create Mock Nifty Historical Volume Data 
        df = pd.DataFrame({
            "Datetime": [
                "2026-09-09 09:15:00",
                "2026-09-09 09:30:00",
                "2026-09-09 09:45:00",
                "2026-09-09 10:00:00",
                "2026-09-09 10:15:00",
                "2026-09-09 10:30:00",
                "2026-09-09 10:45:00",
                "2026-09-09 11:00:00",
                "2026-09-09 11:15:00",
                "2026-09-09 11:30:00"
            ],
            "Market_Condition": [
                "Bullish",
                "Bullish",
                "Neutral",
                "Bearish",
                "Bullish",
                "Neutral",
                "Bearish",
                "Bullish",
                "Neutral",
                "Bullish"
            ]
        })

        # convert Datetime String to proper Datetime
        df["Datetime"] = pd.to_datetime(df["Datetime"])
        return df;



    def createOneWayTableFromDataframe(self):
        df = self.getNiftyHistoricalMarketCondition();
        one_way_table = df["Market_Condition"].value_counts().rename_axis("Market Condition")
        return one_way_table;


oneWayTable = oneWayTable();

print(oneWayTable.createOneWayTableFromDataframe());