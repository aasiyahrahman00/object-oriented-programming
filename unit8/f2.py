from typing import List, Optional


class Room:
    def __init__(self, room_id: str, capacity: int) -> None:
        self.room_id = room_id
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Room {self.room_id} (capacity {self.capacity})"


class Booking:
    def __init__(self, room: Room, user_name: str, time_slot: str) -> None:
        self.room = room
        self.user_name = user_name
        self.time_slot = time_slot

    def __str__(self) -> str:
        return f"{self.time_slot}: {self.room.room_id} booked by {self.user_name}"


class BookingSystem:
    def __init__(self) -> None:
        self.rooms: List[Room] = []
        self.bookings: List[Booking] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def find_room(self, room_id: str) -> Optional[Room]:
        for room in self.rooms:
            if room.room_id == room_id:
                return room
        return None

    def check_slot(self, room: Room, time_slot: str) -> bool:
        for booking in self.bookings:
            if booking.room == room and booking.time_slot == time_slot:
                return False
        return True

    def book_room(self, room_id: str, user_name: str, time_slot: str) -> None:
        # Find the requested room
        room = self.find_room(room_id)

        # Check the room exists
        if room is None:
            print(f"Room {room_id} does not exist.")
            return

        # Check the room is available
        if not self.check_slot(room, time_slot):
            print(f"Room {room_id} is already booked at {time_slot}.")
            return

        # Create the booking
        booking = Booking(room, user_name, time_slot)

        # Save the booking
        self.bookings.append(booking)

        print("Booking successful:", booking)

    def show_bookings(self) -> None:
        print("\nBookings:")

        if not self.bookings:
            print("No bookings.")
            return

        for booking in self.bookings:
            print("-", booking)


if __name__ == "__main__":
    system = BookingSystem()

    system.add_room(Room("1001", 30))
    system.add_room(Room("1007", 60))

    system.book_room("1001", "Alice", "07:00 - 22:00")
    system.book_room("1007", "Emma", "09:00 - 21:00")
    system.book_room("1007", "John", "09:00 - 21:00") 

    system.show_bookings()