<template>
	<div class="new-post">
		<h1>Create a new entry</h1>
		<PostEditor />
	</div>
</template>

<script>
import PostEditor from '~/components/PostEditor'

export default {
	components: {
		PostEditor
	},

	head () {
		return { title: 'New entry – shortdiary' }
	}
}
</script>

<style lang="scss">
.new-post {
	height: 100%;
	display: flex;
	flex-direction: column;
	padding-bottom: 30px;

	.post-editor {
		width: 100%;
		flex-grow: 1;
	}
}
</style>
