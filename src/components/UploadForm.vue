<template>
    <div>
        <form @submit.prevent="uploadPhoto" id="uploadForm" method="POST" enctype="multipart/form-data">
            <div>
                <label for="description">Description</label>
                <input type= "text" id="description" name="description">
            </div>
            <div>
                <label for="photo">Photo</label>
                <input type= "file" id="photo" name="photo">
            </div>
            <button id="Submit" type="Submit" name= "Submit" >Submit</button>
        </form>
    </div>
</template>

<script>
    export default{
        data(){
            return{
            csrf_token: ''
            }
        },
        created() {
                this.getCsrfToken();
        },
        methods:{
            uploadPhoto(){
                let uploadForm = document.getElementById('uploadForm');
                let form_data = new FormData(uploadForm);
                fetch("/api/upload", {  
                    method: 'POST',
                    body: form_data,
                    headers: {
                        'X-CSRFToken': this.csrf_token
                    }
                })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (data) {
                        // display a success message
                        console.log(data);
                    })
                    .catch(function (error) {
                        console.log(error);
                });
            },
            getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
 .              then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
            }
            
        }
    }

</script>