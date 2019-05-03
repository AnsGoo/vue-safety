import axios from "../api";

// 单独导出
const getCMDBList = data => {
  return axios({
    url: "/cmdb/list",
    method: "POST",
    data: data
  });
};




export default {
    getCMDBList,
};
