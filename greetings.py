from core.queue_system.publisher import BasePublisher


bp = BasePublisher(
    routing_key="hello_world",
    body={
        "greeting": "Hello World!, Good Morning"
    }
)
bp.run()