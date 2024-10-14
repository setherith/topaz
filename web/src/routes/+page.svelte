<script lang="ts">
    import Questionnaire from "./Questionnaire.svelte";

    /** @type {import('./$types').PageData} */
    export let data;

    async function getChildNames() {
        const url = "http://localhost:8000/children";
        try {
            const response = await fetch(url);
            if (!response.ok)
                throw new Error(`Response status: ${response.status}`);
            return await response.json();
        } catch (error: any) {
            console.error(error.message);
        }
    }
</script>

{#await getChildNames()}
    <div class="container mx-auto p-8 pb-0">
        <h2 class="h2 content-center">Loading children...</h2>
    </div>
{:then child_names} 
    {#each child_names as child}
        <form method="post">
            <Questionnaire name={child} questions={data.questions} />
        </form>
    {/each}
{/await}