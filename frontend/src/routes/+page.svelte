<script lang="ts">
	let balance: number = 0;
	let shouts: number = 0;
	let steps: number = 0;
	let meditations: number = 0;
	let awards: number = 0;
	let achievements: number = 0;
	let places: number = 0;

	$: answers = {
		balance,
		shouts,
		steps,
		meditations,
		awards,
		achievements,
		places
	};

	let result: string | null = null;

	function handleSubmit() {
		result = 'Processing...';
		setTimeout(() => {
			result = Math.random() < 0.5 ? 'You are stressed...' : 'You are not stressed!';
		}, 1000);
	}
</script>

<h1 class="text-3xl font-bold">&#129760; Stress</h1>
<br />
<div class="flex flex-col items-center gap-3">
	<div
		class="border-2 border-dashed border-orange-200 w-[50%] rounded-md p-3 bg-orange-100/50 text-center"
	>
		{result ? result : 'Result here...'}
	</div>
	<form class="flex flex-col gap-3 items-start bg-orange-100 p-3 rounded-lg w-[50%]">
		<div class="question">
			How often do you shout daily?
			<input bind:value={shouts} type="number" min={0} class="input" required />
		</div>
		<div class="question">
			How many steps do you walk in a day?
			<input bind:value={steps} type="number" min={0} class="input" required />
		</div>
		<div class="question">
			How often do you meditate in a week?
			<input bind:value={meditations} type="number" min={0} class="input" required />
		</div>
		<div class="question">
			How many personal awards do you have?
			<input bind:value={awards} type="number" min={0} class="input" required />
		</div>
		<div class="question">
			How many achievements are you proud of?
			<input bind:value={achievements} type="number" min={0} class="input" required />
		</div>
		<div class="question">
			How many places have you visited over the past week?
			<input bind:value={places} type="number" min={0} class="input" required />
		</div>
	</form>
	<button
		type="submit"
		on:click={handleSubmit}
		class="bg-orange-100 rounded-md px-3 py-2 border-2 border-solid border-orange-400 hover:scale-110 transition-all"
		>Submit</button
	>
</div>
