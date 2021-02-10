# Users Utils

def check_code(test_code_object):
  if test_code_object.activate == False:
    return 'El código no se encuentra activo'
  if test_code_object.is_expired:
    return 'El codigo ha expirado'
  return None