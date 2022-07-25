<template>
  <div class="shipments_container">
    <div class="shipments_content">
      <h1>Shipments: </h1>

      <ul class="shipments_list">
        <li v-for="shipment in shipments" :key="shipment.id">
          <h2>{{ shipment.title }} : {{ shipment.id }} </h2>
          <h3>Date: {{ shipment.created_at}}</h3>
          <h3>Status: {{ shipment.status }}</h3>
          <p>{{ shipment.description }}</p>
          <router-link :to="{ name: 'shipmentEdit', params: { id:shipment.id }}">Edit</router-link>
          <button @click="deleteShipment(shipment)">Delete</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";


export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Shipment",
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
        const response = await axios.get('/api/v1/shipments/');
        // set the data returned as shipments
        this.shipments = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async deleteShipment(shipment) {

      // Confirm if one wants to delete the task
      let confirmation = confirm("Do you want to delete this shipment?");

      if (confirmation) {
        try {

          // Send a request to delete the task
          await axios.delete(`/api/v1/shipments/${shipment.id}/`);

          // Refresh the shipments
          this.getData();
        } catch (error) {

          // Log any error

          console.log(error)
        }
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