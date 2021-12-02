def city_country_name(city, country, population=''):
    """Accept city and country names and output them as a single string"""
    if population:
        final_string = city.title() + " " +country.title() + ", population: " +population
    else:
        final_string = city.title() + " " + country.title()
    return final_string