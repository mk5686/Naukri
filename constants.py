# Configuration and constants used in the script. Update values as needed.

import os

USERNAME = os.getenv("NAUKRI_USERNAME", "your_naukri_username")
PASSWORD = os.getenv("NAUKRI_PASSWORD", "your_naukri_password")
MOBILE = os.getenv("NAUKRI_MOBILE", "your_naukri_phone")
ORIGINAL_RESUME_PATH="your-resume-file-path/Resume.pdf"
MODIFIED_RESUME_PATH="modified-resume-file-path/Resume.pdf"
NAUKRI_LOGIN_URL="https://www.naukri.com/nlogin/login"
NAUKRI_PROFILE_URL="https://www.naukri.com/mnjuser/profile"