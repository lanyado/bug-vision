import inspect
import traceback

import json

class BugVision:
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def get_module_name(self):
        """
        Retrieves the name of the module that called the function.
        """
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        return module.__name__ if module else 'Unknown'

    def log_error(self, exc_type, exc_val, exc_traceback):
        # Format the traceback
        error_message = "".join(traceback.format_exception(exc_type, exc_val, exc_traceback))
        module_name = self.get_module_name()

        # Extract the frame where the error occurred
        tb = exc_traceback
        while tb.tb_next:
            tb = tb.tb_next
        frame = tb.tb_frame
        
        # Get the function that raised the error
        func = frame.f_globals[frame.f_code.co_name]
        
        # Print the source code of the function
        try:
            source_code = inspect.getsource(func)
        except:
            source_code = ""

        error_context = {
            "error_message": error_message,
            "module_name": module_name,
            "source_code": source_code
        }
        for k, v in error_context.items():
            print(f"{k}: {v}")

    def __exit__(self, exc_type, exc_val, exc_traceback):
        if exc_type is not None:
            self.log_error(exc_type, exc_val, exc_traceback)
            return True
