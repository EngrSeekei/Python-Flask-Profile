def find_seat(seating_chart, preference):
    for seat, availability in seating_chart:
        if availability == "Available" and (preference == "Any" or preference.lower() in seat.lower()):
            return seat
    return "Not Available"

def reserve_seat(seating_chart, seat_number):
    updated_seating_chart = [(seat, "Reserved" if seat == seat_number else availability) for seat, availability in seating_chart]
    return updated_seating_chart

# Sample Call:
seating_chart = [("1A", "Available"), ("1B", "Reserved"), ("2A", "Available")]

# Find a preferred seat
preferred_seat = find_seat(seating_chart, "1A")
print(preferred_seat)

# Reserve the preferred seat
seating_chart = reserve_seat(seating_chart, preferred_seat)
print(seating_chart)
