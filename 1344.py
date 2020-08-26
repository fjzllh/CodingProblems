# M 
# Given two numbers, hour and minutes. 
# Return the smaller angle (in degrees) formed between the hour and the minute hand.


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        H = (hour%12) +minutes/60
        
        hour_angle = H*5*6
        
        minutes_angle = minutes * 6
        
        t = abs(hour_angle - minutes_angle)
        
        return min(t, 360-t)
        
        
        
        
        
