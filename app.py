# # # app.py - Live Location Sharing App (With Consent)
# # import streamlit as st
# # import pandas as pd
# # import folium
# # from streamlit_folium import st_folium
# # import datetime
# # import os

# # # ============= CONFIGURATION =============
# # st.set_page_config(page_title="Live Location Tracker", layout="wide")
# # st.title("Live Location Sharing App")
# # st.markdown("**Sirf apni location share karein — kisi aur ki nahi!**")

# # # File to save data
# # DATA_FILE = "locations.csv"

# # # Initialize CSV file
# # if not os.path.exists(DATA_FILE):
# #     df = pd.DataFrame(columns=["Phone", "Latitude", "Longitude", "Timestamp"])
# #     df.to_csv(DATA_FILE, index=False)

# # # ============= FUNCTIONS =============
# # def save_location(phone, lat, lon):
# #     new_data = pd.DataFrame({
# #         "Phone": [phone],
# #         "Latitude": [lat],
# #         "Longitude": [lon],
# #         "Timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
# #     })
# #     new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
# #     st.success("Location saved!")

# # def get_all_locations():
# #     if os.path.exists(DATA_FILE):
# #         return pd.read_csv(DATA_FILE)
# #     return pd.DataFrame()

# # # ============= SIDEBAR - INPUT =============
# # with st.sidebar:
# #     st.header("Share Your Location")
# #     st.text("zainab lakho")
# #     phone = st.text_input("Apna Phone Number Daalein", placeholder="03001234567")
    
# #     # Use a form
# #     with st.form(key="location_form"):
# #         location_btn = st.form_submit_button("Get My Live Location", type="primary")
        
# #         if location_btn:
# #             if not phone:
# #                 st.error("Phone number daalna zaroori hai!")
# #             else:
# #                 st.write("**Allow location access in your browser...**")
# #                 # JavaScript to get location and save to sessionStorage
# #                 js = '''
# #                 <script>
# #                 function getLocation() {
# #                     if (navigator.geolocation) {
# #                         navigator.geolocation.getCurrentPosition(showPosition, showError);
# #                     } else {
# #                         document.getElementById('status').innerText = "Geolocation not supported.";
# #                     }
# #                 }
# #                 function showPosition(position) {
# #                     const lat = position.coords.latitude;
# #                     const lon = position.coords.longitude;
# #                     sessionStorage.setItem('shared_lat', lat);
# #                     sessionStorage.setItem('shared_lon', lon);
# #                     // Trigger form resubmit
# #                     const btn = document.querySelector('[kind="primary"]');
# #                     if (btn) btn.click();
# #                 }
# #                 function showError(error) {
# #                     document.getElementById('status').innerText = "Error: " + error.message;
# #                 }
# #                 getLocation();
# #                 </script>
# #                 <div id="status" style="color: red; margin-top: 10px;"></div>
# #                 '''
# #                 st.components.v1.html(js, height=120)

# # # ============= CAPTURE LOCATION FROM SESSIONSTORAGE (MAIN FIX!) =============
# # # This runs on every rerun
# # # ============= CAPTURE LOCATION FROM SESSIONSTORAGE =============
# # js_capture = """
# # <script>
# # window.addEventListener('load', () => {
# #     const lat = sessionStorage.getItem('shared_lat');
# #     const lon = sessionStorage.getItem('shared_lon');
# #     if (lat && lon) {
# #         Streamlit.setComponentValue({
# #             lat: parseFloat(lat),
# #             lon: parseFloat(lon)
# #         });
# #         sessionStorage.removeItem('shared_lat');
# #         sessionStorage.removeItem('shared_lon');
# #     }
# # });
# # </script>
# # """

# # # Render the JS — NO KEY!
# # location_data = st.components.v1.html(js_capture, height=0)

# # # Only process if we actually got data
# # if location_data and isinstance(location_data, dict):
# #     if "lat" in location_data and "lon" in location_data and phone.strip():
# #         lat = location_data["lat"]
# #         lon = location_data["lon"]
        
# #         # Optional: Avoid duplicates using session_state
# #         if st.session_state.get("last_saved_location") != (phone, lat, lon):
# #             save_location(phone, lat, lon)
# #             st.session_state.last_saved_location = (phone, lat, lon)
        
# #         st.rerun()

# # # ============= MAIN - DISPLAY MAP =============
# # st.header("Live Locations (Sabki)")

# # data = get_all_locations()

# # if not data.empty:
# #     data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
# #     data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')
# #     data = data.dropna(subset=['Latitude', 'Longitude'])

# #     # Center map
# #     center_lat = data['Latitude'].mean()
# #     center_lon = data['Longitude'].mean()
# #     m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# #     for _, row in data.iterrows():
# #         folium.Marker(
# #             [row['Latitude'], row['Longitude']],
# #             popup=f"<b>{row['Phone']}</b><br>{row['Timestamp']}",
# #             tooltip=row['Phone']
# #         ).add_to(m)

# #     st_folium(m, width=700, height=500)
# #     st.subheader("All Shared Locations")
# #     st.dataframe(data[["Phone", "Latitude", "Longitude", "Timestamp"]], use_container_width=True)
# # else:
# #     st.info("Abhi tak koi location share nahi ki gayi.")

# # # ============= FOOTER =============
# # st.markdown("---")
# # st.markdown("**Note:** Yeh app sirf un logon ki location dikhaati hai jinhone khud share ki ho. **Privacy First!**")


# # app.py — Live Location Sharing (Streamlit Cloud Compatible)
# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium
# from datetime import datetime
# import os

# st.set_page_config(page_title="Live Location Tracker", layout="wide")
# st.title("📍 Live Location Sharing App")
# st.markdown("**Apni location share karein — sirf apni! Privacy first 🔒**")

# DATA_FILE = "locations.csv"

# # Initialize CSV
# if not os.path.exists(DATA_FILE):
#     df = pd.DataFrame(columns=["Name", "Latitude", "Longitude", "Timestamp"])
#     df.to_csv(DATA_FILE, index=False)

# # ============= USER INPUT =============
# with st.sidebar:
#     st.header("Share Your Location 🌍")
#     name = st.text_input("Apna Naam Ya Phone Number", placeholder="Zain ya 03001234567")

#     if name:
#         st.info("Location allow karte hi map update hoga ⬇️")

#         from streamlit_js_eval import get_geolocation
#         loc = get_geolocation()

#         if loc:
#             lat = loc["coords"]["latitude"]
#             lon = loc["coords"]["longitude"]

#             df = pd.read_csv(DATA_FILE)
#             new_data = pd.DataFrame({
#                 "Name": [name],
#                 "Latitude": [lat],
#                 "Longitude": [lon],
#                 "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
#             })
#             df = pd.concat([df, new_data], ignore_index=True).dropna(how="all")

#             df.to_csv(DATA_FILE, index=False)
#             st.success(f"✅ Location saved for {name}!")

# # ============= DISPLAY MAP =============
# st.header("🌐 Live Map — Sab Users Ki Location")

# if os.path.exists(DATA_FILE):
#     data = pd.read_csv(DATA_FILE)
#     if not data.empty:
#         data = data.dropna(subset=["Latitude", "Longitude"])
#         data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
#         data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")

#         m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=10)
#         for _, row in data.iterrows():
#             folium.Marker(
#                 [row["Latitude"], row["Longitude"]],
#                 popup=f"<b>{row['Name']}</b><br>{row['Timestamp']}",
#                 tooltip=row["Name"]
#             ).add_to(m)

#         st_folium(m, width=700, height=500)
#         st.subheader("📋 All Shared Locations")
#         st.dataframe(data, use_container_width=True)
#     else:
#         st.info("Abhi tak koi location share nahi hui.")
# else:
#     st.info("Abhi tak koi data file nahi mili.")

# st.markdown("---")
# st.markdown("⚠️ **Note:** Yeh app sirf un users ki location dikhata hai jinhone khud share ki ho.")


# app.py — Loop-Free Version
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime
import os

st.set_page_config(page_title="Live Location Tracker", layout="wide")
st.title("📍 Live Location Sharing App")
st.markdown("**Apni location share karein — sirf apni! Privacy first 🔒**")

DATA_FILE = "locations.csv"

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Latitude", "Longitude", "Timestamp"])
    df.to_csv(DATA_FILE, index=False)

# Sidebar inputs
with st.sidebar:
    st.header("Share Your Location 🌍")
    name = st.text_input("Apna Naam Ya Phone Number", placeholder="Zain ya 03001234567")

    # Session guard — prevent re-saving
    if "location_saved" not in st.session_state:
        st.session_state.location_saved = False

    if name and not st.session_state.location_saved:
        from streamlit_js_eval import get_geolocation
        loc = get_geolocation()

        if loc:
            lat = loc["coords"]["latitude"]
            lon = loc["coords"]["longitude"]

            df = pd.read_csv(DATA_FILE)
            new_data = pd.DataFrame({
                "Name": [name],
                "Latitude": [lat],
                "Longitude": [lon],
                "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            })
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.session_state.location_saved = True
            st.success(f"✅ Location saved for {name}!")

# Map display
st.header("🌐 Live Map — Sab Users Ki Location")

if os.path.exists(DATA_FILE):
    data = pd.read_csv(DATA_FILE)
    if not data.empty:
        data = data.dropna(subset=["Latitude", "Longitude"])
        data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
        data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")

        m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=10)
        for _, row in data.iterrows():
            folium.Marker(
                [row["Latitude"], row["Longitude"]],
                popup=f"<b>{row['Name']}</b><br>{row['Timestamp']}",
                tooltip=row["Name"]
            ).add_to(m)

        st_folium(m, width=700, height=500)
        st.subheader("📋 All Shared Locations")
        st.dataframe(data, width='stretch')
    else:
        st.info("Abhi tak koi location share nahi hui.")
else:
    st.info("Abhi tak koi data file nahi mili.")

st.markdown("---")
st.markdown("⚠️ **Note:** Yeh app sirf un users ki location dikhata hai jinhone khud share ki ho.")
