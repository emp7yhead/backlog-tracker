<template>
  <div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center space-x-4">
  <div>
    <div class="text-xl font-medium text-black">Backlog Tracker</div>
    <p class="text-slate-500">{{ msg }}</p>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
