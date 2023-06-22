import streamlit as st
st.title("Hello Gomycode")

st.header("This is a header")
st.subheader("This is a subheader")
st.text("Hello Gomycode")
st.markdown("### This is a markdown")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
st.write('hello world')
# Press the green button in the gutter to run the script.
if st.checkbox("Show/Hide"):
	# display the text if the checkbox returns True value
	st.text("Showing the widget")
status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):
	st.success("Male")
else:
	st.success("Female")
hobby = st.selectbox("Hobbies: ",
					['Dancing', 'Reading', 'Sports'])
# print the selected hobby :

st.write("Your hobby is: ", hobby)
hobbies = st.multiselect("Hobbies: ",
						['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)
st.write("You selected", len(hobbies), 'hobbies')
st.button("Click me for no reason")
if(st.button("About")):
	st.text("Welcome To Gomycode!!!")
name = st.text_input("Enter Your name", "Type Here ...")
if(st.button('Submit')):
	result = name.title()
	st.success(result)
level = st.slider("Select the level", 1, 5)
# print the level
# format() is used to print value of a variable at a specific position
st.text('Selected: {}'.format(level))



