import urllib.request
import xml.etree.ElementTree as ET
import re

print(" Initializing PAN-INDIA OSINT Infrastructure Scanner...")

# def fetch_national_risk_news():
#     # 1. THE SNIPER QUERY: Strictly asking Google for gas, sewage, metro, and road caving
#     search_query = "sewage+pipe+leak+OR+gas+pipeline+damage+OR+metro+construction+OR+road+caved+OR+sinkhole+india+when:14d"
#     # search_query = "sewage+pipe+leak+OR+gas+pipeline+damage+OR+metro+construction+OR+road+caved+OR+sinkhole+india"
#     url = f"https://news.google.com/rss/search?q={search_query}&hl=en-IN&gl=IN&ceid=IN:en"
    
#     try:
#         req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#         response = urllib.request.urlopen(req)
#         xml_data = response.read()
#         root = ET.fromstring(xml_data)
        
#         print("\n LIVE HIGH-PRECISION INFRASTRUCTURE INTELLIGENCE:")
#         print("-" * 60)
        
#         active_risk_zones = []
        
#         # Target Cities
#         india_zones = [
#             "Chennai", "Coimbatore", "Madurai", "Trichy", "Salem", 
#             "Bengaluru", "Mumbai", "Delhi", "Hyderabad", "Pune", 
#             "Kolkata", "Ahmedabad", "Gurugram", "Noida"
#         ]
        
#         # 2. THE LASER FILTER: The headline MUST contain one of these exact phrases
#         hazard_keywords = [
#             "sewage", "gas pipe", "gas leak", "metro construction", 
#             "metro work", "sinkhole", "caved", "road damage", "crater"
#         ]
        
#         # Scan the top 20 recent articles
#         for item in root.findall('.//item')[:20]:
#             title = item.find('title').text
#             pub_date = item.find('pubDate').text
            
#             # Strict verification: Does the headline contain our exact danger words?
#             is_dangerous = any(re.search(rf"\b{hazard}\b", title, re.IGNORECASE) for hazard in hazard_keywords)
            
#             if is_dangerous:
#                 # If verified, check which city it belongs to
#                 for zone in india_zones:
#                     if re.search(rf"\b{zone}\b", title, re.IGNORECASE):
#                         print(f" PRECISION TARGET DETECTED IN: {zone}")
#                         print(f"   Headline: {title}")
#                         print(f"   Date: {pub_date}\n")
                        
#                         if zone not in active_risk_zones:
#                             active_risk_zones.append(zone)
                            
#         return active_risk_zones

#     except Exception as e:
#         print(f" Failed to fetch live data: {e}")
#         return []


# # Run the scanner
# trending_danger_zones = fetch_national_risk_news()

# print("-" * 60)
# print(f" FINAL SYSTEM OUTPUT - ACTIVE RISK ZONES: {trending_danger_zones}")



def fetch_national_risk_news():
    # 1. Upgraded Query: Now includes metro construction and is strictly limited to 14 Days (2 weeks)
    search_query = "road+collapse+OR+sinkhole+OR+pipeline+burst+OR+metro+construction+OR+excavation+in+india+when:14d"
    url = f"https://news.google.com/rss/search?q={search_query}&hl=en-IN&gl=IN&ceid=IN:en"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        
        print("\n📰 LIVE NATIONAL HAZARD & CONSTRUCTION INTELLIGENCE:")
        print("-" * 60)
        
        active_risk_zones = []
        
        # Target Cities
        india_zones = [
            "Chennai", "Coimbatore", "Madurai", "Trichy", "Salem", 
            "Bengaluru", "Mumbai", "Delhi", "Hyderabad", "Pune", 
            "Kolkata", "Ahmedabad", "Gurugram", "Noida"
        ]
        
        # 2. UPGRADED FILTER: Now allows active underground construction terms
        hazard_keywords = [
            "collapse", "sinkhole", "caved", "crater", "burst", "leak", "crack",
            "construction", "metro", "excavation", "digging", "sewage"
        ]
        
        # Scan the top 20 recent articles
        for item in root.findall('.//item')[:20]:
            title = item.find('title').text
            pub_date = item.find('pubDate').text
            
            # Check if the headline describes a hazard OR heavy construction
            is_dangerous = any(re.search(rf"\b{hazard}\b", title, re.IGNORECASE) for hazard in hazard_keywords)
            
            if is_dangerous:
                # If it's a hazard/construction, check which city it happened in
                for zone in india_zones:
                    if re.search(rf"\b{zone}\b", title, re.IGNORECASE):
                        print(f" ACTIVE RISK DETECTED IN: {zone}")
                        print(f"   Headline: {title}")
                        print(f"   Date: {pub_date}\n")
                        
                        if zone not in active_risk_zones:
                            active_risk_zones.append(zone)
                            
        return active_risk_zones
    
    except Exception as e:
        print(f" Failed to fetch live data: {e}")
        return []


# Run the scanner
trending_danger_zones = fetch_national_risk_news()

print("-" * 60)
print(f" FINAL SYSTEM OUTPUT - ACTIVE RISK ZONES: {trending_danger_zones}")
