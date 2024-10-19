<script>
    export let name;
    export let value;
    export let description;
</script>

<label class="flex items-center space-x-2">
    <input class="radio" type="radio" name={name} value={value} />
    <p>{description}</p>
</label>