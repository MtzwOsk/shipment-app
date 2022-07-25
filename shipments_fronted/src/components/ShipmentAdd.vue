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
            <label for="sender-address">Pickup address: </label>
            <textarea class="form-control" id="sender-address" v-model="sender_address" required></textarea>
          </div>
          <div class="form-group">
            <label for="receiver_address">Delivery address: </label>
            <textarea class="form-control" id="receiver_address" v-model="receiver_address" required></textarea>
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

export default {
  name: "ShipmentAdd",
  data() {
    return {
      shipments: [],
      title: '',
      description: '',
      receiver_address: '',
      sender_address: '',
    }
  },
  methods: {
    async submitForm() {
      try {
        // Send a POST request to the API
        const response = await axios.post('/api/v1/shipments/', {
          title: this.title,
          description: this.description,
          receiver_address: this.receiver_address,
          sender_address: this.receiver_address,
        });

        // Reset the title and description field values.
        this.title = '';
        this.description = '';
        this.receiver_address = '';
        this.sender_address = '';

        console.log('Success Added') // TODO alert
      } catch (error) {
        // Log the error
        console.log(error);
      }
    },
  }
}
</script>

<style scoped>

</style>