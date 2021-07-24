from django.shortcuts import render

monthsList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

nationalitiesList = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian',
                     'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']

qualificationsList = ['Degree',
                      'Diploma',
                      'HND',
                      'Vocational',
                      'Others']


currentJobsFunctionList = ['Accounting, Auditing & Finance',
                           'Admin & Office',
                           'Building & Architecture',
                           'Community & Social Services',
                           'Consulting & Strategy',
                           'Creative & Design',
                           'Customer Service & Support',
                           'Driver & Transport Services',
                           'Engineering & Technology',
                           'Estate Agents & Property Management',
                           'Farming & Agriculture',
                           'Food Services & Catering',
                           'Health & Safety',
                           'Hospitality & Leisure',
                           'Human Resources',
                           'Legal Services',
                           'Management & Business Development',
                           'Marketing & Communications',
                           'Medical & Pharmaceutical',
                           'Product & Project Management',
                           'Quality Control & Assurance ',
                           'Research, Teaching & Training',
                           'Sales',
                           'Software & Data',
                           'Supply Chain & Procurement',
                           'Trades & Services']


def studentRegisterFormController(request):
    dayList = []
    yearList = []
    yearExperienceList = []

    for day in range(1, 32):
        dayList.append(day)

    for year in range(1900, 2015):
        yearList.append(year)

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    yearList.reverse()
    dobMap = {
        "day": dayList,
        "month": monthsList,
        "year": yearList,
    }

    return render(request,
                  'studentRegisterForm.html',
                  {"heading": "Create a Job Seeker Account | ATU Job Portal",
                   "dob": dobMap,
                   "nationalities": nationalitiesList,
                   "qualifications": qualificationsList,
                   "currentJobs": currentJobsFunctionList,
                   "yearExperiences": yearExperienceList})
