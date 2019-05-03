export default {
  // 基础url前缀
  baseURL: "http://127.0.0.1:8000",
  // 请求头信息
  headers: {
    "Content-Type": "application/json;charset=UTF-8",
  },
  // 设置超时时间
  timeout: 10000,
  // 携带凭证
  withCredentials: false,
  // 返回数据类型
  responseType: "json"
};
