from django.db import models


# 学生信息表
class tb_student(models.Model):
    sid = models.IntegerField(primary_key=True, null=False)  # 学号
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=20, null=True)
    bjid = models.IntegerField(null=True)


# 教师信息表
class tb_teacher(models.Model):
    tid = models.IntegerField(primary_key=True, null=False)  # 教师编号
    password = models.CharField(max_length=20, null=False)
    tname = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=20, null=True)


# 管理员信息表
class tb_admin(models.Model):
    uid = models.IntegerField(primary_key=True, null=False)  # 管理员编号
    password = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=20, null=True)


# 试卷信息表
class tb_questionpaper(models.Model):
    qpid = models.IntegerField(primary_key=True, null=False)  # 试卷编号
    qpdate = models.DateField(null=False)  # 出卷时间
    time = models.IntegerField(null=False)  # 考试时长
    tid = models.IntegerField(null=True)  # 教师id


# 试题信息表
class tb_question(models.Model):
    qid = models.IntegerField(primary_key=True, null=False)  # 试题编号
    qcontent = models.CharField(max_length=100, null=False)  # 试题内容
    aoption = models.CharField(max_length=100, null=True)  # a、b、c、d选项
    boption = models.CharField(max_length=100, null=True)
    coption = models.CharField(max_length=100, null=True)
    doption = models.CharField(max_length=100, null=True)
    ganswer = models.CharField(max_length=1, null=True)  # 试题答案
    ganalysis = models.CharField(max_length=200, null=True)  # 试题解析
    oword = models.CharField(max_length=100, null=True)  # 关键字
    gscope = models.CharField(max_length=100, null=True)  # 试题范围
    gdifficulty = models.CharField(max_length=5, null=True)  # 试题难度
    gdate = models.DateField(null=True)  # 添加日期
    gtid = models.IntegerField(null=True)  # 试题类型id
    tid = models.IntegerField(null=True)  # 教师编号


# 试题与试卷信息对应表
class tb_qprelationq(models.Model):
    rid = models.IntegerField(primary_key=True, null=False)  # 对应表id
    num = models.IntegerField(null=True)  # 试题序号
    qpid = models.IntegerField(null=False)  # 试卷id
    qid = models.IntegerField(null=False)  # 试题id


# 考场控制表
class tb_testcontrol(models.Model):
    tcid = models.IntegerField(primary_key=True, null=False)  # 考场控制表id
    state = models.IntegerField(null=True)  # 考场状态
    mode = models.IntegerField(null=False)  # 考试方式
    qpid = models.IntegerField(null=True)  # 试卷id
    tname = models.CharField(max_length=20, null=True)  # 考试名称
    tdate = models.DateField(null=True)  # 考试日期


# 考试记录表
class tb_testnote(models.Model):
    tnid = models.IntegerField(primary_key=True, null=False)  # 考试记录id
    sid = models.IntegerField(null=True)  # 学号
    qpid = models.IntegerField(null=True)  # 试卷id
    tname = models.CharField(max_length=20, null=True)  # 考试名称
    stime = models.DateField(null=True)  # 考试开始时间
    etime = models.DateField(null=True)  # 考试结束时间
    score = models.IntegerField(null=True)  # 交卷时间


# 班级信息表
class bj(models.Model):
    bjid = models.IntegerField(primary_key=True, null=False)  # 班级编号
    bjname = models.CharField(max_length=10, null=True)  # 班级名称
    tid = models.IntegerField(null=True)  # 教师编号


# 试题类型表
class questiontype(models.Model):
    qtid = models.IntegerField(primary_key=True, null=False)  # 试题类型编号
    qtname = models.CharField(max_length=10, null=True)  # 试题类型名
    score = models.IntegerField(null=True)  # 分数


# 答题情况表
class answerstate(models.Model):
    anid = models.IntegerField(primary_key=True, null=False)  # 答题情况编号
    qid = models.IntegerField(null=True)  # 试题编号
    state = models.IntegerField(null=True)  # 答题情况
    tnid = models.IntegerField(null=True)  # 试题记录编号
