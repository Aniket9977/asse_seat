import streamlit as st

# Data Structure to represent the seats
seats = [False] * 80  # Initialize with 80 available seats (False means available)

# Function to display seats
def display_seats():
    seat_display = ""
    for i in range(80):
        seat_display += "[F] " if seats[i] else "[E] "
        if (i + 1) % 7 == 0 and i != 77:  # New row after every 7 seats except the last row
            seat_display += "\n"
    return seat_display

# Function to reserve seats
def reserve_seats(num_seats):
    if num_seats < 1 or num_seats > 7:
        return "You can reserve between 1 and 7 seats only."

    found = False

    # Try to find seats in a single row first
    for i in range(0, 77, 7):
        row = seats[i:i + 7]
        available_seats = row.count(False)

        if available_seats >= num_seats:
            for j in range(7):
                if num_seats == 0:
                    break
                if not seats[i + j]:
                    seats[i + j] = True
                    num_seats -= 1
            found = True
            break

    # If no single row is available, find nearby available seats
    if not found:
        reserved_seats = 0
        for i in range(len(seats)):
            if not seats[i]:
                seats[i] = True
                reserved_seats += 1
                if reserved_seats == num_seats:
                    break

    if found or reserved_seats == num_seats:
        return "Seats reserved successfully!"
    else:
        return "Not enough seats available!"

# Streamlit UI
st.title("Train Seat Reservation System")

# Display Initial Seat Arrangement
st.subheader("Current Seat Arrangement:")
st.text(display_seats())

# User Input for Number of Seats to Reserve
num_seats = st.number_input("Enter the number of seats you want to reserve (1-7):", min_value=1, max_value=7, step=1)

# Reserve Seats Button
if st.button("Reserve Seats"):
    result = reserve_seats(num_seats)
    st.success(result)
    st.subheader("Updated Seat Arrangement:")
    st.text(display_seats())
