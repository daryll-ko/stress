<script lang="ts">
	let balance: number;
	let shouts: number;
	let steps: number;
	let meditations: number;
	let awards: number;
	let achievements: number;
	let places: number;
</script>

<h1 class="text-3xl font-bold">Stress</h1>
<br />
<div class="flex flex-col items-center gap-3">
	<form class="flex flex-col gap-3 items-start bg-orange-100 p-3 rounded-lg w-[50%]">
		<div class="question">
			How often do you shout daily?
			<input bind:value={shouts} type="number" min={0} class="input" />
		</div>
		<div class="question">
			How many steps do you walk in a day?
			<input bind:value={steps} type="number" min={0} class="input" />
		</div>
		<div class="question">
			How often do you meditate in a week?
			<input bind:value={meditations} type="number" min={0} class="input" />
		</div>
		<div class="question">
			How many personal awards do you have?
			<input bind:value={awards} type="number" min={0} class="input" />
		</div>
		<div class="question">
			How many achievements are you proud of?
			<input bind:value={achievements} type="number" min={0} class="input" />
		</div>
		<div class="question">
			How many places have you visited over the past week?
			<input bind:value={places} type="number" min={0} class="input" />
		</div>
	</form>
	<button class="bg-orange-100 rounded-md px-3 py-2 border-2 border-solid border-orange-400 hover:scale-110 transition-all">Submit</button>
</div>
