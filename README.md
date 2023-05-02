# Doughnut Text Formater

Convert any block of text into a doughnut!

```
  Convert a  
 ny b   lock 
  of     tex 
 t into a d  
  oughnut!   
```

## Use

Download `doughnut.py` and pass your text into the `generate_doughnut` function and you will be given a doughnut made of you text.

Example:

```
from doughnut import generate_doughnut
print(generate_doughnut("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"))
```

Will give you the doughnut:

```
          Lorem ipsum dolor           
        sit amet, consectetur         
     adipiscing elit, sed do eiu      
    smod tempor incididunt ut labo    
  re et dolore magna aliqua. Ut eni   
  m ad minim ven      iam, quis nost  
 rud exercita           tion ullamco  
  laboris ni             si ut aliqui 
 p ex ea com              modo conseq 
 uat. Duis a             ute irure do 
 lor in repre           henderit in v 
 oluptate velit        esse cillum d  
  olore eu fugiat nulla pariatur. E   
   xcepteur sint occaecat cupidata    
     t non proident, sunt in culp     
       a qui officia deserunt m       
          ollit anim id est           
               laborum                
```

## Notes:
- You may need to change the `CHARECTER_WIDTH_TO_HEIGHT_RAIO` variable in `doughnut.py` depending on where you are displaying you text.
-  You will need to use a monospaced font for optimal doughnuts.