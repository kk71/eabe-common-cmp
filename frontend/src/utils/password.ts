import CryptoJS from 'crypto-js';

export async function buildEncryptedPasswordHttps(message: string): Promise<string> {
  // 构建console密码登录的加密后密码
  // 注意，加密方式必须和后端对齐，不能随便修改
  const msgUint8 = new TextEncoder().encode(message); // encode as (utf-8) Uint8Array
  const hashBuffer = await window.crypto.subtle.digest('SHA-512', msgUint8); // hash the message
  const hashArray = Array.from(new Uint8Array(hashBuffer)); // convert buffer to byte array
  const hashHex = hashArray.map((b) => b.toString(16).padStart(2, '0')).join(''); // convert bytes to hex string
  return hashHex;
}

export function buildEncryptedPasswordHttp(message: string): string {
  // 构建console密码登录的加密后密码
  // 注意，加密方式必须和后端对齐，不能随便修改
  const hashBuffer = CryptoJS.SHA512(message);
  const hashHex = hashBuffer.toString(CryptoJS.enc.Hex);
  return hashHex;
}

export async function buildEncryptedPassword(message: string): Promise<string> {
  if (location.protocol == 'http:') return buildEncryptedPasswordHttp(message);
  return await buildEncryptedPasswordHttps(message);
}
