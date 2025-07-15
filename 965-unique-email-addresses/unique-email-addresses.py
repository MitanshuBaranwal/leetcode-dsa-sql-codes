class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            mailid, domain=  emails[i].split("@")
            if "." in  mailid:
                mailid =  mailid.replace(".","")
            if "+" in mailid:
                mailid= mailid.split("+")[0]
            finalmail = mailid+"@"+domain
            emails[i] = finalmail
        return len(set(emails))