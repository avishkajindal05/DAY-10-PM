Q1: Conceptual
Explain the LEGB rule with a concrete example. Draw the scope diagram. What happens if you use a variable name that exists in both local and global scope? What does the 'global' keyword do, and why is it considered a code smell? What is the alternative?

Q2: Coding
Write a function memoize(func) that caches results of expensive function calls. When called with the same arguments, return the cached result instead of recomputing.

# Usage:
@memoize
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

# fibonacci(50) should return instantly with memoization
# (without memoization, it would take hours)
Hint: Use a dict as cache. The key is the function arguments (as tuple), the value is the result.

Q3: Debug/Analyze
This code has a mutable default argument bug AND a scope bug. Find and fix both:

total = 0

def add_to_cart(item, cart=[]):      # Bug 1: mutable default
    cart.append(item)
    total = total + len(cart)         # Bug 2: scope issue
    return cart

print(add_to_cart('apple'))
print(add_to_cart('banana'))  # What does this print? Why is it wrong?

What would the original code print for 'banana'?
It would likely crash with an UnboundLocalError due to the total bug. If total weren't there, it would print ['apple', 'banana'] because the 'apple' stayed in the "sticky" default list.