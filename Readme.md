# CRM System Roadmap

## Set up project

- [x] Create Django project
- [x] Configure settings
  - [x] Database, static files, media files, templates
- [x] Install apps
  - [x] Rest framework
  - [x] Auth
- [x] Set up virtual env
- [x] Initialize git repo

## Models

- [x] Company
  - [x] Name, description fields
  - [x] Category foreign key
- [x] Contact
  - [x] First name, last name
  - [x] Email, phone
  - [x] Company foreign key
- [x] Category
  - [x] Name field

## Admin interfaces

- [x] Companies admin
  - [x] List, add, edit companies
  - [x] Contact inline to add/edit contacts
- [x] Contacts admin
  - [x] List, add, edit contacts
- [x] Categories admin

## Authentication

- [x] CustomUser model
- [x] Register view
- [x] Login view
- [x] Logout view
- [x] Limit views by permissions

## Company pages

- [x] Company list view
- [ ] Company detail view
  - [ ] Summary
  - [ ] Contact table
  - [ ] Follow-ups

## Contact pages

- [ ] Contact profile page

## Follow-ups

- [ ] FollowUp model
  - [ ] Company/Contact foreign key
  - [ ] Date, notes fields
- [ ] Add follow-ups in admin and company page
- [ ] Mark follow-ups complete
- [ ] List overdue follow-ups

## Reporting

- [ ] Company report
  - [ ] Categories, names, contacts
- [ ] Contacts report
- [ ] Overdue follow-ups report

## API

- [ ] Company serializer
- [ ] Contact serializer
- [ ] FollowUp serializer
- [ ] Company, Contact, FollowUp viewsets

## Frontend

- [ ] React app
  - [ ] Components
  - [ ] Fetch data from API
  - [ ] Views for companies, contacts

## Deployment

- [ ] PostgreSQL database
- [ ] Gunicorn + Nginx
- [ ] Domain name
- [ ] HTTPS
