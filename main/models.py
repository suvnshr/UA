from django.db import models
import idna

# Create your models here.


class Person(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_email(self):

         # spliting the email into parts
        email_parts = self.email.split("@")

        # decoding the email parts
        decoded_parts = tuple(
            map(
                idna.decode, email_parts
            )
        )

        # Joining the decoded email parts with "@" as the glue
        decoded_email = "@".join(decoded_parts)

        return decoded_email

    @staticmethod
    def is_valid_email(email):

        parts = email.split("@")

        if len(parts) == 2 and all(parts):

            second_part = parts[1]
            pieces = second_part.split(".")

            if len(pieces) >= 2 and all(pieces):
                return True

    def save(self, *args, **kwargs):

        email = self.email

        if Person.is_valid_email(email):

            # spliting the email into parts
            email_parts = email.split("@")

            # encoding the email parts
            encoded_parts = tuple(
                map(
                    # `bytes_object.decode("utf-8")` is used to convert
                    # bytes object to string object

                    lambda string: idna.encode(string).decode("utf-8"),
                    email_parts
                )
            )

            # Joining the encoded email parts with "@" as the glue
            encoded_email = "@".join(encoded_parts)

            # replacing the old email(not encoded)
            # with new email(encoded)
            self.email = encoded_email

            # saving
            return super().save(*args, **kwargs)

        # Raising error as the email is not valid
        raise ValueError("Invalid e-mail provided")
