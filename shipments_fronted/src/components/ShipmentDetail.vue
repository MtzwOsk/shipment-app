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
          <h4>Description: {{ shipment.description }}</h4>
          <h4>Pickup Address: {{ shipment.pickup_address }}</h4>
          <h4>Delivery Address: {{ shipment.delivery_address }}</h4>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

import axios from "axios";
import {notify} from "@kyvg/vue3-notification";


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
        this.created_at = response.data['created_at']

      } catch (error) {
        notify({
          type: "error",
          title: "Problem with get details!",
        });

      }
    },
  },
  created() {
    // Fetch shipment on page load
    this.getData();
  }
}
</script>

<style scoped>

</style>