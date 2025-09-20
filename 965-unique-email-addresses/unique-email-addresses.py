class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st= set()
        for email in emails:
            emailpart1,emailpart2= email.split("@")
            emailpart1= emailpart1.split("+")[0]
            emailpart1= emailpart1.replace(".","")
            st.add(emailpart1+"@"+emailpart2)
        return len(st)