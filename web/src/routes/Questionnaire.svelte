<script>
    import Question from "./Question.svelte";

    export let name;
    export let questions;

    function postBack() {
		fetch("http://localhost:8000/feedback", {
			method: 'POST',
            headers: {
				'Content-Type': 'application/json'
			},
			body: 'test'
		});
	}

</script>

<div class="container mx-auto p-8 pb-0">
    <h2 class="h2">{name}</h2>
    {#each questions as question}
        <Question {question} {name} />
    {/each}
</div>

<div class="container mx-auto px-8 mt-0">
    <section>
        <button type="button" class="btn variant-filled-primary"
         on:click={postBack}>Submit</button>
    </section>
</div>