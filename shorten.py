def shorten(message, diff):
  end = len(message) - diff
  message = message[:end]
  return message
  