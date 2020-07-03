API-Reference
=============

Importing advertisements
------------------------

**POST** `https://grundstuecksboerse.maredata.de:8000/v1/import/{apiKey}`

This method imports property listings. Each plot of land must have 
unique ID. This allows existing advertisments to be identified 
and to update it. Imported advertisements stored at Grundstücksbörse24 
but which are no longer available in a further import are deleted.

The scraper must therefore always transfer the complete result to the interface.

###JSON body
    {
        "data": [
            {
                "uuid": "997f5ef9-460f-404a-92fa-499d84898f07@immobilienscout24.de",
                "title": "Example property",
                "description": "Description of the example property",
                "price": 250000.99,
                "brokerage": 4.9,
                "area": 2000,
                "grz": 0.8,
                "gfz": 0.8,
                "street": "example-street",
                "housenumber": "4b",
                "postcode": "23423",
                "city": "Example-City",
                "source": "example.com",
                "plot_assets": [
                    {
                        "file": "https://example.com/img/example.jpg"
                    },
                    ...
                ]
            },
            ...
        ]
    }

###Parameters
####uuid
_string_ **required**
Unique Identifier for the entry. 
Format: {original_id}@{original_host}. 
Example: `499d84898f07@immobilienscout24.de`

---

####category
_string_
Category of the plot. 
Possible categories: Acker- und Gartenland, Bauerwartungsland, Bauland

---

####title
_string_ **required**
Title of the plot.

---

####description
_string_
Main description of the plot.

---

####description_location
_string_
Description of the location from the plot.

---

####description_other
_string_
Other description of the plot.

---

####price
_float_ **required**
Price of the plot in Euro.

---

####brokerage
_float_
Brokerage for the plot in %.

---

####area
_integer_ **required**
Size of the plot in m²

---

####grz
_float_
Base area number of the plot. The value must be between 0 and 1.
Example: 0.7

---

####gfz
_float_
Floor space of the plot. The value must be between 0 and 1.
Example: 0.7

---

####street
_string_ **required**
Street.

---

####housenumber
_string_

---

####postcode
_string_ **required**

---

####city
_string_ **required**

---

####region
_string_

---

####latitude
_float_

---

####longitude
_float_

---

####arable
_integer_
Buildability of the plot. 
0 = Unknown
1 = Building plan
2 = Buildable according to § 34 BauGe or surrounding development

---

####tapped
_integer_
Developed.
0 = No
1 = Yes
2 = Partially developed
3 = Unknown

---

####building_permit
_boolean_
Building permit.

---

####short_term_building
_boolean_
Buildable in the short term.

---

####utilisation
_string_
Use of the property.

---

####divisible_from
_int_
The property is divisible from the size.

---

####demolition_property
_boolean_
Demolition property.

---

####available_from
_string_
Date from which the property is available.
Format: Y-m-d
Example: 2020-06-15

---

####deal
_string_
Deal for the property. 
Possible values: sale, leasing

---

####source
_string_
URL of the original advertisement.

---

####plot_assets
_array_
List of images for the property.
Example:

    [
        {
            "file": "https://example.com/img/example.jpg"
        },
        ...
    ]