PORSCHE_CHASSIS_TABLE = {
            "911" : [{"generation" : "First", "star_year" : 1965, "end_ year" : 1973},
                     {"generation" : "G-Series", "star_year" : 1974, "end_ year" : 1989, "Note" : "Turbo trims are 930"},
                     {"generation" : "964", "star_year" : 1989, "end_ year" : 1994},
                     {"generation" : "993", "star_year" : 1994, "end_ year" : 1998},
                     {"generation" : "996", "star_year" : 1998, "end_ year" : 2005},
                     {"generation" : "997.1", "star_year" : 2005, "end_ year" : 2012},
                     {"generation" : "991.1", "star_year" : 2012, "end_ year" : 2016},
                     {"generation" : "991.2", "star_year" : 2016, "end_ year" : 2019},
                     {"generation" : "992.1", "star_year" : 2020, "end_ year" : 2024},
                     {"generation" : "992.2", "star_year" : 2024, "end_ year" : float('inf')}],
        
        }

PORSCHE_TRIM_TABLE = {
    "911" : {"generation" : {"First": {"Base" : {"cylinders" : 6,
                                                 "displacement" : 2.0,
                                                 "aspiration" : "NA",
                                                 "drivetrain" : "RWD",
                                                 "transmission" : ("Manual", "Automatic")},
                                       },
                             "G-Series": {},
                             "964": {},
                             "993": {},
                             "996": {},
                             "997.1": {},
                             "991.1": {},
                             "991.2": {},
                             "992.1": {"Carrera": {
                    "cylinders": 6,
                    "displacement": 3.4,
                    "aspiration": "NA",
                    "horsepower": 350,
                    "drivetrain": "RWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Carrera S": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "NA",
                    "horsepower": 400,
                    "drivetrain": "RWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Carrera 4": {
                    "cylinders": 6,
                    "displacement": 3.4,
                    "aspiration": "NA",
                    "horsepower": 350,
                    "drivetrain": "AWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Carrera 4S": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "NA",
                    "horsepower": 400,
                    "drivetrain": "AWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Targa 4": {
                    "cylinders": 6,
                    "displacement": 3.4,
                    "aspiration": "NA",
                    "horsepower": 350,
                    "drivetrain": "AWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Targa",)
                },

                "Targa 4S": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "NA",
                    "horsepower": 400,
                    "drivetrain": "AWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Targa",)
                },

                "Turbo": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "TT",
                    "horsepower": 520,
                    "drivetrain": "AWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Turbo S": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "TT",
                    "horsepower": 560,
                    "drivetrain": "AWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "GT3": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "NA",
                    "horsepower": 475,
                    "drivetrain": "RWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe",)
                },

                "GT3 RS": {
                    "cylinders": 6,
                    "displacement": 4.0,
                    "aspiration": "NA",
                    "horsepower": 500,
                    "drivetrain": "RWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe",)
                },

                "GT3 RS 4.0": {
                    "cylinders": 6,
                    "displacement": 4.0,
                    "aspiration": "NA",
                    "horsepower": 500,
                    "drivetrain": "RWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe",)
                }
            },

            "991.2": {
                "Carrera": {
                    "cylinders": 6,
                    "displacement": 3.0,
                    "aspiration": "TT",
                    "horsepower": 370,
                    "drivetrain": "RWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Carrera T": {
                    "cylinders": 6,
                    "displacement": 3.0,
                    "aspiration": "TT",
                    "horsepower": 370,
                    "drivetrain": "RWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe",)
                },

                "Carrera S": {
                    "cylinders": 6,
                    "displacement": 3.0,
                    "aspiration": "TT",
                    "horsepower": 420,
                    "drivetrain": "RWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Carrera GTS": {
                    "cylinders": 6,
                    "displacement": 3.0,
                    "aspiration": "TT",
                    "horsepower": 450,
                    "drivetrain": "RWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Carrera 4 GTS": {
                    "cylinders": 6,
                    "displacement": 3.0,
                    "aspiration": "TT",
                    "horsepower": 450,
                    "drivetrain": "AWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Targa 4 GTS": {
                    "cylinders": 6,
                    "displacement": 3.0,
                    "aspiration": "TT",
                    "horsepower": 450,
                    "drivetrain": "AWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Targa",)
                },

                "Turbo": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "TT",
                    "horsepower": 540,
                    "drivetrain": "AWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "Turbo S": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "TT",
                    "horsepower": 580,
                    "drivetrain": "AWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe", "Cabriolet")
                },

                "GT3": {
                    "cylinders": 6,
                    "displacement": 4.0,
                    "aspiration": "NA",
                    "horsepower": 500,
                    "drivetrain": "RWD",
                    "transmission": ("Manual", "PDK"),
                    "body_styles": ("Coupe",)
                },

                "GT3 Touring": {
                    "cylinders": 6,
                    "displacement": 4.0,
                    "aspiration": "NA",
                    "horsepower": 500,
                    "drivetrain": "RWD",
                    "transmission": ("Manual",),
                    "body_styles": ("Coupe",)
                },

                "GT3 RS": {
                    "cylinders": 6,
                    "displacement": 4.0,
                    "aspiration": "NA",
                    "horsepower": 520,
                    "drivetrain": "RWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe",)
                },

                "GT2 RS": {
                    "cylinders": 6,
                    "displacement": 3.8,
                    "aspiration": "TT",
                    "horsepower": 700,
                    "drivetrain": "RWD",
                    "transmission": ("PDK",),
                    "body_styles": ("Coupe",)
                },

                "911 R": {
                    "cylinders": 6,
                    "displacement": 4.0,
                    "aspiration": "NA",
                    "horsepower": 500,
                    "drivetrain": "RWD",
                    "transmission": ("Manual",),
                    "body_styles": ("Coupe",)
                },

                "Speedster": {
                    "cylinders": 6,
                    "displacement": 4.0,
                    "aspiration": "NA",
                    "horsepower": 502,
                    "drivetrain": "RWD",
                    "transmission": ("Manual",),
                    "body_styles": ("Speedster",)
                }
            }},
                             "992.2": {},
                             }, },
    
}