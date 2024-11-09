#crude shortening function for long messages
def shorten(message, diff):
  end = len(message) - diff
  message = message[:end]
  return message
  
