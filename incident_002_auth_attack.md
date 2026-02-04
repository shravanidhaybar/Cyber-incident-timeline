# Day 16 – Incident 02: Authentication Attack Analysis

## Incident overview
This incident focuses on suspicious authentication activity
indicating a possible brute-force or credential abuse attack.

## Observed indicators
- Multiple failed login attempts
- Repeated authentication failures for the same user
- Login attempts from unknown or unusual IP addresses
- Sudden successful login after many failures

## Relevant log sources
- /var/log/auth.log
- /var/log/syslog

## Commands used during investigation

### Search for failed login attempts
grep "Failed password" /var/log/auth.log

### Search for successful logins
grep "Accepted password" /var/log/auth.log

### Identify IP addresses involved
grep "ssh" /var/log/auth.log

### Review recent authentication activity
tail -n 50 /var/log/auth.log

## Timeline summary
1. Repeated failed login attempts detected
2. Authentication attempts increase in frequency
3. Possible credential success observed
4. System access potentially compromised

## Analyst assessment
The pattern suggests a brute-force or credential stuffing attack.
Further validation is required to confirm account compromise.

## Recommended response actions
- Reset affected user passwords
- Enable account lockout policies
- Enforce strong password rules
- Implement multi-factor authentication (MFA)
- Monitor for repeated login failures

## Learning outcome
Today I learned:
- How authentication attacks appear in logs
- How SOC analysts identify brute-force patterns
- How to recommend remediation steps
