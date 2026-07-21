"""
SINGLE SOURCE OF TRUTH — ITIL 4 Foundation Training (Voucher Included), C348.

Non-WSQ mirror of the WSQ course TGS-2024049350 (master trainer deck v12),
with the entire funding/compliance layer removed: no assessment, no TRAQOM,
no digital attendance, no SSG/SkillsFuture references. The freed Day-3 time
is reallocated to hands-on labs and exam preparation for the official
ITIL 4 Foundation exam (voucher included with the course).

Guiding principle: the course material must be 100% aligned to the exam
domains so students who take the course can pass the ITIL 4 Foundation exam.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "ITIL 4 Foundation Training"
SHORT_TITLE  = "ITIL 4 Foundation Training"   # used in output filenames
COURSE_CODE  = "C348"
VERSION      = "v13.0"
VERSION_DATE = "21 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 3
MODE         = "Instructor-led classroom training with group case-study and scenario-based activities"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain the key concepts of service management, including services, value, outcomes, costs, risks, utility and warranty, and the roles of service providers and consumers.",
    "LO2: Apply the seven ITIL guiding principles to service management decisions and improvement initiatives in the workplace.",
    "LO3: Describe the four dimensions of service management and evaluate how each dimension affects the delivery of a service.",
    "LO4: Explain the ITIL service value system and the six service value chain activities, and apply the continual improvement model.",
    "LO5: Describe the purpose of the key ITIL practices and apply them to incident, problem, change and service request scenarios.",
]
LO_TITLES = [
    "Key Concepts of Service Management",
    "ITIL Guiding Principles",
    "Four Dimensions of Service Management",
    "The Service Value System",
    "ITIL Practices",
]

# ------------------------------------------------------------------ topics (= exam domains)
TOPICS = [
    dict(num=1, code="01",
         title="Understand Key Concepts of Service Management",
         subtitle="Services · Value · Outcomes, Costs and Risks · Providers and Consumers · Utility and Warranty",
         weighting="25%",
         concepts=[
            "A service is a means of enabling value co-creation by facilitating outcomes customers want to achieve, without the customer having to manage specific costs and risks.",
            "Service management is a set of specialised organisational capabilities for enabling value to customers in the form of services.",
            "Value is co-created through an active relationship between the service provider and the service consumer.",
            "Service consumers take on the roles of customer, user and sponsor; providers deliver service offerings made up of goods, access to resources and service actions.",
            "Outputs are deliverables of an activity; outcomes are the results a stakeholder actually achieves, enabled by those outputs.",
            "Utility is what the service does (fit for purpose); warranty is how the service performs (fit for use).",
         ]),
    dict(num=2, code="02",
         title="ITIL Guiding Principles",
         subtitle="Focus on Value · Start Where You Are · Progress Iteratively · Collaborate · Think Holistically · Keep It Simple · Optimize and Automate",
         weighting="20%",
         concepts=[
            "A guiding principle is a recommendation that guides an organisation in all circumstances, regardless of changes in goals, strategies or type of work.",
            "Focus on value: everything the organisation does should link back, directly or indirectly, to value for itself, its customers and its stakeholders.",
            "Start where you are: assess and reuse what already exists rather than discarding it and rebuilding from scratch.",
            "Progress iteratively with feedback: organise work into smaller manageable sections, executed and completed in a timely manner, using feedback at each iteration.",
            "Collaborate and promote visibility: involve the right people in the right roles to improve buy-in, relevance and the likelihood of long-term success.",
            "Think and work holistically, keep it simple and practical, and optimize before you automate.",
         ]),
    dict(num=3, code="03",
         title="The Four Dimensions of Service Management",
         subtitle="Organizations and People · Information and Technology · Partners and Suppliers · Value Streams and Processes",
         weighting="15%",
         concepts=[
            "The four dimensions ensure a holistic approach to service management; every component of the SVS must be considered from all four.",
            "Organizations and people covers roles, responsibilities, structures, culture and the competencies needed to deliver the service.",
            "Information and technology covers the information and knowledge required, plus the technologies that support and enable the service.",
            "Partners and suppliers covers relationships with other organisations involved in the design, deployment, delivery and support of services.",
            "Value streams and processes covers how the parts of the organisation work together, in an integrated and coordinated way, to enable value creation.",
            "External factors — political, economic, social, technological, legal and environmental (PESTLE) — constrain and shape all four dimensions.",
         ]),
    dict(num=4, code="04",
         title="The Service Value System",
         subtitle="ITIL SVS · Plan · Improve · Engage · Design and Transition · Obtain/Build · Deliver and Support",
         weighting="20%",
         concepts=[
            "The ITIL service value system describes how all components and activities of the organisation work together as a system to enable value creation.",
            "The SVS comprises guiding principles, governance, the service value chain, practices and continual improvement; its inputs are opportunity and demand.",
            "The service value chain is a set of six interconnected activities an organisation performs to deliver a valuable product or service to its consumers.",
            "Plan ensures a shared understanding of vision, status and improvement direction; improve ensures continual improvement of products, services and practices.",
            "Engage provides understanding of stakeholder needs and transparency; design and transition ensures products and services continually meet expectations.",
            "The continual improvement model runs from 'What is the vision?' through to 'How do we keep the momentum going?' in seven steps.",
         ]),
    dict(num=5, code="05",
         title="ITIL Practices",
         subtitle="Continual Improvement · Change Enablement · Incident · Problem · Service Request · Service Desk · Service Level Management",
         weighting="20%",
         concepts=[
            "A practice is a set of organisational resources designed for performing work or accomplishing an objective; ITIL 4 defines 34 practices in three groups.",
            "Incident management minimises the negative impact of incidents by restoring normal service operation as quickly as possible.",
            "Problem management reduces the likelihood and impact of incidents by identifying actual and potential causes; a known error is an analysed problem not yet resolved.",
            "Change enablement maximises the number of successful IT changes by ensuring risks are properly assessed and changes authorised by a change authority.",
            "The service desk captures demand for incident resolution and service requests, and is the entry point and single point of contact for users.",
            "Service level management sets clear business-based targets for service performance, documented in service level agreements (SLAs).",
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Key Concepts of Service Management and the ITIL Guiding Principles",
    2: "The Four Dimensions of Service Management and the Service Value System",
    3: "ITIL Practices, Capstone Labs and Exam Preparation",
}

# ------------------------------------------------------------------ schedule
# (start, end, minutes, kind, activity_text)
# kind: admin | topic | lab | break | lunch | recap — non-lunch minutes total
# 480 (8 instructional hours) per day. "{labN}" expands from the domain files.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","10:00",30,"admin","Welcome, trainer and learner introductions, ground rules and course outline"),
        ("10:00","11:00",60,"topic","Learning outcomes, course overview and how the ITIL 4 Foundation exam and exam voucher work"),
        ("11:00","11:15",15,"break","Tea break"),
        ("11:15","13:00",105,"topic","Topic 1 — Understand Key Concepts of Service Management: services, service management, ITIL and the SVS; value co-creation"),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","15:00",60,"topic","Topic 1 (continued) — service providers, consumers and the customer/user/sponsor roles; service offerings, goods, access to resources and service actions; service relationships"),
        ("15:00","16:00",60,"topic","Topic 1 (continued) — outputs vs outcomes, costs, risks, utility and warranty"),
        ("16:00","16:15",15,"break","Tea break"),
        ("16:15","17:45",90,"lab","Hands-on: "+lab_titles([1])),
        ("17:45","18:30",45,"recap","Topic 1 recap, quiz review and Q&A"),
     ]),
     2: (DAY_THEMES[2], [
        ("9:30","9:45",15,"recap","Day 1 recap"),
        ("9:45","11:00",75,"topic","Topic 2 — ITIL Guiding Principles: the seven principles, with worked workplace examples"),
        ("11:00","11:15",15,"break","Tea break"),
        ("11:15","12:15",60,"lab","Hands-on: "+lab_titles([2])),
        ("12:15","13:00",45,"topic","Topic 3 — The Four Dimensions of Service Management: organizations and people, information and technology"),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","15:15",75,"topic","Topic 3 (continued) — partners and suppliers, value streams and processes; external factors and PESTLE"),
        ("15:15","16:15",60,"lab","Hands-on: "+lab_titles([3])),
        ("16:15","16:30",15,"break","Tea break"),
        ("16:30","18:00",90,"topic","Topic 4 — The Service Value System: the SVS, opportunity and demand, governance, and the six service value chain activities"),
        ("18:00","18:30",30,"recap","Topics 2–4 recap, quiz review and Q&A"),
     ]),
     3: (DAY_THEMES[3], [
        ("9:30","9:45",15,"recap","Day 2 recap"),
        ("9:45","11:00",75,"lab","Topic 4 (continued) — the continual improvement model, seven steps. Hands-on: "+lab_titles([4])),
        ("11:00","11:15",15,"break","Tea break"),
        ("11:15","13:00",105,"topic","Topic 5 — ITIL Practices: practice groups; continual improvement, information security, relationship and supplier management"),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","15:00",60,"topic","Topic 5 (continued) — change enablement, incident management, problem management, service request management, service desk and service level management"),
        ("15:00","16:00",60,"lab","Hands-on: "+lab_titles([5,6])),
        ("16:00","16:15",15,"break","Tea break"),
        ("16:15","17:15",60,"lab","Hands-on: "+lab_titles([7])),
        ("17:15","18:15",60,"lab","Hands-on: "+lab_titles([8])),
        ("18:15","18:30",15,"recap","Course wrap-up, exam voucher booking briefing, practice-exam walkthrough and Q&A"),
     ]),
    }

# ------------------------------------------------------------------ trainer / admin slides
TRAINER_CERT     = "ITIL 4 certified — IT service management, service operations and continual improvement."
TRAINER_DELIVERS = "Professional short courses on IT service management, IT infrastructure and IT operations."

ICE_BREAKER = [
    "Your name and organisation / role.",
    "Your experience with IT service management or IT support (if any).",
    "What you want to be able to improve in your service operations after this course.",
]

# ------------------------------------------------------------------ deck "Core Concepts" section
COURSE_OVERVIEW = dict(
    section_title="IT Service Management Fundamentals",
    concepts_title="What is IT Service Management?",
    concepts=[
        ("A service", "A means of enabling value co-creation by facilitating outcomes customers want, without the customer managing specific costs and risks."),
        ("Service management", "A set of specialised organisational capabilities for enabling value to customers in the form of services."),
        ("ITIL", "A source of good practice in IT service management — validated across diverse environments and situations."),
        ("Value co-creation", "Value is not delivered TO the consumer; it is co-created WITH them through an active service relationship."),
    ],
    framework_title="How the ITIL Service Value System Fits Together",
    framework=[
        ("Inputs", "Opportunity (options to add value) and demand (the need for services) trigger the SVS activities."),
        ("The system", "Guiding principles and governance steer the service value chain, supported by the practices and continual improvement."),
        ("Output", "Value co-created with stakeholders — outcomes enabled, costs and risks removed, continually improved."),
    ],
    statement=dict(
        headline="Value is co-created, not delivered.",
        body="The ITIL SVS describes how every component and activity works together as a system to enable value creation.",
        kicker="WHY IT MATTERS",
    ),
    pillars_title="Core Distinctions You Must Master",
    pillars=[
        ("Utility vs Warranty", [
            "Utility — what the service DOES; functionality offered to meet a need. Fit for purpose.",
            "Warranty — how the service PERFORMS; availability, capacity, reliability, security, continuity. Fit for use.",
            "A service needs BOTH to deliver value.",
        ]),
        ("Output vs Outcome", [
            "Output — a tangible or intangible deliverable of an activity.",
            "Outcome — a result for a stakeholder, enabled by one or more outputs.",
            "Outputs are what you produce; outcomes are why the consumer cared.",
        ]),
        ("Costs and Risks", [
            "A service should REMOVE costs and risks from the consumer.",
            "Consuming a service also IMPOSES costs and risks of its own.",
            "Value is judged on the net effect of both.",
        ]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Read the BrightDesk Services scenario for the lab.",
        "Work the tables and classifications in your small group.",
        "Justify every classification and mapping you record.",
        "Present your group's findings and defend your conclusions.",
        "Cross-check against the ITIL definitions in the Learner Guide.",
    ],
)

# ------------------------------------------------------------------ wrap-up
NEXT_STEPS = dict(
    title="Preparing for the ITIL 4 Foundation Exam",
    items=[
        "An official ITIL 4 Foundation exam voucher is included with this course — book your exam while the material is fresh.",
        "Review the key concepts and definitions in each topic of the Learner Guide.",
        "Re-read the seven guiding principles and be able to apply each to a scenario.",
        "Memorise the purpose statements of the ITIL practices covered in Topic 5.",
        "Be able to distinguish incident, problem, known error, workaround, service request and change.",
        "Attempt the practice exam and review every explanation: https://exams.tertiaryinfotech.com/practice-exams/axelos/axelos-itil4-foundation",
    ],
)

THANK_YOU = dict(
    body="You are now ready to apply ITIL 4 service management practices in your organisation — and to sit the ITIL 4 Foundation exam with your included voucher.",
    kicker="SERVICE MANAGEMENT EXCELLENCE",
)

# ------------------------------------------------------------------ Learner Guide content
LG_INTRO = (
    "Use this guide alongside the course slides and the in-class group activities. ITIL 4 Foundation "
    "is a knowledge-based course: the activities are group discussions, case-study analyses and "
    "scenario triage exercises rather than software labs, so the value comes from working through "
    "the reasoning with your group and defending your conclusions to the class."
)
LG_INTRO2 = (
    "Definitions matter in ITIL. Many exam questions turn on the precise distinction between "
    "two similar terms — output and outcome, utility and warranty, incident and problem, service "
    "request and incident. Where this guide gives a definition, learn it as written."
)

LG_SETUP = dict(
    needs=[
        "No prior ITIL certification or technical prerequisite is required.",
        "Familiarity with an IT support, IT operations or service delivery environment is helpful but not essential.",
        "Bring a real service or workplace situation to discuss — several activities ask you to apply ITIL concepts to your own organisation.",
        "Pen and paper (or a laptop) for the lab worksheets and group presentations.",
    ],
    verify_text="No software setup is required — the labs are worksheet and discussion based.",
    verify_code="",
    conventions=[
        "Each activity states the learning outcome it maps to, so you can trace it back to the exam domains.",
        "Activities are done in small groups of 2–3 persons; each group presents its findings to the class.",
        "The 'Test it' check at the end of each activity is the standard your group's output should meet.",
        "Key ITIL terms appear in the Glossary at the end of this guide — learn the exact definitions.",
        "Record the assumptions your group makes; being able to justify an assumption is part of the skill.",
    ],
)

LAB_NOTE = "Work the labs with your group on the shared BrightDesk Services scenario."

LG_WRAPUP = dict(
    title="Key Distinctions and Quick References",
    intro="Foundation-level exam questions frequently test whether you can separate closely related "
          "terms. Be able to state each difference in one sentence and give an example of each.",
    sections=[
        dict(title="Output vs Outcome", bullets=[
            "Output — a tangible or intangible deliverable of an activity (a delivered package, a completed task, a generated report).",
            "Outcome — a result for a stakeholder, enabled by one or more outputs (the stakeholder can now do something they could not before).",
            "Test: if you can hand it over, it is an output; if it is a change in the stakeholder's situation, it is an outcome.",
        ]),
        dict(title="Utility vs Warranty", bullets=[
            "Utility — what the service DOES; the functionality offered to meet a particular need. Fit for purpose.",
            "Warranty — how the service PERFORMS; availability, capacity, reliability, security and continuity. Fit for use.",
            "A service needs BOTH to deliver value: functionality that is unavailable delivers nothing.",
        ]),
        dict(title="Incident vs Problem vs Known Error", bullets=[
            "Incident — an unplanned interruption to a service, or a reduction in the quality of a service. Restore service as quickly as possible.",
            "Problem — a cause, or potential cause, of one or more incidents. Reduce likelihood and impact.",
            "Known error — a problem that has been analysed and has not been resolved. Often managed with a workaround.",
            "Workaround — a solution that reduces or eliminates the impact of an incident or problem for which a full resolution is not yet available.",
        ]),
        dict(title="Service Request vs Incident", bullets=[
            "Service request — a request from a user or their authorised representative that initiates a normal, pre-defined service action.",
            "Incident — something is broken or degraded that should not be.",
            "Test: was the service working as designed? If yes and the user simply wants something, it is a service request.",
        ]),
        dict(title="Quick Reference — The Seven Guiding Principles", bullets=[
            "Focus on value — everything links back, directly or indirectly, to value for the organisation, its customers and its stakeholders.",
            "Start where you are — assess and reuse what already exists rather than discarding it and rebuilding.",
            "Progress iteratively with feedback — organise work into smaller sections, using feedback at each iteration.",
            "Collaborate and promote visibility — involve the right people in the right roles; make work visible.",
            "Think and work holistically — no service, practice, process, department or supplier stands alone.",
            "Keep it simple and practical — use the minimum number of steps to accomplish an objective.",
            "Optimize and automate — optimize the process first, then automate; never automate a broken process.",
        ]),
        dict(title="Quick Reference — The Six Service Value Chain Activities", bullets=[
            "Plan — ensures a shared understanding of the vision, current status and improvement direction.",
            "Improve — ensures continual improvement of products, services and practices across all value chain activities.",
            "Engage — provides a good understanding of stakeholder needs, transparency and continual engagement.",
            "Design and transition — ensures products and services continually meet stakeholder expectations for quality, cost and time to market.",
            "Obtain/build — ensures service components are available when and where needed, and meet agreed specifications.",
            "Deliver and support — ensures services are delivered and supported according to agreed specifications and stakeholder expectations.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "Book your ITIL 4 Foundation exam using the voucher included with this course while the material is fresh.",
    "Review the key concepts and definitions in each topic of this guide — many exam questions hinge on exact definitions.",
    "Re-read the seven guiding principles and be able to apply each to a written scenario.",
    "Memorise the purpose statements of the ITIL practices covered in Topic 5.",
    "Attempt the practice exam and review every explanation: https://exams.tertiaryinfotech.com/practice-exams/axelos/axelos-itil4-foundation",
    "Revisit any topic whose questions you miss, then re-take the practice exam.",
]

LG_GLOSSARY = [
    ("Service", "A means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks."),
    ("Service management", "A set of specialised organisational capabilities for enabling value to customers in the form of services."),
    ("Value", "The perceived benefits, usefulness and importance of something."),
    ("Value co-creation", "Value is created jointly by the provider and the consumer through an active service relationship — not delivered one way."),
    ("Output", "A tangible or intangible deliverable of an activity."),
    ("Outcome", "A result for a stakeholder, enabled by one or more outputs."),
    ("Utility", "The functionality offered by a product or service to meet a particular need — 'fit for purpose'."),
    ("Warranty", "Assurance that a product or service will meet agreed requirements — 'fit for use'."),
    ("Service offering", "A formal description of one or more services, designed to address the needs of a target consumer group; may include goods, access to resources and service actions."),
    ("Service relationship", "A cooperation between a service provider and a service consumer to co-create value."),
    ("Customer / User / Sponsor", "The consumer roles: the customer defines requirements and owns the outcomes; the user uses the service; the sponsor authorises the budget."),
    ("Service value system (SVS)", "How all the components and activities of the organisation work together as a system to enable value creation."),
    ("Service value chain", "The set of six interconnected activities an organisation performs to deliver a valuable product or service."),
    ("Practice", "A set of organisational resources designed for performing work or accomplishing an objective. ITIL 4 defines 34 practices."),
    ("Guiding principle", "A recommendation that guides an organisation in all circumstances, regardless of changes in goals, strategies or type of work."),
    ("Continual improvement", "A recurring organisational activity performed at all levels to ensure performance continually meets stakeholder expectations."),
    ("Incident", "An unplanned interruption to a service, or a reduction in the quality of a service."),
    ("Problem", "A cause, or potential cause, of one or more incidents."),
    ("Known error", "A problem that has been analysed and has not been resolved."),
    ("Workaround", "A solution that reduces or eliminates the impact of an incident or problem for which a full resolution is not yet available."),
    ("Service request", "A request from a user or a user's authorised representative that initiates a normal, pre-defined service action."),
    ("Change", "The addition, modification or removal of anything that could have a direct or indirect effect on services."),
    ("Change authority", "The person or group who authorises a change."),
    ("Configuration item (CI)", "Any component that needs to be managed in order to deliver an IT service."),
    ("Service level agreement (SLA)", "A documented agreement between a service provider and a customer identifying both the services required and the expected level of service."),
    ("Event", "Any change of state that has significance for the management of a service or other configuration item."),
    ("Four dimensions", "Organizations and people; information and technology; partners and suppliers; value streams and processes."),
    ("PESTLE", "Political, economic, social, technological, legal and environmental — the external factors that constrain an organisation."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", "21 July 2026",
     "Initial non-WSQ release (C348), mirrored from the ITIL 4 Foundation master courseware: "
     "five topics across three days, eight group labs on the BrightDesk Services scenario, and "
     "exam preparation for the included ITIL 4 Foundation exam voucher.", TRAINER),
    ("1.1", "21 July 2026",
     "Course title simplified to 'ITIL 4 Foundation Training' (voucher wording removed from "
     "the document covers; the voucher itself is unchanged).", TRAINER),
    ("13.0", VERSION_DATE,
     "Trainer deck replaced with the full 259-slide SG master deck (v12 lineage), adapted for "
     "the C348 short course: programme-only admin content and framework code references removed, "
     "cover retitled. Version aligned to the master-deck lineage across LP and LG.", TRAINER),
]
