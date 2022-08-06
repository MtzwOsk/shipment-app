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
        <label for="pickup-address">Pickup address: </label>
        <textarea class="form-control" id="pickup_address" v-model="pickup_address" required></textarea>
      </div>
      <div class="form-group">
        <label for="delivery-address">Delivery address: </label>
        <textarea class="form-control" id="delivery_address" v-model="delivery_address" required></textarea>
      </div>
      <div class="form-group">
        <button type="submit">Edit Shipment</button>
      </div>
    </form>
  </div>
</template>

<script>

import axios from "axios";
import {notify} from "@kyvg/vue3-notification";


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
        this.description = response.data['description']
        this.pickup_address = response.data['pickup_address']
        this.delivery_address = response.data['delivery_address']


      } catch (error) {
        notify({
          type: "error",
          title: "Problem with get data, try later !",
        });
      }
    },
    async editShipment(shipment) {
      try {
        // Send a request to API to update the shipment
        const response = await axios.put(`/api/v1/shipments/` + parseInt(this.$route.params.id) + '/', {
          title: this.title,
          description: this.description,
          pickup_address: this.pickup_address,
          delivery_address: this.delivery_address,
        });
        notify({
          type: "success",
          title: "Shipment Edited !",
        });
      } catch (error) {
        notify({
          type: "error",
          title: "Problem with edit, try later !",
        });
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