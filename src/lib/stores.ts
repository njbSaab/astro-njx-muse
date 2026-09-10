/**
 * Client state on nanostores/persistent. Cart lines carry size + colour;
 * wishlist holds handles. The newsletter popup fires once per browser
 * via a persistent flag.
 */
import { persistentAtom } from '@nanostores/persistent';

const json = { encode: JSON.stringify, decode: JSON.parse };

export interface CartLine {
  key: string; // handle|size|color
  handle: string;
  size: string;
  color: string;
  quantity: number;
}
export const cart = persistentAtom<CartLine[]>('njx-muse-cart', [], json);

export function addToCart(handle: string, size: string, color: string, quantity = 1) {
  const key = `${handle}|${size}|${color}`;
  const lines = [...cart.get()];
  const ex = lines.find((l) => l.key === key);
  if (ex) ex.quantity += quantity;
  else lines.push({ key, handle, size, color, quantity });
  cart.set(lines);
}
export function setCartQty(key: string, quantity: number) {
  cart.set(cart.get().map((l) => (l.key === key ? { ...l, quantity } : l)).filter((l) => l.quantity > 0));
}

export const wishlist = persistentAtom<string[]>('njx-muse-wishlist', [], json);
export function toggleWishlist(handle: string): boolean {
  const list = wishlist.get();
  const added = !list.includes(handle);
  wishlist.set(added ? [...list, handle] : list.filter((h) => h !== handle));
  return added;
}

export const popupSeen = persistentAtom<string>('njx-muse-popup-seen', '');
