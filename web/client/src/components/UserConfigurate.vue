<template>
    <div class="flex  align-items-center justify-content-center h-full controls mt-1 mb-3">
        <div>
            <div class="flex align-items-center justify-content-center h-full controls mt-1 mb-2">
                <Button class='mr-2 w-15rem' label="Расчитать" severity="success" />
                <Dropdown v-model="select1" :options="cities" optionLabel="name" placeholder="№ Сиом"
                    class="w-full md:w-14rem" />
                <Dropdown v-model="select2" :options="cities" optionLabel="name" placeholder="№ ВК"
                    class="w-full md:w-14rem" />
                <InputText v-model="inputText" :disabled="true"></InputText>

                {{ dataStore.rows.length }}
            </div>
            <div>
                <Button class="w-15rem" label="Использовать" severity="success"/>
            </div>
        </div>
    </div>

</template>
  
<script  lang="ts">
import { useDataStore } from '@/stores/data';
import { mapState, mapStores } from 'pinia';
import { defineComponent } from 'vue'

export default defineComponent({
    computed: {
        ...mapStores(useDataStore)
    },
    setup() {
        return {
            cities: [
                { name: 'New York', code: 'NY' },
                { name: 'Rome', code: 'RM' },
                { name: 'London', code: 'LDN' },
                { name: 'Istanbul', code: 'IST' },
                { name: 'Paris', code: 'PRS' }
            ],

        }
    },
    data() {
        return {
            select1: null,
            select2: null,
            inputText: 'Класс ЭЧ'
        }
    },
    mounted() {
        this.dataStore.getData();
    }
})
</script>
  
<style scoped>
.controls *+* {
    margin-right: 0.5rem
}
</style>
  