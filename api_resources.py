RESOURCES = {
      'cities': """Returns cities in the database. Omits cities for which there are no data.""",
      'price_items':"""Returns items in our main cost of living section""",
      'currency_exchange_rates':"""Returns our current exchange rates we are using""",
      'city_prices':"""Returns current prices in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                      :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                      :param city: City name (as in numbeo database)
                      :param country: Country name (as in numbeo database or ISO 3166 code)
                      :param city_id: Internal city id (as in numbeo database)
                      :param currency: Currency you want the data to be estimated
                      :param use_estimated: If set to false, for cities with low data coverage, the engine will not try to estimate values from nearby cities (default: true)""",
      'country_prices':"""Returns current country prices
                          :param country:	Country name (as in numbeo database or ISO 3166 code)
                          :param currency: Currency you want the data to be estimated""",
      'close_cities_with_prices':"""Returns close cities for a given query (or coordinates) in our database.
                                  :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                                  :param max_distance: Max distance in km to look up for cities (from the source location provided). Default: 200
                                  :param min_contributors: Minimum number of contributors for a city to be included in the response. Default: 10""",
      'historical_city_prices':"""Returns historical average prices (per year) in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                                  :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                                  :param city: City name (as in numbeo database)
                                  :param country: Country name (as in numbeo database or ISO 3166 code)
                                  :param city_id: Internal city id (as in numbeo database)
                                  :param currency: Currency you want the data to be estimated""",
      'historical_country_prices':"""Returns historical average prices (per year) in a country
                                  :param country: Country name (as in numbeo database or ISO 3166 code)
                                  :param currency: Currency you want the data to be estimated""",
      'historical_currency_exchange_rates':"""Returns our historical exchange rates we are using (at the beginning of the month)
                                              :param month: Month
                                              :year: Year""",
      'city_prices_raw':"""Raw recent data entries for a given city, specified by a query (location or lat,lng) or city and country
                          :param query: Name of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                          :param city: City name (as in numbeo database)
                          :param country: Country name (as in numbeo database or ISO 3166 code)
                          :param city_id: Internal city id (as in numbeo database)
                          :param since_timestamp: If present, the call will return only entries after certain Linux timestamp
                          :param since_internal_id: If present, the call will return only entries having internal_id greater or equal than the id provided""",
      'city_prices_archive_raw':"""Raw archived data entries for a given city, specified by a query (location or lat,lng) or city and country. Our backend processes moves data periodically from the main table to the archive table and using this query you can access data from the archive table.
                                  :param query: Name of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                                  :param city: City name (as in numbeo database)
                                  :param country: Country name (as in numbeo database or ISO 3166 code)
                                  :param city_id: Internal city id (as in numbeo database)
                                  :param currency: Currency you want the data to be estimated""",
      'indices':"""Returns Numbeo's indices for a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                  :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                  :param city: City name (as in numbeo database)
                  :param country: Country name (as in numbeo database or ISO 3166 code)
                  :param city_id: Internal city id (as in numbeo database)""",
      'country_indices':"""Returns Numbeo's indices for a country. Location can be specified with a country name.
                          :param country: Country name (as in numbeo database or ISO 3166 code)""",
      'city_crime':"""Returns aggregate analysis about crime perception in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                      :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                      :param city: City name (as in numbeo database)
                      :param country: Country name (as in numbeo database or ISO 3166 code)
                      :param city_id: Internal city id (as in numbeo database)""",
      'city_crime_raw':"""Returns raw inputs about crime perceptions in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                      :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                      :param city: City name (as in numbeo database)
                      :param country: Country name (as in numbeo database or ISO 3166 code)
                      :param city_id: Internal city id (as in numbeo database)""",
      'city_healthcare':"""Returns aggregate inputs about healthcare quality perception in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                          :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                          :param city: City name (as in numbeo database)
                          :param country: Country name (as in numbeo database or ISO 3166 code)
                          :param city_id: Internal city id (as in numbeo database)""",
      'city_healthcare_raw':"""Returns raw inputs about healthcare quality perception in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                              :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                              :param city: City name (as in numbeo database)
                              :param country: Country name (as in numbeo database or ISO 3166 code)
                              :param city_id: Internal city id (as in numbeo database)""",
      'city_pollution':"""Returns aggregate perceptions about pollution in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                          :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                          :param city: City name (as in numbeo database)
                          :param country: Country name (as in numbeo database or ISO 3166 code)
                          :param city_id: Internal city id (as in numbeo database)
                          """,
      'city_pollution_raw':"""Returns raw inputs about pollution perception in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                              :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                              :param city: City name (as in numbeo database)
                              :param country:	Country name (as in numbeo database or ISO 3166 code)
                              :param city_id: Internal city id (as in numbeo database)""",     
      'city_traffic':"""Returns aggregate analysis of daily commute times (traffic) in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                          :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                          :param city: City name (as in numbeo database)
                          :param country: Country name (as in numbeo database or ISO 3166 code)
                          :param city_id: Internal city id (as in numbeo database)""",
      'city_traffic_raw':"""Returns raw entries about daily commute times (traffic) in a city. Location can be specified with a query containing name or latitude,longitude (with comma separator).
                              :param query: Name or geolocation of the place for which result is requested. Internationalized or ambigous names are usually ok, names resolved with third party normative services.
                              :param city: City name (as in numbeo database)
                              :param country: Country name (as in numbeo database or ISO 3166 code)
                              :param city_id: Internal city id (as in numbeo database)""",
      'country_crime':"""Returns aggregate analysis about crime perception in a given country.
                          :param country: Country name (as in numbeo database or ISO 3166 code)""",
      'country_healthcare':"""Returns aggregate analysis about health care quality perception in a given country.
                          :param country: Country name (as in numbeo database or ISO 3166 code)""",
      'country_pollution':"""Returns aggregate analysis about pollution perceptions in a given country.
                          :param country: Country name (as in numbeo database or ISO 3166 code)""",
      'country_traffic':"""Returns aggregate analysis about traffic perceptions in a given country.
                          :param country: Country name (as in numbeo database or ISO 3166 code)""",
  }