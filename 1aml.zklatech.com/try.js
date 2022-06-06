!function(c) {
    function t(t) {
        for (var e, a, n = t[0], i = t[1], s = t[2], o = 0, r = []; o < n.length; o++)
            a = n[o],
            Object.prototype.hasOwnProperty.call(h, a) && h[a] && r.push(h[a][0]),
            h[a] = 0;
        for (e in i)
            Object.prototype.hasOwnProperty.call(i, e) && (c[e] = i[e]);
        for (p && p(t); r.length; )
            r.shift()();
        return d.push.apply(d, s || []),
        u()
    }
    function u() {
        for (var t, e = 0; e < d.length; e++) {
            for (var a = d[e], n = !0, i = 1; i < a.length; i++) {
                var s = a[i];
                0 !== h[s] && (n = !1)
            }
            n && (d.splice(e--, 1),
            t = m(m.s = a[0]))
        }
        return t
    }
    var a = {}
      , l = {
        app: 0
    }
      , h = {
        app: 0
    }
      , d = [];
    function m(t) {
        if (a[t])
            return a[t].exports;
        var e = a[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return c[t].call(e.exports, e, e.exports, m),
        e.l = !0,
        e.exports
    }
    m.e = function(d) {
        var t = [];
        l[d] ? t.push(l[d]) : 0 !== l[d] && {
            manifest: 1
        }[d] && t.push(l[d] = new Promise(function(t, a) {
            for (var e = "css/" + ({
                manifest: "manifest"
            }[d] || d) + "." + {
                manifest: "69732395"
            }[d] + ".css", n = m.p + e, i = document.getElementsByTagName("link"), s = 0; s < i.length; s++) {
                var o = i[s]
                  , r = o.getAttribute("data-href") || o.getAttribute("href");
                if ("stylesheet" === o.rel && (r === e || r === n))
                    return t()
            }
            for (var c = document.getElementsByTagName("style"), s = 0; s < c.length; s++)
                if ((r = (o = c[s]).getAttribute("data-href")) === e || r === n)
                    return t();
            var u = document.createElement("link");
            u.rel = "stylesheet",
            u.type = "text/css",
            u.onload = t,
            u.onerror = function(t) {
                var e = t && t.target && t.target.src || n
                  , t = new Error("Loading CSS chunk " + d + " failed.\n(" + e + ")");
                t.code = "CSS_CHUNK_LOAD_FAILED",
                t.request = e,
                delete l[d],
                u.parentNode.removeChild(u),
                a(t)
            }
            ,
            u.href = n,
            document.getElementsByTagName("head")[0].appendChild(u)
        }
        ).then(function() {
            l[d] = 0
        }));
        var n, i, e, s, a, o = h[d];
        return 0 !== o && (o ? t.push(o[2]) : (a = new Promise(function(t, e) {
            o = h[d] = [t, e]
        }
        ),
        t.push(o[2] = a),
        (n = document.createElement("script")).charset = "utf-8",
        n.timeout = 120,
        m.nc && n.setAttribute("nonce", m.nc),
        n.src = m.p + "js/" + ({
            manifest: "manifest"
        }[a = d] || a) + "." + {
            manifest: "b5848138"
        }[a] + ".js",
        i = new Error,
        e = function(t) {
            n.onerror = n.onload = null,
            clearTimeout(s);
            var e, a = h[d];
            0 !== a && (a && (e = t && ("load" === t.type ? "missing" : t.type),
            t = t && t.target && t.target.src,
            i.message = "Loading chunk " + d + " failed.\n(" + e + ": " + t + ")",
            i.name = "ChunkLoadError",
            i.type = e,
            i.request = t,
            a[1](i)),
            h[d] = void 0)
        }
        ,
        s = setTimeout(function() {
            e({
                type: "timeout",
                target: n
            })
        }, 12e4),
        n.onerror = n.onload = e,
        document.head.appendChild(n))),
        Promise.all(t)
    }
    ,
    m.m = c,
    m.c = a,
    m.d = function(t, e, a) {
        m.o(t, e) || Object.defineProperty(t, e, {
            enumerable: !0,
            get: a
        })
    }
    ,
    m.r = function(t) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }
    ,
    m.t = function(e, t) {
        if (1 & t && (e = m(e)),
        8 & t)
            return e;
        if (4 & t && "object" == typeof e && e && e.__esModule)
            return e;
        var a = Object.create(null);
        if (m.r(a),
        Object.defineProperty(a, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var n in e)
                m.d(a, n, function(t) {
                    return e[t]
                }
                .bind(null, n));
        return a
    }
    ,
    m.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t.default
        }
        : function() {
            return t
        }
        ;
        return m.d(e, "a", e),
        e
    }
    ,
    m.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }
    ,
    m.p = "/",
    m.oe = function(t) {
        throw t
    }
    ;
    var e = (n = window.webpackJsonp = window.webpackJsonp || []).push.bind(n);
    n.push = t;
    for (var n = n.slice(), i = 0; i < n.length; i++)
        t(n[i]);
    var p = e;
    d.push([0, "vendor", "styles"]),
    u()
}({
    "56d7": function(t, e, a) {
        "use strict";
        a.r(e),
        a("9f45");
        var n = a("16be")
          , i = a.n(n)
          , s = (a("a1c5"),
        a("e2fe"))
          , o = a("b2be9")
          , r = a("d4f4")
          , c = a("acb2")
          , u = {
            name: "biaozhu-common",
            data() {
                return {
                    loading: !1,
                    cb: null,
                    caseList: [],
                    soloData: {
                        address: "",
                        chainName: "",
                        chain: "",
                        remark: "",
                        method: "update"
                    },
                    showModal: !1,
                    ruleValidate: {
                        remark: [{
                            required: !0,
                            message: "标注不能为空",
                            trigger: "blur"
                        }]
                    }
                }
            },
            methods: {
                async show(t, e) {
                    this.$refs.soloData.resetFields(),
                    this.soloData = Object.assign({}, this.soloData, t),
                    this.showModal = !0,
                    this.loading = !0;
                    var a = await Object(r.b)({});
                    0 == a.status && (this.caseList = a.data.caseList || []);
                    t = {
                        address: t.address,
                        chain: t.chain
                    },
                    t = await Object(r.t)(t);
                    0 === t.status ? this.soloData.relationCids = t.data.cidList || [] : this.soloData.relationCids = [],
                    this.loading = !1,
                    this.cb = e
                },
                submit() {
                    let {address: t, remark: e, chain: a, method: n="update", relationCids: i=[]} = this.soloData;
                    const s = {
                        chain: a,
                        address: t,
                        remark: e,
                        method: n,
                        relationCids: i.join(",")
                    };
                    Object(c.a)(s).then(t=>{
                        0 === t.status && (this.showModal = !1,
                        this.$Message.success("操作成功!"),
                        this.cb && this.cb(Object.assign({}, s)))
                    }
                    )
                },
                save() {
                    this.$refs.soloData.validate(t=>{
                        t && this.submit()
                    }
                    )
                }
            }
        }
          , d = (a("a016"),
        a("cba8"))
          , l = Object(d.a)(u, function() {
            var e = this
              , t = e.$createElement
              , a = e._self._c || t;
            return a("Modal", {
                attrs: {
                    title: "标注"
                },
                model: {
                    value: e.showModal,
                    callback: function(t) {
                        e.showModal = t
                    },
                    expression: "showModal"
                }
            }, [a("div", {
                staticClass: "rel"
            }, [a("Form", {
                ref: "soloData",
                attrs: {
                    "label-position": "top",
                    model: e.soloData,
                    rules: e.ruleValidate
                }
            }, [a("FormItem", {
                attrs: {
                    label: "地址"
                }
            }, [e._v(" " + e._s(e.soloData.address) + " ")]), a("p", {
                staticClass: "modal-label-p"
            }, [a("span", [e._v("*")]), e._v(" 标注 "), a("em", [e._v("(地址的标注为私密内容，无需担心泄露敏感信息)")])]), a("FormItem", {
                attrs: {
                    label: "",
                    prop: "remark"
                }
            }, [a("Input", {
                attrs: {
                    placeholder: "请勿填写敏感信息",
                    type: "textarea",
                    autosize: {
                        minRows: 4,
                        maxRows: 5
                    }
                },
                model: {
                    value: e.soloData.remark,
                    callback: function(t) {
                        e.$set(e.soloData, "remark", t)
                    },
                    expression: "soloData.remark"
                }
            })], 1), a("FormItem", {
                directives: [{
                    name: "menu",
                    rawName: "v-menu",
                    value: "/manage/case",
                    expression: "'/manage/case'"
                }],
                attrs: {
                    label: "关联案件"
                }
            }, [a("p", {
                staticClass: "red-biaozhu"
            }, [e._v(" 提示：删除标注内容，将解除该地址与案件的关联关系 ")]), a("Select", {
                attrs: {
                    filterable: !0,
                    multiple: !0,
                    clearable: ""
                },
                model: {
                    value: e.soloData.relationCids,
                    callback: function(t) {
                        e.$set(e.soloData, "relationCids", t)
                    },
                    expression: "soloData.relationCids"
                }
            }, [e._l(e.caseList, function(t) {
                return [a("Option", {
                    key: t.id,
                    attrs: {
                        value: t.id
                    }
                }, [e._v(e._s(t.name))])]
            })], 2)], 1)], 1), e.loading ? a("Spin", {
                attrs: {
                    fix: ""
                }
            }) : e._e()], 1), a("div", {
                attrs: {
                    slot: "footer"
                },
                slot: "footer"
            }, [a("Button", {
                on: {
                    click: function(t) {
                        e.showModal = !1
                    }
                }
            }, [e._v("取消")]), a("Button", {
                attrs: {
                    type: "primary"
                },
                on: {
                    click: e.save
                }
            }, [e._v("保存")])], 1)])
        }, [], !1, null, "b00015c8", null).exports
          , h = {
            install: function(t, e) {
                const n = t.extend(l);
                let i = null;
                t.prototype.$Biaozhu = {
                    show(t, e) {
                        var a;
                        i || (i = new n,
                        a = i.$mount().$el,
                        document.body.appendChild(a)),
                        i.data = Object.assign({}, t),
                        i.show(t, e)
                    }
                }
            }
        }
          , m = a("7c98")
          , p = a.n(m)
          , f = a("388f")
          , g = {
            name: "biaozhu-common",
            data() {
                return {
                    loading: !1,
                    cb: null,
                    caseList: [],
                    soloData: {
                        address: "",
                        name: "",
                        chain: "",
                        token: "",
                        snapshot: "",
                        hasRelation: !1
                    },
                    showModal: !1,
                    ruleValidate: {
                        name: [{
                            required: !0,
                            message: "名称不能为空",
                            trigger: "blur"
                        }]
                    }
                }
            },
            methods: {
                async show(t, e) {
                    if (this.$refs.soloData.resetFields(),
                    this.soloData = Object.assign({}, this.soloData, t),
                    this.showModal = !0,
                    this.soloData.hasRelation) {
                        this.loading = !0;
                        const t = await Object(r.b)({});
                        0 == t.status && (this.caseList = t.data.caseList || []),
                        this.loading = !1
                    }
                    this.cb = e
                },
                submit() {
                    var {address: t, name: e, chain: a, token: n, snapshot: i, relationCid: s="", hasRelation: o=!1} = this.soloData;
                    const r = {
                        name: e,
                        address: t,
                        token: n,
                        chain: a,
                        snapshot: i
                    };
                    o ? (s && (r.relationCid = p.a.toInteger(s)),
                    Object(f.e)(r).then(t=>{
                        0 == t.status && (this.showModal = !1,
                        this.$Message.success("存档成功!"),
                        this.soloData = {
                            address: "",
                            name: "",
                            chain: "",
                            token: "",
                            snapshot: "",
                            hasRelation: !1
                        },
                        this.cb && this.cb(Object.assign({}, r)))
                    }
                    )) : (this.showModal = !1,
                    this.soloData = {
                        address: "",
                        name: "",
                        chain: "",
                        token: "",
                        snapshot: "",
                        hasRelation: !1
                    },
                    this.cb && this.cb(Object.assign({}, r)))
                },
                save() {
                    this.$refs.soloData.validate(t=>{
                        t && this.submit()
                    }
                    )
                },
                cancelHandle() {
                    this.soloData = {
                        address: "",
                        name: "",
                        chain: "",
                        token: "",
                        snapshot: "",
                        hasRelation: !1
                    },
                    this.showModal = !1
                }
            }
        }
          , b = (a("2384"),
        Object(d.a)(g, function() {
            var e = this
              , t = e.$createElement
              , a = e._self._c || t;
            return a("Modal", {
                model: {
                    value: e.showModal,
                    callback: function(t) {
                        e.showModal = t
                    },
                    expression: "showModal"
                }
            }, [a("p", {
                attrs: {
                    slot: "header"
                },
                slot: "header"
            }, [a("span", {
                staticClass: "header-txt"
            }, [e._v("存档名称")]), a("span", {
                staticClass: "header-txt-warn"
            }, [e._v("(存档仅保留一个月)")])]), a("div", {
                staticClass: "rel"
            }, [a("Form", {
                ref: "soloData",
                attrs: {
                    "label-position": "top",
                    model: e.soloData,
                    rules: e.ruleValidate
                }
            }, [a("FormItem", {
                attrs: {
                    label: "存档名称",
                    prop: "name"
                }
            }, [a("Input", {
                attrs: {
                    placeholder: "存档名称"
                },
                model: {
                    value: e.soloData.name,
                    callback: function(t) {
                        e.$set(e.soloData, "name", t)
                    },
                    expression: "soloData.name"
                }
            })], 1), e.soloData.hasRelation ? a("FormItem", {
                directives: [{
                    name: "menu",
                    rawName: "v-menu",
                    value: "/manage/case",
                    expression: "'/manage/case'"
                }],
                attrs: {
                    label: "关联案件"
                }
            }, [a("Select", {
                attrs: {
                    filterable: !0,
                    clearable: ""
                },
                model: {
                    value: e.soloData.relationCid,
                    callback: function(t) {
                        e.$set(e.soloData, "relationCid", t)
                    },
                    expression: "soloData.relationCid"
                }
            }, [e._l(e.caseList, function(t) {
                return [a("Option", {
                    key: t.id,
                    attrs: {
                        value: t.id
                    }
                }, [e._v(e._s(t.name))])]
            })], 2)], 1) : e._e()], 1), e.loading ? a("Spin", {
                attrs: {
                    fix: ""
                }
            }) : e._e()], 1), a("div", {
                attrs: {
                    slot: "footer"
                },
                slot: "footer"
            }, [a("Button", {
                on: {
                    click: e.cancelHandle
                }
            }, [e._v("取消")]), a("Button", {
                attrs: {
                    type: "primary"
                },
                on: {
                    click: e.save
                }
            }, [e._v("保存")])], 1)])
        }, [], !1, null, "0799406b", null)).exports
          , v = {
            install: function(t, e) {
                const n = t.extend(b);
                let i = null;
                t.prototype.$Snapshot = {
                    show(t, e) {
                        var a;
                        i || (i = new n,
                        a = i.$mount().$el,
                        document.body.appendChild(a)),
                        i.data = Object.assign({}, t),
                        i.show(t, e)
                    }
                }
            }
        }
          , y = a("430a")
          , w = {
            name: "ModalTip",
            data() {
                return {
                    tip: "提示",
                    content: "",
                    hasCancel: !1
                }
            },
            methods: {
                ok() {
                    this.onOk(),
                    this.$destroy(!0),
                    this.$el.parentNode.removeChild(this.$el)
                },
                cancel() {
                    this.onCancel(),
                    this.$destroy(!0),
                    this.$el.parentNode.removeChild(this.$el)
                }
            }
        }
          , C = (a("27aa"),
        Object(d.a)(w, function() {
            var t = this
              , e = t.$createElement
              , e = t._self._c || e;
            return e("Modal", {
                attrs: {
                    value: !0,
                    closable: !1,
                    "class-name": "modal-tip",
                    "mask-closable": !1,
                    width: "418"
                },
                on: {
                    "on-ok": t.onOk,
                    "on-cancel": t.onCancel
                }
            }, [e("div", {
                staticClass: "tip",
                attrs: {
                    slot: "header"
                },
                slot: "header"
            }, [t._v(" " + t._s(t.tip) + " ")]), e("div", {
                staticClass: "content"
            }, [t._v(" " + t._s(t.content) + " ")]), e("div", {
                attrs: {
                    slot: "footer"
                },
                slot: "footer"
            }, [t.hasCancel ? e("Button", {
                attrs: {
                    type: "text"
                },
                on: {
                    click: t.cancel
                }
            }, [t._v("取消")]) : t._e(), e("Button", {
                attrs: {
                    type: "primary"
                },
                on: {
                    click: t.ok
                }
            }, [t._v("确定")])], 1)])
        }, [], !1, null, "76f8d942", null)).exports;
        let x, k = y.default.extend(C);
        function T(t={}) {
            x = new k({
                data: {
                    onOk: ()=>{}
                    ,
                    onCancel: ()=>{}
                    ,
                    ...t
                }
            }),
            document.body.appendChild(x.$mount().$el)
        }
        function S(t, e) {
            this.modulus = new M.a(P.encode(t),16),
            this.encryptionExponent = new M.a(P.encode(e),16)
        }
        function O(t) {
            this.error = !1,
            this.parse = function(t) {
                if (!t)
                    return this.error = !0,
                    null;
                for (var e = []; 0 < t.length; ) {
                    var a = t.charCodeAt(0);
                    t = t.substr(1);
                    var n = 0;
                    if (5 == (31 & a))
                        t = t.substr(1);
                    else if (128 & t.charCodeAt(0)) {
                        var i = 127 & t.charCodeAt(0);
                        if (t = t.substr(1),
                        0 < i && (n = t.charCodeAt(0)),
                        1 < i && (n = n << 8 | t.charCodeAt(1)),
                        2 < i)
                            return this.error = !0,
                            null;
                        t = t.substr(i)
                    } else
                        n = t.charCodeAt(0),
                        t = t.substr(1);
                    i = "";
                    if (n) {
                        if (n > t.length)
                            return this.error = !0,
                            null;
                        i = t.substr(0, n),
                        t = t.substr(n)
                    }
                    32 & a ? e.push(this.parse(i)) : e.push(this.value(128 & a ? 4 : 31 & a, i))
                }
                return e
            }
            ,
            this.value = function(t, e) {
                if (1 == t)
                    return !!e;
                if (2 == t)
                    return e;
                if (3 == t)
                    return this.parse(e.substr(1));
                if (5 == t)
                    return null;
                if (6 != t)
                    return null;
                var a = []
                  , t = e.charCodeAt(0);
                a.push(Math.floor(t / 40)),
                a.push(t - 40 * a[0]);
                for (var n = [], i = 0, s = 1; s < e.length; s++) {
                    var o = e.charCodeAt(s);
                    if (n.push(127 & o),
                    128 & o)
                        i++;
                    else {
                        for (var r = 0, c = 0; c < n.length; c++)
                            r += n[c] * Math.pow(128, i--);
                        a.push(r),
                        i = 0,
                        n = []
                    }
                }
                return a.join(".")
            }
            ,
            this.data = this.parse(t)
        }
        var D = a("3786")
          , e = {
            name: "App",
            components: {},
            methods: {
                async updateDiff() {
                    const t = await Object(D.e)({});
                    var e = new Date(t.time.replace(/-/g, "/")) - new Date;
                    localStorage.setItem("diff-time", e)
                }
            },
            mounted() {
                this.updateDiff()
            }
        }
          , A = (a("034f"),
        Object(d.a)(e, function() {
            var t = this.$createElement
              , t = this._self._c || t;
            return t("div", {
                attrs: {
                    id: "app"
                }
            }, [t("router-view")], 1)
        }, [], !1, null, null, null)).exports
          , L = a("4062")
          , n = a.n(L)
          , u = a("ac56")
          , m = a("82ae")
          , I = a.n(m)
          , j = a("3191")
          , g = {
            name: "HeaderBar",
            rotateIcon() {
                return ["menu-3icon_", this.isCollapsed ? "rotate-3icon_" : ""]
            },
            data() {
                return {
                    ruleForm: {
                        password: "",
                        pass: "",
                        checkPass: ""
                    },
                    rules: {
                        pass: [{
                            validator: (t,e,a)=>{
                                "" === e ? a(new Error("请输入密码")) : e.length < 6 ? a(new Error("密码长度6 - 20 字符")) : ("" !== this.ruleForm.checkPass && this.$refs.ruleForm.validateField("checkPass"),
                                a())
                            }
                            ,
                            trigger: "blur"
                        }],
                        checkPass: [{
                            validator: (t,e,a)=>{
                                "" === e ? a(new Error("请再次输入密码")) : e !== this.ruleForm.pass ? a(new Error("两次输入密码不一致!")) : a()
                            }
                            ,
                            trigger: "blur"
                        }]
                    },
                    loading: !1,
                    FormVisible: !1,
                    Username: ""
                }
            },
            mounted() {
                this.Username = localStorage.getItem("Username")
            },
            methods: {
                userOption(t) {
                    this[t] && this[t]()
                },
                alterUser() {
                    this.ruleForm = {
                        password: "",
                        pass: "",
                        checkPass: ""
                    },
                    this.FormVisible = !0
                },
                async loginOut() {
                    await Object(j.c)({}),
                    Object(s.c)(),
                    this.$store.commit("auth/delInfo"),
                    this.$router.push("/login?redirect=" + this.$route.fullPath)
                },
                submitForm(t) {
                    this.$refs[t].validate(t=>{
                        if (!t)
                            return !1;
                        t = this.ruleForm;
                        I.a.post("/api/auth/resetPwd", {
                            oldPwd: t.password,
                            newPwd: t.pass
                        }).then(t=>{
                            0 === t.status ? (Object(s.d)(t.data.jwt_token),
                            this.loading = !1,
                            this.FormVisible = !1,
                            this.$Message.success("密码修改成功")) : this.loading = !1
                        }
                        ).catch(t=>{
                            this.loading = !1
                        }
                        )
                    }
                    )
                },
                resetForm(t) {
                    this.$refs[t].resetFields()
                }
            }
        }
          , w = (a("c537"),
        Object(d.a)(g, function() {
            var e = this
              , t = e.$createElement
              , t = e._self._c || t;
            return t("div", {
                staticClass: "wrapper-header dflex"
            }, [e._t("default"), "changzhou" === e.$cityEnv ? t("div", {
                staticClass: "user-pannel"
            }, [t("Dropdown", {
                attrs: {
                    trigger: "click",
                    placement: "bottom-end"
                },
                on: {
                    "on-click": e.userOption
                }
            }, [t("a", {
                attrs: {
                    href: "javascript:void(0)"
                }
            }, [t("Icon", {
                attrs: {
                    type: "md-contact",
                    size: "32",
                    color: "#6C5EF6"
                }
            })], 1), t("DropdownMenu", {
                attrs: {
                    slot: "list"
                },
                slot: "list"
            }, [t("DropdownItem", {
                attrs: {
                    name: "alterUser"
                }
            }, [e._v("修改密码")]), t("DropdownItem", {
                attrs: {
                    name: "loginOut"
                }
            }, [e._v("退出登录")])], 1)], 1)], 1) : t("div", {
                staticClass: "user-close"
            }, [t("div", {
                staticClass: "box",
                on: {
                    click: e.loginOut
                }
            }, [t("i", {
                staticClass: "iconfont"
            }, [e._v("")]), e._v(" "), t("span", [e._v("退出登录")])])]), t("Modal", {
                attrs: {
                    title: "修改密码",
                    width: "40%"
                },
                model: {
                    value: e.FormVisible,
                    callback: function(t) {
                        e.FormVisible = t
                    },
                    expression: "FormVisible"
                }
            }, [t("Form", {
                ref: "ruleForm",
                attrs: {
                    model: e.ruleForm,
                    "status-icon": "",
                    rules: e.rules
                }
            }, [t("FormItem", {
                attrs: {
                    label: "原密码"
                }
            }, [t("Input", {
                attrs: {
                    type: "password",
                    autocomplete: "off"
                },
                model: {
                    value: e.ruleForm.password,
                    callback: function(t) {
                        e.$set(e.ruleForm, "password", t)
                    },
                    expression: "ruleForm.password"
                }
            })], 1), t("FormItem", {
                attrs: {
                    label: "密码",
                    prop: "pass"
                }
            }, [t("Input", {
                attrs: {
                    type: "password",
                    autocomplete: "off"
                },
                model: {
                    value: e.ruleForm.pass,
                    callback: function(t) {
                        e.$set(e.ruleForm, "pass", t)
                    },
                    expression: "ruleForm.pass"
                }
            })], 1), t("FormItem", {
                attrs: {
                    label: "确认密码",
                    prop: "checkPass"
                }
            }, [t("Input", {
                attrs: {
                    type: "password",
                    autocomplete: "off"
                },
                model: {
                    value: e.ruleForm.checkPass,
                    callback: function(t) {
                        e.$set(e.ruleForm, "checkPass", t)
                    },
                    expression: "ruleForm.checkPass"
                }
            })], 1)], 1), t("div", {
                attrs: {
                    slot: "footer"
                },
                slot: "footer"
            }, [t("Button", {
                attrs: {
                    type: "primary",
                    loading: e.loading
                },
                on: {
                    click: function(t) {
                        return e.submitForm("ruleForm")
                    }
                }
            }, [e._v("提交")]), t("Button", {
                on: {
                    click: function(t) {
                        return e.resetForm("ruleForm")
                    }
                }
            }, [e._v("重置")])], 1)], 1)], 2)
        }, [], !1, null, "133f61c0", null)).exports
          , U = a("64ad")
          , C = {
            name: "MenuPanel",
            props: {
                menuFullList: {
                    type: Array
                },
                isCollapsed: {
                    type: Boolean,
                    default: !1
                }
            },
            data() {
                return {
                    menuName: "",
                    hoverstatus: !1,
                    seletedMenu: null,
                    subMenu: []
                }
            },
            computed: {
                currentRouter() {
                    return this.$route.path
                },
                menuitemClasses: function() {
                    return ["menu-item", this.isCollapsed ? "collapsed-menu" : ""]
                },
                openNames() {
                    let e = [];
                    return this.isCollapsed ? this.menuFullList.forEach(t=>{
                        t.only && e.push(t.name)
                    }
                    ) : e = this.menuFullList.map(t=>t.name),
                    e
                }
            },
            watch: {
                isCollapsed(t) {
                    this.$nextTick(()=>{
                        this.$refs.side_menu.updateOpened()
                    }
                    )
                },
                $route: {
                    handler(a) {
                        this.$nextTick(()=>{
                            const e = a.path;
                            if (e && "/" != e) {
                                let t = a.meta.selectMenu || e.substring(1);
                                setTimeout(()=>{
                                    this.seletedMenu = t
                                }
                                , 100)
                            }
                        }
                        )
                    },
                    deep: !0,
                    immediate: !0
                }
            },
            methods: {
                mouseEnter(t, e, a) {
                    if (!this.isCollapsed)
                        return !1;
                    if (a) {
                        this.subMenu = [],
                        this.menuName = e.name;
                        const a = t.target.getBoundingClientRect().top;
                        return this.$refs.submenu.style.top = a - 2 + "px",
                        void this.stopHoverClose()
                    }
                    this.menuName = "";
                    t = t.target.getBoundingClientRect().top;
                    this.$refs.submenu.style.top = t - 14 + "px";
                    t = this.menuFullList.find(t=>t.id == e.id);
                    this.subMenu = [...t.subList],
                    this.stopHoverClose()
                },
                stopHoverClose() {
                    this.hoverstatus = !0,
                    clearTimeout(this.timer)
                },
                clseHoverstatus() {
                    this.timer = setTimeout(()=>{
                        this.hoverstatus = !1
                    }
                    , 300)
                },
                setOpenName(e) {
                    for (let t = 0; t < this.menuFullList.length; t++) {
                        const a = this.menuFullList[t]
                          , n = a.subList.find(t=>t.url === e);
                        if (n) {
                            a.only ? this.openNames = [] : this.openNames = [a.name];
                            break
                        }
                    }
                },
                jumpTo(t) {
                    this.$emit("choose-menu", t)
                },
                gotoMenu(t) {
                    t = this.getMenuByKey(this.menuFullList, t, "id");
                    this.$emit("choose-menu", t)
                },
                getMenuByKey(e, a, n) {
                    for (let t = 0; t < e.length; t++) {
                        var i = e[t];
                        if (i[n] === a)
                            return i;
                        if (i.subList && 0 < i.subList.length) {
                            i = this.getMenuByKey(i.subList, a, n);
                            if (i)
                                return i
                        }
                    }
                },
                getMenuBySub(e, a) {
                    for (let t = 0; t < e.length; t++) {
                        var n = e[t];
                        if (n.id === a)
                            return n;
                        if (n.subList && 0 < n.subList.length)
                            if (this.getMenuBySub(n.subList, a))
                                return n
                    }
                }
            },
            mounted() {
                U.a.$on("change-gotoMenu", t=>{
                    this.seletedMenu = t,
                    this.gotoMenu(t)
                }
                )
            },
            destroyed() {
                U.a.$off("change-gotoMenu")
            }
        }
          , e = (a("8f10"),
        Object(d.a)(C, function() {
            var a = this
              , t = a.$createElement
              , n = a._self._c || t;
            return n("div", {
                ref: "menuMain",
                staticClass: "menu-main"
            }, [n("Menu", {
                ref: "side_menu",
                staticClass: "menu-style",
                class: a.menuitemClasses,
                attrs: {
                    "active-name": a.seletedMenu,
                    theme: "dark",
                    width: "100%",
                    "open-names": a.openNames
                },
                on: {
                    "on-select": a.gotoMenu
                }
            }, [a._l(a.menuFullList, function(e) {
                return [[e.show ? n("Submenu", {
                    key: e.id,
                    staticStyle: {
                        position: "relative"
                    },
                    attrs: {
                        name: e.name,
                        hide: e.only
                    }
                }, [e.name ? n("template", {
                    slot: "title"
                }, [n("div", {
                    staticClass: "hover-menu",
                    on: {
                        mouseleave: a.clseHoverstatus,
                        mouseenter: function(t) {
                            return a.mouseEnter(t, e)
                        }
                    }
                }, [n("Icon", {
                    staticClass: "mr20",
                    attrs: {
                        custom: e.icon,
                        size: "24"
                    }
                }), n("span", [a._v(" " + a._s(e.name))])], 1)]) : a._e(), a._l(e.subList, function(e) {
                    return n("div", {
                        key: e.id,
                        staticClass: "event-div",
                        on: {
                            mouseleave: a.clseHoverstatus,
                            mouseenter: function(t) {
                                return a.mouseEnter(t, e, 1)
                            }
                        }
                    }, [n("MenuItem", {
                        attrs: {
                            name: e.id,
                            tipName: e.name
                        }
                    }, [n("div", {
                        staticClass: "dflex"
                    }, [e.customIcon ? n("div", [n("Icon", {
                        staticClass: "mr20",
                        attrs: {
                            custom: e.icon,
                            size: "24"
                        }
                    })], 1) : n("div", [n("Icon", {
                        staticClass: "mr20",
                        attrs: {
                            type: e.icon,
                            size: "24"
                        }
                    })], 1), n("div", {
                        staticClass: "menu-name"
                    }, [a._v(a._s(e.name))]), n("div", {
                        staticClass: "flex-grow"
                    })])])], 1)
                })], 2) : a._e()]]
            })], 2), n("div", {
                directives: [{
                    name: "show",
                    rawName: "v-show",
                    value: a.isCollapsed && a.hoverstatus,
                    expression: "isCollapsed && hoverstatus"
                }],
                ref: "submenu",
                staticClass: "close-menu",
                on: {
                    mouseleave: a.clseHoverstatus,
                    mouseenter: a.stopHoverClose
                }
            }, [0 < a.subMenu.length ? n("ul", [a._l(a.subMenu, function(e) {
                return [n("li", {
                    key: e.url,
                    class: {
                        currentRouter: a.currentRouter === e.url
                    },
                    on: {
                        click: function(t) {
                            return a.jumpTo(e)
                        }
                    }
                }, [n("div", {
                    staticClass: "menu-wrap"
                }, [e.customIcon ? n("Icon", {
                    staticClass: "mr10",
                    attrs: {
                        custom: e.icon,
                        size: "24"
                    }
                }) : n("Icon", {
                    staticClass: "mr10",
                    attrs: {
                        type: e.icon,
                        size: "24"
                    }
                }), n("span", [a._v(" " + a._s(e.name))])], 1)])]
            })], 2) : n("div", {
                staticClass: "solo-menu-tip"
            }, [a._v(" " + a._s(a.menuName) + " ")])])], 1)
        }, [], !1, null, "6059fa82", null)).exports
          , m = {
            name: "Breadcrumb",
            data() {
                return {
                    breadcrumb: []
                }
            },
            methods: {
                goBack() {
                    this.breadcrumb[0].url ? this.$router.push({
                        path: this.breadcrumb[0].url,
                        query: this.breadcrumb[0].param || {}
                    }) : this.$router.go(-1)
                }
            },
            mounted() {
                U.a.$on("change-breadcrumb", t=>{
                    this.breadcrumb = t
                }
                )
            },
            beforeDestroy() {
                U.a.$off("change-breadcrumb")
            }
        }
          , g = (a("8177"),
        Object(d.a)(m, function() {
            var t = this
              , e = t.$createElement
              , e = t._self._c || e;
            return t.breadcrumb ? e("div", {
                staticClass: "breadcrumb"
            }, [t.breadcrumb.length && 1 < t.breadcrumb.length ? [e("p", {
                staticClass: "first"
            }, [t._v(t._s(t.breadcrumb[0].name))]), Object.prototype.hasOwnProperty.call(t.breadcrumb[0], "icon") ? [e("i", {
                staticClass: "iconfont back-3icon_ goBack",
                on: {
                    click: t.goBack
                }
            }, [t._v("")])] : [e("Icon", {
                staticClass: "back-3icon_",
                attrs: {
                    type: "md-arrow-back",
                    size: "24",
                    color: "rgba(23,35,61,0.55)"
                },
                on: {
                    click: t.goBack
                }
            })], e("span", {
                staticClass: "now-label"
            }, [t._v(t._s(t.breadcrumb[1] && t.breadcrumb[1].name))])] : [e("span", {
                staticClass: "now-label"
            }, [t._v(t._s(t.breadcrumb[0] && t.breadcrumb[0].name))])]], 2) : t._e()
        }, [], !1, null, "5df19e5f", null)).exports
          , B = [{
            id: "case",
            name: "案件管理",
            icon: "iconfont iconic_toc_px",
            only: !0,
            subList: [{
                id: "manage/case",
                name: "案件管理",
                customIcon: !0,
                icon: "iconfont iconic_toc_px",
                url: "/manage/case"
            }]
        }, {
            id: "addressAnalysic",
            name: "地址研判",
            only: !0,
            customIcon: !0,
            icon: "iconfont icona-dizhiyanpanyanpan",
            subList: [{
                id: "manage/address-analysic",
                name: "地址研判",
                customIcon: !0,
                icon: "iconfont icona-dizhiyanpanyanpan",
                url: "/manage/address-analysic"
            }]
        }, {
            id: "surveyAssist",
            name: "调证协助",
            customIcon: !0,
            icon: "iconfont icontiaozhengxiezhu",
            only: !0,
            subList: [{
                id: "manage/survey-assist",
                name: "调证协助",
                customIcon: !0,
                icon: "iconfont icontiaozhengxiezhu",
                url: "/manage/survey-assist"
            }]
        }, {
            id: "commonTools",
            name: "通用研判工具",
            customIcon: !0,
            icon: "iconfont icontongyongyanpangongju",
            subList: [{
                id: "manage/transaction-details",
                name: "交易流水",
                customIcon: !0,
                icon: "iconfont iconjiaoyiliushui3",
                url: "/manage/transaction-details"
            }, {
                id: "manage/address-liulanqi",
                name: "区块链浏览器",
                customIcon: !0,
                icon: "iconfont iconqukuailianliulanqi",
                url: "/manage/address-liulanqi"
            }, {
                id: "manage/token-query",
                name: "代币查询",
                customIcon: !0,
                icon: "iconfont icondaibichaxun1",
                url: "/manage/token-query"
            }, {
                id: "manage/address-monitor",
                name: "地址监控",
                customIcon: !0,
                icon: "iconfont icondizhijiankong",
                url: "/manage/address-monitor"
            }]
        }, {
            id: "deepTools",
            name: "深度研判工具",
            customIcon: !0,
            icon: "iconfont iconshenduyanpangongju",
            subList: [{
                id: "manage/multidimen-address",
                name: "地址研判Pro",
                customIcon: !0,
                icon: "iconfont icondizhiyanpanPro",
                url: "/manage/multidimen-address"
            }, {
                id: "manage/address-opacity",
                name: "地址全息档案",
                customIcon: !0,
                icon: "iconfont icondizhiquanxidangan",
                url: "/manage/address-opacity"
            }, {
                id: "manage/address-relation",
                name: "地址关联分析",
                icon: "md-git-merge",
                url: "/manage/address-relation"
            }, {
                id: "manage/trade-water-index",
                name: "交易流水可视化",
                customIcon: !0,
                icon: "iconfont iconjiaoyiliushuikeshihua1",
                url: "/manage/trade-water-index"
            }, {
                id: "manage/nbmoney",
                name: "反洗钱交易匹配",
                customIcon: !0,
                icon: "iconfont iconfanxiqianjiaoyipipei1",
                url: "/manage/nbmoney"
            }, {
                id: "manage/relation-analysis",
                name: "关系图谱",
                customIcon: !0,
                icon: "iconfont iconguanxitupu1",
                url: "/manage/relation-analysis"
            }]
        }, {
            id: "btcTools",
            name: "比特币研判工具",
            customIcon: !0,
            icon: "iconfont iconbitebiyanpangongju",
            subList: [{
                id: "manage/transactional-analysis",
                name: "比特币交易分析",
                customIcon: !0,
                icon: "iconfont icondizhijiaoyifenxi",
                url: "/manage/transactional-analysis"
            }]
        }, {
            id: "industryData",
            name: "行业数据",
            customIcon: !0,
            icon: "iconfont iconhangyeshuju",
            subList: [{
                id: "manage/xunibi",
                name: "虚拟币数据",
                customIcon: !0,
                icon: "iconfont iconxunibishuju",
                url: "/manage/xunibi"
            }, {
                id: "manage/exchange",
                name: "交易所数据",
                customIcon: !0,
                icon: "iconfont iconjiaoyisuoshuju",
                url: "/manage/exchange"
            }, {
                id: "manage/richlist",
                name: "富豪榜",
                customIcon: !0,
                icon: "iconfont iconfuhaobang",
                url: "/manage/richlist"
            }, {
                id: "manage/bigtrade",
                name: "大额交易",
                customIcon: !0,
                icon: "iconfont icondaejiaoyi",
                url: "/manage/bigtrade"
            }]
        }, {
            id: "toolsbox",
            name: "百宝箱",
            only: !0,
            customIcon: !0,
            icon: "iconfont iconbaibaoxiang",
            subList: [{
                id: "manage/tool-box",
                name: "百宝箱",
                customIcon: !0,
                icon: "iconfont iconbaibaoxiang",
                url: "/manage/tool-box"
            }]
        }, {
            id: "ziliaoku",
            name: "资料库",
            customIcon: !0,
            icon: "iconfont iconziliaoku",
            subList: [{
                id: "manage/material",
                name: "判例库",
                customIcon: !0,
                icon: "iconfont iconpanliku",
                url: "/manage/material"
            }, {
                id: "manage/indictment",
                name: "起诉书",
                customIcon: !0,
                icon: "iconfont iconqisushuku",
                url: "/manage/indictment"
            }, {
                id: "manage/policy",
                name: "政策法规",
                customIcon: !0,
                icon: "iconfont iconzhengcefagui",
                url: "/manage/policy"
            }]
        }, {
            id: "xiansuoku",
            name: "线索库",
            customIcon: !0,
            icon: "iconfont iconxiansuoku",
            subList: [{
                id: "manage/clue",
                name: "舆情线索",
                customIcon: !0,
                icon: "iconfont iconhuaban",
                url: "/manage/clue"
            }, {
                id: "manage/clue-submit",
                name: "线索提交",
                customIcon: !0,
                icon: "iconfont iconshangchuan",
                url: "/manage/clue-submit"
            }]
        }, {
            id: "personcenter",
            name: "个人中心",
            customIcon: !0,
            icon: "iconfont icongerenzhongxin",
            subList: [{
                id: "manage/address-tag",
                name: "地址标注",
                icon: "3icon_ iconfont iconic_room_px",
                customIcon: !0,
                url: "/manage/address-tag"
            }, {
                id: "manage/help",
                name: "帮助",
                icon: "md-help-circle",
                url: "/manage/help"
            }]
        }]
          , _ = a("93a0")
          , C = {
            name: "Navigation",
            components: {
                HeaderBar: w,
                MenuPanel: e,
                Breadcrumb: g
            },
            computed: {
                rotateIcon() {
                    return ["menu-3icon_", this.isCollapsed ? "rotate-3icon_" : ""]
                },
                nodePower() {
                    return this.$store.state.auth.groupConfig && this.$store.state.auth.groupConfig.nodePower || []
                }
            },
            watch: {
                nodePower: {
                    handler() {
                        this.authMenu()
                    },
                    deep: !0,
                    immediate: !0
                }
            },
            data() {
                return {
                    personServiceFlag: !1,
                    layoutList: [],
                    menuFullList: [],
                    layoutId: null,
                    menuShow: !0,
                    breadcrumbData: [],
                    isCollapsed: !1,
                    qrCodeImg: a("5506")
                }
            },
            methods: {
                onClickGo(t) {
                    this.$router.push({
                        path: t
                    })
                },
                goEntrance() {
                    this.$router.push("/home")
                },
                chooseMenu(t) {
                    this.$router.push({
                        path: t.url,
                        query: {}
                    })
                },
                collapsedSider() {
                    this.$refs.side.toggleCollapse()
                },
                closePersonService() {
                    this.personServiceFlag = !1
                },
                authMenu() {
                    this.cityEnv,
                    B.forEach(t=>{
                        t.show = !0
                    }
                    );
                    let t = Object(_.a)(B);
                    const n = [...this.nodePower];
                    t.forEach(t=>{
                        let a = [];
                        const e = [...t.subList];
                        e.forEach(e=>{
                            n.find(t=>t === e.url) && a.push(e)
                        }
                        ),
                        0 === a.length && (t.show = !1),
                        t.subList = [...a]
                    }
                    ),
                    this.menuFullList = t
                }
            },
            mounted() {
                window.addEventListener("click", this.closePersonService, !1)
            },
            beforeDestroy() {
                window.removeEventListener("click", this.closePersonService)
            }
        }
          , m = (a("ee7c"),
        Object(d.a)(C, function() {
            var e = this
              , t = e.$createElement
              , t = e._self._c || t;
            return t("div", {
                staticClass: "chart-full"
            }, [t("Layout", {
                style: {
                    minHeight: "100vh"
                }
            }, [t("Sider", {
                ref: "side",
                staticClass: "ovh",
                attrs: {
                    collapsible: "",
                    "hide-trigger": "",
                    width: "256",
                    "collapsed-width": 78
                },
                model: {
                    value: e.isCollapsed,
                    callback: function(t) {
                        e.isCollapsed = t
                    },
                    expression: "isCollapsed"
                }
            }, ["changzhou" === e.$cityEnv ? [t("div", {
                class: {
                    "changzhou-logo-open": !e.isCollapsed,
                    "changzhou-logo-close": e.isCollapsed
                },
                on: {
                    click: e.goEntrance
                }
            })] : [t("div", {
                staticClass: "top-logo-item",
                on: {
                    click: e.goEntrance
                }
            }, [t("div", {
                staticClass: "logo"
            }), t("div", {
                staticClass: "logo-text",
                style: {
                    display: e.isCollapsed ? "none" : "inline-block"
                }
            }, [t("p", [e._v("中科链安")]), e._v(" 无匿·虚拟货币犯罪预警追踪 ")])])], e.menuShow ? t("menu-panel", {
                ref: "menuRef",
                attrs: {
                    isCollapsed: e.isCollapsed,
                    menuFullList: e.menuFullList
                },
                on: {
                    "choose-menu": e.chooseMenu
                }
            }) : e._e()], 2), t("Layout", [t("header-bar", [t("div", {
                staticClass: "menu-btn"
            }, [t("Icon", {
                staticClass: "pointer",
                class: e.rotateIcon,
                style: {
                    margin: "0 20px"
                },
                attrs: {
                    type: "md-menu",
                    size: "24"
                },
                nativeOn: {
                    click: function(t) {
                        return e.collapsedSider.apply(null, arguments)
                    }
                }
            })], 1), "changzhou" === e.$cityEnv ? t("div", {
                staticClass: "person-service",
                on: {
                    click: function(t) {
                        t.stopPropagation(),
                        e.personServiceFlag = !e.personServiceFlag
                    }
                }
            }, [e._v(" 专家支持 ")]) : t("div", {
                staticClass: "user-bar"
            }, [t("div", {
                staticClass: "user-bar-service mr25"
            }, [t("div", {
                staticClass: "user-bar-service-box",
                on: {
                    click: function(t) {
                        return e.onClickGo("/manage/platform")
                    }
                }
            }, [t("i", {
                staticClass: "iconfont"
            }, [e._v("")]), e._v(" "), t("span", [e._v("平台服务")])])]), t("div", {
                staticClass: "user-bar-service"
            }, [t("div", {
                staticClass: "user-bar-service-box",
                on: {
                    click: function(t) {
                        t.stopPropagation(),
                        e.personServiceFlag = !e.personServiceFlag
                    }
                }
            }, [t("i", {
                staticClass: "iconfont"
            }, [e._v("")]), e._v(" "), t("span", [e._v("专家支持")])])])]), t("transition", {
                attrs: {
                    name: "fadeInDown"
                }
            }, [t("div", {
                directives: [{
                    name: "show",
                    rawName: "v-show",
                    value: e.personServiceFlag,
                    expression: "personServiceFlag"
                }],
                staticClass: "person-service-info",
                on: {
                    click: function(t) {
                        t.stopPropagation(),
                        e.personServiceFlag = !0
                    }
                }
            }, [t("div", {
                staticClass: "email"
            }, [t("Icon", {
                attrs: {
                    custom: "iconfont iconEmail",
                    size: "20",
                    color: "rgba(23,35,61,0.55)"
                }
            })], 1), t("p", {
                staticClass: "light"
            }, [e._v("邮箱联络")]), t("p", {
                staticClass: "dark"
            }, [e._v("service@zklatech.com")]), t("div", {
                staticClass: "weixin"
            }, [t("Icon", {
                attrs: {
                    custom: "iconfont iconweixin",
                    size: "20",
                    color: "#2FB676"
                }
            })], 1), t("p", {
                staticClass: "light"
            }, [e._v("扫码添加微信")]), t("img", {
                attrs: {
                    src: e.qrCodeImg,
                    width: "100",
                    height: "100"
                }
            })])])], 1), t("breadcrumb"), t("Content", {
                staticClass: "content-wrapper"
            }, [t("router-view")], 1)], 1)], 1)], 1)
        }, [], !1, null, "1a9b457f", null)).exports
          , w = {
            name: "BlankView",
            components: {
                Breadcrumb: g
            },
            computed: {},
            data() {
                return {
                    layoutList: [],
                    layoutId: null,
                    breadcrumbData: []
                }
            },
            methods: {
                goEntrance() {
                    this.$router.push("/entrance")
                }
            }
        }
          , e = (a("54d1"),
        Object(d.a)(w, function() {
            var t = this.$createElement
              , t = this._self._c || t;
            return t("div", {
                staticClass: "chart-full"
            }, [t("Layout", {
                style: {
                    minHeight: "100vh"
                }
            }, [t("Layout", [t("breadcrumb"), t("Content", {
                staticClass: "content-wrapper"
            }, [t("router-view")], 1)], 1)], 1)], 1)
        }, [], !1, null, "c13992f2", null)).exports
          , C = [{
            path: "case",
            meta: {
                title: "案件管理",
                auth: "/manage/case"
            },
            component: ()=>a.e("manifest").then(a.bind(null, "6c64"))
        }, {
            meta: {
                title: "案件管理",
                selectMenu: "manage/case",
                auth: "/manage/case"
            },
            path: "case-detail",
            component: ()=>a.e("manifest").then(a.bind(null, "887c"))
        }, {
            meta: {
                title: "地址全息档案",
                auth: "/manage/address-opacity"
            },
            path: "address-opacity",
            name: "address-opacity",
            component: ()=>a.e("manifest").then(a.bind(null, "a062"))
        }, {
            meta: {
                title: "区块链浏览器",
                auth: "/manage/address-liulanqi"
            },
            path: "address-liulanqi",
            name: "address-liulanqi",
            component: ()=>a.e("manifest").then(a.bind(null, "e0c1"))
        }, {
            meta: {
                title: "地址全息档案",
                auth: "/manage/address-opacity"
            },
            path: "address-opacity-detail-list",
            name: "address-opacity-detail-list",
            component: ()=>a.e("manifest").then(a.bind(null, "7c12"))
        }, {
            meta: {
                title: "地址全息档案",
                auth: "/manage/address-opacity"
            },
            path: "address-opacity-detail-list-opponent",
            name: "address-opacity-detail-list-opponent",
            component: ()=>a.e("manifest").then(a.bind(null, "d732"))
        }, {
            meta: {
                title: "案件管理",
                auth: "/manage/case"
            },
            path: "case-detail",
            component: ()=>a.e("manifest").then(a.bind(null, "b640"))
        }, {
            meta: {
                title: "案件管理",
                auth: "/manage/case"
            },
            path: "briefing-list",
            component: ()=>a.e("manifest").then(a.bind(null, "87a5"))
        }, {
            meta: {
                title: "地址研判",
                auth: "/manage/address-analysic"
            },
            path: "address-analysic",
            component: ()=>a.e("manifest").then(a.bind(null, "1d58"))
        }, {
            meta: {
                title: "地址研判Pro",
                auth: "/manage/multidimen-address"
            },
            path: "multidimen-address",
            component: ()=>a.e("manifest").then(a.bind(null, "8556"))
        }, {
            meta: {
                title: "比特币交易分析",
                auth: "/manage/transactional-analysis"
            },
            name: "TransactionalAnalysis",
            path: "transactional-analysis",
            component: ()=>a.e("manifest").then(a.bind(null, "05dd"))
        }, {
            meta: {
                title: "反洗钱交易匹配",
                auth: "/manage/nbmoney"
            },
            name: "Nbmoney",
            path: "nbmoney",
            component: ()=>a.e("manifest").then(a.bind(null, "1c21"))
        }, {
            name: "TokenQuery",
            path: "token-query",
            meta: {
                title: "代币查询",
                auth: "/manage/token-query"
            },
            component: ()=>a.e("manifest").then(a.bind(null, "7eb0"))
        }, {
            meta: {
                title: "百宝箱",
                auth: "/manage/tool-box"
            },
            name: "ToolBox",
            path: "tool-box",
            component: ()=>a.e("manifest").then(a.bind(null, "70e1"))
        }, {
            meta: {
                title: "虚拟货币汇率查询",
                auth: "/manage/tool-box"
            },
            name: "DcQuery",
            path: "dc-query",
            component: ()=>a.e("manifest").then(a.bind(null, "1cd6"))
        }, {
            meta: {
                title: "安装包信息提取",
                auth: "/manage/tool-box"
            },
            name: "AppQuery",
            path: "app-query",
            component: ()=>a.e("manifest").then(a.bind(null, "5223"))
        }, {
            meta: {
                title: "合约信息",
                auth: "/manage/token-query"
            },
            name: "TokenList",
            path: "token-list",
            component: ()=>a.e("manifest").then(a.bind(null, "5330"))
        }, {
            meta: {
                title: "地址关联分析",
                auth: "/manage/address-relation"
            },
            name: "AddressRelation",
            path: "address-relation",
            component: ()=>a.e("manifest").then(a.bind(null, "4055"))
        }, {
            meta: {
                title: "地址关联分析",
                auth: "/manage/address-relation"
            },
            name: "AddressLineGraph",
            path: "address-line-graph",
            component: ()=>a.e("manifest").then(a.bind(null, "8e8b"))
        }, {
            meta: {
                title: "关系图谱",
                auth: "/manage/relation-analysis"
            },
            name: "RelationAnalysis",
            path: "relation-analysis",
            component: ()=>a.e("manifest").then(a.bind(null, "5268"))
        }, {
            meta: {
                title: "交易流水可视化",
                auth: "/manage/trade-water-index"
            },
            name: "TradeWaterIndex",
            path: "trade-water-index",
            component: ()=>a.e("manifest").then(a.bind(null, "ce02"))
        }, {
            meta: {
                title: "地址监控",
                auth: "/manage/address-monitor"
            },
            name: "AddressMonitor",
            path: "address-monitor",
            component: ()=>a.e("manifest").then(a.bind(null, "2e42"))
        }, {
            meta: {
                title: "地址监控",
                selectMenu: "manage/address-monitor",
                auth: "/manage/address-monitor"
            },
            name: "MonitorRead",
            path: "monitor-read",
            component: ()=>a.e("manifest").then(a.bind(null, "4fb2"))
        }, {
            meta: {
                title: "地址监控",
                selectMenu: "manage/address-monitor",
                auth: "/manage/address-monitor"
            },
            path: "monitor-add",
            component: ()=>a.e("manifest").then(a.bind(null, "316c"))
        }, {
            meta: {
                title: "地址监控",
                selectMenu: "manage/address-monitor",
                auth: "/manage/address-monitor"
            },
            name: "BalanceAdd",
            path: "balance-add",
            component: ()=>a.e("manifest").then(a.bind(null, "a185"))
        }, {
            meta: {
                title: "地址监控",
                selectMenu: "manage/address-monitor",
                auth: "/manage/address-monitor"
            },
            name: "MonitorEdit",
            path: "monitor-edit",
            component: ()=>a.e("manifest").then(a.bind(null, "8210"))
        }, {
            meta: {
                title: "地址监控",
                selectMenu: "manage/address-monitor",
                auth: "/manage/address-monitor"
            },
            name: "MonitorList",
            path: "monitor-list",
            component: ()=>a.e("manifest").then(a.bind(null, "a68e"))
        }, {
            meta: {
                title: "交易流水",
                auth: "/manage/transaction-details"
            },
            path: "transaction-details",
            component: ()=>a.e("manifest").then(a.bind(null, "798d"))
        }, {
            meta: {
                title: "地址标注",
                auth: "/manage/address-tag"
            },
            path: "address-tag",
            component: ()=>a.e("manifest").then(a.bind(null, "859d"))
        }, {
            meta: {
                title: "调证协助",
                auth: "/manage/survey-assist"
            },
            path: "survey-assist",
            component: ()=>a.e("manifest").then(a.bind(null, "e14d"))
        }, {
            meta: {
                title: "调证协助",
                auth: "/manage/survey-assist"
            },
            path: "survey-templates",
            component: ()=>a.e("manifest").then(a.bind(null, "6e91"))
        }, {
            meta: {
                title: "舆情线索",
                auth: "/manage/clue"
            },
            path: "clue",
            component: ()=>a.e("manifest").then(a.bind(null, "b5b3"))
        }, {
            meta: {
                title: "舆情线索",
                selectMenu: "manage/clue",
                auth: "/manage/clue"
            },
            path: "clue-detail/:id",
            component: ()=>a.e("manifest").then(a.bind(null, "cea6"))
        }, {
            meta: {
                title: "线索提交",
                auth: "/manage/clue-submit"
            },
            path: "clue-submit",
            component: ()=>a.e("manifest").then(a.bind(null, "6a31"))
        }, {
            meta: {
                title: "线索提交",
                selectMenu: "manage/clue-submit",
                auth: "/manage/clue-submit"
            },
            path: "clue-from",
            component: ()=>a.e("manifest").then(a.bind(null, "107d"))
        }, {
            meta: {
                title: "舆情线索",
                selectMenu: "manage/clue-submit",
                auth: "/manage/clue-submit"
            },
            path: "clue-read",
            name: "cluereadFrom",
            component: ()=>a.e("manifest").then(a.bind(null, "506c"))
        }, {
            meta: {
                title: "术语解释",
                auth: "/manage/help"
            },
            path: "help",
            component: ()=>a.e("manifest").then(a.bind(null, "8d76"))
        }, {
            meta: {
                title: "交易信息",
                auth: !1
            },
            name: "tradeInfo",
            path: "trade-info",
            component: ()=>a.e("manifest").then(a.bind(null, "634f"))
        }, {
            meta: {
                title: "区块链浏览器",
                selectMenu: "manage/address-liulanqi",
                auth: "/manage/address-liulanqi"
            },
            name: "addressInfo",
            path: "address-info",
            component: ()=>a.e("manifest").then(a.bind(null, "dd5b1"))
        }, {
            meta: {
                title: "区块链浏览器",
                auth: "/manage/address-liulanqi"
            },
            name: "addressInfo/alldaibi",
            path: "addressInfo/alldaibi",
            component: ()=>a.e("manifest").then(a.bind(null, "8f43"))
        }, {
            meta: {
                title: "工作台",
                auth: !1
            },
            name: "Supcon",
            path: "supcon",
            component: ()=>a.e("manifest").then(a.bind(null, "068a"))
        }, {
            meta: {
                title: "平台服务",
                auth: !1
            },
            name: "platform",
            path: "platform",
            component: ()=>a.e("manifest").then(a.bind(null, "a48e"))
        }, {
            meta: {
                title: "判例库",
                auth: "/manage/material"
            },
            name: "Material",
            path: "material",
            component: ()=>a.e("manifest").then(a.bind(null, "dfcd"))
        }, {
            meta: {
                title: "起诉书",
                auth: "/manage/indictment"
            },
            name: "Indictment",
            path: "indictment",
            component: ()=>a.e("manifest").then(a.bind(null, "5cb1"))
        }, {
            meta: {
                title: "判例库",
                selectMenu: "manage/material",
                auth: "/manage/material"
            },
            name: "Verdict",
            path: "verdict",
            component: ()=>a.e("manifest").then(a.bind(null, "457c"))
        }, {
            meta: {
                title: "起诉书",
                selectMenu: "manage/indictment",
                auth: "/manage/indictment"
            },
            name: "Complaint",
            path: "complaint",
            component: ()=>a.e("manifest").then(a.bind(null, "d95d"))
        }, {
            meta: {
                title: "政策法规",
                auth: "/manage/policy"
            },
            name: "Policy",
            path: "policy",
            component: ()=>a.e("manifest").then(a.bind(null, "136a"))
        }, {
            meta: {
                title: "虚拟币数据",
                auth: "/manage/xunibi"
            },
            name: "xunibi",
            path: "xunibi",
            component: ()=>a.e("manifest").then(a.bind(null, "6b67"))
        }, {
            meta: {
                title: "交易所数据",
                auth: "/manage/exchange"
            },
            name: "exchange",
            path: "exchange",
            component: ()=>a.e("manifest").then(a.bind(null, "ee5f"))
        }, {
            meta: {
                title: "富豪榜",
                auth: "/manage/richlist"
            },
            name: "richlist",
            path: "richlist",
            component: ()=>a.e("manifest").then(a.bind(null, "d597"))
        }, {
            meta: {
                title: "大额交易",
                auth: "/manage/bigtrade"
            },
            name: "bigtrade",
            path: "bigtrade",
            component: ()=>a.e("manifest").then(a.bind(null, "bc16"))
        }]
          , M = a("2e8d")
          , N = {
            base64: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
            encode: function(t) {
                if (!t)
                    return !1;
                for (var e, a, n, i, s, o, r = "", c = 0; n = (o = t.charCodeAt(c++)) >> 2,
                i = (3 & o) << 4 | (e = t.charCodeAt(c++)) >> 4,
                s = (15 & e) << 2 | (a = t.charCodeAt(c++)) >> 6,
                o = 63 & a,
                isNaN(e) ? s = o = 64 : isNaN(a) && (o = 64),
                r += this.base64.charAt(n) + this.base64.charAt(i) + this.base64.charAt(s) + this.base64.charAt(o),
                c < t.length; )
                    ;
                return r
            },
            decode: function(t) {
                if (!t)
                    return !1;
                t = t.replace(/[^A-Za-z0-9\+\/\=]/g, "");
                for (var e, a, n, i, s = "", o = 0; e = this.base64.indexOf(t.charAt(o++)),
                a = this.base64.indexOf(t.charAt(o++)),
                n = this.base64.indexOf(t.charAt(o++)),
                i = this.base64.indexOf(t.charAt(o++)),
                s += String.fromCharCode(e << 2 | a >> 4),
                64 != n && (s += String.fromCharCode((15 & a) << 4 | n >> 2)),
                64 != i && (s += String.fromCharCode((3 & n) << 6 | i)),
                o < t.length; )
                    ;
                return s
            }
        }
          , P = {
            hex: "0123456789abcdef",
            encode: function(t) {
                if (!t)
                    return !1;
                for (var e, a = "", n = 0; e = t.charCodeAt(n++),
                a += this.hex.charAt(e >> 4 & 15) + this.hex.charAt(15 & e),
                n < t.length; )
                    ;
                return a
            },
            decode: function(t) {
                if (!t)
                    return !1;
                t = t.replace(/[^0-9abcdef]/g, "");
                for (var e = "", a = 0; e += String.fromCharCode(this.hex.indexOf(t.charAt(a++)) << 4 & 240 | 15 & this.hex.indexOf(t.charAt(a++))),
                a < t.length; )
                    ;
                return e
            }
        }
          , E = {
            getPublicKey: function(t) {
                return !(t = new O(N.decode(t))).error && ("1.2.840.113549.1.1.1" == (t = t.data)[0][0][0] && new S(t[0][1][0][0],t[0][1][0][1]))
            },
            encrypt: function(t, e) {
                if (!e)
                    return !1;
                var a = e.modulus.bitLength() + 7 >> 3;
                if (!(t = this.pkcs1pad2(t, a)))
                    return !1;
                if (!(t = t.modPowInt(e.encryptionExponent, e.modulus)))
                    return !1;
                for (t = t.toString(16); t.length < 2 * a; )
                    t = "0" + t;
                return N.encode(P.decode(t))
            },
            pkcs1pad2: function(t, e) {
                if (e < t.length + 11)
                    return null;
                for (var a = [], n = t.length - 1; 0 <= n && 0 < e; )
                    a[--e] = t.charCodeAt(n--);
                for (a[--e] = 0; 2 < e; )
                    a[--e] = Math.floor(254 * Math.random()) + 1;
                return a[--e] = 2,
                a[--e] = 0,
                new M.a(a)
            }
        }
          , g = a("61b0")
          , w = {
            name: "Login",
            components: {
                wxlogin: g.a
            },
            data() {
                return {
                    appid: "",
                    statecode: "",
                    scope: "snsapi_login",
                    bast64css: "data:text/css;base64,LmltcG93ZXJCb3ggLnFyY29kZSB7d2lkdGg6IDE5MHB4O2hlaWdodDoxOTBweDtib3JkZXI6bm9uZTttYXJnaW4tdG9wOiAyM3B4O30NCi5pbXBvd2VyQm94IC5pbmZvIHt3aWR0aDogMjYwcHg7fQ0KLnN0YXR1c19pY29uIHtkaXNwbGF5OiBub25lfQ0KLmltcG93ZXJCb3ggLnN0YXR1cyB7dGV4dC1hbGlnbjogbGVmdDt9DQouaW1wb3dlckJveCAudGl0bGUge2Rpc3BsYXk6IG5vbmV9DQppZnJhbWUge2hlaWdodDogMzIycHg7fQ0K",
                    loginForm: {
                        userName: "",
                        password: ""
                    },
                    regCode: "",
                    wxid: "",
                    modalRegCode: !1,
                    hideQrcode: !1,
                    clickCount: 0,
                    homeMade: !1
                }
            },
            computed: {
                redirect_uri() {
                    var t = window.location.origin;
                    return window.location.host,
                    encodeURIComponent(t + "/#/login")
                },
                hasCode() {
                    return Boolean(this.$route.query.code)
                }
            },
            watch: {
                "$route.query": {
                    deep: !0,
                    immediate: !0,
                    handler(t) {
                        t.code && this.authWxLogin()
                    }
                }
            },
            methods: {
                async authWxBind() {
                    try {
                        var t = {
                            code: this.$route.query.code,
                            host: window.location.host
                        }
                          , e = await Object(D.c)(t);
                        0 === e.status ? this.loginSuccess(e) : this.loginError()
                    } catch (t) {
                        this.loginError()
                    }
                },
                async authWxLogin() {
                    try {
                        var t = {
                            code: this.$route.query.code,
                            host: window.location.host
                        }
                          , e = await Object(D.d)(t);
                        0 === e.status ? this.loginSuccess(e) : this.loginError()
                    } catch (t) {
                        this.loginError()
                    }
                },
                loginSuccess(t) {
                    var e = t["data"];
                    "wxid"in e ? (this.wxid = t.data.wxid,
                    this.modalRegCode = !0) : (Object(s.d)(e.jwt_token),
                    this.$store.dispatch("auth/authGetUserPower"),
                    this.$router.replace({
                        name: "home"
                    }))
                },
                loginError() {
                    this.regCode = "",
                    this.statecode = Date.parse(new Date),
                    this.$router.replace({
                        name: "login"
                    })
                },
                async Ok() {
                    var t = {
                        wxid: this.wxid,
                        regCode: this.regCode
                    }
                      , t = await Object(D.c)(t);
                    if (0 !== ReadableStream.status)
                        return this.loginError(),
                        !1;
                    this.loginSuccess(t)
                },
                Cancel() {
                    return this.regCode = "",
                    this.statecode = Date.parse(new Date),
                    this.$router.replace({
                        name: "login"
                    }),
                    !1
                },
                loadCanvas() {
                    let a = document.getElementById("c")
                      , n = a.getContext("2d");
                    a.height = window.innerHeight,
                    a.width = window.innerWidth;
                    let i;
                    i = "Ξ฿¥$BTC.ETH.USDT.CHAINSGUARD.TRC.ERC20.TRON".split("");
                    let e = a.width / 16
                      , s = [];
                    for (let t = 0; t < e; t++)
                        s[t] = 1;
                    window.onresize = function() {
                        a.height = window.innerHeight,
                        a.width = window.innerWidth,
                        e = a.width / 16;
                        for (let t = 0; t < e; t++)
                            s[t] = 1
                    }
                    ,
                    setInterval(function() {
                        n.fillStyle = "rgba(0, 0, 0, 0.05)",
                        n.fillRect(0, 0, a.width, a.height),
                        n.fillStyle = "#2d68ba",
                        n.font = "16px arial";
                        for (let t = 0; t < s.length; t++) {
                            var e = i[Math.floor(Math.random() * i.length)];
                            n.fillText(e, 16 * t, 16 * s[t]),
                            (16 * s[t] > a.height || .98 < Math.random()) && (s[t] = 0),
                            s[t]++
                        }
                    }, 88)
                },
                async handleLogin() {
                    var t = E.getPublicKey("MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMNwat8r2Yl4/aTeK10CNEdMCs3PydUb4AJO150HjTmLZjzHfuV6Pjp0eJ/WOEqS+gaVhhhIC41veCpQnRd5OdcCAwEAAQ==")
                      , t = E.encrypt(this.loginForm.password, t)
                      , t = {
                        userName: this.loginForm.userName.trim(),
                        password: t
                    }
                      , t = await Object(D.b)(t);
                    0 == t.status && (localStorage.setItem("Username", this.loginForm.userName.trim()),
                    t = t["data"],
                    Object(s.d)(t.jwt_token),
                    this.$store.dispatch("auth/authGetUserPower"),
                    localStorage.setItem("expireShow", "1"),
                    this.$router.push({
                        path: "/home"
                    }))
                },
                changeLogin() {
                    "changzhou" !== this.cityEnv && (6 < this.clickCount ? this.hideQrcode = !this.hideQrcode : this.clickCount++)
                }
            },
            created() {
                -1 < window.navigator.userAgent.toLowerCase().indexOf("x11") && (this.homeMade = !0),
                "changzhou" === this.cityEnv && (this.hideQrcode = !0);
                var t = window.location.host;
                this.appid = {
                    "aml.chainsguard.com": "wx9de8c2a4aae325c5",
                    "aml.zklatech.com": "wx1e358985a05170c1"
                }[t]
            },
            mounted() {
                this.loadCanvas()
            }
        }
          , w = (a("a63b"),
        Object(d.a)(w, function() {
            var e = this
              , t = e.$createElement
              , t = e._self._c || t;
            return t("div", {
                directives: [{
                    name: "show",
                    rawName: "v-show",
                    value: !e.hasCode,
                    expression: "!hasCode"
                }],
                staticClass: "main"
            }, [t("canvas", {
                attrs: {
                    id: "c"
                }
            }), t("div", {
                attrs: {
                    id: "hidden-btn"
                },
                on: {
                    click: e.changeLogin
                }
            }), t("div", {
                staticClass: "outer-div",
                class: {
                    "outer-div-animate": !e.homeMade
                }
            }), t("div", {
                staticClass: "inner-div",
                class: {
                    "inner-div-animate": !e.homeMade
                }
            }), t("div", {
                staticClass: "login-div",
                class: {
                    "hide-qrcode-background": e.hideQrcode
                }
            }, [e.hideQrcode ? ["changzhou" === e.$cityEnv ? [t("div", {
                staticClass: "chagnzhou-logo"
            })] : [t("div", {
                staticClass: "logo"
            })], t("div", {
                staticClass: "form"
            }, [t("div", {
                staticClass: "item"
            }, [t("label", {
                staticClass: "item-key"
            }, [e._v("账号")]), t("Input", {
                staticClass: "width345",
                attrs: {
                    placeholder: "请输入登录账号..."
                },
                model: {
                    value: e.loginForm.userName,
                    callback: function(t) {
                        e.$set(e.loginForm, "userName", t)
                    },
                    expression: "loginForm.userName"
                }
            })], 1), t("div", {
                staticClass: "item"
            }, [t("label", {
                staticClass: "item-key"
            }, [e._v("密码")]), t("Input", {
                staticClass: "width345",
                attrs: {
                    type: "password",
                    placeholder: "请输入登录密码…"
                },
                model: {
                    value: e.loginForm.password,
                    callback: function(t) {
                        e.$set(e.loginForm, "password", t)
                    },
                    expression: "loginForm.password"
                }
            })], 1), t("div", {
                staticClass: "submit",
                on: {
                    click: e.handleLogin
                }
            })])] : [t("div", {
                staticClass: "qrcode-border"
            }), t("div", {
                staticClass: "we-form"
            }, [t("wxlogin", {
                key: e.statecode,
                attrs: {
                    appid: e.appid,
                    scope: e.scope,
                    redirect_uri: e.redirect_uri,
                    theme: "black",
                    state: e.statecode,
                    href: e.bast64css,
                    rel: "external nofollow"
                }
            })], 1)]], 2), t("Modal", {
                attrs: {
                    width: "368",
                    title: "注册码",
                    "ok-text": "确定",
                    "cancel-text": "取消"
                },
                on: {
                    "on-ok": e.Ok,
                    "on-cancel": e.Cancel
                },
                model: {
                    value: e.modalRegCode,
                    callback: function(t) {
                        e.modalRegCode = t
                    },
                    expression: "modalRegCode"
                }
            }, [t("div", {
                staticClass: "pb16"
            }, [t("Input", {
                staticClass: "w320",
                attrs: {
                    type: "text",
                    placeholder: "请输入注册码..."
                },
                model: {
                    value: e.regCode,
                    callback: function(t) {
                        e.regCode = t
                    },
                    expression: "regCode"
                }
            })], 1)])], 1)
        }, [], !1, null, "00865c88", null)).exports
          , g = {
            name: "Login",
            components: {
                wxlogin: g.a
            },
            data() {
                return {
                    kefu: a("a036"),
                    appid: "wxc35f37bc9428b000",
                    statecode: "",
                    scope: "snsapi_login",
                    bast64css: "data:text/css;base64,LmltcG93ZXJCb3ggLnFyY29kZSB7d2lkdGg6IDE5MHB4O2hlaWdodDoxOTBweDtib3JkZXI6bm9uZTttYXJnaW4tdG9wOiAyM3B4O30NCi5pbXBvd2VyQm94IC5pbmZvIHt3aWR0aDogMjYwcHg7fQ0KLnN0YXR1c19pY29uIHtkaXNwbGF5OiBub25lfQ0KLmltcG93ZXJCb3ggLnN0YXR1cyB7dGV4dC1hbGlnbjogbGVmdDt9DQouaW1wb3dlckJveCAudGl0bGUge2Rpc3BsYXk6IG5vbmV9DQppZnJhbWUge2hlaWdodDogMzIycHg7fQ0K",
                    loginForm: {
                        userName: "",
                        password: ""
                    },
                    regCode: "",
                    wxid: "",
                    modalRegCode: !1,
                    hideQrcode: !1,
                    clickCount: 0,
                    homeMade: !1,
                    onDuty: !1,
                    tabSelected: !0,
                    loading: !1
                }
            },
            computed: {
                redirect_uri() {
                    var t = window.location.origin;
                    return window.location.host,
                    encodeURIComponent(t + "/#/login")
                },
                hasCode() {
                    return Boolean(this.$route.query.code)
                }
            },
            watch: {
                "$route.query": {
                    deep: !0,
                    immediate: !0,
                    handler(t) {
                        t.code && this.authWxLogin()
                    }
                }
            },
            methods: {
                async authWxLogin() {
                    try {
                        var t = {
                            code: this.$route.query.code,
                            host: window.location.host
                        }
                          , e = await Object(D.d)(t);
                        0 === e.status ? this.loginSuccess(e) : this.loginfail()
                    } catch (t) {
                        this.loginfail()
                    }
                },
                loginSuccess(t) {
                    var e = t["data"];
                    "wxid"in e ? (this.wxid = t.data.wxid,
                    this.modalRegCode = !0) : (Object(s.d)(e.jwt_token),
                    this.$store.dispatch("auth/authGetUserPower"),
                    this.$router.replace({
                        name: "home"
                    }))
                },
                loginfail() {
                    this.regCode = "",
                    this.statecode = Date.parse(new Date),
                    this.$router.replace({
                        name: "login"
                    })
                },
                duty() {
                    this.$router.push({
                        name: "duty"
                    })
                },
                setTab(t) {
                    this.tabSelected = t
                },
                async Ok() {
                    var t = {
                        wxid: this.wxid,
                        regCode: this.regCode
                    }
                      , t = await Object(D.c)(t);
                    if (0 !== t.status)
                        return this.loginfail(),
                        !1;
                    this.loginSuccess(t)
                },
                Cancel() {
                    return this.regCode = "",
                    this.statecode = Date.parse(new Date),
                    this.$router.replace({
                        name: "login"
                    }),
                    !1
                },
                async handleLogin() {
                    var t = E.getPublicKey("MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMNwat8r2Yl4/aTeK10CNEdMCs3PydUb4AJO150HjTmLZjzHfuV6Pjp0eJ/WOEqS+gaVhhhIC41veCpQnRd5OdcCAwEAAQ==")
                      , t = E.encrypt(this.loginForm.password, t)
                      , t = {
                        userName: this.loginForm.userName.trim(),
                        password: t
                    }
                      , t = await Object(D.b)(t);
                    0 == t.status && (localStorage.setItem("Username", this.loginForm.userName.trim()),
                    t = t["data"],
                    Object(s.d)(t.jwt_token),
                    this.$store.dispatch("auth/authGetUserPower"),
                    localStorage.setItem("expireShow", "1"),
                    this.$router.push({
                        name: "home"
                    }))
                },
                changeLogin() {
                    "changzhou" !== this.cityEnv && (6 < this.clickCount ? this.hideQrcode = !this.hideQrcode : this.clickCount++)
                }
            },
            created() {
                -1 < window.navigator.userAgent.toLowerCase().indexOf("x11") && (this.homeMade = !0),
                "changzhou" === this.cityEnv && (this.hideQrcode = !0);
                var t = window.location.host;
                this.appid = {
                    "trace.zklatech.com": "wxc35f37bc9428b000"
                }[t]
            }
        };
        (a("e472"),
        Object(d.a)(g, function() {
            var e = this
              , t = e.$createElement
              , t = e._self._c || t;
            return t("div", {
                directives: [{
                    name: "show",
                    rawName: "v-show",
                    value: !e.hasCode,
                    expression: "!hasCode"
                }],
                staticClass: "main"
            }, [t("div", {
                attrs: {
                    id: "hidden-btn"
                },
                on: {
                    click: e.changeLogin
                }
            }), t("div", {
                staticClass: "login-div"
            }, [t("div", {
                staticClass: "login-ad"
            }, [t("div", {
                staticClass: "login-logo",
                class: {
                    "changzhou-login-logo": "changzhou" == e.cityEnv
                }
            }), t("div", {
                staticClass: "login-new-logo"
            }), t("p", {
                staticClass: "nobg"
            }, [e._v("虚拟货币犯罪预警追踪")])]), t("div", {
                staticClass: "login-form"
            }, [t("div", {
                staticClass: "tab"
            }, [t("div", {
                staticClass: "tab-tit"
            }, [t("div", {
                staticClass: "tabitem",
                class: {
                    select: e.tabSelected
                },
                on: {
                    click: function(t) {
                        return e.setTab(!0)
                    }
                }
            }, [e._v(" 登录 ")]), t("div", {
                staticClass: "tabitem",
                class: {
                    select: !e.tabSelected
                },
                on: {
                    click: function(t) {
                        return e.setTab(!1)
                    }
                }
            }, [e._v(" 申请使用 ")]), t("div", {
                staticClass: "line",
                class: {
                    right: !e.tabSelected
                }
            })]), t("div", {
                staticClass: "tab-con"
            }, [t("div", {
                directives: [{
                    name: "show",
                    rawName: "v-show",
                    value: e.tabSelected,
                    expression: "tabSelected"
                }],
                staticClass: "form"
            }, [e.hideQrcode ? [t("div", {
                staticClass: "logo"
            }), t("div", {
                staticClass: "form"
            }, [t("div", {
                staticClass: "item"
            }, [t("label", {
                staticClass: "item-key"
            }, [e._v("账号")]), t("Input", {
                staticClass: "form-input-style",
                attrs: {
                    placeholder: "请输入登录账号..."
                },
                model: {
                    value: e.loginForm.userName,
                    callback: function(t) {
                        e.$set(e.loginForm, "userName", t)
                    },
                    expression: "loginForm.userName"
                }
            })], 1), t("div", {
                staticClass: "item"
            }, [t("label", {
                staticClass: "item-key"
            }, [e._v("密码")]), t("Input", {
                staticClass: "form-input-style",
                attrs: {
                    type: "password",
                    placeholder: "请输入登录密码…"
                },
                model: {
                    value: e.loginForm.password,
                    callback: function(t) {
                        e.$set(e.loginForm, "password", t)
                    },
                    expression: "loginForm.password"
                }
            })], 1), t("div", {
                staticClass: "submit",
                on: {
                    click: e.handleLogin
                }
            }, [e._v("账号登录")])])] : [t("div", {
                staticClass: "form-erweima"
            }, [t("wxlogin", {
                key: e.statecode,
                attrs: {
                    appid: e.appid,
                    scope: e.scope,
                    redirect_uri: e.redirect_uri,
                    theme: "black",
                    state: e.statecode,
                    href: e.bast64css,
                    rel: "external nofollow"
                }
            })], 1)], t("div", {
                staticClass: "form-note"
            }, [e._v(" 登录平台即代表同意 "), t("span", {
                on: {
                    click: e.duty
                }
            }, [e._v("《使用协议》")])])], 2), t("div", {
                directives: [{
                    name: "show",
                    rawName: "v-show",
                    value: !e.tabSelected,
                    expression: "!tabSelected"
                }],
                staticClass: "kefu"
            }, [t("img", {
                staticClass: "kefu-img",
                attrs: {
                    src: e.kefu
                }
            }), t("div", {
                staticClass: "kefu-step"
            })])])])])]), t("Modal", {
                attrs: {
                    width: "368",
                    title: "注册码",
                    "ok-text": "确定",
                    "cancel-text": "取消"
                },
                on: {
                    "on-ok": e.Ok,
                    "on-cancel": e.Cancel
                },
                model: {
                    value: e.modalRegCode,
                    callback: function(t) {
                        e.modalRegCode = t
                    },
                    expression: "modalRegCode"
                }
            }, [t("div", {
                staticClass: "pb16"
            }, [t("Input", {
                staticClass: "w320",
                attrs: {
                    type: "text",
                    placeholder: "请输入注册码..."
                },
                model: {
                    value: e.regCode,
                    callback: function(t) {
                        e.regCode = t
                    },
                    expression: "regCode"
                }
            })], 1)]), e.loading ? t("Spin", {
                attrs: {
                    fix: ""
                }
            }) : e._e()], 1)
        }, [], !1, null, "3c4d569b", null)).exports;
        y.default.use(u.a);
        const F = [{
            path: "/",
            redirect: {
                name: "login"
            }
        }, {
            path: "/login",
            name: "login",
            component: w,
            meta: {
                title: " ",
                auth: !1
            }
        }, {
            path: "/duty",
            name: "duty",
            component: ()=>a.e("manifest").then(a.bind(null, "a9b7")),
            meta: {
                title: " ",
                auth: !1
            }
        }, {
            path: "/home",
            name: "home",
            meta: {
                title: "首页",
                auth: !1
            },
            component: ()=>a.e("manifest").then(a.bind(null, "bc13"))
        }, {
            path: "/entrance",
            name: "entrance",
            redirect: {
                name: "login"
            }
        }, {
            path: "/manage",
            name: "manage",
            component: m,
            children: C
        }, {
            path: "/manage-blank",
            name: "manage-blank",
            component: e,
            children: [{
                meta: {
                    title: "交易流水可视化",
                    auth: "/manage/trade-water-index"
                },
                name: "TradeWaterRouter",
                path: "trade-water",
                component: ()=>a.e("manifest").then(a.bind(null, "cda9"))
            }, {
                meta: {
                    title: "交易流水可视化",
                    auth: "/manage/trade-water-index"
                },
                name: "TradeWaterTable",
                path: "trade-water-table",
                component: ()=>a.e("manifest").then(a.bind(null, "2127"))
            }, {
                path: "address-opacity-detail",
                name: "address-opacity-detail",
                meta: {
                    title: "地址全息档案",
                    auth: "/manage/address-opacity"
                },
                component: ()=>a.e("manifest").then(a.bind(null, "cae4"))
            }, {
                meta: {
                    title: "案件管理",
                    auth: "/manage/case"
                },
                path: "case-detail",
                component: ()=>a.e("manifest").then(a.bind(null, "b640"))
            }, {
                meta: {
                    title: "案件管理",
                    auth: "/manage/case"
                },
                path: "collection-address",
                component: ()=>a.e("manifest").then(a.bind(null, "5305"))
            }, {
                meta: {
                    title: "案件管理",
                    auth: "/manage/case"
                },
                path: "survey-address",
                component: ()=>a.e("manifest").then(a.bind(null, "e8f7"))
            }, {
                meta: {
                    title: "地址研判",
                    auth: "/manage/address-analysic"
                },
                name: "ConcludeResult",
                path: "conclude-result",
                component: ()=>a.e("manifest").then(a.bind(null, "2040"))
            }, {
                meta: {
                    title: "地址研判Pro",
                    auth: "/manage/multidimen-address"
                },
                name: "MultidimenAddress",
                path: "multidimen-address",
                component: ()=>a.e("manifest").then(a.bind(null, "8556"))
            }, {
                meta: {
                    title: "地址研判Pro",
                    auth: "/manage/multidimen-address"
                },
                name: "MultidimenResult",
                path: "multidimen-result",
                component: ()=>a.e("manifest").then(a.bind(null, "7b2c"))
            }, {
                meta: {
                    title: "比特币交易分析",
                    auth: "/manage/transactional-analysis"
                },
                name: "AnalysisResult",
                path: "analysis-result",
                component: ()=>a.e("manifest").then(a.bind(null, "d663"))
            }, {
                meta: {
                    title: "关系图谱",
                    auth: "/manage/relation-analysis"
                },
                name: "RelationResult",
                path: "relation-result",
                component: ()=>a.e("manifest").then(a.bind(null, "906c"))
            }, {
                meta: {
                    title: "案件管理",
                    auth: "/manage/case"
                },
                path: "briefing-list",
                component: ()=>a.e("manifest").then(a.bind(null, "87a5"))
            }, {
                meta: {
                    title: "地址关联分析",
                    auth: "/manage/address-relation"
                },
                name: "AddressRelationResult",
                path: "address-relation-result",
                component: ()=>a.e("manifest").then(a.bind(null, "0064"))
            }, {
                meta: {
                    title: "案件管理",
                    auth: "/manage/case"
                },
                name: "fullUpAddressAnalyse",
                path: "fullUpAddress-analyse/:cid/:dcType/:id",
                component: ()=>a.e("manifest").then(a.bind(null, "8744"))
            }]
        }]
          , V = new u.a({
            routes: F
        })
          , R = u.a.prototype.push;
        u.a.prototype.push = function(t) {
            return R.call(this, t).catch(t=>t)
        }
        ;
        var z = V
          , q = a("4360")
          , Q = (a("f3ca"),
        a("0ac6"),
        a("a342"),
        a("cf47"));
        const Z = I.a.CancelToken;
        var ee, a = Boolean(true || !1);
        console.log(Object(Q.b)("" + (Date.parse(new Date) + ee), `${Q.d}${s.a}`));
        new Map,
        I.a.interceptors.request.use(function(t) {
            t.cancelToken = new Z(t=>{
                y.default.prototype.__cancels__.push(t)
            }
            );
            var e, a = Boolean(t.headers.noNotice || !1);


            return "/api/unfilter/time" != t.url && (e = localStorage.getItem("diff-time") && Number(localStorage.getItem("diff-time")),
            t.headers.diff_time = e,
            t.headers.x_token = Object(Q.b)("" + (Date.parse(new Date) + e), `${Q.d}${s.a}`)),
            t.headers.autoNotice = !a,
            t.headers.jwt_token = Object(s.b)(),
            t
        }, function(t) {
            return Promise.reject(t)
        }),
        I.a.interceptors.response.use(function(t) {
            var {status: e, msg: a} = t.data;
            if (void 0 === e)
                return t;
            switch (e) {
            case -335:
            case -340:
            case 0:
                return t.data;
            case -10:
                {
                    const t = async()=>{
                        const t = await Object(D.e)({});
                        var e = new Date(t.time.replace(/-/g, "/")) - new Date;
                        localStorage.setItem("diff-time", e)
                    }
                    ;
                    return L.Notice.info({
                        title: "提示",
                        desc: "请求超时，请重试"
                    }),
                    void t()
                }
            case -100:
                return q.a.commit("auth/delInfo"),
                void L.Modal.info({
                    title: "登录提示",
                    content: "登录已超时，请重新登录。",
                    okText: "确定",
                    onOk: ()=>{
                        Object(s.c)(),
                        window.open(window.location.origin + "/#/login", "_blank")
                    }
                });
            case -300:
                return t.data;
            default:
                return "/api/unfilter/time" == t.config.url || t.config.headers.autoNotice ? (L.Notice.info({
                    title: "提示",
                    desc: a
                }),
                t) : t.data
            }
        }, function(t) {
            t && t.stack && -1 < t.stack.indexOf("timeout") && (L.Notice.destroy(),
            L.Notice.info({
                title: "提示",
                desc: "网络连接超时，请稍后重试"
            }));
            var e = t.response && t.response.status;
            return 440 !== e && 441 !== e && 442 !== e || (window.location.href = `${window.location.origin}${t.response.data}`),
            Promise.reject(t)
        });
        var C = I.a
          , e = a("38bc")
          , $ = a.n(e)
          , u = (a("70e7"),
        function() {
            var e = this
              , t = e.$createElement
              , t = e._self._c || t;
            return t("Modal", {
                attrs: {
                    width: "480px",
                    "mask-closable": !1,
                    "footer-hide": !0,
                    closable: !1
                },
                model: {
                    value: e.flag,
                    callback: function(t) {
                        e.flag = t
                    },
                    expression: "flag"
                }
            }, [t("div", {
                staticClass: "_404page"
            }, [t("img", {
                attrs: {
                    src: e.imgSrc
                }
            }), t("p", [e._v("抱歉，您访问的页面不存在")]), t("div", {
                staticClass: "home-btn",
                on: {
                    click: e.goHome
                }
            }, [e._v("确定")])])])
        }
        )
          , e = {
            name: "chargeTip",
            components: {
                Modal: L.Modal
            },
            data() {
                return {
                    flag: !1,
                    imgSrc: a("551b")
                }
            },
            methods: {
                show(t) {
                    this.event = t,
                    this.flag = !0
                },
                close() {
                    this.flag = !1
                },
                goHome() {
                    this.close(),
                    this.event("/home")
                }
            }
        }
          , H = (a("af02"),
        Object(d.a)(e, u, [], !1, null, "724b3642", null)).exports;
        const G = new y.default({
            render(t) {
                return t(H)
            }
        });
        G.$mount(),
        document.body.appendChild(G.$el);
        const W = G.$children[0];
        var X = {
            show: function(t) {
                W.show(t)
            }
        };
        $.a.configure({
            showSpinner: !1
        });
        const Y = ["/login", "/duty", "/logout"];
        z.beforeEach(async(e,t,a)=>{
            y.default.prototype.__cancels__.forEach(t=>{
                t()
            }
            ),
            y.default.prototype.__cancels__ = [],
            $.a.start();
            const n = Object(s.b)();
            if (n) {
                let t = [];
                q.a.state.auth.groupConfig && q.a.state.auth.groupConfig.nodePower && (t = q.a.state.auth.groupConfig.nodePower);
                const n = e.meta.auth;
                if (n && !t.includes(n) || void 0 === n)
                    return X.show(a),
                    !1;
                "/login" === e.path ? (a({
                    path: "/home"
                }),
                $.a.done()) : (a(),
                e.meta.title ? document.title = "无匿-" + e.meta.title : document.title = "无匿")
            } else
                -1 !== Y.indexOf(e.path) ? a() : (a("/login?redirect=" + e.path),
                $.a.done())
        }
        ),
        z.afterEach(()=>{
            $.a.done()
        }
        );
        var u = a("0af2")
          , J = a.n(u)
          , u = {
            name: "TablePager",
            data() {
                var t = this.pageSizeOpts[0];
                return {
                    curPage: this.pageIndex,
                    pageSize: t,
                    pageTotal: 0,
                    sortObj: null,
                    dataSort: [],
                    dataShow: []
                }
            },
            props: {
                initauto: {
                    type: Boolean,
                    default: !0
                },
                dataFull: {
                    type: Array
                },
                totalCount: {
                    type: Number
                },
                pageIndex: {
                    type: Number,
                    default: 1
                },
                pageSizeOpts: {
                    type: Array,
                    default: ()=>[10, 20, 30, 40]
                }
            },
            computed: {},
            watch: {
                dataFull: function(t) {
                    this.pageTotal = t.length,
                    this.dataSort = J()(t),
                    this.sortData()
                },
                totalCount: function(t) {
                    this.pageTotal = t
                },
                pageIndex(t) {
                    this.curPage = t
                }
            },
            methods: {
                changePage(t) {
                    t = ((this.curPage = t) - 1) * this.pageSize;
                    this.dataShow = this.dataSort.slice(t, t + this.pageSize),
                    this.$emit("change-data", this.dataShow, {
                        page: this.curPage,
                        pageSize: this.pageSize
                    })
                },
                changePageSize(t) {
                    this.pageSize = t,
                    this.dataShow = this.dataSort.slice(0, this.pageSize),
                    this.$emit("change-data", this.dataShow, {
                        page: this.curPage,
                        pageSize: this.pageSize
                    })
                },
                sortData(t) {
                    const a = t || this.sortObj;
                    if (a) {
                        if (this.sortObj = a,
                        !a.column || "custom" !== a.column.sortType) {
                            const n = a.key
                              , i = a.order;
                            return "normal" === i ? this.dataSort = J()(this.dataFull) : (this.dataSort.sort((t,e)=>a.column.sortMethod ? a.column.sortMethod(t[n], e[n], i) : "asc" === i ? t[n] > e[n] ? 1 : -1 : "desc" === i ? t[n] < e[n] ? 1 : -1 : void 0),
                            this.changePage(1)),
                            this.dataSort
                        }
                        t && this.$emit("sort-type-custom", a)
                    } else
                        this.changePage(this.curPage)
                }
            },
            mounted() {
                this.dataFull && (this.pageTotal = this.dataFull.length,
                this.dataSort = J()(this.dataFull)),
                this.totalCount && (this.pageTotal = this.totalCount),
                this.initauto && this.changePage(1);
                const t = this.$slots.default[0].componentInstance;
                t.$on("on-sort-change", this.sortData)
            }
        }
          , u = (a("03af"),
        Object(d.a)(u, function() {
            var t = this
              , e = t.$createElement
              , e = t._self._c || e;
            return e("div", {
                staticClass: "table-main"
            }, [t._t("default"), e("Page", {
                attrs: {
                    transfer: "",
                    "show-elevator": "",
                    "show-total": "",
                    "show-sizer": "",
                    total: t.pageTotal,
                    current: t.curPage,
                    "page-size": t.pageSize,
                    "page-size-opts": t.pageSizeOpts,
                    "class-name": "page-operate"
                },
                on: {
                    "on-change": t.changePage,
                    "on-page-size-change": t.changePageSize
                }
            })], 2)
        }, [], !1, null, "5b48a6b2", null)).exports;
        function K(t, e) {
            let a = e.value;
            "function" == typeof a && (a = a());
            e = q.a.state.auth.groupConfig || {};
            if (0 == e[a])
                t.parentNode && t.parentNode.removeChild(t);
            else if (2 == e[a]) {
                const n = t.cloneNode(!0);
                n.onclick = ()=>{
                    o.a.show()
                }
                ,
                t.parentNode && t.parentNode.replaceChild(n, t)
            }
        }
        function tt(t, e) {
            e = e.value;
            const a = q.a.state.auth.groupConfig.nodePower || [];
            a.includes(e) || t.parentNode && t.parentNode.removeChild(t)
        }
        i.a.polyfill(),
        y.default.prototype.__cancels__ = [],
        y.default.prototype.$axios = C,
        y.default.config.productionTip = !1,
        y.default.directive("menu", {
            inserted(t, e) {
                tt(t, e)
            },
            update(t, e) {
                tt(t, e)
            }
        }),
        y.default.directive("permission", {
            inserted(t, e) {
                K(t, e)
            },
            update(t, e) {
                K(t, e)
            }
        }),
        y.default.component("TablePager", u),
        y.default.use(n.a, {
            transfer: !0,
            size: "large"
        }),
        y.default.use(h),
        y.default.use(v),
        y.default.prototype.$modaltip = T,
        async function() {
            y.default.prototype.$cityEnv = "",
            window.cityEnv = "",
            Object(s.b)() && await q.a.dispatch("auth/authGetUserPower"),
            y.default.mixin({
                computed: {
                    cityEnv() {
                        return ""
                    },
                    erc20Token() {
                        return q.a.state.auth.groupConfig.erc20Token
                    },
                    trc20Token() {
                        return q.a.state.auth.groupConfig.trc20Token
                    },
                    hecoChain() {
                        return q.a.state.auth.groupConfig.hecoChain
                    },
                    bscChain() {
                        return q.a.state.auth.groupConfig.bscChain
                    }
                },
                methods: {
                    cancelAxios() {
                        y.default.prototype.__cancels__.forEach(t=>{
                            t()
                        }
                        ),
                        y.default.prototype.__cancels__ = []
                    }
                }
            }),
            new y.default({
                router: z,
                store: q.a,
                render: t=>t(A)
            }).$mount("#app")
        }()
    },
});