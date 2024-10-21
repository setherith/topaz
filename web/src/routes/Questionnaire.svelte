<script lang="ts">
    import { group } from "console";

    export let name: String;
    export let questions;
    let value = 0;

    function submit() {
		fetch("http://localhost:8000/feedback", {
			method: 'POST',
            headers: {
				'Content-Type': 'application/json'
			},
			body: '{"name": "' + name + '", \
                    "scores": [3,1,1]}'
		});
	}

</script>

<div class="container mx-auto p-8 pb-0">
    <h2 class="h2">{name}</h2>
    {#each questions as question}
        <div class="form-input my-5">
            <label class="label">
                <span>{question.title}</span>
                <div class="space-y-2">
                    <fieldset id={question.title} >
                        {#each {length: 3} as x, i}
                            <label class="flex items-center space-x-2">
                                <input class="radio" type="radio" value={question.responses[i].score} name={question.title} />
                                <p>{question.responses[i].description} {question.title}</p>
                            </label>
                        {/each}
                    </fieldset>
                </div>
            </label>
        </div>
    {/each}
</div>

<div class="container mx-auto px-8 mt-0">
    <section>
        <button type="button" class="btn variant-filled-primary"
         on:click={submit}>Submit</button>
    </section>
</div>