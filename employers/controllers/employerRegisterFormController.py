from django.shortcuts import render


positionList = ['C-level: CEO / COO / CIO / CFO / CTO / CPO',
                'Senior Management: Head of Department / Team Lead',
                'Middle Management: Supervisor / Unit Head',
                'Junior Level: Associate / Officer', ]

industriesList = ["Advertising, Media & Communications",
                  "Agriculture, Fishing & Forestry",
                  "Automotive & Aviation",
                  "Banking, Finance & Insurance",
                  "Construction",
                  "Education",
                  "Energy & Utilities",
                  "Enforcement & Security",
                  "Entertainment, Events & Sport",
                  "Government",
                  "Healthcare",
                  "Hospitality & Hotel",
                  "IT & Telecoms",
                  "Law & Compliance",
                  "Manufacturing & Warehousing",
                  "Mining, Energy & Metals",
                  "NGO, NPO & Charity",
                  "Real Estate",
                  "Recruitment",
                  "Retail, Fashion & FMCG",
                  "Shipping & Logistics",
                  "Tourism & Travel"]

employeesNumberList = ["1-10", "11-20", "21-30",
                       "31-40", "41-50", "50-100", "More than 100"]

employerTypeList = ["Direct Employer", "Recruitment Agency"]


def employerRegisterFormController(request):
    return render(request,
                  'employerRegisterForm.html',
                  {"heading": "Create an Employer Account | ATU Job Portal",
                   "positions": positionList,
                   "industries": industriesList,
                   "employeesNumbers": employeesNumberList,
                   "employerTypes": employerTypeList})
