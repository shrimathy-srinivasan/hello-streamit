!pip install streamlit

import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title('Find the Largest Number')

    a = st.number_input('Enter first number:')
    b = st.number_input('Enter second number:')
    c = st.number_input('Enter third number:')

    if st.button('Find Largest'):
        largest_number = find_largest_number(a, b, c)
        st.success(f'The largest number is: {largest_number}')

if __name__ == '__main__':
    main()
