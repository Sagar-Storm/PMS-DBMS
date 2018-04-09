def get_address_folder(instance, filename):
    return '{0}/{1}'.format(instance.ApplicationId.ApplicantId.MailId, "addressproof." + filename.split(".")[1])


def get_photo_folder(instance, filename):
    return '{0}/{1}'.format(instance.ApplicationId.ApplicantId.MailId, "passport_photo." + filename.split(".")[1])


def get_birth_certificate_folder(instance, filename):
    return '{0}/{1}'.format(instance.ApplicationId.ApplicantId.MailId, "birth_certificate." + filename.split(".")[1])

def get_payment_receipt_folder(instance, filename):
  return '{0}/{1}'.format(instance.ApplicationId.ApplicantId.MailId, "payment_receipt." + filename.split(".")[1])

def get_user_image_folder(instance, filename):
    return 0
