import { ElMessageBox } from 'element-plus';

export const confirmBox = async (content: string, caption: string | undefined = undefined, options: any = undefined): Promise<boolean> => {
  // 更简单的ElMessageBox.confirm
  // 只返回boolean，不需要在业务代码中再加以try判断
  try {
    return (await ElMessageBox.confirm(content, caption, options)) == 'confirm';
  } catch (e) {
    return false;
  }
};
