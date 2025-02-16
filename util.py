
class HttpException(Exception):
	"""Exception raised for custom error in the application."""

	def __init__(self, message, http_error_code):
		super().__init__(message)
		self.message = message
		self.http_error_code = http_error_code

	def __str__(self):
		return self.message