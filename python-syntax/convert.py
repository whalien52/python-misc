def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
    
    permitted = ["f","c"]
    
    if unit_in not in permitted or unit_out not in permitted:
        if unit_in not in permitted:
            return "should be Invalid unit " + unit_in
        else:
            return "should be Invalid unit " + unit_out
    
    adjusted_temp = 0;
    if unit_in == "f":
        adjusted_temp = (temp - 32) * 5.0/9.0
    elif unit_in == "c":
        adjusted_temp = 9.0/5.0 * temp + 32 
    
    return "should be " + str(adjusted_temp)


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

