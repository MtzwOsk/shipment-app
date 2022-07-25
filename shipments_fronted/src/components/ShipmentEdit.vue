<template>
  <div>
    <p>Edit shipment {{ $route.params.id }}</p>

    <form id="shipmentEditFrom" v-on:submit.prevent="editShipment">
      <label for="shipmentEditFrom">Shipment edit form</label>
      <div class="form-group">
        <label for="title">Title: </label>
        <input type="text" class="form-control" id="title" v-model="title" required>
      </div>
      <div class="form-group">
        <label for="description">Description: </label>
        <textarea class="form-control" id="description" v-model="description" required></textarea>
      </div>
      <div class="form-group">
        <button type="submit">Edit Shipment</button>
      </div>
    </form>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "ShipmentEdit",
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
        this.shipments = response.data;
        this.title = response.data['title'] // TODO FORM init
        this.description = response.data['description'] // TODO FORM init

      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async editShipment(shipment) {
      try {
        // Send a request to API to update the shipment
        const response = await axios.put(`/api/v1/shipments/`+ parseInt(this.$route.params.id) + '/', {
          title: this.title,
          description: this.description
        });

      } catch (error) {

        // Log any error
        console.log(error);
      }
    }
  },
  created() {
    // Fetch shipments on page load
    this.getData();
  }
}
</script>

<style scoped>

</style>