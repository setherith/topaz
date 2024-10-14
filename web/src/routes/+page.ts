/** @type {import('./$types').PageLoad} */
export function load({ }) {
	return {
		questions: [
			{
				title: 'Mood',
				responses: [
					{ 
						score: 3,
						description: 'Good behaviour most of the day'
					},
					{ 
						score: 2,
						description: 'Some bouts of funk' 
					},
					{
						score: 1,
						description: 'Terror child!'
					}
				]
			},
			{
				title: 'Helped Out',
				responses: [
					{ 
						score: 3,
						description: 'A lot'
					},
					{ 
						score: 2,
						description: 'Sometimes'
					},
					{
						score: 1,
						description: 'No help at all'
					}
				]
			},
			{
				title: 'Ate Well',
				responses: [
					{ 
						score: 3,
						description: 'Clean plate' 
					},
					{ 
						score: 2,
						description: 'Most of it'
					},
					{
						score: 1,
						description: 'Hardly touched it' 
					}
				]
			}
		]
	};
}