<template>
  <div class="shipments_container">
    <div class="shipments_content">
      <div>
        Add shipment
      </div>
      <div class="add_shipment">
        <form v-on:submit.prevent="submitForm">
          <div class="form-group">
            <label for="title">Title: </label>
            <input type="text" class="form-control" id="title" v-model="title" required>
          </div>
          <div class="form-group">
            <label for="description">Description: </label>
            <textarea class="form-control" id="description" v-model="description" required></textarea>
          </div>

          <div class="form-group">
            <label for="pickup_address">Pickup address: </label>
            <textarea class="form-control" id="pickup-address" v-model="pickup_address" required></textarea>
          </div>
          <div class="form-group">
            <label for="delivery_address">Delivery address: </label>
            <textarea class="form-control" id="delivery-address" v-model="delivery_address" required></textarea>
          </div>

          <div class="form-group">
            <button type="submit">Add Shipment</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {notify} from "@kyvg/vue3-notification";

export default {
  name: "ShipmentAdd",
  data() {
    return {
      shipments: [],
      title: '',
      description: '',
      delivery_address: '',
      pickup_address: '',
    }
  },
  methods: {
    async submitForm() {
      try {
        // Send a POST request to the API
        const response = await axios.post('/api/v1/shipments/', {
          title: this.title,
          description: this.description,
          pickup_address: this.pickup_address,
          delivery_address: this.delivery_address,
        });

        notify({
          type: "success",
          title: "Shipment added !",
        });

        // Reset the title and description field values.
        this.title = '';
        this.description = '';
        this.pickup_address = '';
        this.delivery_address = '';

      } catch (error) {
        // Log the error
        notify({
          type: "error",
          title: "Problem with added, try later !",
        });
      }
    },
  }
}
</script>

<style scoped>

</style>