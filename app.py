import streamlit as st

st.set_page_config(page_title="Expense Tracker", page_icon="💸", layout="centered")

st.title("💸 Expense Tracker")
st.caption("Add, view, and total your daily expenses")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

# --- Add Expense ---
st.subheader("Add Expense")
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    name = st.text_input("Description", placeholder="e.g. Lunch, Bus fare...", label_visibility="collapsed")
with col2:
    amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0, format="%.2f", label_visibility="collapsed")
with col3:
    if st.button("➕ Add", use_container_width=True):
        if amount <= 0:
            st.error("Please enter an amount greater than 0.")
        else:
            st.session_state.expenses.append({"name": name.strip() or "—", "amount": amount})
            st.rerun()

st.divider()

# --- KPI Cards ---
expenses = st.session_state.expenses
total = sum(e["amount"] for e in expenses)
count = len(expenses)
avg = total / count if count else 0
highest = max((e["amount"] for e in expenses), default=0)

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total", f"₹{total:,.2f}")
k2.metric("Count", count)
k3.metric("Average", f"₹{avg:,.2f}")
k4.metric("Highest", f"₹{highest:,.2f}")

st.divider()

# --- Expense List ---
st.subheader("Expenses")
if not expenses:
    st.info("No expenses yet. Add one above.")
else:
    for i, e in enumerate(expenses):
        c1, c2, c3 = st.columns([3, 1, 0.5])
        c1.write(f"**{i+1}.** {e['name']}")
        c2.write(f"₹{e['amount']:,.2f}")
        if c3.button("✕", key=f"del_{i}"):
            st.session_state.expenses.pop(i)
            st.rerun()

    st.divider()
    if st.button("🗑️ Clear All", type="secondary"):
        st.session_state.expenses = []
        st.rerun()

# --- Footer ---
st.markdown("---")
st.caption("Built by [Arham Hassan](https://github.com/Arham-15) · [View source](https://github.com/Arham-15/expense-tracker)")
