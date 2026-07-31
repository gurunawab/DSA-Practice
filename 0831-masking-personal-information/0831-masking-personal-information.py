class Solution:
    def maskPII(self, s: str) -> str:
        
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')

            return f"{name[0]}*****{name[-1]}@{domain}"

        else:
            digits = [ch for ch in s if ch.isdigit()]
            local_number = "***-***-" + "".join(digits[-4:])

            country_code_len = len(digits) - 10
            
            if country_code_len == 0:
                return local_number
            else:
                return f"+{'*' * country_code_len}-{local_number}"    