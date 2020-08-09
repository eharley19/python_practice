stringTest = "  Go hang a salami, I'm a lasagna hog  "

assert stringTest.upper() == "  GO HANG A SALAMI, I'M A LASAGNA HOG  "
assert stringTest.lower() == "  go hang a salami, i'm a lasagna hog  "
assert stringTest.title() == "  Go Hang A Salami, I'M A Lasagna Hog  "
assert stringTest.strip() == "Go hang a salami, I'm a lasagna hog"
assert stringTest.rstrip() == "  Go hang a salami, I'm a lasagna hog"
assert stringTest.find("Go") == 2
assert stringTest.replace("a", "e") == "  Go heng e selemi, I'm e lesegne hog  "
assert stringTest. == ["Go", "hang", "a", "salami,", "I'm", "a", "lasagna", "hog"]