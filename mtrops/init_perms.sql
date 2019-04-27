/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50640
 Source Host           : 127.0.0.1:3306
 Source Schema         : mtrops

 Target Server Type    : MySQL
 Target Server Version : 50640
 File Encoding         : 65001

 Date: 06/07/2018 23:33:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app_cmdb_hostgroup
-- ----------------------------
DROP TABLE IF EXISTS `app_cmdb_hostgroup`;
CREATE TABLE `app_cmdb_hostgroup`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `msg` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `group_name`(`group_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_cmdb_hostgroup
-- ----------------------------
INSERT INTO `app_cmdb_hostgroup` VALUES (1, 'test', '测试');

-- ----------------------------
-- Table structure for app_cmdb_hostinfo
-- ----------------------------
DROP TABLE IF EXISTS `app_cmdb_hostinfo`;
CREATE TABLE `app_cmdb_hostinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IP` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `passwd` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `device_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `port` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `msg` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `hostname` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `in_ip` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `os_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `service_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `os_version` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mem_total` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mem_swap` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cpu_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cpu_num` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mount_home` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mount_root` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mount_alidata` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `kernel` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addTime` datetime(6) NOT NULL,
  `host_group_id` int(11) NOT NULL,
  `idc_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `IP`(`IP`) USING BTREE,
  INDEX `app_cmdb_hostinfo_host_group_id_e737b89a_fk_app_cmdb_`(`host_group_id`) USING BTREE,
  INDEX `app_cmdb_hostinfo_idc_id_844ff49c_fk_app_cmdb_idc_id`(`idc_id`) USING BTREE,
  CONSTRAINT `app_cmdb_hostinfo_host_group_id_e737b89a_fk_app_cmdb_` FOREIGN KEY (`host_group_id`) REFERENCES `app_cmdb_hostgroup` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `app_cmdb_hostinfo_idc_id_844ff49c_fk_app_cmdb_idc_id` FOREIGN KEY (`idc_id`) REFERENCES `app_cmdb_idc` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_cmdb_hostinfo
-- ----------------------------
INSERT INTO `app_cmdb_hostinfo` VALUES (1, '192.168.49.132', 'root', 'ONeday0313', '服务器', '22', '测试', NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2018-07-06 15:13:32.826000', 1, 1);

-- ----------------------------
-- Table structure for app_cmdb_idc
-- ----------------------------
DROP TABLE IF EXISTS `app_cmdb_idc`;
CREATE TABLE `app_cmdb_idc`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idc_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `msg` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idc_name`(`idc_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_cmdb_idc
-- ----------------------------
INSERT INTO `app_cmdb_idc` VALUES (1, '本地', '测试');

-- ----------------------------
-- Table structure for app_cmdb_loginuser
-- ----------------------------
DROP TABLE IF EXISTS `app_cmdb_loginuser`;
CREATE TABLE `app_cmdb_loginuser`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login_user` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `login_passwd` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `private_key` varchar(2048) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `people_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `login_user`(`login_user`) USING BTREE,
  INDEX `app_cmdb_loginuser_people_id_e4a23a40_fk_app_rbac_userinfo_id`(`people_id`) USING BTREE,
  CONSTRAINT `app_cmdb_loginuser_people_id_e4a23a40_fk_app_rbac_userinfo_id` FOREIGN KEY (`people_id`) REFERENCES `app_rbac_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_cmdb_loginuser
-- ----------------------------
INSERT INTO `app_cmdb_loginuser` VALUES (1, 'root', 'Oneday0313', '', 1);

-- ----------------------------
-- Table structure for app_code_codepost
-- ----------------------------
DROP TABLE IF EXISTS `app_code_codepost`;
CREATE TABLE `app_code_codepost`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_ip` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `site_path` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `postsite_msg` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `current_version` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `version_info` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `upcode_date` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `post_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `app_code_codepost_post_site_id_3cc1c40e_fk_app_code_site_id`(`post_site_id`) USING BTREE,
  CONSTRAINT `app_code_codepost_post_site_id_3cc1c40e_fk_app_code_site_id` FOREIGN KEY (`post_site_id`) REFERENCES `app_code_site` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for app_code_depend
-- ----------------------------
DROP TABLE IF EXISTS `app_code_depend`;
CREATE TABLE `app_code_depend`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `depend_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `depend_version` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `install_script` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_code_depend
-- ----------------------------
INSERT INTO `app_code_depend` VALUES (1, 'python', '2.7', '');
INSERT INTO `app_code_depend` VALUES (2, 'django', '1.11.9', '');
INSERT INTO `app_code_depend` VALUES (3, 'openpyxl', '2.5.2', '');
INSERT INTO `app_code_depend` VALUES (4, 'salt', '0.15', '');

-- ----------------------------
-- Table structure for app_code_postrecord
-- ----------------------------
DROP TABLE IF EXISTS `app_code_postrecord`;
CREATE TABLE `app_code_postrecord`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `current_version` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `version_info` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `upcode_date` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CodePost_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `app_code_postrecord_CodePost_id_cfece235_fk_app_code_codepost_id`(`CodePost_id`) USING BTREE,
  CONSTRAINT `app_code_postrecord_CodePost_id_cfece235_fk_app_code_codepost_id` FOREIGN KEY (`CodePost_id`) REFERENCES `app_code_codepost` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for app_code_project
-- ----------------------------
DROP TABLE IF EXISTS `app_code_project`;
CREATE TABLE `app_code_project`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `project_msg` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `project_name`(`project_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_code_project
-- ----------------------------
INSERT INTO `app_code_project` VALUES (1, 'devops', '运维开发');

-- ----------------------------
-- Table structure for app_code_site
-- ----------------------------
DROP TABLE IF EXISTS `app_code_site`;
CREATE TABLE `app_code_site`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `site_msg` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `site_url` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `site_depend` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `site_name`(`site_name`) USING BTREE,
  UNIQUE INDEX `site_url`(`site_url`) USING BTREE,
  INDEX `app_code_site_project_id_a9c3ee61_fk_app_code_project_id`(`project_id`) USING BTREE,
  CONSTRAINT `app_code_site_project_id_a9c3ee61_fk_app_code_project_id` FOREIGN KEY (`project_id`) REFERENCES `app_code_project` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_code_site
-- ----------------------------
INSERT INTO `app_code_site` VALUES (1, 'mtrops', '木头人运维管理平台', 'https://gitee.com/12x/mtrops.git', 'django/openpyxl/python/salt', 1);

-- ----------------------------
-- Table structure for app_rbac_permission
-- ----------------------------
DROP TABLE IF EXISTS `app_rbac_permission`;
CREATE TABLE `app_rbac_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `perms_title` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `perms_url` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `perms_type` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pmenu_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `perms_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `perms_icon` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 85 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_rbac_permission
-- ----------------------------
INSERT INTO `app_rbac_permission` VALUES (20, '首页', '/', '一级菜单', '0', '20', 'fa fa-lg fa-dashboard');
INSERT INTO `app_rbac_permission` VALUES (21, '资产管理', '/cmdb/', '一级菜单', '0', '21', 'fa fa-lg fa-bars');
INSERT INTO `app_rbac_permission` VALUES (22, '发布管理', '/code/', '一级菜单', '0', '22', 'fa fa-lg fa-code');
INSERT INTO `app_rbac_permission` VALUES (23, '后台管理', '/rbac/', '一级菜单', '0', '23', 'fa fa-lg fa-address-card');
INSERT INTO `app_rbac_permission` VALUES (24, 'CMDB', '/cmdb/hostinfo/', '二级菜单', '21', '21024', 'CMDB');
INSERT INTO `app_rbac_permission` VALUES (25, '主机组', '/cmdb/hostgroup/', '二级菜单', '21', '21025', '主机组菜单');
INSERT INTO `app_rbac_permission` VALUES (26, '添加资产', '/cmdb/addhost/', '功能', '21024', '21024026', '添加主机资产');
INSERT INTO `app_rbac_permission` VALUES (27, '项目管理', '/code/project/', '二级菜单', '22', '22027', '项目管理');
INSERT INTO `app_rbac_permission` VALUES (28, '站点管理', '/code/site/', '二级菜单', '22', '22028', '站点管理');
INSERT INTO `app_rbac_permission` VALUES (29, '环境部署', '/code/depend/', '二级菜单', '77', '77029', '环境部署');
INSERT INTO `app_rbac_permission` VALUES (30, '站点发布', '/code/postcode/', '二级菜单', '22', '22030', '站点发布');
INSERT INTO `app_rbac_permission` VALUES (31, '用户管理', '/rbac/usermg/', '二级菜单', '23', '23031', '用户管理');
INSERT INTO `app_rbac_permission` VALUES (32, '角色管理', '/rbac/role/', '二级菜单', '23', '23032', '角色管理');
INSERT INTO `app_rbac_permission` VALUES (34, '权限管理', '/rbac/perms/', '二级菜单', '23', '23034', '权限管理');
INSERT INTO `app_rbac_permission` VALUES (35, 'IDC', '/cmdb/idc/', '二级菜单', '21', '21035', '机房菜单');
INSERT INTO `app_rbac_permission` VALUES (37, '添加权限', '/rbac/addperms/', '功能', '23034', '23034037', '添加权限');
INSERT INTO `app_rbac_permission` VALUES (38, '修改权限', '/rbac/editperms/', '功能', '23034', '23034038', '修改权限');
INSERT INTO `app_rbac_permission` VALUES (40, '删除权限', '/rbac/delperms/', '功能', '23034', '23034040', '删除权限');
INSERT INTO `app_rbac_permission` VALUES (41, '添加角色', '/rbac/addrole/', '功能', '23032', '23032041', '添加角色');
INSERT INTO `app_rbac_permission` VALUES (42, '修改角色', '/rbac/editrole/', '功能', '23032', '23032042', '修改角色');
INSERT INTO `app_rbac_permission` VALUES (43, '删除角色', '/rbac/delrole/', '功能', '23032', '23032043', '删除角色');
INSERT INTO `app_rbac_permission` VALUES (44, '角色授权', '/rbac/roleperms/', '功能', '23032', '23032044', '角色授权');
INSERT INTO `app_rbac_permission` VALUES (45, '提交角色权限', '/rbac/addroleperms/', '功能', '23032', '23032045', '提交角色权限');
INSERT INTO `app_rbac_permission` VALUES (46, '添加用户', '/rbac/adduser/', '功能', '23031', '23031046', '添加用户');
INSERT INTO `app_rbac_permission` VALUES (47, '修改用户', '/rbac/edituser/', '功能', '23031', '23031047', '修改用户');
INSERT INTO `app_rbac_permission` VALUES (48, '删除用户', '/rbac/deluser/', '功能', '23031', '23031048', '删除用户');
INSERT INTO `app_rbac_permission` VALUES (49, '删除资产', '/cmdb/delhost/', '功能', '21024', '21024049', '删除资产');
INSERT INTO `app_rbac_permission` VALUES (50, '同步', '/cmdb/synchost/', '功能', '21024', '21024050', '同步资产信息');
INSERT INTO `app_rbac_permission` VALUES (51, '详细信息', '/cmdb/detailinfo/', '功能', '21024', '21024051', '详细信息');
INSERT INTO `app_rbac_permission` VALUES (52, '过滤资产', '/cmdb/filterhost/', '功能', '21024', '21024052', '过滤资产');
INSERT INTO `app_rbac_permission` VALUES (53, '修改资产', '/cmdb/edithost/', '功能', '21024', '21024053', '修改资产');
INSERT INTO `app_rbac_permission` VALUES (54, '导出资产', '/cmdb/expcmdb/', '功能', '21024', '21024054', '导出资产');
INSERT INTO `app_rbac_permission` VALUES (55, '添加主机组', '/cmdb/addgroup/', '功能', '21025', '21025055', '添加主机组');
INSERT INTO `app_rbac_permission` VALUES (56, '修改主机组', '/cmdb/editgroup/', '功能', '21025', '21025056', '修改主机组');
INSERT INTO `app_rbac_permission` VALUES (57, '删除主机组', '/cmdb/delgroup/', '功能', '21025', '21025057', '删除主机组');
INSERT INTO `app_rbac_permission` VALUES (58, '添加IDC', '/cmdb/addidc/', '功能', '21035', '21035058', '添加IDC');
INSERT INTO `app_rbac_permission` VALUES (59, '修改IDC', '/cmdb/editidc/', '功能', '21035', '21035059', '修改IDC');
INSERT INTO `app_rbac_permission` VALUES (60, '删除IDC', '/cmdb/delidc/', '功能', '21035', '21035060', '删除IDC');
INSERT INTO `app_rbac_permission` VALUES (61, '添加项目', '/code/addproject/', '功能', '22027', '22027061', '添加项目');
INSERT INTO `app_rbac_permission` VALUES (62, '修改项目', '/code/editproject/', '功能', '22027', '22027062', '修改项目');
INSERT INTO `app_rbac_permission` VALUES (63, '删除项目', '/code/delproject/', '功能', '22027', '22027063', '删除项目');
INSERT INTO `app_rbac_permission` VALUES (64, '添加站点', '/code/addsite/', '功能', '22028', '22028064', '添加站点');
INSERT INTO `app_rbac_permission` VALUES (65, '修改站点', '/code/editsite/', '功能', '22028', '22028065', '修改站点');
INSERT INTO `app_rbac_permission` VALUES (66, '删除站点', '/code/delsite/', '功能', '22028', '22028066', '删除站点');
INSERT INTO `app_rbac_permission` VALUES (67, '添加依赖', '/code/addepend/', '功能', '77029', '77029067', '添加依赖');
INSERT INTO `app_rbac_permission` VALUES (68, '修改依赖', '/code/editdepend/', '功能', '77029', '77029068', '修改依赖');
INSERT INTO `app_rbac_permission` VALUES (69, '删除依赖', '/code/deldepend/', '功能', '77029', '77029069', '删除依赖');
INSERT INTO `app_rbac_permission` VALUES (70, '添加发布', '/code/addpost/', '功能', '22030', '22030070', '添加发布');
INSERT INTO `app_rbac_permission` VALUES (71, '更新代码', '/code/upcode/', '功能', '22030', '22030071', '更新代码');
INSERT INTO `app_rbac_permission` VALUES (72, '更新记录', '/code/recordlog/', '功能', '22030', '22030072', '更新记录');
INSERT INTO `app_rbac_permission` VALUES (73, '删除站点发布', '/code/delpost/', '功能', '22030', '22030073', '删除站点发布');
INSERT INTO `app_rbac_permission` VALUES (74, '代码回滚', '/code/rollback/', '功能', '22030', '22030074', '');
INSERT INTO `app_rbac_permission` VALUES (75, '站点查询', '/code/filtersite/', '功能', '22030', '22030075', '');
INSERT INTO `app_rbac_permission` VALUES (76, '日志管理', '/log/', '一级菜单', '0', '76', 'fa fa-lg fa-book');
INSERT INTO `app_rbac_permission` VALUES (77, '系统管理', '/system/', '一级菜单', '0', '77', 'fa fa-lg fa-desktop');
INSERT INTO `app_rbac_permission` VALUES (78, 'ELK 日志', '/log/elk/', '二级菜单', '76', '76078', '');
INSERT INTO `app_rbac_permission` VALUES (79, '漏洞扫描', '/sys/nessus/', '二级菜单', '77', '77079', '');
INSERT INTO `app_rbac_permission` VALUES (80, 'webssh', '/sys/webssh/', '二级菜单', '77', '77080', '');
INSERT INTO `app_rbac_permission` VALUES (81, '系统账号', '/cmdb/loginuser/', '二级菜单', '21', '21081', '');
INSERT INTO `app_rbac_permission` VALUES (82, '上传文件', '/sys/upfile/', '功能', '77080', '77080082', '');
INSERT INTO `app_rbac_permission` VALUES (83, '下载文件', '/sys/downfile/', '功能', '77080', '77080083', '');
INSERT INTO `app_rbac_permission` VALUES (84, '执行部署', '/code/install/', '功能', '77029', '77029084', '');

-- ----------------------------
-- Table structure for app_rbac_role
-- ----------------------------
DROP TABLE IF EXISTS `app_rbac_role`;
CREATE TABLE `app_rbac_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_title` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_msg` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `role_title`(`role_title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_rbac_role
-- ----------------------------
INSERT INTO `app_rbac_role` VALUES (1, 'user', '只有查看功能');
INSERT INTO `app_rbac_role` VALUES (2, 'admin', '管理员,具有添加、审核、发布、删除内容的权限');
INSERT INTO `app_rbac_role` VALUES (3, 'administrator', '超级管理员，拥有至高无上权限');

-- ----------------------------
-- Table structure for app_rbac_role_perms
-- ----------------------------
DROP TABLE IF EXISTS `app_rbac_role_perms`;
CREATE TABLE `app_rbac_role_perms`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `app_rbac_role_perms_role_id_permission_id_7b6c8e4e_uniq`(`role_id`, `permission_id`) USING BTREE,
  INDEX `app_rbac_role_perms_permission_id_b15394d1_fk_app_rbac_`(`permission_id`) USING BTREE,
  CONSTRAINT `app_rbac_role_perms_permission_id_b15394d1_fk_app_rbac_` FOREIGN KEY (`permission_id`) REFERENCES `app_rbac_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `app_rbac_role_perms_role_id_bd0ef9f9_fk_app_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `app_rbac_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 64 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_rbac_role_perms
-- ----------------------------
INSERT INTO `app_rbac_role_perms` VALUES (1, 3, 20);
INSERT INTO `app_rbac_role_perms` VALUES (2, 3, 21);
INSERT INTO `app_rbac_role_perms` VALUES (3, 3, 22);
INSERT INTO `app_rbac_role_perms` VALUES (4, 3, 23);
INSERT INTO `app_rbac_role_perms` VALUES (5, 3, 24);
INSERT INTO `app_rbac_role_perms` VALUES (6, 3, 25);
INSERT INTO `app_rbac_role_perms` VALUES (7, 3, 26);
INSERT INTO `app_rbac_role_perms` VALUES (8, 3, 27);
INSERT INTO `app_rbac_role_perms` VALUES (9, 3, 28);
INSERT INTO `app_rbac_role_perms` VALUES (10, 3, 29);
INSERT INTO `app_rbac_role_perms` VALUES (11, 3, 30);
INSERT INTO `app_rbac_role_perms` VALUES (13, 3, 31);
INSERT INTO `app_rbac_role_perms` VALUES (14, 3, 32);
INSERT INTO `app_rbac_role_perms` VALUES (15, 3, 34);
INSERT INTO `app_rbac_role_perms` VALUES (16, 3, 35);
INSERT INTO `app_rbac_role_perms` VALUES (17, 3, 37);
INSERT INTO `app_rbac_role_perms` VALUES (18, 3, 38);
INSERT INTO `app_rbac_role_perms` VALUES (19, 3, 40);
INSERT INTO `app_rbac_role_perms` VALUES (20, 3, 41);
INSERT INTO `app_rbac_role_perms` VALUES (21, 3, 42);
INSERT INTO `app_rbac_role_perms` VALUES (22, 3, 43);
INSERT INTO `app_rbac_role_perms` VALUES (23, 3, 44);
INSERT INTO `app_rbac_role_perms` VALUES (24, 3, 45);
INSERT INTO `app_rbac_role_perms` VALUES (25, 3, 46);
INSERT INTO `app_rbac_role_perms` VALUES (26, 3, 47);
INSERT INTO `app_rbac_role_perms` VALUES (27, 3, 48);
INSERT INTO `app_rbac_role_perms` VALUES (28, 3, 49);
INSERT INTO `app_rbac_role_perms` VALUES (29, 3, 50);
INSERT INTO `app_rbac_role_perms` VALUES (30, 3, 51);
INSERT INTO `app_rbac_role_perms` VALUES (31, 3, 52);
INSERT INTO `app_rbac_role_perms` VALUES (32, 3, 53);
INSERT INTO `app_rbac_role_perms` VALUES (33, 3, 54);
INSERT INTO `app_rbac_role_perms` VALUES (34, 3, 55);
INSERT INTO `app_rbac_role_perms` VALUES (35, 3, 56);
INSERT INTO `app_rbac_role_perms` VALUES (36, 3, 57);
INSERT INTO `app_rbac_role_perms` VALUES (37, 3, 58);
INSERT INTO `app_rbac_role_perms` VALUES (38, 3, 59);
INSERT INTO `app_rbac_role_perms` VALUES (39, 3, 60);
INSERT INTO `app_rbac_role_perms` VALUES (40, 3, 61);
INSERT INTO `app_rbac_role_perms` VALUES (41, 3, 62);
INSERT INTO `app_rbac_role_perms` VALUES (42, 3, 63);
INSERT INTO `app_rbac_role_perms` VALUES (43, 3, 64);
INSERT INTO `app_rbac_role_perms` VALUES (44, 3, 65);
INSERT INTO `app_rbac_role_perms` VALUES (45, 3, 66);
INSERT INTO `app_rbac_role_perms` VALUES (46, 3, 67);
INSERT INTO `app_rbac_role_perms` VALUES (47, 3, 68);
INSERT INTO `app_rbac_role_perms` VALUES (48, 3, 69);
INSERT INTO `app_rbac_role_perms` VALUES (49, 3, 70);
INSERT INTO `app_rbac_role_perms` VALUES (50, 3, 71);
INSERT INTO `app_rbac_role_perms` VALUES (51, 3, 72);
INSERT INTO `app_rbac_role_perms` VALUES (52, 3, 73);
INSERT INTO `app_rbac_role_perms` VALUES (53, 3, 74);
INSERT INTO `app_rbac_role_perms` VALUES (54, 3, 75);
INSERT INTO `app_rbac_role_perms` VALUES (56, 3, 77);
INSERT INTO `app_rbac_role_perms` VALUES (59, 3, 80);
INSERT INTO `app_rbac_role_perms` VALUES (60, 3, 81);
INSERT INTO `app_rbac_role_perms` VALUES (61, 3, 82);
INSERT INTO `app_rbac_role_perms` VALUES (62, 3, 83);
INSERT INTO `app_rbac_role_perms` VALUES (63, 3, 84);

-- ----------------------------
-- Table structure for app_rbac_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `app_rbac_userinfo`;
CREATE TABLE `app_rbac_userinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `app_rbac_userinfo_role_id_43d09ae7_fk_app_rbac_role_id`(`role_id`) USING BTREE,
  CONSTRAINT `app_rbac_userinfo_role_id_43d09ae7_fk_app_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `app_rbac_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `app_rbac_userinfo_user_id_83046718_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of app_rbac_userinfo
-- ----------------------------
INSERT INTO `app_rbac_userinfo` VALUES (1, '13432089040', '离线', 3, 1);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 79 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add group', 2, 'add_group');
INSERT INTO `auth_permission` VALUES (5, 'Can change group', 2, 'change_group');
INSERT INTO `auth_permission` VALUES (6, 'Can delete group', 2, 'delete_group');
INSERT INTO `auth_permission` VALUES (7, 'Can add permission', 3, 'add_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can change permission', 3, 'change_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can delete permission', 3, 'delete_permission');
INSERT INTO `auth_permission` VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (19, 'Can add task', 7, 'add_taskstate');
INSERT INTO `auth_permission` VALUES (20, 'Can change task', 7, 'change_taskstate');
INSERT INTO `auth_permission` VALUES (21, 'Can delete task', 7, 'delete_taskstate');
INSERT INTO `auth_permission` VALUES (22, 'Can add worker', 8, 'add_workerstate');
INSERT INTO `auth_permission` VALUES (23, 'Can change worker', 8, 'change_workerstate');
INSERT INTO `auth_permission` VALUES (24, 'Can delete worker', 8, 'delete_workerstate');
INSERT INTO `auth_permission` VALUES (25, 'Can add periodic task', 9, 'add_periodictask');
INSERT INTO `auth_permission` VALUES (26, 'Can change periodic task', 9, 'change_periodictask');
INSERT INTO `auth_permission` VALUES (27, 'Can delete periodic task', 9, 'delete_periodictask');
INSERT INTO `auth_permission` VALUES (28, 'Can add crontab', 10, 'add_crontabschedule');
INSERT INTO `auth_permission` VALUES (29, 'Can change crontab', 10, 'change_crontabschedule');
INSERT INTO `auth_permission` VALUES (30, 'Can delete crontab', 10, 'delete_crontabschedule');
INSERT INTO `auth_permission` VALUES (31, 'Can add interval', 11, 'add_intervalschedule');
INSERT INTO `auth_permission` VALUES (32, 'Can change interval', 11, 'change_intervalschedule');
INSERT INTO `auth_permission` VALUES (33, 'Can delete interval', 11, 'delete_intervalschedule');
INSERT INTO `auth_permission` VALUES (34, 'Can add saved group result', 12, 'add_tasksetmeta');
INSERT INTO `auth_permission` VALUES (35, 'Can change saved group result', 12, 'change_tasksetmeta');
INSERT INTO `auth_permission` VALUES (36, 'Can delete saved group result', 12, 'delete_tasksetmeta');
INSERT INTO `auth_permission` VALUES (37, 'Can add task state', 13, 'add_taskmeta');
INSERT INTO `auth_permission` VALUES (38, 'Can change task state', 13, 'change_taskmeta');
INSERT INTO `auth_permission` VALUES (39, 'Can delete task state', 13, 'delete_taskmeta');
INSERT INTO `auth_permission` VALUES (40, 'Can add periodic tasks', 14, 'add_periodictasks');
INSERT INTO `auth_permission` VALUES (41, 'Can change periodic tasks', 14, 'change_periodictasks');
INSERT INTO `auth_permission` VALUES (42, 'Can delete periodic tasks', 14, 'delete_periodictasks');
INSERT INTO `auth_permission` VALUES (43, 'Can add host group', 15, 'add_hostgroup');
INSERT INTO `auth_permission` VALUES (44, 'Can change host group', 15, 'change_hostgroup');
INSERT INTO `auth_permission` VALUES (45, 'Can delete host group', 15, 'delete_hostgroup');
INSERT INTO `auth_permission` VALUES (46, 'Can add idc', 16, 'add_idc');
INSERT INTO `auth_permission` VALUES (47, 'Can change idc', 16, 'change_idc');
INSERT INTO `auth_permission` VALUES (48, 'Can delete idc', 16, 'delete_idc');
INSERT INTO `auth_permission` VALUES (49, 'Can add host info', 17, 'add_hostinfo');
INSERT INTO `auth_permission` VALUES (50, 'Can change host info', 17, 'change_hostinfo');
INSERT INTO `auth_permission` VALUES (51, 'Can delete host info', 17, 'delete_hostinfo');
INSERT INTO `auth_permission` VALUES (52, 'Can add login user', 18, 'add_loginuser');
INSERT INTO `auth_permission` VALUES (53, 'Can change login user', 18, 'change_loginuser');
INSERT INTO `auth_permission` VALUES (54, 'Can delete login user', 18, 'delete_loginuser');
INSERT INTO `auth_permission` VALUES (55, 'Can add role', 19, 'add_role');
INSERT INTO `auth_permission` VALUES (56, 'Can change role', 19, 'change_role');
INSERT INTO `auth_permission` VALUES (57, 'Can delete role', 19, 'delete_role');
INSERT INTO `auth_permission` VALUES (58, 'Can add user info', 20, 'add_userinfo');
INSERT INTO `auth_permission` VALUES (59, 'Can change user info', 20, 'change_userinfo');
INSERT INTO `auth_permission` VALUES (60, 'Can delete user info', 20, 'delete_userinfo');
INSERT INTO `auth_permission` VALUES (61, 'Can add permission', 21, 'add_permission');
INSERT INTO `auth_permission` VALUES (62, 'Can change permission', 21, 'change_permission');
INSERT INTO `auth_permission` VALUES (63, 'Can delete permission', 21, 'delete_permission');
INSERT INTO `auth_permission` VALUES (64, 'Can add project', 22, 'add_project');
INSERT INTO `auth_permission` VALUES (65, 'Can change project', 22, 'change_project');
INSERT INTO `auth_permission` VALUES (66, 'Can delete project', 22, 'delete_project');
INSERT INTO `auth_permission` VALUES (67, 'Can add site', 23, 'add_site');
INSERT INTO `auth_permission` VALUES (68, 'Can change site', 23, 'change_site');
INSERT INTO `auth_permission` VALUES (69, 'Can delete site', 23, 'delete_site');
INSERT INTO `auth_permission` VALUES (70, 'Can add depend', 24, 'add_depend');
INSERT INTO `auth_permission` VALUES (71, 'Can change depend', 24, 'change_depend');
INSERT INTO `auth_permission` VALUES (72, 'Can delete depend', 24, 'delete_depend');
INSERT INTO `auth_permission` VALUES (73, 'Can add code post', 25, 'add_codepost');
INSERT INTO `auth_permission` VALUES (74, 'Can change code post', 25, 'change_codepost');
INSERT INTO `auth_permission` VALUES (75, 'Can delete code post', 25, 'delete_codepost');
INSERT INTO `auth_permission` VALUES (76, 'Can add post record', 26, 'add_postrecord');
INSERT INTO `auth_permission` VALUES (77, 'Can change post record', 26, 'change_postrecord');
INSERT INTO `auth_permission` VALUES (78, 'Can delete post record', 26, 'delete_postrecord');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$36000$TFcmw0iJZQtO$CnayVxr3zda6xeWXdjSowRoQpktIWAP+Hrfiu1lvMSU=', '2018-07-06 15:16:07.824000', 1, 'admin', '', 'admin', '13432089040@139.com', 1, 1, '2018-06-24 09:38:36.378000');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for celery_taskmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_taskmeta`;
CREATE TABLE `celery_taskmeta`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `task_id`(`task_id`) USING BTREE,
  INDEX `celery_taskmeta_hidden_23fd02dc`(`hidden`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for celery_tasksetmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_tasksetmeta`;
CREATE TABLE `celery_tasksetmeta`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `taskset_id`(`taskset_id`) USING BTREE,
  INDEX `celery_tasksetmeta_hidden_593cfc24`(`hidden`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (15, 'app_cmdb', 'hostgroup');
INSERT INTO `django_content_type` VALUES (17, 'app_cmdb', 'hostinfo');
INSERT INTO `django_content_type` VALUES (16, 'app_cmdb', 'idc');
INSERT INTO `django_content_type` VALUES (18, 'app_cmdb', 'loginuser');
INSERT INTO `django_content_type` VALUES (25, 'app_code', 'codepost');
INSERT INTO `django_content_type` VALUES (24, 'app_code', 'depend');
INSERT INTO `django_content_type` VALUES (26, 'app_code', 'postrecord');
INSERT INTO `django_content_type` VALUES (22, 'app_code', 'project');
INSERT INTO `django_content_type` VALUES (23, 'app_code', 'site');
INSERT INTO `django_content_type` VALUES (21, 'app_rbac', 'permission');
INSERT INTO `django_content_type` VALUES (19, 'app_rbac', 'role');
INSERT INTO `django_content_type` VALUES (20, 'app_rbac', 'userinfo');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (10, 'djcelery', 'crontabschedule');
INSERT INTO `django_content_type` VALUES (11, 'djcelery', 'intervalschedule');
INSERT INTO `django_content_type` VALUES (9, 'djcelery', 'periodictask');
INSERT INTO `django_content_type` VALUES (14, 'djcelery', 'periodictasks');
INSERT INTO `django_content_type` VALUES (13, 'djcelery', 'taskmeta');
INSERT INTO `django_content_type` VALUES (12, 'djcelery', 'tasksetmeta');
INSERT INTO `django_content_type` VALUES (7, 'djcelery', 'taskstate');
INSERT INTO `django_content_type` VALUES (8, 'djcelery', 'workerstate');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-06-24 09:24:52.538000');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2018-06-24 09:24:53.344000');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2018-06-24 09:24:53.544000');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2018-06-24 09:24:53.567000');
INSERT INTO `django_migrations` VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2018-06-24 09:24:53.741000');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2018-06-24 09:24:53.813000');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0003_alter_user_email_max_length', '2018-06-24 09:24:53.911000');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0004_alter_user_username_opts', '2018-06-24 09:24:53.934000');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0005_alter_user_last_login_null', '2018-06-24 09:24:53.997000');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0006_require_contenttypes_0002', '2018-06-24 09:24:54.003000');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2018-06-24 09:24:54.031000');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0008_alter_user_username_max_length', '2018-06-24 09:24:54.122000');
INSERT INTO `django_migrations` VALUES (13, 'djcelery', '0001_initial', '2018-06-24 09:24:54.999000');
INSERT INTO `django_migrations` VALUES (14, 'sessions', '0001_initial', '2018-06-24 09:24:55.068000');
INSERT INTO `django_migrations` VALUES (15, 'app_rbac', '0001_initial', '2018-06-24 09:29:24.667000');
INSERT INTO `django_migrations` VALUES (16, 'app_cmdb', '0001_initial', '2018-06-24 09:29:25.180000');
INSERT INTO `django_migrations` VALUES (17, 'app_code', '0001_initial', '2018-06-24 09:29:25.701000');
INSERT INTO `django_migrations` VALUES (18, 'app_code', '0002_auto_20180629_0940', '2018-07-06 15:31:47.949000');
INSERT INTO `django_migrations` VALUES (19, 'app_code', '0003_remove_depend_install_form', '2018-07-06 15:31:48.028000');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('oouhin1aue6oxxou4u740l2ig0rye8s4', 'ZGQyMjNjMGU0M2M0M2Y5M2ViYWM0NzcwNGVhODNhZTUxNjMxY2YxOTp7InVzZXJuYW1lIjoiYWRtaW4iLCJtZW51X2FsbF9saXN0IjpbeyJwZXJtc19udW0iOiIyMCIsInBlcm1zX3VybCI6Ii8iLCJwZXJtc19pY29uIjoiZmEgZmEtbGcgZmEtZGFzaGJvYXJkIiwibWVudV90d28iOltdLCJwZXJtc190aXRsZSI6Ilx1OTk5Nlx1OTg3NSJ9LHsicGVybXNfbnVtIjoiMjEiLCJwZXJtc191cmwiOiIvY21kYi8iLCJwZXJtc19pY29uIjoiZmEgZmEtbGcgZmEtYmFycyIsIm1lbnVfdHdvIjpbeyJwZXJtc190aXRsZSI6IkNNREIiLCJwZXJtc191cmwiOiIvY21kYi9ob3N0aW5mby8iLCJwZXJtc19udW0iOiIyMTAyNCIsInBtZW51X2lkIjoiMjEifSx7InBlcm1zX3RpdGxlIjoiXHU0ZTNiXHU2NzNhXHU3ZWM0IiwicGVybXNfdXJsIjoiL2NtZGIvaG9zdGdyb3VwLyIsInBlcm1zX251bSI6IjIxMDI1IiwicG1lbnVfaWQiOiIyMSJ9LHsicGVybXNfdGl0bGUiOiJJREMiLCJwZXJtc191cmwiOiIvY21kYi9pZGMvIiwicGVybXNfbnVtIjoiMjEwMzUiLCJwbWVudV9pZCI6IjIxIn1dLCJwZXJtc190aXRsZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiJ9LHsicGVybXNfbnVtIjoiMjIiLCJwZXJtc191cmwiOiIvY29kZS8iLCJwZXJtc19pY29uIjoiZmEgZmEtbGcgZmEtY29kZSIsIm1lbnVfdHdvIjpbeyJwZXJtc190aXRsZSI6Ilx1OTg3OVx1NzZlZVx1N2JhMVx1NzQwNiIsInBlcm1zX3VybCI6Ii9jb2RlL3Byb2plY3QvIiwicGVybXNfbnVtIjoiMjIwMjciLCJwbWVudV9pZCI6IjIyIn0seyJwZXJtc190aXRsZSI6Ilx1N2FkOVx1NzBiOVx1N2JhMVx1NzQwNiIsInBlcm1zX3VybCI6Ii9jb2RlL3NpdGUvIiwicGVybXNfbnVtIjoiMjIwMjgiLCJwbWVudV9pZCI6IjIyIn0seyJwZXJtc190aXRsZSI6Ilx1N2FkOVx1NzBiOVx1NTNkMVx1NWUwMyIsInBlcm1zX3VybCI6Ii9jb2RlL3Bvc3Rjb2RlLyIsInBlcm1zX251bSI6IjIyMDMwIiwicG1lbnVfaWQiOiIyMiJ9XSwicGVybXNfdGl0bGUiOiJcdTUzZDFcdTVlMDNcdTdiYTFcdTc0MDYifSx7InBlcm1zX251bSI6IjIzIiwicGVybXNfdXJsIjoiL3JiYWMvIiwicGVybXNfaWNvbiI6ImZhIGZhLWxnIGZhLWFkZHJlc3MtY2FyZCIsIm1lbnVfdHdvIjpbeyJwZXJtc190aXRsZSI6Ilx1NzUyOFx1NjIzN1x1N2JhMVx1NzQwNiIsInBlcm1zX3VybCI6Ii9yYmFjL3VzZXJtZy8iLCJwZXJtc19udW0iOiIyMzAzMSIsInBtZW51X2lkIjoiMjMifSx7InBlcm1zX3RpdGxlIjoiXHU4OWQyXHU4MjcyXHU3YmExXHU3NDA2IiwicGVybXNfdXJsIjoiL3JiYWMvcm9sZS8iLCJwZXJtc19udW0iOiIyMzAzMiIsInBtZW51X2lkIjoiMjMifSx7InBlcm1zX3RpdGxlIjoiXHU2NzQzXHU5NjUwXHU3YmExXHU3NDA2IiwicGVybXNfdXJsIjoiL3JiYWMvcGVybXMvIiwicGVybXNfbnVtIjoiMjMwMzQiLCJwbWVudV9pZCI6IjIzIn1dLCJwZXJtc190aXRsZSI6Ilx1NTQwZVx1NTNmMFx1N2JhMVx1NzQwNiJ9XSwiX2F1dGhfdXNlcl9pZCI6IjEiLCJwZXJtc19saXN0IjpbIi8iLCIvY21kYi8iLCIvY29kZS8iLCIvcmJhYy8iLCIvY21kYi9ob3N0aW5mby8iLCIvY21kYi9ob3N0Z3JvdXAvIiwiL2NtZGIvYWRkaG9zdC8iLCIvY29kZS9wcm9qZWN0LyIsIi9jb2RlL3NpdGUvIiwiL2NvZGUvZGVwZW5kLyIsIi9jb2RlL3Bvc3Rjb2RlLyIsIi9yYmFjL3VzZXJtZy8iLCIvcmJhYy9yb2xlLyIsIi9yYmFjL3Blcm1zLyIsIi9jbWRiL2lkYy8iLCIvcmJhYy9hZGRwZXJtcy8iLCIvcmJhYy9lZGl0cGVybXMvIiwiL3JiYWMvZGVscGVybXMvIiwiL3JiYWMvYWRkcm9sZS8iLCIvcmJhYy9lZGl0cm9sZS8iLCIvcmJhYy9kZWxyb2xlLyIsIi9yYmFjL3JvbGVwZXJtcy8iLCIvcmJhYy9hZGRyb2xlcGVybXMvIiwiL3JiYWMvYWRkdXNlci8iLCIvcmJhYy9lZGl0dXNlci8iLCIvcmJhYy9kZWx1c2VyLyIsIi9jbWRiL2RlbGhvc3QvIiwiL2NtZGIvc3luY2hvc3QvIiwiL2NtZGIvZGV0YWlsaW5mby8iLCIvY21kYi9maWx0ZXJob3N0LyIsIi9jbWRiL2VkaXRob3N0LyIsIi9jbWRiL2V4cGNtZGIvIiwiL2NtZGIvYWRkZ3JvdXAvIiwiL2NtZGIvZWRpdGdyb3VwLyIsIi9jbWRiL2RlbGdyb3VwLyIsIi9jbWRiL2FkZGlkYy8iLCIvY21kYi9lZGl0aWRjLyJdLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjY0ZjEyZmNmNzkzOTUyYzViZTkzZGE5NzRjMGJmZjg1YWQ4NjQ1NjkifQ==', '2018-06-25 10:23:49.570000');
INSERT INTO `django_session` VALUES ('uxc76jt4cjmvzw3dgv8p0ihhylywwnfy', 'YTNlODRmYmE4Yjc3OTdkZjg3MWE2YjdkMGNiYTE5NDFjNjhiMzUwMDp7InVzZXJuYW1lIjoiYWRtaW4iLCJtZW51X2FsbF9saXN0IjpbeyJwZXJtc19udW0iOiIyMCIsInBlcm1zX3VybCI6Ii8iLCJwZXJtc190aXRsZSI6Ilx1OTk5Nlx1OTg3NSIsIm1lbnVfdHdvIjpbXSwicGVybXNfaWNvbiI6ImZhIGZhLWxnIGZhLWRhc2hib2FyZCJ9LHsicGVybXNfbnVtIjoiMjEiLCJwZXJtc191cmwiOiIvY21kYi8iLCJwZXJtc190aXRsZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsIm1lbnVfdHdvIjpbeyJwZXJtc190aXRsZSI6IkNNREIiLCJwZXJtc191cmwiOiIvY21kYi9ob3N0aW5mby8iLCJwbWVudV9pZCI6IjIxIiwicGVybXNfbnVtIjoiMjEwMjQifSx7InBlcm1zX3RpdGxlIjoiXHU0ZTNiXHU2NzNhXHU3ZWM0IiwicGVybXNfdXJsIjoiL2NtZGIvaG9zdGdyb3VwLyIsInBtZW51X2lkIjoiMjEiLCJwZXJtc19udW0iOiIyMTAyNSJ9LHsicGVybXNfdGl0bGUiOiJJREMiLCJwZXJtc191cmwiOiIvY21kYi9pZGMvIiwicG1lbnVfaWQiOiIyMSIsInBlcm1zX251bSI6IjIxMDM1In0seyJwZXJtc190aXRsZSI6Ilx1N2NmYlx1N2VkZlx1OGQyNlx1NTNmNyIsInBlcm1zX3VybCI6Ii9jbWRiL2xvZ2ludXNlci8iLCJwbWVudV9pZCI6IjIxIiwicGVybXNfbnVtIjoiMjEwODEifV0sInBlcm1zX2ljb24iOiJmYSBmYS1sZyBmYS1iYXJzIn0seyJwZXJtc19udW0iOiIyMiIsInBlcm1zX3VybCI6Ii9jb2RlLyIsInBlcm1zX3RpdGxlIjoiXHU1M2QxXHU1ZTAzXHU3YmExXHU3NDA2IiwibWVudV90d28iOlt7InBlcm1zX3RpdGxlIjoiXHU5ODc5XHU3NmVlXHU3YmExXHU3NDA2IiwicGVybXNfdXJsIjoiL2NvZGUvcHJvamVjdC8iLCJwbWVudV9pZCI6IjIyIiwicGVybXNfbnVtIjoiMjIwMjcifSx7InBlcm1zX3RpdGxlIjoiXHU3YWQ5XHU3MGI5XHU3YmExXHU3NDA2IiwicGVybXNfdXJsIjoiL2NvZGUvc2l0ZS8iLCJwbWVudV9pZCI6IjIyIiwicGVybXNfbnVtIjoiMjIwMjgifSx7InBlcm1zX3RpdGxlIjoiXHU3YWQ5XHU3MGI5XHU1M2QxXHU1ZTAzIiwicGVybXNfdXJsIjoiL2NvZGUvcG9zdGNvZGUvIiwicG1lbnVfaWQiOiIyMiIsInBlcm1zX251bSI6IjIyMDMwIn1dLCJwZXJtc19pY29uIjoiZmEgZmEtbGcgZmEtY29kZSJ9LHsicGVybXNfbnVtIjoiMjMiLCJwZXJtc191cmwiOiIvcmJhYy8iLCJwZXJtc190aXRsZSI6Ilx1NTQwZVx1NTNmMFx1N2JhMVx1NzQwNiIsIm1lbnVfdHdvIjpbeyJwZXJtc190aXRsZSI6Ilx1NzUyOFx1NjIzN1x1N2JhMVx1NzQwNiIsInBlcm1zX3VybCI6Ii9yYmFjL3VzZXJtZy8iLCJwbWVudV9pZCI6IjIzIiwicGVybXNfbnVtIjoiMjMwMzEifSx7InBlcm1zX3RpdGxlIjoiXHU4OWQyXHU4MjcyXHU3YmExXHU3NDA2IiwicGVybXNfdXJsIjoiL3JiYWMvcm9sZS8iLCJwbWVudV9pZCI6IjIzIiwicGVybXNfbnVtIjoiMjMwMzIifSx7InBlcm1zX3RpdGxlIjoiXHU2NzQzXHU5NjUwXHU3YmExXHU3NDA2IiwicGVybXNfdXJsIjoiL3JiYWMvcGVybXMvIiwicG1lbnVfaWQiOiIyMyIsInBlcm1zX251bSI6IjIzMDM0In1dLCJwZXJtc19pY29uIjoiZmEgZmEtbGcgZmEtYWRkcmVzcy1jYXJkIn0seyJwZXJtc19udW0iOiI3NyIsInBlcm1zX3VybCI6Ii9zeXN0ZW0vIiwicGVybXNfdGl0bGUiOiJcdTdjZmJcdTdlZGZcdTdiYTFcdTc0MDYiLCJtZW51X3R3byI6W3sicGVybXNfdGl0bGUiOiJcdTczYWZcdTU4ODNcdTkwZThcdTdmNzIiLCJwZXJtc191cmwiOiIvY29kZS9kZXBlbmQvIiwicG1lbnVfaWQiOiI3NyIsInBlcm1zX251bSI6Ijc3MDI5In0seyJwZXJtc190aXRsZSI6IndlYnNzaCIsInBlcm1zX3VybCI6Ii9zeXMvd2Vic3NoLyIsInBtZW51X2lkIjoiNzciLCJwZXJtc19udW0iOiI3NzA4MCJ9XSwicGVybXNfaWNvbiI6ImZhIGZhLWxnIGZhLWRlc2t0b3AifV0sIl9hdXRoX3VzZXJfaWQiOiIxIiwicGVybXNfbGlzdCI6WyIvIiwiL2NtZGIvIiwiL2NvZGUvIiwiL3JiYWMvIiwiL2NtZGIvaG9zdGluZm8vIiwiL2NtZGIvaG9zdGdyb3VwLyIsIi9jbWRiL2FkZGhvc3QvIiwiL2NvZGUvcHJvamVjdC8iLCIvY29kZS9zaXRlLyIsIi9jb2RlL2RlcGVuZC8iLCIvY29kZS9wb3N0Y29kZS8iLCIvcmJhYy91c2VybWcvIiwiL3JiYWMvcm9sZS8iLCIvcmJhYy9wZXJtcy8iLCIvY21kYi9pZGMvIiwiL3JiYWMvYWRkcGVybXMvIiwiL3JiYWMvZWRpdHBlcm1zLyIsIi9yYmFjL2RlbHBlcm1zLyIsIi9yYmFjL2FkZHJvbGUvIiwiL3JiYWMvZWRpdHJvbGUvIiwiL3JiYWMvZGVscm9sZS8iLCIvcmJhYy9yb2xlcGVybXMvIiwiL3JiYWMvYWRkcm9sZXBlcm1zLyIsIi9yYmFjL2FkZHVzZXIvIiwiL3JiYWMvZWRpdHVzZXIvIiwiL3JiYWMvZGVsdXNlci8iLCIvY21kYi9kZWxob3N0LyIsIi9jbWRiL3N5bmNob3N0LyIsIi9jbWRiL2RldGFpbGluZm8vIiwiL2NtZGIvZmlsdGVyaG9zdC8iLCIvY21kYi9lZGl0aG9zdC8iLCIvY21kYi9leHBjbWRiLyIsIi9jbWRiL2FkZGdyb3VwLyIsIi9jbWRiL2VkaXRncm91cC8iLCIvY21kYi9kZWxncm91cC8iLCIvY21kYi9hZGRpZGMvIiwiL2NtZGIvZWRpdGlkYy8iLCIvY21kYi9kZWxpZGMvIiwiL2NvZGUvYWRkcHJvamVjdC8iLCIvY29kZS9lZGl0cHJvamVjdC8iLCIvY29kZS9kZWxwcm9qZWN0LyIsIi9jb2RlL2FkZHNpdGUvIiwiL2NvZGUvZWRpdHNpdGUvIiwiL2NvZGUvZGVsc2l0ZS8iLCIvY29kZS9hZGRlcGVuZC8iLCIvY29kZS9lZGl0ZGVwZW5kLyIsIi9jb2RlL2RlbGRlcGVuZC8iLCIvY29kZS9hZGRwb3N0LyIsIi9jb2RlL3VwY29kZS8iLCIvY29kZS9yZWNvcmRsb2cvIiwiL2NvZGUvZGVscG9zdC8iLCIvY29kZS9yb2xsYmFjay8iLCIvY29kZS9maWx0ZXJzaXRlLyIsIi9zeXN0ZW0vIiwiL3N5cy93ZWJzc2gvIiwiL2NtZGIvbG9naW51c2VyLyIsIi9zeXMvdXBmaWxlLyIsIi9zeXMvZG93bmZpbGUvIiwiL2NvZGUvaW5zdGFsbC8iXSwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJ3ZWJzc2hfaW5mbyI6IntcInVzZXJuYW1lXCI6IFwicm9vdFwiLCBcInB1YmxpY2tleVwiOiBcIk5vbmVcIiwgXCJwYXNzd29yZFwiOiBcIk9uZWRheTAzMTNcIiwgXCJob3N0bmFtZVwiOiBcIjEyNy4wLjAuMVwiLCBcInBvcnRcIjogMjJ9IiwiX2F1dGhfdXNlcl9oYXNoIjoiNjRmMTJmY2Y3OTM5NTJjNWJlOTNkYTk3NGMwYmZmODVhZDg2NDU2OSJ9', '2018-07-07 15:32:47.859000');

-- ----------------------------
-- Table structure for djcelery_crontabschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_crontabschedule`;
CREATE TABLE `djcelery_crontabschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hour` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `day_of_week` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `day_of_month` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `month_of_year` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for djcelery_intervalschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_intervalschedule`;
CREATE TABLE `djcelery_intervalschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for djcelery_periodictask
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictask`;
CREATE TABLE `djcelery_periodictask`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `task` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `args` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `kwargs` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `queue` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `exchange` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `routing_key` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `expires` datetime(6) NULL DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) NULL DEFAULT NULL,
  `total_run_count` int(10) UNSIGNED NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `crontab_id` int(11) NULL DEFAULT NULL,
  `interval_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_`(`crontab_id`) USING BTREE,
  INDEX `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_`(`interval_id`) USING BTREE,
  CONSTRAINT `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_` FOREIGN KEY (`crontab_id`) REFERENCES `djcelery_crontabschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_` FOREIGN KEY (`interval_id`) REFERENCES `djcelery_intervalschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for djcelery_periodictasks
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictasks`;
CREATE TABLE `djcelery_periodictasks`  (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for djcelery_taskstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_taskstate`;
CREATE TABLE `djcelery_taskstate`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `task_id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tstamp` datetime(6) NOT NULL,
  `args` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `kwargs` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `eta` datetime(6) NULL DEFAULT NULL,
  `expires` datetime(6) NULL DEFAULT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `traceback` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `runtime` double NULL DEFAULT NULL,
  `retries` int(11) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `worker_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `task_id`(`task_id`) USING BTREE,
  INDEX `djcelery_taskstate_state_53543be4`(`state`) USING BTREE,
  INDEX `djcelery_taskstate_name_8af9eded`(`name`) USING BTREE,
  INDEX `djcelery_taskstate_tstamp_4c3f93a1`(`tstamp`) USING BTREE,
  INDEX `djcelery_taskstate_hidden_c3905e57`(`hidden`) USING BTREE,
  INDEX `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id`(`worker_id`) USING BTREE,
  CONSTRAINT `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id` FOREIGN KEY (`worker_id`) REFERENCES `djcelery_workerstate` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for djcelery_workerstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_workerstate`;
CREATE TABLE `djcelery_workerstate`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_heartbeat` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `hostname`(`hostname`) USING BTREE,
  INDEX `djcelery_workerstate_last_heartbeat_4539b544`(`last_heartbeat`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
