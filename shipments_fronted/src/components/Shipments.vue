<template>
  <div class="shipments_container">
    <div class="shipments_content">
      <h1>Shipments: </h1>

      <ul class="shipments_list">
        <li v-for="shipment in shipments" :key="shipment.id">
          <h2>{{ shipment.title }} : {{ shipment.id }} </h2>
          <h3>Status: {{ shipment.status }}</h3>
          <p>{{ shipment.description }}</p>
          <router-link :to="{ name: 'shipmentEdit', params: { id:shipment.id }}" tag="button">
            <Button>Edit</Button>
          </router-link>
          |
          <router-link :to="{ name: 'shipmentDetail', params: { id:shipment.id }}" tag="button">
            <Button>Details</Button>
          </router-link>
          |
          <button @click="deleteShipment(shipment)">Delete</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {notify} from "@kyvg/vue3-notification";


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
        notify({
          type: "error",
          title: "Problem with get list, try later !",
        });
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
          notify({
            type: "error",
            title: "Problem with edit, try later !",
          });
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