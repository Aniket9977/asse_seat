# asse_seat

# Train Seat Reservation System

This is a simple Train Seat Reservation System built with Python and Streamlit. It allows users to reserve seats in a train coach, where the coach has 80 seats arranged in rows of 7, with the last row containing 3 seats. The system prioritizes seat reservation in the same row whenever possible, and provides the next nearest available seats if a row cannot accommodate the requested number.

## Features

- **Seat Arrangement Visualization**: The app visually represents the seat arrangement, showing which seats are booked (`[E]`) and which are available (`[F]`).
- **Book Up to 7 Seats**: Users can reserve between 1 and 7 seats in one booking.
- **Priority Booking**: The system prioritizes booking seats in the same row when possible.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

- **Python 3.x**: You need Python 3 installed. You can download it from [Python's official website](https://www.python.org/downloads/).
- **Streamlit**: Install Streamlit using pip:
  
  ```sh
  pip install streamlit
