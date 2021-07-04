# MGF-Filter
![MGF-Filter](https://raw.githubusercontent.com/joanapaulaso/MGF-Filter/main/mgf-filter.png)
#### This is a very simple application in which you can filter an MS/MS ".mgf" extension file that has a "SCANS" line as an ion identificator, so it can be used within SIRIUS.

I created this app, because by using MS-DIAL to process metabolomics data, I usually use MetaboAnalyst to filter the table exported from MS-DIAL. Afterwards, I end up with a list of IDs way shorter than it was initially exported. So, in order to use precisely those filtered IDs from the new table within SIRIUS software, MGF-Filter does the trick.

You can either run the python app, if you have python installed:
  
    python mgffilter.py
  
Or you can access the "dist" folder and run the executable.

1. The IDs File is a simple ".txt" file with the list of IDs you want to filter within the ".mgf" file (the ones you want to keep), separeted by a line break. Do not add any other text separator nor a table header.
2. The MGF Original File, of course, is the ".mgf" exported from MS-DIAL (as the GNPS export option).
3. Give it a beautiful filename.
4. Click Convert!

The new filtered MGF file will show up within the same folder that you ran the application.
#### Example files are given
