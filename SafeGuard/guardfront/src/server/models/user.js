import axios from "../api";

// 单独导出
const getUserList = data => {
  return axios({
    url: "/user/list",
    method: "POST",
    data: data
  });
};




export default {
    getUserList,
};
