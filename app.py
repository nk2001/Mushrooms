import streamlit as st
#from PIL import Image
import numpy as np
#from tensorflow.keras.models import load_model
import joblib


st.title('Mushroom Identification App')
st.header("Edible or Poisonous")
st.subheader("This App would identify if the mushroom os edible or not")
st.text("Dataset used from UCI repository: https://archive.ics.uci.edu/ml/datasets/Mushroom")


#image = Image.open('istockphoto.jpg')
#st.image(image, use_column_width=True)
st.subheader('Please fill in the details below and click on the button below!')


CapShape = st.selectbox('Cap-Shape', ('bell','conical','convex','flat','knobbed','sunken'))
capsurface=             st.selectbox("Cap-surface", (' fibrous','grooves','scaly','smooth'))
capcolor=              st.selectbox( "Cap-color", ('brown','buff','cinnamon','gray','green','pink','purple','red','white','yellow'))
bruises=                st.selectbox("Bruises", ('yes', 'no'))
odor=                   st.selectbox( "Odor", ('almond','anise','creosote','fishy','foul','musty','none','pungent','spicy'))
gillattachment=          st.selectbox('Gill-attachment', ('attached', 'free'))

gillspacing=            st.selectbox('Gill-spacing', ('close', 'crowded'))
gillsize=               st.selectbox('Gill-size', ('broad','narrow'))
gillcolor=              st.selectbox('Gill-color', ('black',
 'brown',
 'buff',
 'chocolate',
 'gray',
 'green',
 'orange',
 'pink',
 'purple',
 'red',
 'white',
 'yellow'))
stalkshape=              st.selectbox('Stalk-shape', ('enlarging', 'tapering'))
stalkroot=               st.selectbox('Stack-root', ('missing', 'bulbous', 'club', 'equal', 'rooted', ))
stalksurfaceabovering= st.selectbox('Stalk-surface-above-ring', ('fibrous', 'scaly', 'silky', 'smooth'))
stalksurfacebelowring= st.selectbox('Stalk-surface-below-ring', ('fibrous', 'scaly', 'silky', 'smooth'))
stalkcolorabovering=   st.selectbox('Stack-color-above-ring', ('brown',
	'buff',
	'cinnamon',
	'gray',
	'orange',
	'pink',
	'red',
	'white',
	'yellow'))
stalkcolorbelowring=   st.selectbox('Stalk-color-below-ring', ('brown',
 'buff',
 'cinnamon',
 'gray',
 'orange',
 'pink',
 'red',
 'white',
 'yellow'))
veilcolor=               st.selectbox('Veil-color', ('brown', 'orange', 'white', 'yellow'))
ringnumber=              st.selectbox('Ring-number', ('none', 'one', 'two'))
ringtype=               st.selectbox('Ring-type', (
 'evanescent',
 'flaring',
 'large',
 'none',
 'pendant'))
sporeprintcolor= st.selectbox('Spore-print-color',('black',
 'brown',
 'buff',
 'chocolate',
 'green',
 'orange',
 'purple',
 'white',
 'yellow'))
population=               st.selectbox('Population', ('abundant', 'clustered', 'numerous', 'scattered', 'several', 'solitary'))
habitat=                 st.selectbox('Habitat', ('grasses', 'leaves', 'meadows', 'paths', 'urban', 'waste', 'woods'))



#Set up a dictionary to index and get the value selected

CapShapeD = {'bell':0,'conical':1,'convex':2,'flat':3,'knobbed':4,'sunken':5}
capsurfaceD=             {' fibrous':0,'grooves':1,'scaly':2,'smooth':3}
capcolorD=              {'brown':0,'buff':1,'cinnamon':2,'gray':3,'green':4,'pink':5,'purple':6,'red':7,'white':8,'yellow':9}
bruisesD=                {'yes':0, 'no':1}
odorD=                   {'almond':0,'anise':1,'creosote':2,'fishy':3,'foul':4,'musty':5,'none':6,'pungent':7,'spicy':8}
gillattachmentD=          {'attached':0,  'free':1}

gillspacingD=            {'close':0, 'crowded':1}
gillsizeD=               {'broad':0,'narrow':1}
gillcolorD=              {'black':0,
 'brown':1,
 'buff':2,
 'chocolate':3,
 'gray':4,
 'green':5,
 'orange':6,
 'pink':7,
 'purple':8,
 'red':9,
 'white':10,
 'yellow':11}
stalkshapeD=              {'enlarging':0, 'tapering':1}
stalkrootD=               {'missing':0, 'bulbous':1, 'club':2, 'equal':3, 'rooted':4}
stalksurfaceaboveringD= {'fibrous':0, 'scaly':1, 'silky':2, 'smooth':3}
stalksurfacebelowringD= {'fibrous':0, 'scaly':1, 'silky':2, 'smooth':3}
stalkcoloraboveringD=   {'brown':0,
	'buff':1,
	'cinnamon':2,
	'gray':3,
	'orange':4,
	'pink':5,
	'red':6,
	'white':7,
	'yellow':8}
stalkcolorbelowringD=   {'brown':0,
	'buff':1,
	'cinnamon':2,
	'gray':3,
	'orange':4,
	'pink':5,
	'red':6,
	'white':7,
	'yellow':8}
veilcolorD=               {'brown':0, 'orange':1, 'white':2, 'yellow':3}
ringnumberD=              {'none':0, 'one':1, 'two':2}
ringtypeD=               {
 'evanescent':0,
 'flaring':1,
 'large':2,
 'none':3,
 'pendant':4}
sporeprintcolorD= {'black':0,
 'brown':1,
 'buff':2,
 'chocolate':3,
 'green':4,
 'orange':5,
 'purple':6,
 'white':7,
 'yellow':8}
populationD=               {'abundant':0,'clustered':1, 'numerous':2, 'scattered':3, 'several':4, 'solitary':5}
habitatD=                 {'grasses':0, 'leaves':1, 'meadows':2, 'paths':3, 'urban':4, 'waste':5, 'woods':6}



input_array = []
							  
CapShape_arr = [0] * 6
CapShape_arr[CapShapeD[CapShape]] = 1

capsurface_arr = [0] * 4 
capsurface_arr[capsurfaceD[capsurface]] = 1

capcolor_arr = [0] * 10  
capcolor_arr[capcolorD[capcolor]] = 1

bruises_arr = [0] * 2 
bruises_arr[bruisesD[bruises]] = 1

odor_arr = [0] * 9
odor_arr[odorD[odor]] = 1

gillattachment_arr =  [0] * 2 
gillattachment_arr[gillattachmentD[gillattachment]] = 1

gillspacing_arr =   [0] * 2 
gillspacing_arr[gillspacingD[gillspacing]] = 1

gillsize_arr = [0] * 2 
gillsize_arr[gillsizeD[gillsize]] = 1

gillcolor_arr = [0] * 12 
gillcolor_arr[gillcolorD[gillcolor]] = 1

stalkshape_arr = [0] * 2 
stalkshape_arr[stalkshapeD[stalkshape]] = 1

stalkroot_arr =  [0] * 5
stalkroot_arr[stalkrootD[stalkroot]] = 1

stalksurfaceabovering_arr =  [0] * 4 
stalksurfaceabovering_arr[stalksurfaceaboveringD[stalksurfaceabovering]] = 1

stalksurfacebelowring_arr = [0] * 4
stalksurfacebelowring_arr[stalksurfacebelowringD[stalksurfacebelowring]] = 1

stalkcolorabovering_arr = [0] * 9  
stalkcolorabovering_arr[stalkcoloraboveringD[stalkcolorabovering]] = 1

stalkcolorbelowring_arr = [0] * 9 
stalkcolorbelowring_arr[stalkcolorbelowringD[stalkcolorbelowring]] = 1

veilcolor_arr =  [0] * 4 
veilcolor_arr[veilcolorD[veilcolor]] = 1

ringnumber_arr = [0] * 3 
ringnumber_arr[ringnumberD[ringnumber]] = 1

ringtype_arr = [0] * 5 
ringtype_arr[ringtypeD[ringtype]] = 1

sporeprintcolor_arr = [0] * 9 
sporeprintcolor_arr[sporeprintcolorD[sporeprintcolor]] = 1

population_arr =  [0] * 6
population_arr[populationD[population]] = 1  
         
habitat_arr =  [0] * 7
habitat_arr[habitatD[habitat]] = 1              

input_array.extend(CapShape_arr +capsurface_arr +capcolor_arr +bruises_arr +odor_arr +gillattachment_arr +gillspacing_arr +gillsize_arr +gillcolor_arr +stalkshape_arr +stalkroot_arr+
stalksurfaceabovering_arr +stalksurfacebelowring_arr +stalkcolorabovering_arr +stalkcolorbelowring_arr +veilcolor_arr +ringnumber_arr +ringtype_arr +sporeprintcolor_arr+
population_arr +habitat_arr)
new_mushroom = np.array(input_array)
								  
#load the model built earlier								  
#model=load_model("mushroom_model.h5")
model = joblib.load("mushroom_model_LR.pkl")							 

if (st.button('Check if Edible or Poisonous')):
	result = model.predict(np.array(new_mushroom).reshape(1,-1))
	if (result[0] == 1):
		st.subheader("This mushroom is POISONOUS")
	else:
		st.subheader("This mushroom is EDIBLE")
