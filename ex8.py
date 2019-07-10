formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    #this will be printed with "" instead of '' because we have ' already in "didn't"
    "But it didn't sing.",
    "So I said goodnight."
)