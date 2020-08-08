# -- coding: utf-8 --
his_name = 'Zed A. Shaw'
his_age = 35 # not a lie
his_height = 74 # inches
his_weight = 180 # lbs
his_eyes = 'Blue'
his_teeth = 'White'
his_hair = 'Brown'

print ("Let's talk about %s." % his_name)
print ("He's %d inches tall." % his_height)
print ("He's %d pounds heavy." % his_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (his_eyes, his_hair))
print ("His teeth are usually %s depending on the coffee." % his_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (his_age, his_height, his_weight, his_age + his_height + his_weight ))

Talha_age = 17
tahia_age = 21
nafisa_age = 23

print("The individual age of nafisa, tahia, and talha is %d, %d, %d and their age sum is %d." % (nafisa_age, tahia_age, Talha_age, nafisa_age + tahia_age + Talha_age))
print("The individual age of nafisa, tahia, and talha is %r, %r, %r and their age sum is %r." % (nafisa_age, tahia_age, Talha_age, nafisa_age + tahia_age + Talha_age))
print (round(1.7333))