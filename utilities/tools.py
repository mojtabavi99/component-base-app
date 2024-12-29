import os
import re
import string
import secrets


class Alerts:
    """
    All static alerts that are used in apps
    """

    # Persian Alerts
    WRONG_MOBILE_FORMAT_FA = 'شماره موبایل وارد شده اشتباه است'
    MISSING_USER_DATA_FA = 'اطلاعات کاربر یافت نشد'
    DELETE_UNDONE_FA = 'در فرآیند حذف مشکلی پیش آمده'
    DUPLICATE_MOBILE_FA = 'شماره موبایل تکراری است'
    DUPLICATE_EMAIL_FA = 'ایمیل وارد شده تکراری است'
    FAILED_TO_EXECUTE_FA = 'خطا در اعمال دستورات'
    FILE_NOT_SENT_FA = 'فایلی ارسال نشده است'
    FAILED_TO_UPLOAD_FA = 'خطا در بارگذاری فایل‌ها'
    SERVER_SIDE_ERROR_FA = 'خطایی از سمت سرور رخ داده است'
    WRONG_VERIFY_TOKEN_FA = 'کد تایید وارد شده اشتباه است'
    MISSING_REQUIRED_PARAMETER_FA = 'لطفا تمامی اطلاعات مورد نیاز را وارد کنید'
    AUTH_DENIED_FA = 'شما اجازه دسترسی به این بخش را ندارید'
    NUMERIC_DATA_IS_NEEDED_FA = 'لطفا از اعداد استفاده کنید'

    # English Alerts
    WRONG_MOBILE_FORMAT_EN = 'Your Mobile Number is Wrong'
    MISSING_USER_DATA_EN = 'User Information Not Found'
    DELETE_UNDONE_EN = 'Delete Process is Undone'
    DUPLICATE_MOBILE_EN = 'Your Mobile Number is Duplicated'
    DUPLICATE_EMAIL_EN = 'Your Email is Duplicated'
    FAILED_TO_EXECUTE_EN = 'Failed to Execute Process Successfully'
    FILE_NOT_SENT_EN = 'No File has Sent'
    FAILED_TO_UPLOAD_EN = 'Failed to Upload File'
    SERVER_SIDE_ERROR_EN = 'An Error Occurred in Server'
    WRONG_VERIFY_TOKEN_EN = 'Your Verify Code is Wrong'
    MISSING_REQUIRED_PARAMETER_EN = 'Some Required Parameters are Missing'
    AUTH_DENIED_EN = 'Your Access Denied'


class Gadgets:
    """
    Some common methods that are fit for all apps
    """

    @staticmethod
    def FileExist(path):
        """
        Checks if a file exists at the given path.

        Args:
            path (str): The file path to check.
        Returns:
            True if the file existing in its path, False otherwise.
        """
        return os.path.isfile(path)


    @staticmethod
    def RenameFile(current, new):
        """
        Change file name to new ordering name
        
        Args:
            current (str): The current file path.
            new (str): The new file path.
            
        Returns:
            dict: A dictionary containing:
                - error: Boolean indicating if the rename is failed (True if failed).
                - alert: A message describing the result.
        """
        try:
            os.rename(current, new)
            return {'error': False, 'alert': ''}
        except FileNotFoundError:
            alert = f'Error: The file "{current}" does not exist.'
        except PermissionError:
            alert = f'Error: Permission denied to rename "{current}".'
        except Exception as e:
            alert = f'Error: {e}'

        return {'error': True, 'alert': alert}


    @staticmethod
    def ConvertToEnglishDigits(text):
        """
        Converts non-English digits in a string to English digits.
        
        Args:
            text (str): The input string containing non-English digits.
            
        Returns:
            str: The string with all digits converted to English.
        """
        digit_map = {
            "۰": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4", "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9",  # Arabic digits
            "۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7", "۸": "8", "۹": "9",  # Persian digits
        }
        return ''.join(digit_map.get(char, char) for char in text)


    @staticmethod
    def ConvertToPersianDigits(text):
        """
        Converts English digits in a string to Persian digits.
        
        Args:
            text (str): The input string containing English digits.
            
        Returns:
            str: The string with all English digits converted to Persian.
        """
        # Mapping English digits (0-9) to Persian digits (۰-۹)
        digit_map = {
            "0": "۰", "1": "۱", "2": "۲", "3": "۳", "4": "۴", "5": "۵", 
            "6": "۶", "7": "۷", "8": "۸", "9": "۹"
        }
        return ''.join(digit_map.get(char, char) for char in text)
    
    
    @staticmethod
    def ValidateMobileFormat(number):
        """
        Validates the format of a mobile number.
    
        The number must:
        - Be exactly 11 digits long.
        - Start with '09'.
        
        Args:
            number (str): The mobile number to validate.
            
        Returns:
            dict: A dictionary containing:
                - error: Boolean indicating if the number is invalid (True if invalid).
                - alert: A message describing the result.
        """
        mobile = Gadgets.ConvertToEnglish(str(number))
        if mobile.isnumeric() is True:
            pattern = r'^09\d{9}$'
            if bool(re.match(pattern, mobile)):
                return {'error': True, 'alert': Alerts.WRONG_MOBILE_FORMAT_FA}
        else:
            return {'error': True, 'alert': Alerts.NUMERIC_DATA_IS_NEEDED_FA}

        return {'error': False, 'alert': ''}


    @staticmethod
    def GenerateMobileToken(length=5):
        """
        Generates a random token for mobile verification.
        
        Args:
            length (int): The length of the token to generate (default is 5).
            
        Returns:
            str: The generated token as a string.
        """
        token = ''.join(secrets.choice(string.digits) for i in range(length))
        return '12345'


    @staticmethod
    def GenerateEmailToken(length=32):
        """
        Return a random string for email verify
        """
        token = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))
        return token


    # @staticmethod
    # def SetToClock(sec):
    #     """
    #     Converts seconds to H:M:S time format
    #     """
    #     hours = int(sec / 3600)
    #     minutes = int(sec % 3600 / 60)
    #     seconds = int(sec - minutes * 60)

    #     if hours < 10:
    #         hours = '0' + str(hours)
    #     if minutes < 10:
    #         minutes = '0' + str(minutes)
    #     if seconds < 10:
    #         seconds = '0' + str(seconds)

    #     return hours + ':' + minutes + ':' + seconds

    # @staticmethod
    # def PersianDateToTimestamp():
    #     """
    #     Converts Persian Date to timestamp format
    #     """
    #     pass

    # @staticmethod
    # def GregorianDateToTimestamp():
    #     """
    #     Converts Gregorian Date to timestamp format
    #     """
    #     pass

    # @staticmethod
    # def datetimeToTimestamp(time):
    #     """
    #     Converts Datetime format to timestamp format
    #     """
    #     pass
