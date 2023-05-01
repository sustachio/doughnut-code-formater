# Doughnut Text Formater

Have you ever wanted you text to look like a bunch of doughnuts? No? Well heres a tool that does just that!

## Use

Download `doughnut.py` and pass your text into the `generate_doughnut` function and you will be given a doughnut made of you text.

Example:

The code:

    from doughnut import generate_doughnut
    print(generate_doughnut("Have you ever wanted you text to look like a bunch of doughnuts? No? Well heres a tool that does just that!"))

Will give you the doughnut:

           Have        
         you ever w    
      anted you text   
     to loo    k like  
    a bunc       h of  
    doughn       uts?  
     No? Wel   l heres 
       a tool that do  
        es just tha    
            t!         


You may need to change the `CHARECTER_WIDTH_TO_HEIGHT_RAIO` variable in `doughnut.py` depending on where you are displaying you text. You will need to use a monospaced font for optimal doughnuts.