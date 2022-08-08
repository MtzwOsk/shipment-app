<template>
  <v-row>
    <v-col justify="center" class="fill-height">
      <v-card class="mx-auto" max-width="344" tonal v-for="shipment in shipments" :key="shipment.id">
        <v-toolbar color="#42b983">
          <v-icon large>mdi-email
          </v-icon>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-list-item three-line>
          <v-card-title>
            {{ shipment.title }}
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            {{ shipment.description }}
          </v-card-text>
          <v-divider></v-divider>
          <v-card-text>{{ shipment.delivery_address }}</v-card-text>
          <v-divider></v-divider>
          <v-card-text>{{ shipment.pickup_address }}</v-card-text>
          <v-divider></v-divider>
          <v-card-text>{{ shipment.status }}</v-card-text>
          <v-divider></v-divider>
        </v-list-item>

        <v-card-text>
          <v-timeline align-top dense>
            <v-timeline-item v-for="shipment in shipments">
              <div>
                <div class="font-weight-normal">
                  <v-col>
                    <strong>{{ shipment.created_at }}</strong>
                  </v-col>
                </div>
              </div>
            </v-timeline-item>
          </v-timeline>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
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
        // set the date
        response.data.created_at = new Date(response.data.created_at).toString();
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
</style>