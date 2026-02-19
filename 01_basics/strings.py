chai = "    Masala Chai    "
print(chai)
print(chai.strip())

chai1 = "Lemon Chai"
print(chai1.replace("Lemon", "Ginger"))

chaiGroup = "Lemon, Ginger, Masala, Mint"
print(chaiGroup.split(", "))

chai = "Masala Chai"
print(chai.find("Chai"))
print(chai.find("chai"))

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

chai_type = "Masala Chai"
quantity = 2
order = "I ordered {} cups of {}"
print(order.format(quantity, chai_type))

chai_variety = ["Lemon", "Ginger", "Masala"]
print(chai_variety)
print(", ".join(chai_variety))

chai = "Masala Chai"
print(len(chai))

for letter in chai:
    print(letter)
    
chai = "He said, \"Masala Chai is awesome\""
print(chai)

chaiYay = "Masala\nChai"
print(chaiYay)

chaiYayhehe = r"Masala\nChai"
print(chaiYayhehe)

hehe = "Masala Chai"
print("Masala" in hehe)