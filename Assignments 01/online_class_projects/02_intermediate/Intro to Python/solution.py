MARS_MULTIPLE = 0.378

def main():

    earth_weight_str = input("Enter  a weight  on earth:")

    earth_weight = float(earth_weight_str)



    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    # Note the string concatenation!
    print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

if __name__ == '__main__':
    main()
 