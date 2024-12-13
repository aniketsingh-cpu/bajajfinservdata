import json
import math
from collections import Counter
from datetime import datetime

# If data is in a file named data.json
# with open('data.json', 'r') as f:
#     data = json.load(f)

# If data is in a variable named data (as provided in the prompt), then directly:

import json

json_str = """
[
    {
        "_id": "T6hf3rb5",
        "appointmentId": "40d2-9c9f",
        "patientDetails": {
            "_id": "T6hb630b3",
            "firstName": "Css",
            "lastName": "",
            "emailId": "",
            "gender": "",
            "alternateContact": "",
            "birthDate": null
        },
        "phoneNumber": "96686896670",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619404",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619804",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T65g3rb5",
        "appointmentId": "40dbtc9f",
        "patientDetails": {
            "_id": "T6h33b300",
            "firstName": "Lokesh",
            "lastName": "",
            "emailId": "",
            "gender": "M",
            "birthDate": "1996-05-16T18:30:00.000Z"
        },
        "phoneNumber": "9496368916",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619404",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619804",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "30",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T7g6Srb5",
        "appointmentId": "g3Wt5c9f",
        "patientDetails": {
            "_id": "TjhB4373",
            "phrId": "63b5hvy614d5",
            "firstName": "Shila",
            "lastName": "Das",
            "emailId": ""
        },
        "phoneNumber": "7787204833",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619404",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "10",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619404",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "60",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "619404",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "94bg8W8d",
        "appointmentId": "fb6-a535",
        "patientDetails": {
            "_id": "6df4R5b",
            "phrId": "644nig7y",
            "firstName": "Bhavika",
            "lastName": "Ben Panchal",
            "emailId": "",
            "gender": "F",
            "birthDate": "1988-04-24T14:30:00.000Z"
        },
        "phoneNumber": "9376756879",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619704",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T6h8H56c",
        "appointmentId": "67h7KL9",
        "patientDetails": {
            "_id": "lK9hy06a",
            "firstName": "Raghu Viju",
            "lastName": "",
            "emailId": "",
            "alternateContact": ""
        },
        "phoneNumber": "5267384241",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619384",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-1-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "628424",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T9Jh8c8",
        "appointmentId": "Hy7Y91",
        "patientDetails": {
            "_id": "kI9d5c6",
            "firstName": "Dinesh Kumar",
            "lastName": "",
            "emailId": "",
            "gender": "M",
            "birthDate": "1983-05-16T18:30:00.000Z",
            "chat": {
                "_id": "09hUb5c7"
            },
            "customId": "3FPEUCW8HACJ"
        },
        "phoneNumber": "+919826374025",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "643404",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "615604",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "617704",
                    "medicineName": "E",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "685404",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "9Is624b9",
        "appointmentId": "10dY8a-4a",
        "patientDetails": {
            "_id": "i9R324b7",
            "phrId": "67Yt2b97",
            "firstName": "Lalit",
            "lastName": "Sankhwal",
            "emailId": "",
            "gender": "M",
            "alternateContact": "",
            "birthDate": "2003-06-27T14:30:00.000Z"
        },
        "phoneNumber": "7587265252",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "632304",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "617624",
                    "medicineName": "E",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T8H9c3c6",
        "appointmentId": "e8056Ye8",
        "patientDetails": {
            "_id": "T6h41b5ad3d8002ad9c3c4",
            "firstName": "Ravi",
            "lastName": "",
            "emailId": "",
            "chat": {
                "_id": "T6h41b5ad3d8002ad9c3c5"
            },
            "customId": "8AV4ICI5I389"
        },
        "phoneNumber": "5586958767",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": "cold",
                    "mediusId": ""
                }
            ],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619404",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T8Ud380",
        "appointmentId": "dbc0-c66b",
        "patientDetails": {
            "_id": "T9Iy347e",
            "firstName": "Dinesh",
            "lastName": "",
            "emailId": "",
            "gender": "M",
            "birthDate": "1983-05-16T18:30:00.000Z",
            "chat": {
                "_id": "T9IsT37f"
            },
            "customId": "0308MSAHYR8K"
        },
        "phoneNumber": "9987602525",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "E",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T345fG4",
        "appointmentId": "1576a7",
        "patientDetails": {
            "_id": "T4Rb1a2",
            "firstName": "Sanjay",
            "lastName": "",
            "emailId": "",
            "gender": "M",
            "birthDate": "1998-05-16T18:30:00.000Z",
            "chat": {
                "_id": "7Yd9b1a3"
            },
            "customId": "8S7A3D4K4WZH"
        },
        "phoneNumber": "9234354366",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T4F6a175",
        "appointmentId": "b6Te4ac",
        "patientDetails": {
            "_id": "Tr4T2173",
            "phrId": "6E48U79",
            "firstName": "Akshay",
            "lastName": "Akshay",
            "emailId": "",
            "gender": "M",
            "birthDate": "1988-04-08T00:00:00.000Z",
            "chat": {
                "_id": "Tr4W174",
                "channelId": "9IrR9ce7"
            },
            "customId": "83AH0K04SSTV"
        },
        "phoneNumber": "4863281056",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "E",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "TW3r002",
        "appointmentId": "bu5Qfb",
        "patientDetails": {
            "_id": "T6Wa50",
            "firstName": "Nirmala",
            "lastName": "",
            "emailId": "",
            "gender": "F",
            "birthDate": "1971-05-16T18:30:00.000Z",
            "chat": {
                "_id": "T6h3635ad3d8002ad9b001"
            },
            "customId": "832ZIS6ZCAHH"
        },
        "phoneNumber": "8687986800",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "E",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "611304",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "6U6Ra36",
        "appointmentId": "86U8Y45",
        "patientDetails": {
            "_id": "65sRa36",
            "firstName": "Satish",
            "lastName": "",
            "emailId": "",
            "birthDate": "1970-05-16T18:30:00.000Z",
            "chat": {
                "_id": "6Y6a36"
            },
            "customId": "YW883CARSES3"
        },
        "phoneNumber": "",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": "puo",
                    "mediusId": ""
                }
            ],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "u7Y7Aa5",
        "appointmentId": "Ufd7231",
        "patientDetails": {
            "_id": "UG67231",
            "phrId": "T6a7231",
            "firstName": "Kalaiarasi",
            "lastName": "Kalaiarasi",
            "emailId": "",
            "gender": "F",
            "alternateContact": "",
            "birthDate": "1997-07-31T00:00:00.000Z"
        },
        "phoneNumber": "7152684236",
        "consultationData": {
            "labTest": [],
            "emrTemplates": [],
            "doctorNotes": "",
            "sharePrescription": false,
            "languageCode": "en",
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "_id": "6T67a6a4",
            "chiefComplaints": [
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": "fever and bodyache since today morning",
                    "mediusId": ""
                },
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": " 2 episodes of vomiting today morning",
                    "mediusId": ""
                },
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": " slight abdominal pain",
                    "mediusId": ""
                },
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": " No loose stools",
                    "mediusId": ""
                },
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": " No urinary complains",
                    "mediusId": ""
                },
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": " LMP-1\/5\/23",
                    "mediusId": ""
                },
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": " h\/o travel 2-3 days back",
                    "mediusId": ""
                }
            ],
            "updatedAt": "2023-05-16T14:42:50.620Z",
            "createdAt": "2023-05-16T14:42:50.620Z",
            "customThree": [],
            "customTwo": [],
            "customOne": [],
            "investigationInstructions": [],
            "medicineTemplates": [],
            "investigationTemplates": [],
            "adviceTemplates": [],
            "findings": [],
            "emergencyInstructionsTemplate": [],
            "emergencyInstructions": [],
            "prognosis": [],
            "investigations": [],
            "procedures": [],
            "advices": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "attachments": [],
            "examinationNote": [],
            "disease": []
        }
    },
    {
        "_id": "T3R5dec",
        "appointmentId": "E4u5Ea2",
        "patientDetails": {
            "_id": "E4u5Ea2",
            "firstName": "Satyanaaryan",
            "lastName": "",
            "emailId": "",
            "alternateContact": "",
            "chat": {
                "_id": "E4u5Ea2"
            },
            "customId": "E4u5Ea2"
        },
        "phoneNumber": "",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T4E7Ge6",
        "appointmentId": "T4E3e410",
        "patientDetails": {
            "_id": "T4E7Ge6",
            "firstName": "Nivitha",
            "lastName": "",
            "emailId": "",
            "gender": "F",
            "birthDate": "1997-05-16T18:30:00.000Z"
        },
        "phoneNumber": "9184723620",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "E5336545",
        "appointmentId": "04Re22d",
        "patientDetails": {
            "_id": "04Re22d",
            "firstName": "Tejpal",
            "lastName": "",
            "emailId": "",
            "gender": "M",
            "birthDate": "1972-05-16T18:30:00.000Z",
            "chat": {
                "_id": "04Re22d"
            },
            "customId": "04Re22d"
        },
        "phoneNumber": "",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": "G\/E",
                    "mediusId": ""
                }
            ],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T7Ys58b",
        "appointmentId": "af9784hf",
        "patientDetails": {
            "_id": "u7dWa589",
            "firstName": "Nandhini",
            "lastName": "",
            "emailId": "",
            "gender": "F",
            "birthDate": "2001-05-16T18:30:00.000Z"
        },
        "phoneNumber": "5847346075",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "619504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "Y874Us5w",
        "appointmentId": "I8eW201",
        "patientDetails": {
            "_id": "TU7e913",
            "firstName": "Dhanamma",
            "lastName": "",
            "emailId": "",
            "gender": "F",
            "chat": {
                "_id": "u8e6fgd14"
            },
            "customId": "y7ewr5w"
        },
        "phoneNumber": "9064537237",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "619504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "Y7s5G42",
        "appointmentId": "f7r501cb1",
        "patientDetails": {
            "_id": "H8s2d40",
            "firstName": "Kushal",
            "lastName": "",
            "emailId": ""
        },
        "phoneNumber": "",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": "cold",
                    "mediusId": ""
                }
            ],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "Y7eE5cd8",
        "appointmentId": "cf092c8t6c",
        "patientDetails": {
            "_id": "u9cd6",
            "phrId": "6463U8s231",
            "firstName": "Daniya",
            "lastName": "Zehra",
            "emailId": "",
            "gender": "F",
            "birthDate": "2001-08-27T00:00:00.000Z"
        },
        "phoneNumber": "992727892",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "619504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "I9984e8",
        "appointmentId": "O02n262e",
        "patientDetails": {
            "_id": "Pdh97S6",
            "phrId": "Jus0480",
            "firstName": "Jay",
            "lastName": "Sharma",
            "emailId": "",
            "gender": "M",
            "birthDate": "1998-11-19T23:30:00.000Z"
        },
        "phoneNumber": "6888324121",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "612504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "Tu78a783",
        "appointmentId": "5dfN9s41",
        "patientDetails": {
            "_id": "h02U8a781",
            "firstName": "Preethi",
            "lastName": "",
            "emailId": "",
            "gender": "F",
            "birthDate": "1996-05-16T18:30:00.000Z",
            "chat": {
                "_id": "T6h9a782"
            },
            "customId": "H8NdI3MAW"
        },
        "phoneNumber": "8248594521",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "611504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "619504",
                    "medicineName": "G",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "619304",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "U9D2w6c",
        "appointmentId": "cc86re0f",
        "patientDetails": {
            "_id": "T6h40a5ad3d8002ad9c06a",
            "firstName": "VITTHAL SHANKARRAO GHATE",
            "lastName": "",
            "alternateContact": "+917797689682",
            "customId": "83AAWWI24W63",
            "chat": {
                "_id": "T6h40a1becc5002908b235"
            }
        },
        "phoneNumber": "+917938475936",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "612504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "T6hY6sEe",
        "appointmentId": "bd99dU7",
        "patientDetails": {
            "_id": "Y7sHec",
            "firstName": "Naresh",
            "lastName": "",
            "emailId": "",
            "gender": "M",
            "birthDate": "1992-05-16T18:30:00.000Z"
        },
        "phoneNumber": "+9124648979746",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": "cough cold",
                    "mediusId": ""
                }
            ],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "H7sT6c",
        "appointmentId": "bcWe50",
        "patientDetails": {
            "_id": "T6h408981ayf32b63bcfa",
            "firstName": "Suresh",
            "lastName": "Gaikwad",
            "emailId": "",
            "alternateContact": "",
            "chat": {
                "_id": "Hsb690S"
            },
            "customId": "ABCD1419"
        },
        "phoneNumber": "+916883788633",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "E",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "8Utyd5b",
        "appointmentId": "7au8se3",
        "patientDetails": {
            "_id": "T6U67af9",
            "firstName": "Govardhan",
            "lastName": "",
            "emailId": "",
            "alternateContact": "",
            "chat": {
                "_id": "u7sg9be5a"
            },
            "customId": "Gya7sfw"
        },
        "phoneNumber": "+916636278363",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "612504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "y87Ta5c7",
        "appointmentId": "432cT213",
        "patientDetails": {
            "_id": "R53Et5W",
            "firstName": "Rajeshwari",
            "lastName": "",
            "emailId": "",
            "gender": "F",
            "birthDate": "1999-05-16T18:30:00.000Z",
            "chat": {
                "_id": "T6h2fT5535c6"
            },
            "customId": "K44RwH0T"
        },
        "phoneNumber": "6525356535",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "612504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "612504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "Ub7S65b7",
        "appointmentId": "D3fFr42c",
        "patientDetails": {
            "_id": "dE3r$2b5",
            "firstName": "Santosh",
            "lastName": "",
            "emailId": "",
            "gender": "F",
            "birthDate": "1972-05-16T18:30:00.000Z"
        },
        "phoneNumber": "",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [
                {
                    "templates": [],
                    "symptomSnomedId": "",
                    "symptomSnomedName": "stone pain",
                    "mediusId": ""
                }
            ],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "yD7s2d7",
        "appointmentId": "7uyT6Rs",
        "patientDetails": {
            "_id": "TI93Hd5",
            "firstName": "Tarachand",
            "lastName": "",
            "emailId": "",
            "gender": "M",
            "alternateContact": "",
            "birthDate": "1980-03-22T18:30:00.000Z",
            "chat": {
                "_id": "TH8W2d6"
            },
            "customId": "90hjdX2"
        },
        "phoneNumber": "+919093872282",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "612504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "C",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    },
    {
        "_id": "I9Sb4e8",
        "appointmentId": "O02n2e",
        "patientDetails": {
            "_id": "Pdh97S6",
            "phrId": "Jus0480",
            "firstName": "Jay",
            "lastName": "Sharma",
            "emailId": "",
            "gender": "M",
            "birthDate": "1991-11-19T23:30:00.000Z"
        },
        "phoneNumber": "+916888324121",
        "consultationData": {
            "adviceTemplates": [],
            "advices": [],
            "attachments": [],
            "chiefComplaints": [],
            "customOne": [],
            "customThree": [],
            "customTwo": [],
            "disease": [],
            "doctorNotes": "",
            "emergencyInstructions": [],
            "emergencyInstructionsTemplate": [],
            "emrTemplates": [],
            "examinationNote": [],
            "findings": [],
            "investigationInstructions": [],
            "investigationTemplates": [],
            "investigations": [],
            "isBalicAppointment": false,
            "isQuickPrescription": false,
            "labTest": [],
            "languageCode": "en",
            "medicineTemplates": [],
            "medicines": [
                {
                    "medicineId": "612504",
                    "medicineName": "A",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                },
                {
                    "medicineId": "612504",
                    "medicineName": "D",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": false
                },
                {
                    "medicineId": "612504",
                    "medicineName": "B",
                    "medicineNameStrengthType": "",
                    "frequency": "1-0-1",
                    "duration": "90",
                    "durationIn": "DAYS",
                    "instruction": "AFTER MEAL",
                    "isActive": true
                }
            ],
            "procedures": [],
            "prognosis": [],
            "sharePrescription": false
        }
    }
]
"""
data = json.loads(json_str)  
# ---------- Helper Functions ----------

def is_missing(value):
    # Missing is defined as None, empty string or not present
    if value is None:
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    return False

def calculate_age(birthdate_str):
    # Calculate age based on a reference date (e.g., today's date)
    # If birthdate_str is None or invalid, return None
    if not birthdate_str or is_missing(birthdate_str):
        return None
    try:
        bdate = datetime.fromisoformat(birthdate_str.replace("Z",""))
        today = datetime(2023, 5, 16)  # fixed reference date
        age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
        return age
    except:
        return None

def categorize_age(age):
    # Child: 0–12, Teen: 13–19, Adult: 20–59, Senior: 60+
    if age is None:
        return None
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teen"
    elif 20 <= age <= 59:
        return "Adult"
    else:
        return "Senior"

# ---------- Extract Data ----------

first_names = []
last_names = []
birth_dates = []
genders = []
medicine_counts = []
medicine_name_list = []
medicine_status_list = []  # True for active, False for inactive

for entry in data:
    pd = entry.get("patientDetails", {})
    first_name = pd.get("firstName", "")
    last_name = pd.get("lastName", "")
    birth_date = pd.get("birthDate", None)
    gender = pd.get("gender", "")

    first_names.append(first_name)
    last_names.append(last_name)
    birth_dates.append(birth_date if birth_date else None)
    genders.append(gender)

    consultation = entry.get("consultationData", {})
    meds = consultation.get("medicines", [])
    medicine_counts.append(len(meds))
    for m in meds:
        medicine_name_list.append(m.get("medicineName", ""))
        medicine_status_list.append(m.get("isActive", False))


total_records = len(data)

# ---------- Q4: Percentage of missing values (firstName, lastName, DOB) ----------

missing_firstname = sum(is_missing(fn) for fn in first_names)
missing_lastname = sum(is_missing(ln) for ln in last_names)
missing_birthdate = sum(is_missing(bd) for bd in birth_dates)

perc_missing_firstname = round((missing_firstname / total_records) * 100, 2)
perc_missing_lastname = round((missing_lastname / total_records) * 100, 2)
perc_missing_birthdate = round((missing_birthdate / total_records) * 100, 2)

print("Q4:", f"{perc_missing_firstname:.2f},{perc_missing_lastname:.2f},{perc_missing_birthdate:.2f}")

# ---------- Q5: Percentage of female gender after imputation with mode ----------

# Determine mode of existing non-missing genders
valid_genders = [g for g in genders if not is_missing(g)]
gender_counts = Counter(valid_genders)
if gender_counts:
    mode_gender = gender_counts.most_common(1)[0][0]
else:
    # If no valid genders, assume one (say 'M'), but dataset has genders so not needed
    mode_gender = "M"

# Impute missing genders with mode_gender
imputed_genders = [g if not is_missing(g) else mode_gender for g in genders]
female_count = sum(1 for g in imputed_genders if g.upper() == "F")
perc_female = round((female_count / total_records) * 100, 2)

print("Q5:", f"{perc_female:.2f}")

# ---------- Q6: Count of Adults ----------

ages = [calculate_age(bd) for bd in birth_dates]
age_groups = [categorize_age(a) for a in ages]
adult_count = sum(1 for ag in age_groups if ag == "Adult")

print("Q6:", adult_count)

# ---------- Q7: Average number of medicines per record ----------
avg_meds = round(sum(medicine_counts) / total_records, 2)
print("Q7:", avg_meds)

# ---------- Q8: 3rd most frequently prescribed medicineName ----------
medicine_freq = Counter(medicine_name_list)

# Sort by frequency descending
freq_pairs = medicine_freq.most_common()
# freq_pairs is like [(med, count), (med, count), ...]

# If there's a tie for first/second, we still consider the third distinct frequency.
# A standard interpretation:
# 1) Identify distinct frequencies:
#    Example: If top frequencies are: 17 (for A,D), 13 (C), 12 (B)...
#    The "3rd most frequently prescribed" means 3rd after sorting by frequency.
# In this dataset, we can just directly take the sorted result by frequency.
# However, if there's a tie, we must be careful. The problem states "3rd most frequently".
# We'll interpret it as the 3rd entry in the sorted order.

# Let's assume "3rd most frequently" means the 3rd entry in the frequency list:
# If you need to consider ties differently, you'd have to handle them. 
# Based on the reasoning provided earlier, let's just pick the third by descending order.

# freq_pairs is sorted: 
# If there's a tie for first place, both occupy ranks 1 and 2 in the list. The next one is rank 3.
# Just take the 3rd element in freq_pairs.
if len(freq_pairs) < 3:
    third_most = freq_pairs[-1][0] if freq_pairs else None
else:
    third_most = freq_pairs[2][0]

print("Q8:", third_most)

# ---------- Q9: Percentage distribution of active vs inactive medicines ----------
total_meds = len(medicine_status_list)
active_count = sum(medicine_status_list)
inactive_count = total_meds - active_count

perc_active = round((active_count / total_meds) * 100, 2) if total_meds > 0 else 0.00
perc_inactive = round((inactive_count / total_meds) * 100, 2) if total_meds > 0 else 0.00

print("Q9:", f"{perc_active:.2f},{perc_inactive:.2f}")
