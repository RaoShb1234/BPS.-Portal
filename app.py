import streamlit as st

st.set_page_config(page_title="BPS Portal - Fees Payment", page_icon="🎓")

st.markdown('<div style="background:#0a5c36;color:white;padding:20px;text-align:center;border-radius:10px"><h1>BPS PORTAL</h1><p>Fees Payment System</p></div>', unsafe_allow_html=True)

roll = st.text_input("Roll Number Likho")

if roll:
    st.success(f"Roll: {roll} - Found")
    
    # Fees Details
    st.markdown("### 💰 Fees Details")
    st.table({
        "Particular": ["Admit Card Duplicate Fee", "Enrolment Fee", "Late Fee"],
        "Amount": ["Rs. 1000", "Rs. 2500", "Rs. 500"],
    })
    st.markdown("**Total Payable: Rs. 4000**")
    
    st.markdown("---")
    st.markdown("### 💳 Payment Method Select Karo")
    
    method = st.selectbox("Payment Method", ["JazzCash", "Easypaisa", "Bank Card", "E-Pay Challan"])
    
    if method in ["JazzCash", "Easypaisa"]:
        mobile = st.text_input(f"{method} Mobile Number (03XX-XXXXXXX)")
        cnic = st.text_input("CNIC Last 6 Digits")
    
    elif method == "Bank Card":
        st.text_input("Card Number")
        col1, col2 = st.columns(2)
        col1.text_input("Expiry")
        col2.text_input("CVV")
    
    else:
        st.info("Challan No: BPS-2025-4000\nBank: NBP, HBL me jama karwao")
    
    if st.button("Pay Now - Rs. 4000", use_container_width=True):
        st.balloons()
        st.success("✅ Payment Successful!")
        st.markdown(f"""
        **Receipt:**
        - Roll No: {roll}
        - Amount Paid: Rs. 4000
        - Transaction ID: BPS{roll}2025
        - Date: 2025-11-11
        - Status: PAID
        """)
        st.button("Download Paid Admit Card", use_container_width=True)

else:
    st.info("Roll Number likho to Fees dikhegi")
