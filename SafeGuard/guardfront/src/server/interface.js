import common from "./models/common";
import user from "./models/user"
import cmdb from "./models/cmdb"

// 默认全部导出
export default {
  ...common,
  ...user,
  ...cmdb,
};
