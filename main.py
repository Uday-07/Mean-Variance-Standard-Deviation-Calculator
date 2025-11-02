import mean_var_std
from unittest import main

# Test your function
print("Testing with [0,1,2,3,4,5,6,7,8]:")
result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
print(result)

print("\nRunning unit tests...")
# Run unit tests automatically
main(module='test_module', exit=False)
