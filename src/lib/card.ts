/**
 * Shared product card renderer — used by the home carousels and the catalog
 * grid. All interactivity (hover bar, quick size add, wishlist, quick view)
 * is delegated globally in the layout via data-card-* attributes.
 */
export const esc = (s: string) =>
  String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]!));

export const fmt = (n: number) => '€' + n.toFixed(2);

export function cardHTML(p: any, wished: boolean): string {
  const sale = p.oldPrice != null;
  return `
  <article class="group relative" data-card="${p.handle}" data-color="0">
    <div class="relative aspect-[3/4] w-full overflow-hidden bg-tint">
      <a href="/products/${p.handle}" class="absolute inset-0 block">
        <img src="${p.image}" alt="${esc(p.name)}" loading="lazy" class="absolute inset-0 h-full w-full object-cover transition-[opacity,transform] duration-700 group-hover:scale-[1.04] ${p.image2 ? 'group-hover:opacity-0' : ''}" />
        ${p.image2 ? `<img src="${p.image2}" alt="" loading="lazy" class="absolute inset-0 h-full w-full object-cover opacity-0 transition-[opacity,transform] duration-700 group-hover:scale-[1.04] group-hover:opacity-100" />` : ''}
      </a>
      <span class="note pointer-events-none absolute bottom-2.5 left-3 text-white/80 mix-blend-difference">${esc(p.name.toLowerCase())} · <span class="hidden group-hover:inline">full look</span><span class="group-hover:hidden">studio</span></span>
      ${p.badge ? `<span class="cap-xs absolute left-3 top-3 px-2.5 py-1.5 text-white" style="background:${p.badge === 'LAST CHANCE' ? '#6f5bd6' : '#191936'}">${esc(p.badge)}</span>` : ''}
      <button data-card-wish="${p.handle}" aria-label="Wishlist" class="absolute right-2 top-2 flex h-8 w-8 items-center justify-center text-[14px] transition ${wished ? 'text-acc' : 'text-ink/45'}"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
      <div class="absolute inset-x-0 bottom-0 translate-y-full border-t border-line bg-white/95 px-3.5 py-3 opacity-0 transition-all duration-300 group-hover:translate-y-0 group-hover:opacity-100">
        <div class="flex w-full items-center justify-between" data-card-bar>
          <button data-card-qv="${p.handle}" class="cap cursor-pointer">Quick view</button>
          <button data-card-open-sizes="${p.handle}" class="cap cursor-pointer">+ Add to bag</button>
        </div>
        <div class="hidden w-full items-center justify-center gap-3" data-card-sizes>
          <span class="cap-xs text-muted">Size</span>
          ${p.sizes.map((z: string) => `<button data-card-size="${esc(z)}" data-h="${p.handle}" class="cursor-pointer px-1 py-0.5 text-[11px] tracking-[0.1em]">${esc(z)}</button>`).join('')}
        </div>
      </div>
    </div>
    <div class="flex flex-col gap-2 px-0.5 pt-3.5">
      <a href="/products/${p.handle}" class="cap-tag leading-relaxed">${esc(p.name)}</a>
      <div class="flex items-baseline gap-2.5 text-[12px] tracking-[0.04em]">
        ${sale
          ? `<span class="text-acc">${fmt(p.price)}</span><span class="text-muted line-through">${fmt(p.oldPrice)}</span>`
          : `<span>${fmt(p.price)}</span>`}
      </div>
      <div class="flex min-h-[14px] items-center gap-1.5">
        ${p.colors.map((c: any, i: number) => `<button data-card-swatch="${i}" title="${esc(c.name)}" class="h-3 w-3 cursor-pointer border ${i === 0 ? 'border-ink' : 'border-line'}" style="background:${c.hex}"></button>`).join('')}
      </div>
    </div>
  </article>`;
}
