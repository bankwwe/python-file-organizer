# python-file-organizer
A simple Python script that automatically organizes files in a directory  
by their file extensions, helping keep folders clean and structured.
---
## Features
- Automatically sorts files into categories based on file extensions
- Supports documents, images, videos, audio files, archives, programs, and code files
- Creates destination folders automatically if they do not exist
- Logs all file movements to a text file for tracking and review
---
## Supported Categories
- **Documents**: `.pdf`, `.docx`, `.doc`, `.txt`, `.pptx`, `.xlsx`, `.csv`, `.rtf`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`, `.heic`, `.psd`
- **Videos**: `.mp4`, `.mkv`, `.mov`, `.avi`, `.wmv`
- **Audio**: `.mp3`, `.wav`, `.flac`, `.m4a`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Programs**: `.exe`, `.msi`, `.dmg`, `.pkg`, `.apk`
- **Code**: `.py`, `.js`, `.html`, `.css`, `.cpp`, `.json`
---
## How to Use
1. Make sure Python 3 is installed on your system
2. Run the script:
```bash
## EXAMPLE
Example
Before:
Downloads/
 ├── report.pdf
 ├── photo.jpg
 ├── music.mp3
 ├── program.exe
After:
Downloads/
 ├── Documents/report.pdf
 ├── Images/photo.jpg
 ├── Audio/music.mp3
 ├── Programs/program.exe
