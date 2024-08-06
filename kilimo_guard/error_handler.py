import traceback
from django.conf import settings

class ErrorHandler:
    def django_handle_info(message):
        print(message)
        print("...............................................................................")
        
    def django_handle_error(error):    
        if settings.MODE=="dev":          
            print(f'{"🚨" * 20}')                
            print(error)        
            print("_______________________________________________________________________________")
            print(traceback.format_exc())      
            print(f'{"🚨" * 20}')
        else:                   
            # TODO
            # Handle Error well on production
            pass
        return