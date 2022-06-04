import pandas as pd

# import gsheets


class Writer:
    def __init__(self):
        pass

    def csv_write(self, data: pd.DataFrame) -> str:
        """Write DataFrame to a CSV file

        Writes dataframe to a CSV file as a string.

        Parameters
        ----------
        data: pd.DataFrame
           DataFrame object to write to csv

         Returns
         --------
         CSV format of data as a string.

        """
        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)

        return data.to_csv()

    def gsheets_write(self):
        raise NotImplementedError
