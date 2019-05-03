<template>
  <div>
    <a-row style="margin:5px">
      <a-col :span="2">
        <a-button type="primary" class="btn-ensure" @click="onCreate">
          <a-icon type="plus"/>添加资产
        </a-button>
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
      :dataSource="cmdbList"
      rowKey="id"
      size="small"
      :pagination="pagination"
    >
      <span slot="order" slot-scope="text,record,index">{{(curPage-1)*(pageSize)+index+1}}</span>
       <span slot="device_type" slot-scope="text,record">
       <span  v-if="text==0">Worker</span>
       <span  v-if="text==1">HAVA服务器</span>
       <span  v-if="text==2">Jenkins服务器</span>
      </span>
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
    title: "HostName",
    dataIndex: "hostname",
    align: "center",
    sorter: (a, b) => a.username.localeCompare(b.username)
  },
  {
    title: "IP",
    dataIndex: "ip",
    align: "center"
  },
  {
    title: "资产类型",
    dataIndex: "device_type",
    align: "center",
    scopedSlots: {
      customRender: "device_type"
    }
  },
  {
    title: "创建者",
    dataIndex: "user",
    align: "center",
  },
  {
    title: "创建时间",
    dataIndex: "addtime",
    align: "center",

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
      cmdbList: [],
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
    this.getCMDBList();
  },
  methods: {
    getCMDBList() {
      this.$api.getCMDBList({ group: 1 }).then(resp => {
        this.cmdbList = resp;
        this.pagination.total = this.cmdbList.length;
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

