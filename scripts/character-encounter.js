import { mountContinuousPortrait } from '@base/continuous-portrait';
import { portrait } from '../shared/portrait.mjs';

export function mount({ element }) {
  const wrapper = element.closest('[data-gazette-component]');
  const binding = document.getElementById('portrait-resources');
  const resources = binding ? JSON.parse(binding.textContent) : [];
  if (wrapper) return mountContinuousPortrait(wrapper, portrait, resources);
}
