export const buildTextThumbnail = (obj) => {
  // 获取一段文本的缩略。
  if (obj.constructor == String) obj = { text: obj };
  let subStr = obj.text.substring(0, obj.max_length || 30);
  if (obj.text.length > (obj.max_length || 30)) {
    subStr += ' ...';
  }
  return subStr;
};
