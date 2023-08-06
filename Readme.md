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
- [x] Company detail view
  - [x] Summary
  - [x] Contact table
  - [x] Follow-ups

## Contact pages

- [x] Contact profile page

## Follow-ups

- [x] FollowUp model
  - [x] Company/Contact foreign key
  - [x] Date, notes fields
- [x] Add follow-ups in admin and company page
- [x] Mark follow-ups complete
- [x] List overdue follow-ups

## Reporting

- [x] Company report
  - [x] Categories, names, contacts
- [x] Contacts report
- [x] Overdue follow-ups report

## Templates

- [x] Base template
- [ ] Homepage
- [ ] Company list
- [ ] Company detail
- [ ] Contact detail
- [ ] Registration
- [ ] Login

## Views

- [ ] Home view
- [ ] Company list view
- [ ] Company detail view
- [ ] Contact detail view
- [ ] Registration view
- [ ] Login view

## URLs

- [ ] Home
- [ ] Companies
- [ ] Company detail
- [ ] Contacts
- [ ] Login
- [ ] Logout
- [ ] Register

## API

- [x] Company serializer
- [x] Contact serializer
- [x] FollowUp serializer
- [x] Company, Contact, FollowUp viewsets

## Deployment

- [ ] PostgreSQL database
- [ ] Gunicorn + Nginx
- [ ] Domain name
- [ ] HTTPS
