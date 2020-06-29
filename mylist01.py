#!/usr/bin/python3

# single line comment 

"""

"""

def main():
    movies = [] # one way to create a list
    movies.append("Avatar") # .append is a list  method that applies the value
                            # passed to it at the END of the list
    
    movies.append("Back to Future")
    movies.append("Ghostbusters")

    #print(movies[0]) # use the print FUNCTION to display to std out
    print(movies.pop())

if __name__ == "__main__":
    main()
    main()
    main()

