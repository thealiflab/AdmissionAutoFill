from PIL import Image, ImageFont, ImageDraw

# pip install Pillow

TEXT_COLOR = (0, 0, 0)


def position_text_page_1(student_name, preferred_name, gender, age, dob, grade_level, address, nationality, religion,
                         passport_or_certificate, name_of_sibling, previous_SDIS, academic_year, enrollment_month,
                         father_name,
                         father_occupation, father_phone, father_email, mother_name, mother_occupation, mother_phone,
                         mother_email, contact_1_name, contact_1_phone, contact_1_email, contact_1_relation,
                         contact_2_name, contact_2_phone, contact_2_email, contact_2_relation, other_info):
    form_page_1 = Image.open("assets/1.jpg")
    draw = ImageDraw.Draw(form_page_1)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("font/Montserrat-Medium.ttf", 45)
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text((625, 590), f"{student_name}", TEXT_COLOR, font=font)
    draw.text((625, 660), f"{preferred_name}", TEXT_COLOR, font=font)
    draw.text((625, 730), f"{dob}", TEXT_COLOR, font=font)
    draw.text((625, 790), f"{address}", TEXT_COLOR, font=font)

    if gender == "Male":
        draw.text((1760, 890), "M", TEXT_COLOR, font=font)
    elif gender == "Female":
        draw.text((1630, 890), "F", TEXT_COLOR, font=font)

    draw.text((625, 920), f"{nationality}", TEXT_COLOR, font=font)
    draw.text((625, 990), f"{religion}", TEXT_COLOR, font=font)
    draw.text((1350, 1005), f"{age}", TEXT_COLOR, font=font)
    draw.text((625, 1050), f"{passport_or_certificate}", TEXT_COLOR, font=font)
    draw.text((1350, 1100), f"{grade_level}", TEXT_COLOR, font=font)

    draw.text((290, 1260), f"{name_of_sibling}", TEXT_COLOR, font=font)
    draw.text((1350, 1260), f"{academic_year}", TEXT_COLOR, font=font)
    draw.text((1350, 1360), f"{enrollment_month}", TEXT_COLOR, font=font)
    draw.text((290, 1370), f"{previous_SDIS}", TEXT_COLOR, font=font)

    draw.text((570, 1510), f"{father_name}", TEXT_COLOR, font=font)
    draw.text((1350, 1560), f"{father_phone}", TEXT_COLOR, font=font)
    draw.text((570, 1580), f"{father_occupation}", TEXT_COLOR, font=font)
    draw.text((570, 1640), f"{father_email}", TEXT_COLOR, font=font)
    draw.text((570, 1740), f"{mother_name}", TEXT_COLOR, font=font)
    draw.text((1350, 1780), f"{mother_phone}", TEXT_COLOR, font=font)
    draw.text((570, 1800), f"{mother_occupation}", TEXT_COLOR, font=font)
    draw.text((570, 1870), f"{mother_email}", TEXT_COLOR, font=font)

    draw.text((570, 2010), f"{contact_1_name}", TEXT_COLOR, font=font)
    draw.text((1350, 2050), f"{contact_1_relation}", TEXT_COLOR, font=font)
    draw.text((570, 2070), f"{contact_1_phone}", TEXT_COLOR, font=font)
    draw.text((570, 2140), f"{contact_1_email}", TEXT_COLOR, font=font)
    draw.text((570, 2210), f"{contact_2_name}", TEXT_COLOR, font=font)
    draw.text((1350, 2250), f"{contact_2_relation}", TEXT_COLOR, font=font)
    draw.text((570, 2270), f"{contact_2_phone}", TEXT_COLOR, font=font)
    draw.text((570, 2340), f"{contact_2_email}", TEXT_COLOR, font=font)
    draw.text((610, 2415), f"{other_info}", TEXT_COLOR, font=font)

    form_page_1.save('output/o1.jpg')


def position_text_page_2(is_first_year, prior_school_address_phone_grade_year, emergency_treatment, dress_code,
                         field_trip, photo_video_release):
    form_page_2 = Image.open("assets/2.jpg")
    draw = ImageDraw.Draw(form_page_2)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("font/Montserrat-Medium.ttf", 45)
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text((1160, 230), f"{is_first_year}", TEXT_COLOR, font=font)
    draw.text((1160, 300), f"{prior_school_address_phone_grade_year}", TEXT_COLOR, font=font)
    draw.text((1160, 300), f"{prior_school_address_phone_grade_year}", TEXT_COLOR, font=font)

    # I agree
    draw.text((500, 1000), f"{emergency_treatment}", TEXT_COLOR, font=font)
    draw.text((500, 1600), f"{dress_code}", TEXT_COLOR, font=font)

    if field_trip == "Yes":
        draw.text((330, 2050), f"{field_trip}", TEXT_COLOR, font=font)
    elif field_trip == "No":
        draw.text((510, 2050), f"{field_trip}", TEXT_COLOR, font=font)

    draw.text((500, 2650), f"{photo_video_release}", TEXT_COLOR, font=font)

    form_page_2.save('output/o2.jpg')


def position_text_page_3(school_directory, q1, q2, q3, q4, q5, q6, q7):
    form_page_3 = Image.open("assets/3.jpg")
    draw = ImageDraw.Draw(form_page_3)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("font/Montserrat-Medium.ttf", 45)
    # draw.text((x, y),"Sample Text",(r,g,b))

    # School Directory
    if school_directory == "Yes":
        draw.text((350, 380), f"{school_directory}", TEXT_COLOR, font=font)
    elif school_directory == "No":
        draw.text((520, 380), f"{school_directory}", TEXT_COLOR, font=font)

    # Q1
    if q1 == "Yes":
        draw.text((330, 760), f"{q1}", TEXT_COLOR, font=font)
    elif q1 == "No":
        draw.text((500, 760), f"{q1}", TEXT_COLOR, font=font)

    # Q2
    if q2 == "Yes":
        draw.text((330, 870), f"{q2}", TEXT_COLOR, font=font)
    elif q2 == "No":
        draw.text((500, 870), f"{q2}", TEXT_COLOR, font=font)

    # Q2
    if q3 == "Yes":
        draw.text((330, 990), f"{q3}", TEXT_COLOR, font=font)
    elif q3 == "No":
        draw.text((500, 990), f"{q3}", TEXT_COLOR, font=font)

    # Q4
    if q4 == "Yes":
        draw.text((330, 1110), f"{q4}", TEXT_COLOR, font=font)
    elif q4 == "No":
        draw.text((500, 1110), f"{q4}", TEXT_COLOR, font=font)

    # Q5
    if q5 == "Yes":
        draw.text((330, 1220), f"{q5}", TEXT_COLOR, font=font)
    elif q5 == "No":
        draw.text((500, 1220), f"{q5}", TEXT_COLOR, font=font)

    # Q6
    if q6 == "Yes":
        draw.text((330, 1380), f"{q6}", TEXT_COLOR, font=font)
    elif q6 == "No":
        draw.text((500, 1380), f"{q6}", TEXT_COLOR, font=font)

    # Q7
    if q7 == "Yes":
        draw.text((330, 1610), f"{q7}", TEXT_COLOR, font=font)
    elif q7 == "No":
        draw.text((500, 1610), f"{q7}", TEXT_COLOR, font=font)

    form_page_3.save('output/o3.jpg')


def position_text_page_4(meningitis, meningitis_date, scarlet_fever, scarlet_fever_date, mumps, mumps_date,
                         whooping_cough,
                         whooping_cough_date, tuberculosis, tuberculosis_date, diabetes, diabetes_date, rheumatic_fever,
                         rheumatic_fever_date, diphtheria, diphtheria_date, german_measles, german_measles_date,
                         poliomyelitis, poliomyelitis_date, chickenpox, chickenpox_date, epilepsy, epilepsy_date,
                         heart_disease, heart_disease_date, kidney_disease, kidney_disease_date, allergies_or_asthma,
                         injuries_or_surgeries, medicine_details):
    form_page_4 = Image.open("assets/4.jpg")
    draw = ImageDraw.Draw(form_page_4)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("font/Montserrat-Medium.ttf", 45)
    # draw.text((x, y),"Sample Text",(r,g,b))

    # --------------------- All Diseases ---------------------
    # Meningitis
    if meningitis == "Yes":
        draw.text((740, 1070), f"{meningitis}", TEXT_COLOR, font=font)
    elif meningitis == "No":
        draw.text((870, 1070), f"{meningitis}", TEXT_COLOR, font=font)

    # Meningitis Date
    draw.text((980, 1070), f"{meningitis_date}", TEXT_COLOR, font=font)

    # scarlet_fever
    if scarlet_fever == "Yes":
        draw.text((740, 1140), f"{scarlet_fever}", TEXT_COLOR, font=font)
    elif scarlet_fever == "No":
        draw.text((870, 1140), f"{scarlet_fever}", TEXT_COLOR, font=font)

    # scarlet_fever Date
    draw.text((980, 1140), f"{scarlet_fever_date}", TEXT_COLOR, font=font)

    # Mumps
    if mumps == "Yes":
        draw.text((740, 1210), f"{mumps}", TEXT_COLOR, font=font)
    elif mumps == "No":
        draw.text((870, 1210), f"{mumps}", TEXT_COLOR, font=font)

    # Mumps Date
    draw.text((980, 1210), f"{mumps_date}", TEXT_COLOR, font=font)

    # Whooping Cough
    if whooping_cough == "Yes":
        draw.text((740, 1280), f"{whooping_cough}", TEXT_COLOR, font=font)
    elif whooping_cough == "No":
        draw.text((870, 1280), f"{whooping_cough}", TEXT_COLOR, font=font)

    # Whooping Cough Date
    draw.text((980, 1280), f"{whooping_cough_date}", TEXT_COLOR, font=font)

    # Tuberculosis
    if tuberculosis == "Yes":
        draw.text((740, 1340), f"{tuberculosis}", TEXT_COLOR, font=font)
    elif tuberculosis == "No":
        draw.text((870, 1340), f"{tuberculosis}", TEXT_COLOR, font=font)

    # Tuberculosis Date
    draw.text((980, 1340), f"{tuberculosis_date}", TEXT_COLOR, font=font)

    # Diabetes
    if diabetes == "Yes":
        draw.text((740, 1410), f"{diabetes}", TEXT_COLOR, font=font)
    elif diabetes == "No":
        draw.text((870, 1410), f"{diabetes}", TEXT_COLOR, font=font)

    # Diabetes Date
    draw.text((980, 1410), f"{diabetes_date}", TEXT_COLOR, font=font)

    # Rheumatic Fever
    if rheumatic_fever == "Yes":
        draw.text((740, 1480), f"{rheumatic_fever}", TEXT_COLOR, font=font)
    elif rheumatic_fever == "No":
        draw.text((870, 1480), f"{rheumatic_fever}", TEXT_COLOR, font=font)

    # Rheumatic Fever Date
    draw.text((980, 1480), f"{rheumatic_fever_date}", TEXT_COLOR, font=font)

    # Diphtheria
    if diphtheria == "Yes":
        draw.text((740, 1550), f"{diphtheria}", TEXT_COLOR, font=font)
    elif diphtheria == "No":
        draw.text((870, 1550), f"{diphtheria}", TEXT_COLOR, font=font)

    # Diphtheria Date
    draw.text((980, 1550), f"{diphtheria_date}", TEXT_COLOR, font=font)

    # German Measles
    if german_measles == "Yes":
        draw.text((740, 1620), f"{german_measles}", TEXT_COLOR, font=font)
    elif german_measles == "No":
        draw.text((870, 1620), f"{german_measles}", TEXT_COLOR, font=font)

    # German Measles Date
    draw.text((980, 1620), f"{german_measles_date}", TEXT_COLOR, font=font)

    # Poliomyelitis
    if poliomyelitis == "Yes":
        draw.text((740, 1690), f"{poliomyelitis}", TEXT_COLOR, font=font)
    elif poliomyelitis == "No":
        draw.text((870, 1690), f"{poliomyelitis}", TEXT_COLOR, font=font)

    # Poliomyelitis Date
    draw.text((980, 1690), f"{poliomyelitis_date}", TEXT_COLOR, font=font)

    # Chickenpox
    if chickenpox == "Yes":
        draw.text((740, 1760), f"{chickenpox}", TEXT_COLOR, font=font)
    elif chickenpox == "No":
        draw.text((870, 1760), f"{chickenpox}", TEXT_COLOR, font=font)

    # Chickenpox Date
    draw.text((980, 1760), f"{chickenpox_date}", TEXT_COLOR, font=font)

    # Epilepsy
    if epilepsy == "Yes":
        draw.text((740, 1830), f"{epilepsy}", TEXT_COLOR, font=font)
    elif epilepsy == "No":
        draw.text((870, 1830), f"{epilepsy}", TEXT_COLOR, font=font)

    # Epilepsy Date
    draw.text((980, 1830), f"{epilepsy_date}", TEXT_COLOR, font=font)

    # Heart Disease
    if heart_disease == "Yes":
        draw.text((740, 1900), f"{heart_disease}", TEXT_COLOR, font=font)
    elif heart_disease == "No":
        draw.text((870, 1900), f"{heart_disease}", TEXT_COLOR, font=font)

    # Epilepsy Date
    draw.text((980, 1900), f"{heart_disease_date}", TEXT_COLOR, font=font)

    # Kidney Disease
    if kidney_disease == "Yes":
        draw.text((740, 1970), f"{kidney_disease}", TEXT_COLOR, font=font)
    elif kidney_disease == "No":
        draw.text((870, 1970), f"{kidney_disease}", TEXT_COLOR, font=font)

    # Epilepsy Date
    draw.text((980, 1970), f"{kidney_disease_date}", TEXT_COLOR, font=font)

    # --------------------- x ---------------------
    draw.text((700, 2190), f"{allergies_or_asthma}", TEXT_COLOR, font=font)
    draw.text((640, 2310), f"{injuries_or_surgeries}", TEXT_COLOR, font=font)
    draw.text((150, 2590), f"{medicine_details}", TEXT_COLOR, font=font)

    form_page_4.save('output/o4.jpg')


def position_text_page_5(wear_glasses, wear_glasses_date, hearing_problem, hearing_problem_date, child_other_problem,
                         mother_tongue, spoken_home, SEN, nature_of_need, medical_practitioner, prescribed_medication, i_confirm):
    form_page_4 = Image.open("assets/5.jpg")
    draw = ImageDraw.Draw(form_page_4)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("font/Montserrat-Medium.ttf", 45)
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text((700, 240), f"{wear_glasses}", TEXT_COLOR, font=font)
    draw.text((1500, 240), f"{wear_glasses_date}", TEXT_COLOR, font=font)

    draw.text((700, 340), f"{hearing_problem}", TEXT_COLOR, font=font)
    draw.text((1500, 340), f"{hearing_problem_date}", TEXT_COLOR, font=font)

    draw.text((150, 530), f"{child_other_problem}", TEXT_COLOR, font=font)

    draw.text((920, 900), f"{mother_tongue}", TEXT_COLOR, font=font)
    draw.text((920, 980), f"{spoken_home}", TEXT_COLOR, font=font)

    draw.text((320, 1170), f"{SEN}", TEXT_COLOR, font=font)

    draw.text((780, 1210), f"{nature_of_need}", TEXT_COLOR, font=font)

    draw.text((1500, 1400), f"{medical_practitioner}", TEXT_COLOR, font=font)
    draw.text((1800, 1520), f"{prescribed_medication}", TEXT_COLOR, font=font)


    draw.text((400, 2500), f"{i_confirm}", TEXT_COLOR, font=font)



    form_page_4.save('output/o5.jpg')
