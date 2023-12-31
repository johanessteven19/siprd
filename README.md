# SIPRD
## Our Team
Product Owner: Rifqi Hilman
Scrum Master: M. Naufal Irbahanna
Devops: Danny August
Dev Team:
- Avatar Putra Pertama Azka
- Jerome Emmanuel
- Johanes Steven
- Rizki Maulana Rahmadi
- Seto Adhi Prasetyo
- Yolanda W. Sirait

## Our Project
Sistem Informasi Peer Review Karya Ilmiah is a website designed to aid in streamlining the peer review process. By providing an online platform for university lecturers, peer-reviewers, and other university staff to submit and review scientific works, our website makes it easy for anyone involved in the peer review process to get the job done.

## Requirements
- Python 3.9.5 or later
- pip
- venv

## How To Run This App Locally
1. Clone this repository

```bash
git clone git@gitlab.cs.ui.ac.id:ppl-fasilkom-ui/ppl-ki-ganjil-2021-2022/si-peer-review-dosen/siprd.git
```

2. Navigate to the directory `siprd`

3. Create a python virtual environment

```bash
python -m venv env # depending on your computer/os, it may be python3
```

4. Activate the virtual environment

```bash
source env/bin/activate # MacOS / Linux
```

5. Install the required dependencies

```bash
pip install -r requirements.txt
```

6. Run the server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```