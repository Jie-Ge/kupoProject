
s = function(t, e) {
    t.constructor == String ? t = e && "binary" === e.encoding ? a.stringToBytes(t) : i.stringToBytes(t) : o(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
    for (var n = r.bytesToWords(t), u = 8 * t.length, c = 1732584193, l = -271733879, f = -1732584194, h = 271733878, d = 0; d < n.length; d++)
        n[d] = 16711935 & (n[d] << 8 | n[d] >>> 24) | 4278255360 & (n[d] << 24 | n[d] >>> 8);
    n[u >>> 5] |= 128 << u % 32,
    n[14 + (u + 64 >>> 9 << 4)] = u;
    var p = s._ff
      , g = s._gg
      , v = s._hh
      , y = s._ii;
    for (d = 0; d < n.length; d += 16) {
        var m = c
          , b = l
          , _ = f
          , x = h;
        l = y(l = y(l = y(l = y(l = v(l = v(l = v(l = v(l = g(l = g(l = g(l = g(l = p(l = p(l = p(l = p(l, f = p(f, h = p(h, c = p(c, l, f, h, n[d + 0], 7, -680876936), l, f, n[d + 1], 12, -389564586), c, l, n[d + 2], 17, 606105819), h, c, n[d + 3], 22, -1044525330), f = p(f, h = p(h, c = p(c, l, f, h, n[d + 4], 7, -176418897), l, f, n[d + 5], 12, 1200080426), c, l, n[d + 6], 17, -1473231341), h, c, n[d + 7], 22, -45705983), f = p(f, h = p(h, c = p(c, l, f, h, n[d + 8], 7, 1770035416), l, f, n[d + 9], 12, -1958414417), c, l, n[d + 10], 17, -42063), h, c, n[d + 11], 22, -1990404162), f = p(f, h = p(h, c = p(c, l, f, h, n[d + 12], 7, 1804603682), l, f, n[d + 13], 12, -40341101), c, l, n[d + 14], 17, -1502002290), h, c, n[d + 15], 22, 1236535329), f = g(f, h = g(h, c = g(c, l, f, h, n[d + 1], 5, -165796510), l, f, n[d + 6], 9, -1069501632), c, l, n[d + 11], 14, 643717713), h, c, n[d + 0], 20, -373897302), f = g(f, h = g(h, c = g(c, l, f, h, n[d + 5], 5, -701558691), l, f, n[d + 10], 9, 38016083), c, l, n[d + 15], 14, -660478335), h, c, n[d + 4], 20, -405537848), f = g(f, h = g(h, c = g(c, l, f, h, n[d + 9], 5, 568446438), l, f, n[d + 14], 9, -1019803690), c, l, n[d + 3], 14, -187363961), h, c, n[d + 8], 20, 1163531501), f = g(f, h = g(h, c = g(c, l, f, h, n[d + 13], 5, -1444681467), l, f, n[d + 2], 9, -51403784), c, l, n[d + 7], 14, 1735328473), h, c, n[d + 12], 20, -1926607734), f = v(f, h = v(h, c = v(c, l, f, h, n[d + 5], 4, -378558), l, f, n[d + 8], 11, -2022574463), c, l, n[d + 11], 16, 1839030562), h, c, n[d + 14], 23, -35309556), f = v(f, h = v(h, c = v(c, l, f, h, n[d + 1], 4, -1530992060), l, f, n[d + 4], 11, 1272893353), c, l, n[d + 7], 16, -155497632), h, c, n[d + 10], 23, -1094730640), f = v(f, h = v(h, c = v(c, l, f, h, n[d + 13], 4, 681279174), l, f, n[d + 0], 11, -358537222), c, l, n[d + 3], 16, -722521979), h, c, n[d + 6], 23, 76029189), f = v(f, h = v(h, c = v(c, l, f, h, n[d + 9], 4, -640364487), l, f, n[d + 12], 11, -421815835), c, l, n[d + 15], 16, 530742520), h, c, n[d + 2], 23, -995338651), f = y(f, h = y(h, c = y(c, l, f, h, n[d + 0], 6, -198630844), l, f, n[d + 7], 10, 1126891415), c, l, n[d + 14], 15, -1416354905), h, c, n[d + 5], 21, -57434055), f = y(f, h = y(h, c = y(c, l, f, h, n[d + 12], 6, 1700485571), l, f, n[d + 3], 10, -1894986606), c, l, n[d + 10], 15, -1051523), h, c, n[d + 1], 21, -2054922799), f = y(f, h = y(h, c = y(c, l, f, h, n[d + 8], 6, 1873313359), l, f, n[d + 15], 10, -30611744), c, l, n[d + 6], 15, -1560198380), h, c, n[d + 13], 21, 1309151649), f = y(f, h = y(h, c = y(c, l, f, h, n[d + 4], 6, -145523070), l, f, n[d + 11], 10, -1120210379), c, l, n[d + 2], 15, 718787259), h, c, n[d + 9], 21, -343485551),
        c = c + m >>> 0,
        l = l + b >>> 0,
        f = f + _ >>> 0,
        h = h + x >>> 0
    }
    return r.endian([c, l, f, h])
}

s()