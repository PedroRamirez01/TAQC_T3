test_data_checkout = [
    ("valid_data", { 
        "FIRST_NAME": "Pedrito",
        "LAST_NAME": "González",
        "COUNTRY": "United States", 
        "CITY": "Springfield",
        "ADRESS": "Calle siempre viva 123",
        "PHONE_NUMBER": "123456789",
        "EMAIL": "pedritogonzalez123@gmail.com",
        "DISCOUNT_CODE": "123",
        "CARD_NUMBER": "4242424242424242",
        "CARD_EXPIRATION": "12/25",
        "CARD_CVV": "123"
    }),
    ("invalid_data",{
        "FIRST_NAME": "#",
        "LAST_NAME": "$",
        "COUNTRY": "United States", 
        "CITY": "?",
        "ADRESS": "#",
        "PHONE_NUMBER": "&",
        "EMAIL": "pedritogonzalez123@gmail.com",
        "DISCOUNT_CODE": "123456",
        "CARD_NUMBER": "4242424242424242",
        "CARD_EXPIRATION": "12/25",
        "CARD_CVV": "123"
    }),
    ("no_data", {
        "FIRST_NAME": "",
        "LAST_NAME": "",
        "COUNTRY": "", 
        "CITY": "",
        "ADRESS": "",
        "PHONE_NUMBER": "",
        "EMAIL": "",
        "DISCOUNT_CODE": "",
        "CARD_NUMBER": "",
        "CARD_EXPIRATION": "",
        "CARD_CVV": ""
    }),
]