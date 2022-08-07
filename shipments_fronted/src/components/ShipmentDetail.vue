<template>
  <div class="shipments_container columns is-multiline">
    <h1>Shipments: </h1>
    <div v-for="shipment in shipments" :key="shipment.id" class="shipment-item">
      <h2>Title: {{ shipment.title }} </h2>
      <h2>ID: {{ shipment.id }} </h2>
      <h3>Date: {{ shipment.created_at }}</h3>
      <h3>Status: {{ shipment.status }}</h3>
      <h4>Description: {{ shipment.description }}</h4>
      <h4>Pickup Address: {{ shipment.pickup_address }}</h4>
      <h4>Delivery Address: {{ shipment.delivery_address }}</h4>
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
    }
  },
  methods: {
    async getData() {
      try {
        // fetch shipment
        const response = await axios.get(
            '/api/v1/shipments/' + parseInt(this.$route.params.id) + '/'
        )
        // set the data returned as shipments
        this.shipments = [response.data];
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

<style>
.shipment-item {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  padding: var(--size-base);
  border-bottom: 1px solid var(--color-main);
}
</style>