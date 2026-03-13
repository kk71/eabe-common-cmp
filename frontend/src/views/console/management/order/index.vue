<template>
  <filterable-list-frame
    v-model:filterData="data.filterData"
    v-model:pagination="data.p"
    :filter-data-typing="data.filterDataTyping"
    @filter-changed="onLoad"
  >
    <el-form ref="form" :model="data.filterData" class="filter-box" label-position="right" label-width="70px">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="搜索">
            <plain-text v-model="data.filterData.keyword" clearable placeholder="" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="产品类型">
            <csm v-model="data.filterData.product_type" flag="product-type" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="订单状态">
            <csm v-model="data.filterData.status" flag="order-status" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="区域">
            <csm v-model="data.filterData.origin" flag="order-origin" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-space style="margin-bottom: 10px">
      <el-button type="primary" @click="importDialog.visible = true">导入订单</el-button>
      <el-button @click="downloadImportTemplate">下载模板</el-button>
    </el-space>

    <el-table ref="listTable" :data="data.data" stripe v-loading="loading">
      <el-table-column type="selection" width="50" />
      <el-table-column prop="order_id" label="订单编号" min-width="200" />
      <el-table-column label="客户名称" min-width="200">
        <template #default="{ row }">
          <el-tooltip
            v-if="(row.customer_code || '').trim()"
            effect="dark"
            :content="`客户编号：${(row.customer_code || '').trim()}`"
            placement="top"
          >
            <span>{{ row?.customer?.name || '-' }}</span>
          </el-tooltip>
          <span v-else>{{ row?.customer?.name || '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="batch_code" label="批次" min-width="200" />
      <el-table-column label="产品" prop="product_name" min-width="160" />
      <el-table-column prop="resource_code" label="资源编号" min-width="200" />
      <el-table-column prop="order_guanxi_id" label="订购关系ID" min-width="120" />
      <table-column-smv label="区域" prop="origin" flag="order-origin" min-width="140" />
      <table-column-smv label="订单类型" prop="product_type" flag="product-type" min-width="140" />
      <table-column-dt prop="order_date" label="下单日期" min-width="120" type="date" />
      <table-column-smv label="状态" prop="status" flag="order-status" min-width="140" />
      <el-table-column label="支付状态" min-width="140">
        <template #default="{ row }">
          <el-tag v-if="row.status === 'paid'" type="success">已支付</el-tag>
          <el-tag v-else-if="row.status === 'pay_failed'" type="danger">支付失败</el-tag>
          <el-tag v-else type="warning">进行中</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="total_price" label="总金额" min-width="150" sortable />

      <el-table-column label="操作" width="140" fixed="right">
        <template #default="{ row }">
          <el-button
            v-if="row.status !== 'paid'"
            type="primary"
            link
            size="small"
            @click="handleManualPay(row)"
          >
            重试扣费
          </el-button>
          <el-button type="primary" link size="small" @click="openOrderTxDialog(row)">查看流水</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="txDialog.visible" :title="`钱包流水 - 订单 ${txDialog.orderId}`" width="800px">
      <el-table :data="txDialog.data" v-loading="loading" stripe>
        <el-table-column prop="tx_id" label="流水编号" min-width="200" />
        <el-table-column prop="tx_type" label="类型" min-width="80" />
        <el-table-column prop="change_amount" label="变动金额" min-width="120" />
        <el-table-column prop="balance_after" label="变动后余额" min-width="120" />
        <el-table-column prop="remark" label="备注" min-width="180" />
        <table-column-dt prop="create_time" label="时间" min-width="180" />
      </el-table>
      <template #footer>
        <el-button @click="txDialog.visible = false">关闭</el-button>
      </template>
    </el-dialog>

    <el-dialog v-model="importDialog.visible" title="导入订单（CSV / Excel）" width="760px">
      <el-alert type="info" show-icon :closable="false" style="margin-bottom: 10px">
        <template #title>
          选择 CSV 或 Excel(xlsx) 上传，后台仅导入入库，扣费由定时任务到期执行。字段顺序：
          订单编号、批次、产品名称、资源编号、订购关系ID、客户编号(code)、区域、订单类型、下单日期、状态、总金额
        </template>
      </el-alert>
      <el-upload
        drag
        :auto-upload="false"
        :limit="1"
        accept=".csv,.xlsx"
        :on-change="onImportFileChange"
        :on-remove="onImportFileRemove"
      >
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">拖拽文件到此处，或 <em>点击选择</em></div>
        <template #tip>
          <div class="el-upload__tip">支持 .csv / .xlsx，首行表头会自动跳过；客户编号需在客户表已存在</div>
        </template>
      </el-upload>
      <template #footer>
        <el-button @click="importDialog.visible = false">取消</el-button>
        <el-button type="primary" :disabled="!importDialog.file" @click="doImportOrders">导入</el-button>
      </template>
    </el-dialog>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getOrders, payOrderByWallet, getWalletTransactions, importOrdersFile } from '@/api/console';
  import { UploadFilled } from '@element-plus/icons-vue';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);

  const router = useRouter();

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      keyword: '',
      product_type: null,
      order_type: null,
      status: null,
      origin: null,
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
      keyword: String,
    }),
    data: [],
  });

  const txDialog = reactive({
    visible: false,
    orderId: '',
    data: [],
  });

  const importDialog = reactive({
    visible: false,
    file: null,
  });

  const handleManualPay = async (row) => {
    await waitRequest(
      loading,
      payOrderByWallet({
        params: {
          id: row.id,
        },
      }),
    );
    await onLoad();
  };

  const openOrderTxDialog = async (row) => {
    txDialog.orderId = row.order_id;
    txDialog.visible = true;
    await loadOrderTransactions();
  };

  const loadOrderTransactions = async () => {
    if (!txDialog.orderId) return;
    const resp = await waitRequest(
      loading,
      getWalletTransactions({
        params: {
          page: 1,
          per_page: 50,
          keyword: txDialog.orderId,
        },
      }),
    );
    txDialog.data = resp.data.data.filter((i) => i.related_order_id === txDialog.orderId);
  };

  async function onLoad() {
    const resp = await waitRequest(
      loading,
      getOrders({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    data.p = resp.data.pagination;
    data.data = resp.data.data;
  }

  const doImportOrders = async () => {
    if (!importDialog.file) return;
    const fd = new FormData();
    fd.append('file', importDialog.file);
    fd.append('skip_header', 'true');
    await waitRequest(
      loading,
      importOrdersFile({
        data: fd,
        headers: { 'Content-Type': 'multipart/form-data' },
      }),
    );
    importDialog.visible = false;
    importDialog.file = null;
    await onLoad();
  };

  const onImportFileChange = (uploadFile) => {
    importDialog.file = uploadFile?.raw || null;
  };
  const onImportFileRemove = () => {
    importDialog.file = null;
  };

  const downloadImportTemplate = () => {
    const base = import.meta.env.BASE_URL || '/';
    const url = `${base.replace(/\/+$/, '/')}templates/order_import_template.xlsx`;
    const a = document.createElement('a');
    a.href = url;
    a.download = 'order_import_template.xlsx';
    document.body.appendChild(a);
    a.click();
    a.remove();
  };

  onMounted(async () => {
    emits('update-title', '订单管理');
    await onLoad();
  });
</script>
