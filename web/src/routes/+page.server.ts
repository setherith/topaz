/** @type {import('./$types').Actions} */
export const actions = {
	default: async ({ request }) => {
		console.log(request.body);
	}
};