<template>
  <v-row justify="center">
    <v-col align-self="center" class="center-block" cols="col-6" md="4">
      <v-card>
<!--        <v-toolbar color="#42b983">-->
<!--          <v-app-bar-nav-icon></v-app-bar-nav-icon>-->

<!--          <v-toolbar-title>Shipments</v-toolbar-title>-->

<!--          <v-spacer></v-spacer>-->

<!--          <v-btn icon>-->
<!--            <v-icon>mdi-magnify</v-icon>-->
<!--          </v-btn>-->
<!--        </v-toolbar>-->
        <v-list v-for="(shipment, i) in shipments" two-line>
          <v-list-item-title v-html="shipment.status"></v-list-item-title>
          <v-list-item-subtitle v-html="shipment.title"></v-list-item-subtitle>

          <!--          <v-row justify="center">-->
          <router-link :to="{ name: 'shipmentEdit', params: { id:shipment.id }}">
            <v-btn>Edit</v-btn>
          </router-link>
          |
          <router-link :to="{ name: 'shipmentDetail', params: { id:shipment.id }}">
            <v-btn>Detail</v-btn>
          </router-link>
          |
          <v-btn @click="deleteShipment(shipment)">Delete</v-btn>
          <!--            <v-divider inset=""></v-divider>-->
          <!--          </v-row>-->
          <v-divider inset></v-divider>
        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from "axios";
import {notify} from "@kyvg/vue3-notification";


export default {
  name: "Shipments",
  data() {
    return {
      shipments: [
        {'title': 'test', 'status': 'wait', 'id': '123', 'description': 'description'},
        {'title': 'test', 'status': 'ready', 'id': '123123', 'description': 'description'}
      ],
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

<style>


</style>