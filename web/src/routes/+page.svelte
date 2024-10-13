<script lang="ts">
    import Questionnaire from "./Questionnaire.svelte";

	/** @type {import('./$types').PageData} */
	export let data;
</script>

{#each data.names as child}
    <Questionnaire name={child} questions={data.questions} />
{/each}

<div class="container mx-auto px-8 mt-0">
    <section>
        <!-- <a class="btn variant-filled-primary" on:click={submit}>Vote</a> -->
    </section>
</div>