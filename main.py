from paste_text import mail_text
from functions import position_text_page_1, position_text_page_2, position_text_page_3, position_text_page_4, position_text_page_5

mail_text.strip()

mail_text = mail_text.splitlines()

for (i, item) in enumerate(mail_text, start=1):
    print(i - 1, item)


# n = 1
# language = ""
# for line in mail_text:
#     # print(f"{n} + {line}")
#     if n == 3:
#         language = line
#     n += 1
#
# print(language)

def formatted_text(get_list):
    needed_list_part = get_list[1:]
    final_text = " ".join(needed_list_part)
    return final_text


# mail_text[].split()
# formatted_text()

# -------------------------- 1.Student Information --------------------------

StudentName_list = mail_text[2].split()
StudentName = formatted_text(StudentName_list)

PreferredName_list = mail_text[3].split()
PreferredName = formatted_text(PreferredName_list)

Gender_list = mail_text[4].split()
Gender = formatted_text(Gender_list)

Age_list = mail_text[5].split()
Age = formatted_text(Age_list)

DOB_list = mail_text[6].split()
DOB = formatted_text(DOB_list)
# DOB -> Year-Month-Date

GradeLevel_list = mail_text[7].split()
GradeLevel = formatted_text(GradeLevel_list)

Address_list = mail_text[8].split()
Address = formatted_text(Address_list)

Nationality_list = mail_text[9].split()
Nationality = formatted_text(Nationality_list)

Religion_list = mail_text[10].split()
Religion = formatted_text(Religion_list)

PassportOrBirthCertificate_list = mail_text[11].split()
PassportOrBirthCertificate = formatted_text(PassportOrBirthCertificate_list)

AcademicYear_list = mail_text[12].split()
AcademicYear = formatted_text(AcademicYear_list)

EnrolmentMonth_list = mail_text[13].split()
EnrolmentMonth = formatted_text(EnrolmentMonth_list)

# print(f"""StudentName: {StudentName}
# PreferredName: {PreferredName}
# Gender: {Gender}
# Age: {Age}
# DOB: {DOB}
# GradeLevel: {GradeLevel}
# Address: {Address}
# Nationality: {Nationality}
# Religion: {Religion}
# PassportOrBirthCertificate: {PassportOrBirthCertificate}
# AcademicYear: {AcademicYear}
# EnrolmentMonth: {EnrolmentMonth}""")
# -------------------------- x --------------------------
# -------------------------- 2.Siblings Information --------------------------

NameOfSibling_list = mail_text[17].split()
NameOfSibling = formatted_text(NameOfSibling_list)

PreviousSDIS_list = mail_text[18].split()
PreviousSDIS = formatted_text(PreviousSDIS_list)
# -------------------------- x --------------------------
# -------------------------- 3.Parent Information --------------------------
FatherName_list = mail_text[22].split()
FatherName = formatted_text(FatherName_list)

FatherOccupation_list = mail_text[23].split()
FatherOccupation = formatted_text(FatherOccupation_list)

FatherPhone_list = mail_text[24].split()
FatherPhone = formatted_text(FatherPhone_list)

FatherEmail_list = mail_text[25].split()
FatherEmail = formatted_text(FatherEmail_list)

MotherName_list = mail_text[26].split()
MotherName = formatted_text(MotherName_list)

MotherOccupation_list = mail_text[27].split()
MotherOccupation = formatted_text(MotherOccupation_list)

MotherPhone_list = mail_text[28].split()
MotherPhone = formatted_text(MotherPhone_list)

MotherEmail_list = mail_text[29].split()
MotherEmail = formatted_text(MotherEmail_list)
# -------------------------- x --------------------------
# -------------------------- 4.Emergency Contact --------------------------
Contact1Name_list = mail_text[33].split()
Contact1Name = formatted_text(Contact1Name_list)

Contact1Phone_list = mail_text[34].split()
Contact1Phone = formatted_text(Contact1Phone_list)

Contact1Email_list = mail_text[35].split()
Contact1Email = formatted_text(Contact1Email_list)

Contact1Relation_list = mail_text[36].split()
Contact1Relation = formatted_text(Contact1Relation_list)

Contact2Name_list = mail_text[37].split()
Contact2Name = formatted_text(Contact2Name_list)

Contact2Phone_list = mail_text[38].split()
Contact2Phone = formatted_text(Contact2Phone_list)

Contact2Email_list = mail_text[39].split()
Contact2Email = formatted_text(Contact2Email_list)

Contact2Relation_list = mail_text[40].split()
Contact2Relation = formatted_text(Contact2Relation_list)

OtherInfo_list = mail_text[42].split()
OtherInfo = formatted_text(OtherInfo_list)
# -------------------------- x --------------------------
# -------------------------- 5.School Information --------------------------
isFirstYear_list = mail_text[46].split()
isFirstYear = formatted_text(isFirstYear_list)

PriorSchoolAddressPhoneGradeYear_list = mail_text[47].split()
PriorSchoolAddressPhoneGradeYear = formatted_text(PriorSchoolAddressPhoneGradeYear_list)

EmergencyTreatment_list = mail_text[48].split()
EmergencyTreatment = formatted_text(EmergencyTreatment_list)

DressCode_list = mail_text[49].split()
DressCode = formatted_text(DressCode_list)

FieldTrip_list = mail_text[50].split()
FieldTrip = formatted_text(FieldTrip_list)

PhotoVideoRelease_list = mail_text[51].split()
PhotoVideoRelease = formatted_text(PhotoVideoRelease_list)
# -------------------------- x --------------------------
# -------------------------- 6.School Directory --------------------------
SchoolDirectory_list = mail_text[55].split()
SchoolDirectory = formatted_text(SchoolDirectory_list)

# -------------------------- x --------------------------
# -------------------------- 7.School Policies --------------------------
Q1_list = mail_text[59].split()
Q1 = formatted_text(Q1_list)

Q2_list = mail_text[60].split()
Q2 = formatted_text(Q2_list)

Q3_list = mail_text[61].split()
Q3 = formatted_text(Q3_list)

Q4_list = mail_text[62].split()
Q4 = formatted_text(Q4_list)

Q5_list = mail_text[63].split()
Q5 = formatted_text(Q5_list)

Q6_list = mail_text[64].split()
Q6 = formatted_text(Q6_list)

Q7_list = mail_text[65].split()
Q7 = formatted_text(Q7_list)

# -------------------------- x --------------------------
# -------------------------- 8. Medical Information --------------------------
# Diseases

Meningitis_list = mail_text[69].split()
MeningitisDate_list = mail_text[70].split()
Meningitis = formatted_text(Meningitis_list)
MeningitisDate = formatted_text(MeningitisDate_list)

ScarletFever_list = mail_text[71].split()
ScarletFeverDate_list = mail_text[72].split()
ScarletFever = formatted_text(ScarletFever_list)
ScarletFeverDate = formatted_text(ScarletFeverDate_list)

Mumps_list = mail_text[73].split()
MumpsDate_list = mail_text[74].split()
Mumps = formatted_text(Mumps_list)
MumpsDate = formatted_text(MumpsDate_list)

WhoopingCough_list = mail_text[75].split()
WhoopingCoughDate_list = mail_text[76].split()
WhoopingCough = formatted_text(WhoopingCough_list)
WhoopingCoughDate = formatted_text(WhoopingCoughDate_list)

Tuberculosis_list = mail_text[77].split()
TuberculosisDate_list = mail_text[78].split()
Tuberculosis = formatted_text(Tuberculosis_list)
TuberculosisDate = formatted_text(TuberculosisDate_list)

Diabetes_list = mail_text[79].split()
DiabetesDate_list = mail_text[80].split()
Diabetes = formatted_text(Diabetes_list)
DiabetesDate = formatted_text(DiabetesDate_list)

RheumaticFever_list = mail_text[81].split()
RheumaticFeverDate_list = mail_text[82].split()
RheumaticFever = formatted_text(RheumaticFever_list)
RheumaticFeverDate = formatted_text(RheumaticFeverDate_list)

Diphtheria_list = mail_text[83].split()
DiphtheriaDate_list = mail_text[84].split()
Diphtheria = formatted_text(Diphtheria_list)
DiphtheriaDate = formatted_text(DiphtheriaDate_list)

GermanMeasles_list = mail_text[85].split()
GermanMeaslesDate_list = mail_text[86].split()
GermanMeasles = formatted_text(GermanMeasles_list)
GermanMeaslesDate = formatted_text(GermanMeaslesDate_list)

Poliomyelitis_list = mail_text[87].split()
PoliomyelitisDate_list = mail_text[88].split()
Poliomyelitis = formatted_text(Poliomyelitis_list)
PoliomyelitisDate = formatted_text(PoliomyelitisDate_list)

ChickenPox_list = mail_text[89].split()
ChickenPoxDate_list = mail_text[90].split()
ChickenPox = formatted_text(ChickenPox_list)
ChickenPoxDate = formatted_text(ChickenPoxDate_list)

Epilepsy_list = mail_text[91].split()
EpilepsyDate_list = mail_text[92].split()
Epilepsy = formatted_text(Epilepsy_list)
EpilepsyDate = formatted_text(EpilepsyDate_list)

HeartDisease_list = mail_text[93].split()
HeartDiseaseDate_list = mail_text[94].split()
HeartDisease = formatted_text(HeartDisease_list)
HeartDiseaseDate = formatted_text(HeartDiseaseDate_list)

KidneyDisease_list = mail_text[95].split()
KidneyDiseaseDate_list = mail_text[96].split()
KidneyDisease = formatted_text(KidneyDisease_list)
KidneyDiseaseDate = formatted_text(KidneyDiseaseDate_list)

# other medical info
MedicalPractitioner_list = mail_text[98].split()
MedicalPractitioner = formatted_text(MedicalPractitioner_list)

PrescribedMedication_list = mail_text[99].split()
PrescribedMedication = formatted_text(PrescribedMedication_list)

AllergiesOrAsthma_list = mail_text[100].split()
AllergiesOrAsthma = formatted_text(AllergiesOrAsthma_list)

InjuriesOrSurgeries_list = mail_text[101].split()
InjuriesOrSurgeries = formatted_text(InjuriesOrSurgeries_list)

MedicineDetails_list = mail_text[102].split()
MedicineDetails = formatted_text(MedicineDetails_list)

WearGlasses_list = mail_text[104].split()
WearGlasses = formatted_text(WearGlasses_list)

WearGlassesDate_list = mail_text[105].split()
WearGlassesDate = formatted_text(WearGlassesDate_list)

HearingProblem_list = mail_text[106].split()
HearingProblem = formatted_text(HearingProblem_list)

HearingProblemDate_list = mail_text[107].split()
HearingProblemDate = formatted_text(HearingProblemDate_list)

ChildOtherProblem_list = mail_text[108].split()
ChildOtherProblem = formatted_text(ChildOtherProblem_list)

SEN_list = mail_text[109].split()
SEN = formatted_text(SEN_list)

NatureOfNeed_list = mail_text[110].split()
NatureOfNeed = formatted_text(NatureOfNeed_list)
# -------------------------- x --------------------------
# -------------------------- 9. Language Spoken --------------------------
MotherTongue_list = mail_text[114].split()
MotherTongue = formatted_text(MotherTongue_list)

SpokenHome_list = mail_text[115].split()
SpokenHome = formatted_text(SpokenHome_list)
# -------------------------- x --------------------------
# -------------------------- 10. Confirmation --------------------------
IConfirm_list = mail_text[119].split()
IConfirm = formatted_text(IConfirm_list)

position_text_page_1(student_name=StudentName, preferred_name=PreferredName, gender=Gender, age=Age, dob=DOB,
                     grade_level=GradeLevel, address=Address, nationality=Nationality, religion=Religion,
                     passport_or_certificate=PassportOrBirthCertificate, name_of_sibling=NameOfSibling,
                     previous_SDIS=PreviousSDIS, academic_year=AcademicYear, enrollment_month=EnrolmentMonth,
                     father_name=FatherName,
                     father_occupation=FatherOccupation, father_phone=FatherPhone, father_email=FatherEmail,
                     mother_name=MotherName, mother_occupation=MotherOccupation, mother_phone=MotherPhone,
                     mother_email=MotherEmail, contact_1_name=Contact1Name, contact_1_phone=Contact1Phone,
                     contact_1_email=Contact2Email, contact_1_relation=Contact1Relation, contact_2_name=Contact2Name,
                     contact_2_phone=Contact2Phone, contact_2_email=Contact2Email, contact_2_relation=Contact2Relation,
                     other_info=OtherInfo)

position_text_page_2(is_first_year=isFirstYear, prior_school_address_phone_grade_year=PriorSchoolAddressPhoneGradeYear, emergency_treatment=EmergencyTreatment, dress_code=DressCode, field_trip=FieldTrip, photo_video_release=PhotoVideoRelease)

position_text_page_3(school_directory=SchoolDirectory, q1=Q1, q2=Q2, q3=Q3, q4=Q4, q5=Q5, q6=Q6, q7=Q7,
                     )

position_text_page_4(meningitis=Meningitis, meningitis_date=MeningitisDate, scarlet_fever=ScarletFever,
                     scarlet_fever_date=ScarletFeverDate, mumps=Mumps, mumps_date=MumpsDate,
                     whooping_cough=WhoopingCough,
                     whooping_cough_date=WhoopingCoughDate, tuberculosis=Tuberculosis,
                     tuberculosis_date=TuberculosisDate, diabetes=Diabetes, diabetes_date=DiabetesDate,
                     rheumatic_fever=RheumaticFever,
                     rheumatic_fever_date=RheumaticFeverDate, diphtheria=Diphtheria, diphtheria_date=DiphtheriaDate,
                     german_measles=GermanMeasles, german_measles_date=GermanMeaslesDate,
                     poliomyelitis=Poliomyelitis, poliomyelitis_date=PoliomyelitisDate, chickenpox=ChickenPox,
                     chickenpox_date=ChickenPoxDate, epilepsy=Epilepsy, epilepsy_date=EpilepsyDate,
                     heart_disease=HeartDisease, heart_disease_date=HeartDiseaseDate, kidney_disease=KidneyDisease,
                     kidney_disease_date=KidneyDiseaseDate, allergies_or_asthma=AllergiesOrAsthma, injuries_or_surgeries=InjuriesOrSurgeries, medicine_details=MedicineDetails)


position_text_page_5(wear_glasses=WearGlasses, wear_glasses_date=WearGlassesDate, hearing_problem=HearingProblem, hearing_problem_date=HearingProblemDate, child_other_problem=ChildOtherProblem,
                         mother_tongue=MotherTongue, spoken_home=SpokenHome, SEN=SEN, nature_of_need=NatureOfNeed, i_confirm=IConfirm, medical_practitioner=MedicalPractitioner, prescribed_medication=PrescribedMedication)


