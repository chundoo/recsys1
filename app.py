import streamlit as st

import pickle






houses = pickle.load(open("houses_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
houses_list=houses['Name'].values

st.header("House Recommender System")

import streamlit.components.v1 as components







selectvalue=st.selectbox("Select house location from dropdown", houses_list)

def recommend(house):
    index=houses[houses['Name']==house].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    
    recommend_image=[]
    recommend_name=[]
    
    for i in distance[1:6]:
        
       
        recommend_image.append(houses.iloc[i[0]].Image)
        recommend_name.append(houses.iloc[i[0]].Name)
    return recommend_image, recommend_name



if st.button("Show Recommend"):
    house_image, house_name = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        
        st.image(house_image[0])
        st.text(house_name[0])
    with col2:
        
        st.image(house_image[1])
        st.text(house_name[1])
    with col3:
       
        st.image(house_image[2])
        st.text(house_name[2])
    with col4:
        
        st.image(house_image[3])
        st.text(house_name[3])
    with col5:
       
        st.image(house_image[4])
        st.text(house_name[4])