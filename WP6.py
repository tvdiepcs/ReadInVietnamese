def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    return [i for i in hotel_daily_rates if i[1]<=maximum_daily_rate]

hotel_daily_rates = [('Majestic Saigon Hotel', 93), ('Hotel Grand Saigon', 120), ('Sofitel Saigon Plaza', 123), ('Hotel Continental', 62), ('Caravelle Hotel', 180), ('Sheraton Saigon Hotel', 216), ('Park Hyatt Saigon', 209)]
find_cheapest_hotels(hotel_daily_rates, 85)