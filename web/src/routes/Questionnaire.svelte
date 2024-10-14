<script>
    import Question from "./Question.svelte";

    export let name;
    export let questions;

</script>

<div class="container mx-auto p-8 pb-0">
    <h2 class="h2">{name}</h2>
    {#each questions as question}
        <Question {question} {name} />
    {/each}
</div>

<div class="container mx-auto px-8 mt-0">
    <section>
        <button class="btn variant-filled-primary">Submit</button>
    </section>
</div>