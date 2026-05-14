import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ── Data ──────────────────────────────────────────────────────────────────────

prev_week = [
    # A-names (resolved 4–10 May, created >= 27 Apr)
    {'assignee': 'AbdulRauf Siddiqui', 'issue_count': 2, 'story_points_sum': 5.5,
     'issue_titles': 'UB-3605: Export Agent-wise recordings in a zip, UB-3580: Add Date filter in Accounts report export'},
    {'assignee': 'Ahmed Hussain Warwani', 'issue_count': 7, 'story_points_sum': 4.0,
     'issue_titles': 'DOPS-74: Provide S3 links of updated videos to Uzair., DOPS-73: Interview Of Ahmed Khan, DOPS-70: Optimization of burgerlab server using multi-worker setup., DOPS-69: crons to sync the insights are running every 15 minutes on burgerlab, Increase the time for all branches, DOPS-58: URL open error on SPL Downtime Shell Select On-Prem server., DOPS-55: setup TMS logger on all production wallet servers, DOPS-51: Setup tms_stage index for elastic search stage'},
    {'assignee': 'Ali Hashim', 'issue_count': 34, 'story_points_sum': 57.75,
     'issue_titles': "MR-294: Multiple bill payments, issue with saved bills, update copies, MR-292: Send QR and bank details with account receipts, MR-291: Check if backend is getting analytics for onelink (Appsflyer), MR-290: Change transaction message to utility - 3 variations, MR-289: App copy - No internet / Transaction status pending, MR-284: Change - Accounts banner copies and fix all CTA buttons, MR-283: Remove Arshiya's access, KT, transfer of responsibilities, MR-282: Remove Saddar's old page from restricted business portfolio, MR-244: Edit video scripts for onboarding stories, MR-219: Review business receipt copies, MR-183: Task management and plan, MR-182: Playstore creatives for UB, MR-181: Video scripts for onboarding stories, MR-180: Review assets for unbundl, MR-163: T&C copy for share and earn according to new design, MR-162: New creatives on FB ads, MR-161: Copies for UB for Categories, Invoices, PO, Filters, MR-151: Share and earn banner CTAs, MR-150: Share and Earn copy fixes, MR-144: Update Urdu onboarding stories, MR-137: Review Sale and Expense copy, MR-135: Align Jira for the team, MR-134: Fix onboarding stories, MR-130: S&E terms & conditions look off, MR-129: Test new build for product based PNs, MR-43: App copies for udhaar, MR-42: Push notifiaction changes and edits for share and earn, MR-41: GA Funnel for Udhaar Blog, MR-39: V1 of growth framework doc. Analyse and discuss with Fahad, MR-38: New team mate's role and udhaar's plan with Fahad - Meeting, MR-11: Push notifications for Share and earn and routing, MR-10: Copy review and fixes, MR-9: Saddar product push notifications, MR-1: ads spend & analyse FB ads weekly report"},
    {'assignee': 'Ali Iqbal', 'issue_count': 24, 'story_points_sum': 68.0,
     'issue_titles': "MR-268: Designed 4 mobile Play Store stories for Oscars (light mode)., MR-267: Updated all copies across both mobile and tablet stories., MR-266: Designed 4 mobile tablet Play Store stories for Oscars., MR-265: Designed 4 mobile Play Store stories for Oscars (dark mode)., MR-264: Spot & Win Creative, MR-262: Udhaar book reminder post with 2 supporting images, MR-261: Targeting Rupin in this creative with 2 supporting images, MR-260: Focusing on Udhaar book App (02 Udhaar book creatives for social media post 2 supporting images), MR-259: Focusing on wallet (02 Udhaar book creatives for social media post 2 supporting images), MR-208: Design 01 Saddar billboard meme, with an engaging and relatable concept optimized for social media., MR-206: Develop 02 Saddar catalog icon images, ensuring they are clean, scalable, and consistent with the design system., MR-205: Create 02 Saddar web and in-app banners, optimized for both platforms with a cohesive look and feel., MR-203: Design 02 Saddar catalog banner images, aligned with brand guidelines and visual consistency., MR-149: Unbundle Creatives for Oscar, MR-147: Saddar Product images thumbnail for videos, MR-116: Social media creatives. (2 creatives + 4 supporting images), MR-109: Saddar Product images thumbnail for videos, MR-79: Design 5 Saddar Organic Social Post Creatives, MR-65: Design Oscar Paid Ad Creatives — Restaurant Vertical (3-4 variants), MR-37: Saddar social media creative with dimensions, MR-28: Udhaar book carousel, MR-27: Saddar Product images thumbnail for videos, MR-18: Saddar App and web banner, MR-2: Unbundle 8 Ads Creatives"},
    {'assignee': 'Anwar Ahmed', 'issue_count': 7, 'story_points_sum': 32.0,
     'issue_titles': 'UB-3472: add attachments list in invoice, UB-3381: discussion with QA and backend regarding business receipt, wallet receipt revamp deisgn and apis, UB-3339: complete functionality compatibilties of all the receipt, invoice and the success screen, UB-3303: Bank details card with QR code, UB-3301: Develop Business Receipt Screen revamp, UB-3300: Develop Invoice complete UI revamp and logic, UB-3299: Develop Business Success Screens (UI & Logic)'},
    {'assignee': 'Asfand', 'issue_count': 5, 'story_points_sum': 25.0,
     'issue_titles': 'UB-3566: Smoke testing on beta, UB-3290: PO test cases verification, UB-3289: Quick sale copies verification, UB-3288: Quick sale desgin verification testing, UB-3287: Quick sale test cases verification'},
    {'assignee': 'Ashhad Ahmed', 'issue_count': 7, 'story_points_sum': 29.5,
     'issue_titles': 'UB-3661: Banner Image, CTA Text and Description update, UB-3646: Loyalty & Share-n-Earn Refund Refactor, UB-3645: Voucher Module R&D & API Integration, UB-3643: Django Form POS Reporting & Dashboard UI Assets, UB-3418: Notification Resolvers & Exclusion Logic, UB-3417: Batch Notification Engine & Payload Integration, UB-3347: Create Django Form to Allow Agent to Download User POS Data'},
    {'assignee': 'Asim Ur Rehman', 'issue_count': 4, 'story_points_sum': 37.0,
     'issue_titles': 'UB-3670: Get updated pull in my current branch and recheck all flow, UB-3480: Put Api in Add contact flow and category, UB-3345: Get Pull and update my current branch, UB-3341: Add contact and category flow in wallet listing detail page'},
    {'assignee': 'Ateeb Shaikh', 'issue_count': 10, 'story_points_sum': 25.0,
     'issue_titles': 'UB-3695: Backfill and Update recent transactions of Test Users for Recharges and Bill Payments Management Command, UB-3694: Fixes and Test after PR Review, UB-3642: Fixes all recharges and bills new V3 APIs, UB-3616: Update the Recharge Api and Management Command to also include the Pagination supported Values in API and Managment Command, UB-3615: Save Recent Consumers and Pagination in Meta Model In Bill Payment API Successful Bill Payment, UB-3614: Populate Recent Consumers and Pagination old meta thought management Command, UB-3519: Udhaar: Payment Settlement Integration, UB-3517: Wallet: Deactivate + Reuse after 99999 Logic, UB-3516: Udhaar: Khata Create/Delete Integration, UB-3515: Wallet: Virtual QR + Incoming Mapping'},
    # B–M names
    {'assignee': 'Aun Zaidi', 'issue_count': 2, 'story_points_sum': 0,
     'issue_titles': 'MR-248: Anwar maqsood AI onboarding, MR-247: Rupin app onboarding video (Shah Bhai)'},
    {'assignee': 'Ayyan Bin Fawad', 'issue_count': 13, 'story_points_sum': 39,
     'issue_titles': 'UB-3599: Design Rupin brochure for distribution in market, UB-3591: Transcribe customer conversion call recordings using eleven labs, UB-3590: Review product document for archival/recycle bin and share comments, UB-3589: Review document for accounts section redesign and share thoughts, UB-3565: Call 10 1bill users to gather feedback on why they prefer it to bank transfers, UB-3563: Listen to inbound calls and identify opportunities for application and improvement at agent level, UB-3561: Listen to customer conversion calls and identify issues faced in conversion, UB-3559: Call 10 users about feedback on how they manage stock levels(if they use stock in/stock out or manage inventory through invoices/POs), UB-3558: Call 10 users to ask what they use my accounts feature for and if they share accounts from there, UB-3557: Call 10 users on feedback about potential new features(recycle bin, dark mode, sms reminders, PNL), UB-3555: Call 10 users who saw stories but did not create Rupin account to see why they cancelled and if the feature would interest them, UB-3552: Share details on changes required/elements requested with Areeb, UB-3551: Design initial website for RUPIN using Oscar CMS elements'},
    {'assignee': 'Bilal Ali Khan', 'issue_count': 32, 'story_points_sum': 30.0,
     'issue_titles': 'MR-280: Saddar KT, MR-231: Unbundl creatives for the themes (transparency, culture, utility), MR-228: April Social media report, MR-213: RUPIN web copies, MR-170: Udhaar Book (Playstore creatives), MR-159: Shoot Udhaar Book video, MR-158: Oscar (Playstore creatives), MR-155: Social Media Posts, MR-154: Review copies given by Ammar Hashmi, MR-153: Draft "Earn on Fuel" strategy for QR payments., MR-152: Write an Employer Branding script, MR-127: Community Management, MR-126: Udhaar Book Voiceover, MR-122: March - social media performance report, MR-120: Saddar Whatsapp Messages, MR-117: Udhaar Book video voiceover, MR-115: Content Calendar (Apr 2026), MR-113: Research for outreach ideas for growth strategy, MR-112: Growth strategy ideas, MR-111: Facebook and Insta community management, MR-110: Share and earn Marketing strategies, MR-44: Analysing Google Analytics dashboard for growth strategy, MR-36: Rupin growth strategy, MR-35: Oscar Creatives, MR-34: Instagram creatives, MR-33: Shoot employer branding video, MR-32: Growth Discussion with team, MR-26: Growth strategy doc., MR-24: Commission video creative ideas, MR-13: P&L Slider - Edits, MR-8: Push Notifcations, MR-3: Unbundle Creative'},
    {'assignee': 'Bilal Shaikh', 'issue_count': 4, 'story_points_sum': 16,
     'issue_titles': 'OP-5084: CMS modifications for RUPIN, OP-5075: Accounting Review, OP-5074: Meeting for formulas, OP-5061: CMS modfification for Oscar'},
    {'assignee': 'Hamza Naveed', 'issue_count': 7, 'story_points_sum': 27,
     'issue_titles': 'SCR-221: Cash Sales Difference in Z Report & Sales Summary, SCR-220: Inventory Issue, SCR-219: Rockstar Vapor Issues, OP-5085: Moved all Dashboard Reporting to stage and fixes for some filters that occurred due to GET to POST, OP-5080: Converting All Dashboard Reports APIs from GET to POST with necessary changes required from query params to post data, OP-5078: New Report: Basket Report, OP-5012: Filter out Settings in Settings API according to subtypes'},
    {'assignee': 'Muhammad Aamir', 'issue_count': 3, 'story_points_sum': 15,
     'issue_titles': 'DOPS-71: analyze Servers Load avg and response time of APIs, DOPS-46: apply secrets manager on staging ec2 with limited permissions, DOPS-43: create guide docs and update devops repo with script and implementation'},
    {'assignee': 'Muhammad Sharjeel', 'issue_count': 4, 'story_points_sum': 0,
     'issue_titles': 'SCR-218: Foodpanda Margin Visibility for Shell, SCR-217: Shell Ev Station Complete Flow Creation, SCR-216: Zero Sales Report for Shell, SCR-215: Insight sale logs reporting on shell select'},
    {'assignee': 'Muhammad Zain', 'issue_count': 9, 'story_points_sum': 14.5,
     'issue_titles': 'UW-1481: Enable form submission on Enter key press across all Udhaar web forms, UW-1480: Integrate calculator-enabled input with full functionality in Quick Sale, Quick Expense, and Account Transactions forms, UW-1471: Tesing and bug fixing for PinCode section from Setting, UW-1457: Implement "PIN Updated Successfully" UI, UW-1456: Integrate new PIN update functionality, UW-1455: Implement Create New PIN UI, UW-1454: Integrate current PIN verification functionality, UW-1453: Display error UI for incorrect PIN, UW-1452: Implement Enter Current PIN UI'},
    {'assignee': 'maroob', 'issue_count': 6, 'story_points_sum': 48,
     'issue_titles': 'OP-5109: prepayment bill calculations discount and subtotal fixes and deploy to prod, OP-5067: Test cases Execution 251 to 473, OP-5066: Test cases Execution 1 to 250, OP-5064: R&D for receipt customization and payment method tax selection, OP-5063: Reciept and prepayment slip fixes, OP-5060: Add Payment method selection options for Restuarants order screen'},
    {'assignee': 'muhammad Ubaid', 'issue_count': 20, 'story_points_sum': 40.0,
     'issue_titles': 'OP-5059: Order Data Handling & Edge Cases Items mapping, OP-5058: Order Details API Integration Fetch single order, OP-5057: Handle Order Filters / Search, OP-5056: Order History API Integration, OP-5055: Map & Handle Credit History Data, OP-5054: Credit History API Integration Fetch payment history, OP-5053: Handle Pay Credit Flow Logic, OP-5052: Implement Pay Credit API Integration Submit credit payment, OP-5051: Error & Edge Handling for Details Screen Missing fields Partial data, OP-5050: Handle Credit Data Logic Credit balance Validation, OP-5049: Handle Loyalty Points Logic Available points Mapping & formatting, OP-5048: Customer Details API Integration Fetch single customer data, OP-5047: Handle Non-Ideal States, OP-5046: Debounce Search Optimization Prevent excessive API calls, OP-5045: Implement Filters (if API supports) Example: visits / date, OP-5044: Implement Search API Integration Search by name/phone, OP-5043: Handle Empty / No Data State No customers API failure fallback, OP-5042: State Management for Customer List Loading Success Error, OP-5041: Handle Pagination Page limit handling Load more / next page, OP-5040: Implement Customer List API Integration'},
]

curr_week = [
    # A-names (unresolved, created >= 27 Apr)
    {'assignee': 'AbdulRauf Siddiqui', 'issue_count': 5, 'story_points_sum': 53,
     'issue_titles': 'UB-3801: add CSV method for manual call logs, UB-3793: Add call classification in recordings., UB-3754: Accounts, In/Out, Sale POS, Invoice Report Fixes, UB-3753: PBX Manager Dashboard, UB-3500: AI Whatsapp chat support'},
    {'assignee': 'Ahmed Hussain Warwani', 'issue_count': 4, 'story_points_sum': 0,
     'issue_titles': 'DOPS-88: Interview of Muhammad Rehan Khan, DOPS-61: Establish site-to-site VPN connectivity for partners in the secondary region, so that external integrations remain accessible during outages., DOPS-56: research and setup roll back functionality on bitbucket pipelines., DOPS-38: Coordination with Wateen to get the CIR connection for RAAST'},
    {'assignee': 'Ali Hashim', 'issue_count': 12, 'story_points_sum': 0,
     'issue_titles': "MR-343: PNs to new wallet completed (no txn) and abandoned process, MR-342: Convert users searching Check Bill - Strategy and design changes, MR-293: Onboarding video review, MR-288: Udhara book / Rupin new listing (images), MR-287: Oscar playstore images, MR-285: Oscar videos coordination, MR-245: Share requirements for building an in-house push notification tool, MR-210: Call new wallet abandoned / successful customers for feedback, MR-145: Sort onesignal pricing and plan, MR-40: Share plan for V1 of growth plan, MAR-236: Call new wallet abandoned / successful customers for feedback, MAR-208: Playstore creatives for UB"},
    {'assignee': 'Ali Iqbal', 'issue_count': 1, 'story_points_sum': 16,
     'issue_titles': 'MR-64: Update Oscar Play Store Screenshots & Feature Graphics'},
    {'assignee': 'Anwar Ahmed', 'issue_count': 9, 'story_points_sum': 31,
     'issue_titles': 'UB-3807: wallet listing revamp new filters flow revamp, UB-3792: wallet listing revamp add contact flow, UB-3791: wallet listing revamp functionality, UB-3790: wallet listing ui revamp complete, UB-3789: wallet listing revamp discussion with backend, UB-3373: events integration for wallet and business receipt, UB-3372: test cases for wallet and business receipt entire flow, UB-3371: new icons installation for wallet and business receipt entire flow, UB-3297: Business and wallet receipt and success screen revamp and wallet listing revamp'},
    {'assignee': 'Areeb Sheikh', 'issue_count': 8, 'story_points_sum': 27,
     'issue_titles': 'MR-53: Shoot Clothing + Pharmacy Demo Videos (On-Site), MR-52: Script Pharmacy POS Demo Video (60-90 sec), MR-51: Script Clothing Store POS Demo Video (60-90 sec), MR-49: Review & QA Both Landing Page Copies Before Handoff to Dev, MR-48: Write Pharmacy Landing Page — Feature Blocks 3-4, Comparison, FAQs, CTA, MR-47: Write Pharmacy Landing Page Copy — Hero + Overview + Feature Blocks 1-2, MR-46: Write Clothing Landing Page — Testimonials, Comparison Table, FAQs, CTA, MR-45: Write Clothing Landing Page Copy — Hero + Overview + Feature Blocks'},
    {'assignee': 'Arshiya', 'issue_count': 21, 'story_points_sum': 30,
     'issue_titles': 'MR-179: Call customers for video review, MR-160: Facebook community managment, MR-139: Facebook community managment, MR-133: qoura posting, MR-132: facebook community managment, MR-131: earbuds and smartwatch catalogue creative, MR-128: saddar post ideation, MR-125: Facebook community managment, MR-124: Saddar social media creative post & website banner, MR-119: Qoura posting, MR-78: Collect Text/Video Testimonials from Repeat Customers, MR-77: Send WhatsApp Marketing Blast with Impromptu Videos, MR-76: Create Saddar Organic Social Content Plan & Post 5 Times, MR-75: Identify & Reach Out to 2-3 Influencers, MR-74: Plan Saddar marketing Strategy, MR-73: Plan & Shoot 2-3 Impromptu WhatsApp Marketing Videos, MR-72: Audit & Remove Poor-Reviewed Products, MR-71: Set Up Abandoned Cart WhatsApp Auto-Messages, MR-14: Banners ideation for Saddar, MAR-237: saddar social media 5 post, MAR-205: Plan Saddar marketing Strategy'},
    {'assignee': 'Asfand', 'issue_count': 2, 'story_points_sum': 14,
     'issue_titles': 'UB-3292: PO copies verification, UB-3291: PO desgin verification testing'},
    {'assignee': 'Ashhad Ahmed', 'issue_count': 14, 'story_points_sum': 75,
     'issue_titles': "UB-3445: Integrate Redeem Points into Voucher Purchase Flow, UB-3444: Implement Points Deduction & Calculation Logic, UB-3443: Implement Points Validation Logic for Redemption, UB-3442: Add redeem_points Flag to Buy Voucher API, UB-3441: Implement Business Logic for purpose Handling, UB-3440: Add purpose Field to Buy Voucher API, UB-3427: Voucher API'S Development Doc, UB-3349: Identify File-Based Fields in Udhaar & Wallet Microservice and Migrate Storage to S3 for DR Readiness, UB-3328: Integrate Coins Flow into Voucher Purchase API, UB-3327: Implement Coins Business Logic in Voucher System, UB-3326: Add Coins Fields & Database Schema Updates, UB-3325: Implement Popular Voucher API v2 Endpoint, UB-3324: Define Popular Voucher API v2 Contract & Schema, UB-3323: Voucher Revamp – API Enhancements and Feature Updates"},
    {'assignee': 'Asim Ur Rehman', 'issue_count': 5, 'story_points_sum': 64.5,
     'issue_titles': 'UB-3769: wallet permissions flow for accepted user, UB-3622: Update All categories logic with selected language in wallet flows, UB-3259: Remove Api from easyload customer for get total recharge and total commision, UB-3222: Update Detail pages of wallet listing, UB-3159: Update All detail pages of Business Tools (Quick sale and expense, invoice, purchase order, sale pos)'},
    {'assignee': 'Ateeb Shaikh', 'issue_count': 19, 'story_points_sum': 56,
     'issue_titles': 'UB-3634: Bills should be allowed to be paid even after due date, as long as 1link confirms that the bill can be paid., UB-3482: Limits for test users to be capped at 5k per month and 1000 per transaction., UB-3481: If a payable object is scheduled but not running, then a new payable can be created from the payables ledger action. Once new payable is created, previous payable will be marked as complete., UB-3411: Integration with Bill Payment Flow + Validation Layer, UB-3410: Consumer Number Extraction Engine (Biller-aware parser), UB-3409: QR Payload Extraction API Integration, UB-3408: Biller QR Format Discovery & Mapping Design, UB-3407: Testing, UB-3406: Refund + Reconciliation Workflow, UB-3405: Settlement Report Validation Logic, UB-3404: Admin Panel + Manual Control, UB-3403: Create the new Model to store the Rejected Transactions, UB-3401: Create dedicated URL flow for .get()-based partner API views and regression-test behavior., UB-3400: Identify views using .get() on async tasks that trigger partner API calls., UB-3399: Validate and fix late-fee refund behavior for failed bill payments., UB-3398: Audit and refactor async tasks that use Django Client/APIClient to call internal views., UB-3395: Address the Errors if any Bank Faces while Scanning the QR, UB-3394: Test the QR with Every Bank, UB-3392: Create the new QR with only the Required Tags'},
    # B–M names
    {'assignee': 'Aun Zaidi', 'issue_count': 9, 'story_points_sum': 38,
     'issue_titles': 'MR-249: Rupin onboarding video (female version), MR-246: Onboarding videos, MR-59: Create Short-Form Cuts of All 4 Videos for Social Media, MR-58: Edit Pharmacy Client Testimonial — Final Cut, MR-57: Edit Clothing Client Testimonial — Final Cut, MR-56: Generate Clothing Demo Video with Ai— Final Cut, MR-55: Edit Clothing Store Demo Video — Final Cut, MR-54: Shoot Client Testimonials — Clothing + Pharmacy Owners (On-Site), MAR-210: Onboarding videos'},
    {'assignee': 'Ayyan Bin Fawad', 'issue_count': 7, 'story_points_sum': 3,
     'issue_titles': 'UB-3739: Create plan using Claude and transcribed calls to increase growth from Saddar calls, UB-3738: Transcribe calls from Saddar agents using Notebook LLM, UB-3594: Rupin Stockbook Redesign, UB-3593: Analyze customer feedback and create Stockbook Redesign Document, UB-3588: Review upcoming features, UB-3560: Customer Conversion Management, UB-3553: Customer calls'},
    {'assignee': 'Bilal Ali Khan', 'issue_count': 15, 'story_points_sum': 0,
     'issue_titles': 'MR-341: Check Bill plan, MR-331: Social media posting, MR-330: Community management, MR-329: Instagram activity follow up, MR-328: Consumer calls, MR-327: V1 Growth document, MR-326: Share and Earn GTM, MR-227: Copies, MR-225: Call to consumers, MR-157: Calls to consumers, MR-138: Oscar Playstore screenshots., MAR-191: Shoot employer branding video, MAR-189: Calls to consumers, MAR-187: Social Media Posts, MAR-186: Udhaar Book (Playstore creatives)'},
    {'assignee': 'Bilal Shaikh', 'issue_count': 5, 'story_points_sum': 8,
     'issue_titles': 'OP-5147: Dashboard P & L, OP-5143: Aramco report testing, OP-5133: Oscar AI adjustments, OP-5086: Vendor Bills PO to Bill, OP-5070: Discussed Accounting APIs'},
    {'assignee': 'Hamza Naveed', 'issue_count': 2, 'story_points_sum': 0,
     'issue_titles': 'OP-5104: Incorrect validation message shown on partial payment in Pay Credit flow, OP-5103: Incorrect validation message displayed when entering 0 amount in Pay Credit modal'},
    {'assignee': 'maroob', 'issue_count': 7, 'story_points_sum': 16,
     'issue_titles': 'OP-5141: Categories & Items Text is Not Displayed in Sentence Case in POS Default View, OP-5115: Error handling and Filter implementation, OP-5114: update pdf export template according to API data, OP-5113: balance sheet API integration, OP-5112: P & L Api integration, OP-5071: Accounting APIs Integration & FE, OP-5069: oscar.pk Fixes'},
    {'assignee': 'Muhammad Aamir', 'issue_count': 7, 'story_points_sum': 11,
     'issue_titles': 'DOPS-87: Apply security headers to cobu all 3 domains, DOPS-86: Create pipeline for website cms prod, DOPS-84: setup cobu-api on Singapore region, DOPS-68: Custom CI/CD pipeline for just code update on all prod servers., DOPS-66: Develop a script that validates DR site health (databases, VPN connectivity, and service availability) during drills, so that we can confirm all systems are functioning correctly after failover., DOPS-59: Configure Redis dump for Udhaar core cache and wallet cache, so that cache data can be restored in case of failure., DOPS-57: Setup ubuntu server on PC for oscar'},
    {'assignee': 'Muhammad Sharjeel', 'issue_count': 2, 'story_points_sum': 0,
     'issue_titles': 'SCR-227: Burger Lab Calling service enable and disable option, SCR-224: Happy Hour Reporting on central Shell'},
    {'assignee': 'Muhammad Sheheryar Izhar', 'issue_count': 7, 'story_points_sum': 81,
     'issue_titles': "UB-3748: SMS Bundle Development PR Changes and Test, UB-3526: Setup an upload routine for refunds data processed by Recon team. This refunds data would then automatically process the pending refunds., UB-3354: Care Form Requirements, UB-3337: Wallet listing updates, UB-3336: Bill payment flow - udhaar blog, UB-3171: Optimize and Compress Application Images Before Upload to S3, OP-5139: Fixed Existing Oscar API's"},
    {'assignee': 'muhammad Ubaid', 'issue_count': 22, 'story_points_sum': 90,
     'issue_titles': 'OP-5178: Test Case and Code Merge on Stage, OP-5177: Test Case and Code Merge on Stage, OP-5175: Mobile Dashboard AI Summary / suggestion API Implementation, OP-5174: Mobile Create a Chat Matrix Tool Tips, OP-5173: Mobile Create a Ui for Ai Summary for Oscar Ai, OP-5172: Create a Dynamic Listing Component for Data Labs, OP-5171: Create a Functionality for Exports Csv, OP-5170: Implement a Recommendation API for Date Labs., OP-5169: Implement a Api for Data Labs for Table Data, OP-5168: Create a Searching Field and and Date Range Component, OP-5167: Create a Non ideal and tabs For Data Labs, OP-5166: Dashboard AI Summary / suggestion API Implementation, OP-5165: Create a Chat Matrix Tool Tips, OP-5164: Create a Ai Summary Component and Changes banner Size, OP-5163: Mobile app Oscar AI Dashboard, OP-5162: Oscar AI Data Labs Fronted, OP-5161: Oscar AI Dashboard Fronted, OP-5158: Customer and Order History Bugs Fixes, OP-5102: Customer creation date is not displayed in Summary & Detail section for newly created customers, OP-5101: Customer name and order count are not displayed on Customer Summary & Detail screen header, OP-5100: Loyalty points are calculated incorrectly for customers across orders, OP-4997: Oscar AI Chat'},
    {'assignee': 'Muhammad Zain', 'issue_count': 17, 'story_points_sum': 14.0,
     'issue_titles': 'UW-1542: Implement export invoice test cases, UW-1541: Implement send reminder test cases, UW-1540: Implement delete invoice test cases, UW-1539: Implement edit invoice test cases, UW-1538: Implement record payment test cases, UW-1537: Implement sale invoice add discount and tax test cases, UW-1536: Implement sale invoice create invoice test cases, UW-1535: Implement sale invoice non-ideal test cases, UW-1534: Remove sidebar from new business form authorized user flow, UW-1530: Implement Sale POS (Udhaar payment flow) test cases, UW-1529: Implement Sale POS (Stock list cash flow) test cases, UW-1528: Implement Sale POS (Draft sales) test cases, UW-1527: Implement Sale POS (Edit open item name) test cases, UW-1526: Implement Sale POS (Add customer, Add discount, Add tax, Open item cash flow) test cases, UW-1525: Implement Sale POS non ideal test cases, UW-1524: Implement uncategorized page main non ideal, UW-1510: Implement business overview cash flow test cases'},
]

# Sort both datasets by assignee name (case-insensitive)
prev_week.sort(key=lambda x: x['assignee'].lower())
curr_week.sort(key=lambda x: x['assignee'].lower())

# ── Styles ────────────────────────────────────────────────────────────────────

HEADER_FILL = PatternFill(fill_type='solid', fgColor='D9D9D9')
HEADER_FONT = Font(name='Calibri', bold=True, size=11)
CELL_FONT   = Font(name='Calibri', size=10)
WRAP_ALIGN  = Alignment(wrap_text=True, vertical='top')
TOP_ALIGN   = Alignment(vertical='top')
THIN_BORDER = Border(
    left=Side(style='thin', color='CCCCCC'),
    right=Side(style='thin', color='CCCCCC'),
    top=Side(style='thin', color='CCCCCC'),
    bottom=Side(style='thin', color='CCCCCC'),
)

HEADERS = ['Assignee', 'Total Issues', 'Issue Titles', 'Story Points']
COL_WIDTHS = [22, 14, 100, 14]


def write_sheet(ws, data, title):
    ws.title = title

    # Header row
    for col_idx, (header, width) in enumerate(zip(HEADERS, COL_WIDTHS), start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = TOP_ALIGN
        cell.border = THIN_BORDER
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    ws.row_dimensions[1].height = 20

    # Data rows
    for row_idx, item in enumerate(data, start=2):
        values = [
            item['assignee'],
            item['issue_count'],
            item['issue_titles'],
            item['story_points_sum'],
        ]
        for col_idx, value in enumerate(values, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = CELL_FONT
            cell.border = THIN_BORDER
            if col_idx == 3:
                cell.alignment = WRAP_ALIGN
            else:
                cell.alignment = TOP_ALIGN

        # Auto-height: estimate ~15pt per wrapped line in col C (width ~100 chars)
        title_len = len(item['issue_titles'])
        lines = max(1, -(-title_len // 100))  # ceiling division
        ws.row_dimensions[row_idx].height = max(20, lines * 15)

    # Freeze header row
    ws.freeze_panes = 'A2'


# ── Build workbook ─────────────────────────────────────────────────────────────

wb = openpyxl.Workbook()
wb.remove(wb.active)  # remove default sheet

write_sheet(wb.create_sheet(), prev_week, 'Previous Week Performance')
write_sheet(wb.create_sheet(), curr_week, 'Current Week Assignments')

output_path = '/home/user/Toko_x_Claude/weekly_jira_report.xlsx'
wb.save(output_path)
print(f'Saved: {output_path}')
