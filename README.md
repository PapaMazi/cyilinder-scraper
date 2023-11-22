# cyilinder-scraper
Simple python script used to scrape RANSAC cylinder data from Cloud Compare

Scrapes data from DB Tree.

### How it works
After running the RANSAC Shape Detection plugin on Cloud Compare, the cylinder data will be shown in the DB tree. Note how many cylinders were created as it is required as input when running the script. Select 'Cylinder_0001' and go back to the code in whatever IDE you will run the code in. Once the code is run, input the number of cylinders that was created and the script will alt-tab to cloud compare and scrape cylinder radius/height data and output it as a .csv file. 
