<template>
  <div class="shipments_container">
    <div class="shipments_content">
      <div class="add_shipment">
        <v-form id="shipmentEditFrom" v-on:submit.prevent="submitForm">
          <v-row justify="center">
            <v-col align-self="center" class="center-block">
              <v-text-field label="Title" v-model="title" aria-required="true">
              </v-text-field>
              <v-text-field label="Description" v-model="description" aria-required="true">
              </v-text-field>
              <v-text-field label="Pickup address" v-model="pickup_address" aria-required="true">
              </v-text-field>
              <v-text-field label="Delivery address" v-model="delivery_address" aria-required="true">
              </v-text-field>
            </v-col>
          </v-row>
          <div class="form-group">
            <v-btn color="#42b983" type="submit">Edit Shipment</v-btn>
          </div>
        </v-form>
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