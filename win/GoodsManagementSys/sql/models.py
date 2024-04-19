import sqlalchemy

metadata = sqlalchemy.MetaData()
ALL_TABLE = metadata.tables

goods_base = sqlalchemy.Table(
    "goods_base",
    metadata,
    sqlalchemy.Column(
        "货物编号",
        sqlalchemy.INTEGER,
        primary_key=True,
        autoincrement=True,
        comment="货物编号",
    ),
    sqlalchemy.Column(
        "货物名称", sqlalchemy.VARCHAR(255), nullable=False, comment="货物名称"
    ),
    sqlalchemy.Column("规格", sqlalchemy.VARCHAR(255), comment="规格"),
    sqlalchemy.Column("数量", sqlalchemy.INTEGER, nullable=False, comment="数量"),
    sqlalchemy.Column("类别", sqlalchemy.VARCHAR(255), comment="类别"),
    sqlalchemy.Column("单位", sqlalchemy.VARCHAR(255), comment="单位"),
    sqlalchemy.Column("卖方", sqlalchemy.VARCHAR(255), comment="卖方"),
    sqlalchemy.Column("备注", sqlalchemy.Text, comment="备注"),
)

goods_out = sqlalchemy.Table(
    "goods_out",
    metadata,
    sqlalchemy.Column(
        "出库编号",
        sqlalchemy.INTEGER,
        primary_key=True,
        autoincrement=True,
        comment="出库编号",
    ),
    sqlalchemy.Column(
        "货物编号",
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey(goods_base.c["货物编号"]),
        nullable=False,
        comment="货物编号",
    ),
    sqlalchemy.Column(
        "货物名称", sqlalchemy.VARCHAR(255), nullable=False, comment="货物名称"
    ),
    sqlalchemy.Column("数量", sqlalchemy.INTEGER, nullable=False, comment="数量"),
    sqlalchemy.Column("日期", sqlalchemy.DateTime, nullable=False, comment="操作日期"),
)

goods_in = sqlalchemy.Table(
    "goods_in",
    metadata,
    sqlalchemy.Column(
        "入库编号",
        sqlalchemy.INTEGER,
        primary_key=True,
        autoincrement=True,
        comment="入库编号",
    ),
    sqlalchemy.Column(
        "货物编号",
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey(goods_base.c["货物编号"]),
        nullable=False,
        comment="货物编号",
    ),
    sqlalchemy.Column(
        "货物名称", sqlalchemy.VARCHAR(255), nullable=False, comment="货物名称"
    ),
    sqlalchemy.Column("数量", sqlalchemy.INTEGER, nullable=False, comment="数量"),
    sqlalchemy.Column("日期", sqlalchemy.DateTime, nullable=False, comment="操作日期"),
)
