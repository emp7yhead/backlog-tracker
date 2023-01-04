<template>
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="sm:text-center pt-20">
      <h2 class="text-lg font-semibold leading-8 text-indigo-600">Backlog Tracker</h2>
      <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Simple pet-project builded to train skill in intresting technologies.</p>
      <p class="mx-auto mt-6 max-w-2xl text-lg leading-8 text-gray-600">Lorem ipsum dolor sit amet consect adipisicing elit. Possimus magnam voluptatum cupiditate veritatis in accusamus quisquam.</p>
    </div>

    <div class="mt-20 max-w-lg sm:mx-auto md:max-w-none">
      <div class="grid grid-cols-1 gap-y-16 md:grid-cols-3 md:gap-x-12 md:gap-y-16">
        <div v-for="feature in features" :key="feature.name" class="relative flex flex-col gap-6 sm:flex-row md:flex-col lg:flex-row">
          <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-500 text-white sm:shrink-0">
          <component :is="feature.icon" class="h-8 w-8" aria-hidden="true" />
          </div>
          <div class="sm:min-w-0 sm:flex-1">
            <p class="text-lg font-semibold leading-8 text-gray-900">{{ feature.name }}</p>
            <p class="mt-2 text-base leading-7 text-gray-600">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </div>
      <div class="hidden pt-20 sm:mb-8 sm:flex sm:justify-center">
        <div class="relative overflow-hidden rounded-full py-1.5 px-4 text-sm leading-6 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
          <span class="text-gray-600">
            Looking for source code? <a href="https://github.com/emp7yhead/backlog-tracker" class="font-semibold text-indigo-600"><span class="absolute inset-0" aria-hidden="true" /> Check Github <span aria-hidden="true">&rarr;</span></a>
          </span>
        </div>
      </div>
    </div>
</template>

<script setup>
import { BoltIcon, GlobeAltIcon, ScaleIcon } from '@heroicons/vue/24/outline'

const features = [
  {
    name: 'FastAPI',
    description:
      'Modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.',
    icon: GlobeAltIcon,
  },
  {
    name: 'Vue.js',
    description:
      'An approachable, performant and versatile framework for building web user interfaces.',
    icon: ScaleIcon,
  },
  {
    name: 'TailwindCSS',
    description:
      'A utility-first CSS framework packed with classes that can be composed to build any design, directly in your markup.',
    icon: BoltIcon,
  },
];
</script>
