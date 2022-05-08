"""
This will become a module.

For now it is in a notebook, but we'll put it in 
a .py file, and import it.

"""

import pyreadstat

class StatsPays:
    def __init__(self, filename, name):
        """
        Parameters
        ----------
        filename : str
            the file we load data from
        name: str
            the country of interest.
        
        """
        df, meta = pyreadstat.read_sav(filename)
        self.data = df[df["COUNTRYNEW"] == name]
        self.meta = meta

    def question(self, v):
        return self.meta.column_names_to_labels[v]

    def modalites(self, v):
        return self.meta.value_labels[meta.variable_to_label[v]]
