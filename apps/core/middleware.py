import logging

logger = logging.getLogger(__name__)

class GlobalExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:
            logger.critical(
                "Unhandled exception",
                exc_info=True,
                extra={
                    "path": request.path,
                    "method": request.method,
                    "user": getattr(request.user, "id", None),
                }
            )
            raise
