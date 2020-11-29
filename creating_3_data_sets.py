from ua.univer.lesson.lesson06.information.class_information import Information

Yulia = Information("Julia", "Kyiv", "26","232323223")
Denis = Information("Denis", "Kyiv", "27","777777777")
Alex = Information("Alex", "Kyiv", "20","333333333333")

Yulia.update_name("Julia")
print(Yulia.get_name())
Yulia.update_address("Lviv")
print(Yulia.get_address())
Yulia.update_age("17")
print(Yulia.get_age())
Yulia.update_telephone("90897897897")
print(Yulia.get_telephone())
