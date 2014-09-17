#!/usr/bin/env ruby
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def multipleof(number, multiple)
    result = number % multiple
    if result == 0
        return 1 
    end
    return 0
end

countto = 999 
result = 0

for x in 1..countto do
    if multipleof(x, 3) == 1
        puts "#{x} is a multiple of 3"
        result = result + x
    elsif multipleof(x, 5) == 1
        puts "#{x} is a multiple of 5"
        result = result + x
    end
end

puts result
