# RateMyCar

## Goal

- Make a (multiple)linear regression model that estimates the values of car models compared to each other, i.e. comparing your 911 to other 911's
- Also have more detailed specifications about the cars themselves

## Data

Manufacturer -> Model -> Generation -> Trim + Specs, Other Ownership Variables

### Manufacturer Chassis Code Lookup

As of right now:

Manufacturer_Table = { 'Model Name': [{'generation': str, 'start_year': int, 'end_year': int}], }
***exception to inf value used to denote the generation has not yet finished production

### Manufacturer Trim Lookup

As of right now:
```python
Trim_table = {'Model Name': 'generation': {'generation identifier' : {
        "trim" : {
            "cylinders": int,
            "displacement": Liters(float),
            "horsepower": Mechanical Horespower(int),       # 1*
            "aspiration": "NA" | "T" | "TT" | "H",          # 2*  
            "torque": ft-lbs(int),                          # 3*
            "drivetrain": "RWD" | "AWD",                    # 4*
            "transmission": ("Manual", "Automatic"),        # 5*
            "body_styles": ("Coupe", ...) },                # 5*
        }
    },
}
```

1* -> PS(Metric HP) : PS / 1.014 = HP
2* -> NA = Naturally Aspirated, T = Turbocharged(singular), TT = Twin Turbo, H = Hybrid
***Unsure wether to combine H into monicer, i.e. new 911 GTS is a hybrid single turbo 3.6L
3* -> NM * 0.738 = ft-lbs
4* -> RWD = Rear-wheel Drive, AWD = All-wheel Drive
5* Tuple can exclude values

## Methodology

### Manufacturer Notes

#### Porcsche

##### 911

- 992.1: confirm if targa models were offered with manual or not
- 996: pre 2002 had different power figures for trims
- 993: pre 1996 had different power figures for trims
- 993 GT2: change in power figures 1997, need to resolve any conflicts
- 964: might need to append model variants/trims
- G-series: could be discrepencies due to updates at points in time

## Contributors

If you like cars as much as I do and would want to work on this please feel free to reach out and let me know!

- Gianni Bisante (me - owner)
