<template>
  <div>
    <a-row style="margin:5px">
      <a-col :span="2">
        <!-- <a-button class="btn-info" @click="onCreate">
          <a-icon type="plus"/>创建用户
        </a-button> -->
      </a-col>
      <a-col :span="2" :offset="20">
        <a-button class="btn-danger" @click="onDelete">
          <a-icon type="delete"/>删除
        </a-button>
      </a-col>
    </a-row>
    <a-table
      :rowSelection="{selectedRowKeys: selectedRowKeys, onChange: onSelectChange}"
      :columns="columns"
      :dataSource="userList"
      rowKey="id"
      size="small"
      :pagination="pagination"
    >
      <span slot="order" slot-scope="text,record,index">{{(curPage-1)*(pageSize)+index+1}}</span>
      <span slot="deal" slot-scope="text,record">
        <a-button type="primary" size="small">
          <a-icon type="edit"/>
        </a-button>
      </span>
    </a-table>
  </div>
</template>
<script>
const columns = [
  {
    title: "序号",
    align: "center",
    scopedSlots: {
      customRender: "order"
    }
  },
  {
    title: "账号",
    dataIndex: "username",
    align: "center",
    sorter: (a, b) => a.username.localeCompare(b.username)
  },
  {
    title: "Email",
    dataIndex: "email",
    align: "center"
  },
  {
    title: "在职状态",
    dataIndex: "is_staff",
    align: "center",
    customRender: (text, recoder) => (text == true ? "是" : "否")
  },
  {
    title: "管理员",
    dataIndex: "is_superuser",
    align: "center",
    customRender: (text, recoder) => (text == true ? "是" : "否")
  },
  {
    title: "最后一次登录时间",
    dataIndex: "last_login",
    align: "center",
    customRender: text =>
      text.split("T")[0] + " " + text.split("T")[1].split(".")[0]
  },
  {
    title: "操作",
    align: "center",
    scopedSlots: {
      customRender: "deal"
    }
  }
];

const pagination = {};
export default {
  name: "UserList",
  data() {
    return {
      userList: [],
      columns,
      selectedRowKeys: [],
      curPage: 1,
      pageSize: 5,
      pagination: {
        total: 0,
        pageSizeOptions: ["5", "10", "20", "50"],
        showQuickJumper: true,
        showSizeChanger: true,
        defaultPageSize: 5,
        onChange: this.pageSizeChange,
        showTotal: (total, range) => `共 ${total} 条`
      }
    };
  },
  mounted() {
    this.getUserList();
  },
  methods: {
    getUserList() {
      this.$api.getUserList({ group: 1 }).then(resp => {
        this.userList = resp;
        this.pagination.total = this.userList.length;
      });
    },
    onSelectChange(selectedRowKeys) {
      console.log("selectedRowKeys changed: ", selectedRowKeys);
      this.selectedRowKeys = selectedRowKeys;
    },
    pageSizeChange(current, size) {
      this.curPage = current;
      this.pageSize = size;
    },
    onCreate() {},
    onDelete() {
      console.log(this.selectedRowKeys);
    }
  }
};
</script>

