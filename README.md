# piring
- WHAT
- rpi detects ring sound (or any other noise from LineIn) from USB sound card connected to rpi (zero in my case)

- when ring detects sounds -> sends UDP multicast to the network address 239.0.0.0
-- used UDP packet, as it's simple and fast solution

- WHY
We don't hear ring sound in far corners of our house / when we are outside. IOS/Android application provided with ring itself is slow as a hell (even though system cost was 800eur). We need to be notified immediately when someone is in the front door.


- TBD - integration into HomeAssistant