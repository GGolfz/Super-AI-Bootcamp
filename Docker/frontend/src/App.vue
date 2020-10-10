<template>
  <div id="app">
    Uplaod File
    <input type="text" v-modal="text" /> <br/>
    <button @click="predict()">predict</button> <br/>
    Output : {{output}}
  </div>
  
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data(){
    return{
      output: '',
      text:''
    }
  },
  methods:{
    predict(){
      axios.post('http://localhost:5000/iris',null,{data:{params:this.text}}).then(
        res=>{
          console.log(res)
          this.output = res.data;
        }
      )
    }
  }
}
</script>

<style>
</style>
