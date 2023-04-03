<template>
    
    <ProfileForm />

 </template>
 <script>
 
 import ProfileForm from '~/components/profile/ProfileForm.vue';

 export default {
     name: "",
     middleware: 'auth',
 }
 </script>
 