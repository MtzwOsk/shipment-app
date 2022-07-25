<template>
  <div class="shipments_container">
    <div class="shipments_content">
      <h1>Shipments: </h1>

      <ul class="shipments_list">
        <li v-for="shipment in shipments" :key="shipment.id">
          <h2>Title: {{ shipment.title }} </h2>
          <h2>ID: {{ shipment.id }} </h2>
          <h3>Date: {{ shipment.created_at }}</h3>
          <h3>Status: {{ shipment.status }}</h3>
          <p>{{ shipment.description }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "ShipmentDetail",
  data() {
    return {
      shipments: [],
      title: '',
      description: ''
    }
  },
  methods: {
    async getData() {
      try {
        // fetch shipments
        const response = await axios.get(
            '/api/v1/shipments/' + parseInt(this.$route.params.id) + '/'
        )
        // set the data returned as shipments
        this.shipments = [response.data];
        this.title = response.data['title'] // TODO FORM init
        this.description = response.data['description'] // TODO FORM init
        this.created_at = response.date.get('created_at')

      } catch (error) { // TODO handle err
        // log the error
        console.log(error);
      }
    },
  },
  created() {
    // Fetch shipments on page load
    this.getData();
  }
}
</script>

<style scoped>

</style>