<template>
  <div class="shipments_container">
    <div class="shipments_content">
      <div>
        Add shipment
      </div>
      <div class="add_shipment">
        <form v-on:submit.prevent="submitForm">
          <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" id="title" v-model="title" required>
          </div>
          <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" v-model="description" required></textarea>
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
      description: ''
    }
  },
  methods: {
    async submitForm() {
      try {
        // Send a POST request to the API
        const response = await axios.post('/api/v1/shipments/', {
          title: this.title,
          description: this.description,
          completed: false
        });
        // Append the returned data to the shipments array
        // this.shipments.push(response.data);
        // Reset the title and description field values.
        this.title = '';
        this.description = '';
        console.log('Success Added') // TODO
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