# WEBSITE BLOCKER

## ABOUT

* Simple python script for blocking websites in the specified time
* For the program to be executed, Python must be installed
***

## FEATURES

* Block the URL
* Block only between the specified time.
***

## TO AUTOMIZE THE PROCCESS 

### LINUX OS:
We can set up the task using crontab. Run following:  
```sudo contab -e```  

Then add this line in the end of the file:  
```@reboot python /path_to_the_scr```    
*This will execute the script when os starts*  

### WINDOWS:
Process can be automated using Task Scheduler  
For more info see the bellow site:  
[How to create automated task](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10)
