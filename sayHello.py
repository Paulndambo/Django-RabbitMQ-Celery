from core.queue_system.publisher import BasePublisher

bp = BasePublisher(
    routing_key="print_students_list",
    body=[
        {
            "name": "Paul Ndambo",
            "course": "Information Technology",
            "specialty": "Sofware Development"
        },
        {
            "name": "John Doe",
            "course": "Computer Science",
            "speciaty": "Blockchain Development"
        }
    ]
)

bp.run()