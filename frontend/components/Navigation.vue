<template>
	<div class="main-nav-container">
		<nav>
			<div class="name"><n-link :to="$auth.loggedIn ? '/dashboard' : '/'">shortdiary</n-link></div>
			<el-menu :default-active="$route.path" mode="horizontal" class="main-nav" @select="navSelect">
				<el-menu-item v-for="item of nav_items" :key="item.path" :index="item.path">
					<fa v-if="item.icon" :icon="['far', item.icon]" /> {{ item.label }}
				</el-menu-item>
			</el-menu>
			<el-menu mode="horizontal" @select="navSelect">
				<el-submenu popper-class="submenu-right">
					<template slot="title">
						<template v-if="$auth.loggedIn">
							<GravatarImg :email="$auth.user.email" :size="25" class="nav-avatar" /> {{ $auth.user.username }}
						</template>
						<template v-else>
							Legal
						</template>
					</template>

					<template v-if="$auth.loggedIn">
						<el-menu-item index="/settings"><fa :icon="['far', 'wrench']" /> <span>Settings</span></el-menu-item>
						<el-menu-item index="logout"><fa :icon="['far', 'sign-out']" /> <span>Sign out</span></el-menu-item>
					</template>

					<el-menu-item-group>
						<el-menu-item><fa :icon="['fab', 'github']" /> <a href="https://github.com/lutoma/shortdiary" target="_blank" rel="noopener">Source code</a></el-menu-item>
						<el-menu-item><fa :icon="['far', 'file-contract']" /> <a href="https://fnordserver.eu/en/imprint/" target="_blank" rel="noopener">Legal notice</a></el-menu-item>
						<el-menu-item><fa :icon="['far', 'shield-check']" /> <a href="https://fnordserver.eu/en/privacy-policy/" target="_blank" rel="noopener">Privacy</a></el-menu-item>
					</el-menu-item-group>
				</el-submenu>
			</el-menu>
		</nav>
	</div>
</template>

<script>
import GravatarImg from '~/components/GravatarImg'

export default {
	components: {
		GravatarImg
	},

	methods: {
		navSelect(path, _) {
			if (!path) {
				return
			}

			// Bit hacky
			if (path === 'logout') {
				this.$auth.logout()
			} else {
				this.$router.push({ path })
			}
		}

	},
	computed: {
		nav_items() {
			let items

			if (this.$auth.loggedIn) {
				items = [
					{ path: '/dashboard', label: 'Dashboard', icon: 'list' },
					{ path: '/new', label: 'New entry', icon: 'pencil' },
					{ path: '/stats', label: 'Stats', icon: 'chart-bar' },
					{ path: '/leaderboard', label: 'Leaderboard', icon: 'medal' },
					{ path: '/discover', label: 'Discover', icon: 'compass' }
				]
			} else {
				items = [
					{ path: '/login', label: 'Sign in', icon: 'sign-in' },
					{ path: '/join', label: 'Join', icon: 'user-friends' }
				]
			}

			return items
		}
	}
}
</script>

<style lang="scss">
// This CSS is a bit incoherent as we mostly have to override a whole lot of
// Element-UI shenanigans

.main-nav-container {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	z-index: 2000;

	background: #036564;
	border-bottom: 3px solid #CDB380;
	box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);

	.main-nav {
		flex-grow: 1;
	}

	nav {
		max-width: 1600px;
		padding: 0 2rem;

		margin: 0 auto;
		display: flex;
		align-items: center;

		.name {
			font-family: "Exo 2", "Fira Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
			font-size: 25px;
			font-weight: 600;
			margin-right: 50px;

			&, a {
				color: white;
				text-decoration: none;
			}
		}

		.el-menu--horizontal {
			border-bottom: none;
			background: initial;

			.el-menu-item, .el-submenu .el-submenu__title {
				color: white;
				font-weight: 600;
				border-right: solid #025554 1px;
				height: 50px;
				line-height: 50px;
				font-size: .9rem;
				border-bottom: none !important;

				&:first-of-type {
					border-left: solid #025554 1px;
				}
			}

			.el-submenu__title {
				background: transparent !important;
			}

			.el-menu-item.is-active, .el-menu-item:not(.is-disabled):focus, .el-menu-item:not(.is-disabled):hover, .el-submenu.is-opened .el-submenu__title {
				border-bottom: none;
				background-color: rgba(0, 0, 0, 0.1) !important;
				color: white;
			}
		}
	}
}

.submenu-right {
	.el-menu-item {
		svg {
			min-width: 20px;
		}

		a, span {
			color: #036564 !important;

			&:hover {
				text-decoration: underline;
			}
		}
	}
}

.nav-avatar {
	width: 25px;
	height: 25px;
	border-radius: 50%;
	margin-right: 5px;
}
</style>
