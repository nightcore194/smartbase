<template>
    <div class="flex flex-column h-full">
        <div class="flex-grow-1 flex">
            <TableSIOM class="flex-grow-1 scroll"></TableSIOM>
            <TableVK class="flex-grow-1 scroll"></TableVK>
        </div>
        <div class="flex-grow-1">
            <UserConfigurate></UserConfigurate>
        </div>
        <div class="flex-grow-1 flex">
            <TabelPrognos class="flex-grow-1 scroll border-round-2xl"></TabelPrognos>
        </div>
    </div>
</template>

<script  lang="ts">
import { defineComponent } from 'vue'
import TableSIOM from './components/TableSIOM.vue'
import TableVK from './components/TableVK.vue'
import TabelPrognos from './components/TabelPrognos.vue'
import UserConfigurate from './components/UserConfigurate.vue'
export default defineComponent({
    components: { TableSIOM, TableVK, TabelPrognos ,UserConfigurate },
    mounted() {

    }
})
</script>

<style scoped></style>
