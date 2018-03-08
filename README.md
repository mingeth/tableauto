# tableau auto file splitter

How to use
- splits out TSV datatab exports from Tableau by splitting column
- download the python script to a folder and create a subfolder called `in`
- export your data to crosstab and put into the `in` folder
- the filename should be structured in an intelligent way (e.g. `A1234_ACO_0_<type of report>.csv`)
- run the script on the command line (`python <script.py>`)
- the splitter will auto create an `out` folder and put the split files into it
- only uses python standard libraries for now, no `pip` necessary

Debugging
- the `<type of report>` in the input filename must exist in the `split_column` function in the script, or be defaulted to 'TIN Name'
- each type of report is mapped to a column to split, if your data does not contain a 'TIN Name' tab, please add it to the dictionary
