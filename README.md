# Etna-Stud
Webapp aiming to provide students statistics about projects and stuff.

## Installation

### Dependencies

```bash
python3.5
virtualenv
```

## Structure
Okay, so, I'm currently more in a R&D phase, looking for some ideas.

### Cheap one
First one, the no-cost one, would be to store data in a DB such as SQLite,
in order to avoid having to request the APIs everytime we want data.

### Could-cost-a-little
Second one may be using Firebase, which would allow to only create *client*
websites, and maybe even CLI tools (I highly prefer these).
Problem is, I would have to set it up.

### Real cost
The least preferred one would be to rent a server, but I prefer to not spend
a penny on an open-source project (yet).

### Alternative
If the project is really successful, I may talk to my school and try to
have them host it there. I don't know about this one, I highly prefer
to have it totally parallel to school, but still, I thought about it.

### Conclusion
Theses structures will probably follow each other, if the project has any success.
I'll start with the free one, then each major version bump will be a change in structure.


## Objectives

- Provide a simple and easy way of having informations about students at school
- Allow student to have views that may be missing on the intranet
  + Notes per projects (only notes per students are available)
  + "Ranking"
  + Maybe have a more concise view of logging time
- Quicker to access than the intranet


This project isn't aiming to replace the intranet.
Students have to check it every day, in order to have up-to-date informations
about their scholarity.

## Ideas

> Should be mirrored in issues

- Store data in MariaDB or something like it, in order to avoid having
  to look up every promotions and users each time a user wants his grade.


