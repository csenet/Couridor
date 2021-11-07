import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import {getAuth} from 'firebase/auth';
import Welcome from "@/views/Welcome";
import SignUp from "@/views/SignUp";
import Profile from "@/views/Profile";
import Explorer from "@/views/Explorer";
import ThemeList from "@/views/ThemaList";
import Test from "@/views/Test"

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Welcome',
        component: Welcome
    },
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/profile/:username',
        name: 'Profile',
        component: Profile,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/explorer',
        name: 'Explorer',
        component: Explorer
    },
    {
        path: '/themelist/:theme',
        name: 'ThemeList',
        component: ThemeList
    },
    {
        path:'/test',
        name:'Test',
        component: Test
    }
]

const router = new VueRouter({
    routes
})

router.beforeEach((to, from, next) => {
    let requiresAuth = to.matched.some(record => record.meta.requiresAuth)
    let currentUser = getAuth().currentUser;
    if (requiresAuth) {
        if (!currentUser) {
            next({
                path: '/login',
                query: {redirect: to.fullPath}
            })
        } else {
            next()
        }
    } else {
        next()
    }
})

router.beforeEach((to, from, next) => {
    let requiresAuth = to.matched.some(record => record.meta.requiresAuth)
    let currentUser = getAuth().currentUser;
    if (requiresAuth) {
        if (!currentUser) {
            next({
                path: '/login',
                query: {redirect: to.fullPath}
            })
        } else {
            next()
        }
    } else {
        next()
    }
})

router.beforeEach((to, from, next) => {
    let requiresAuth = to.matched.some(record => record.meta.requiresAuth)
    let currentUser = getAuth().currentUser;
    if (requiresAuth) {
        if (!currentUser) {
            next({
                path: '/login',
                query: {redirect: to.fullPath}
            })
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router
