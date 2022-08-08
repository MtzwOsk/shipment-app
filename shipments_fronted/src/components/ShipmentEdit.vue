<template>
  <div>
    <v-app-bar-title>Edit shipment: {{ $route.params.id }}</v-app-bar-title>
    <v-form id="shipmentEditFrom" v-on:submit.prevent="editShipment">
      <v-row justify="center">
        <v-col align-self="center" cols="col-6" md="4">
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
      description: '',
      pickup_address: '',
      delivery_address: '',
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
        this.title = response.data['title']
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
          title: "Shipment has been Edited !",
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
    this.getData();
  }
}
</script>

<style scoped>

</style>