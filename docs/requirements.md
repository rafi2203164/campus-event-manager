# Campus Event Manager: Requirements

## 1. Overview

Campus Event Manager is a web application where students can find and book tickets for campus events (seminars, workshops, cultural programs, sports days). Organizers create and manage their events, and an admin approves events and sees reports. All data is stored in a database so it stays after the app is closed.

**Users (roles):** Student, Organizer, Admin.

## 2. Modules

| No. | Module | What it does |
|-----|--------|--------------|
| M1 | User and Login | Register, login, logout, role-based access |
| M2 | Event Management | Create, edit, cancel, approve and search events |
| M3 | Booking and Tickets | Book and cancel tickets, track seats, ticket types |
| M4 | Payment | Pay for a booking, discounts, refunds |
| M5 | Notifications | Tell users about bookings and event changes |
| M6 | Reports | Bookings per event and total revenue for the admin |

## 3. Functional Requirements

| ID | Requirement |
|----|-------------|
| FR1 | A user can register with name, email and password. The email must be unique. |
| FR2 | A user can log in and log out. Each role sees only its own pages. |
| FR3 | An organizer can create an event with title, category, date, venue, seat limit and ticket price. |
| FR4 | An organizer can edit or cancel their own event. |
| FR5 | An admin can approve or reject a new event. Only approved events are visible to students. |
| FR6 | A student can list events and search by title, category or date. |
| FR7 | A student can book a ticket for an approved event if seats are available. |
| FR8 | The system supports ticket types: Free, Standard and VIP. |
| FR9 | The system applies a discount rule at booking (for example early-bird or student discount). |
| FR10 | A student pays for a booking through a payment gateway. The booking is confirmed only after payment succeeds. |
| FR11 | A student can cancel a booking before the event. The seat is returned and a refund is recorded. |
| FR12 | The system sends a notification when a booking is confirmed, or when an event is changed or cancelled. |
| FR13 | An admin can view the number of bookings and the revenue of each event. |

## 4. Non-Functional Requirements

| ID | Requirement |
|----|-------------|
| NFR1 | **Security:** passwords are stored as hashes, and pages are protected by role. |
| NFR2 | **Reliability:** the system never books more seats than the seat limit. |
| NFR3 | **Performance:** normal pages load in under 2 seconds. |
| NFR4 | **Usability:** a student can book a ticket in no more than 4 clicks from the event list. |
| NFR5 | **Maintainability and extensibility:** a new ticket type, discount rule or notification channel can be added without changing the existing code. |
| NFR6 | **Testability:** business logic is covered by automated tests (target: at least 80% coverage of the service layer). |
| NFR7 | **Portability:** the app runs on Windows and Linux with Python 3. |

## 5. User Stories

| ID | User story | Acceptance criteria |
|----|-----------|---------------------|
| US1 | As a student, I want to register, so that I can book events. | Duplicate email is rejected. Password is saved as a hash. |
| US2 | As a user, I want to log in and out, so that my account is safe. | Wrong password shows an error. Pages of other roles are blocked. |
| US3 | As a student, I want to search events, so that I can find what I like. | Search by title, category and date returns matching approved events only. |
| US4 | As a student, I want to see event details, so that I can decide to book. | Date, venue, price and seats left are shown. |
| US5 | As a student, I want to book a ticket, so that I have a seat. | Seats left go down by one. A full event cannot be booked. |
| US6 | As a student, I want to choose a ticket type, so that I can pick what suits me. | Free, Standard and VIP have different prices. |
| US7 | As a student, I want discounts applied automatically, so that I pay less when I qualify. | Early-bird or student discount reduces the final price. |
| US8 | As a student, I want to pay online, so that my booking is confirmed. | Booking is confirmed only after successful payment. Failed payment keeps the seat free. |
| US9 | As a student, I want to cancel a booking, so that I can get my money back. | Seat is returned. Refund is recorded. Past events cannot be cancelled. |
| US10 | As an organizer, I want to create and edit events, so that students can join. | New event waits for approval. Only the owner can edit. |
| US11 | As an admin, I want to approve events, so that only proper events are shown. | Approved events appear for students. Rejected ones do not. |
| US12 | As a user, I want notifications, so that I know about my bookings and changes. | A message is sent on booking confirmation and on event change or cancellation. |
| US13 | As an admin, I want reports, so that I can see how events perform. | Bookings and revenue per event are shown. |

## 6. Prototype (Text Mock-ups)

**Event list (student)**
```
+--------------------------------------------------+
| Campus Event Manager        [Login] [Register]   |
+--------------------------------------------------+
| Search: [__________]  Category: [All v]  [Search]|
|                                                  |
| +----------------------+ +----------------------+|
| | Tech Seminar         | | Cultural Night       ||
| | 12 Dec | Auditorium  | | 15 Dec | Main Field  ||
| | Seats left: 40       | | Seats left: 5        ||
| | [View details]       | | [View details]       ||
| +----------------------+ +----------------------+|
+--------------------------------------------------+
```

**Event details and booking (student)**
```
+--------------------------------------------------+
| Tech Seminar                                     |
| Date: 12 Dec   Venue: Auditorium                 |
| Seats left: 40                                   |
|                                                  |
| Ticket type: ( ) Free  (o) Standard  ( ) VIP     |
| Price: 200      Discount: -20 (early bird)       |
| Total: 180                                       |
|                                                  |
| [Book and Pay]                                   |
+--------------------------------------------------+
```

**Create event (organizer)**
```
+--------------------------------------------------+
| Create Event                                     |
| Title:    [______________________]               |
| Category: [Seminar v]   Date: [__/__/____]       |
| Venue:    [______________________]               |
| Seats:    [____]        Price: [____]            |
| [Submit for approval]                            |
+--------------------------------------------------+
```

## 7. Process Model: Agile (Scrum-style, one-week iterations)

I chose Agile with short one-week iterations and a task board.

- **Requirements will grow while building.** Ideas such as new discount rules come up only after the first version works. Agile accepts this, while Waterfall would need everything fixed in advance.
- **Working software every week.** Each iteration ends with one module or feature that runs and passes its tests. This fits test-driven development and continuous integration, because tests run on every change.
- **Fits a one-person project.** Only the useful parts of Scrum are kept: a backlog (the user stories above), a weekly goal, and a short review at the end of each week, which is written in the learning log.

**Rejected alternative: Waterfall.** All requirements, design and code would have to be finished one after the other before any testing. A mistake found late would be expensive to fix, and there would be nothing to demo until the end.
