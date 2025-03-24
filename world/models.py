from django.contrib.gis.db import models


class NeCountries(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    featurecla = models.CharField(max_length=15, blank=True, null=True)
    scalerank = models.IntegerField(blank=True, null=True)
    labelrank = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    sovereignt = models.CharField(max_length=32, blank=True, null=True)  # Field name made lowercase.
    sov_a3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_dif = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=17, blank=True, null=True)  # Field name made lowercase.
    tlc = models.CharField(max_length=1, blank=True, null=True)  # Field name made lowercase.
    admin = models.CharField(max_length=36, blank=True, null=True)  # Field name made lowercase.
    adm0_a3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    geou_dif = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    geounit = models.CharField(max_length=36, blank=True, null=True)  # Field name made lowercase.
    gu_a3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    su_dif = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    subunit = models.CharField(max_length=36, blank=True, null=True)  # Field name made lowercase.
    su_a3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    brk_diff = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=29, blank=True, null=True)  # Field name made lowercase.
    name_long = models.CharField(max_length=36, blank=True, null=True)  # Field name made lowercase.
    brk_a3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    brk_name = models.CharField(max_length=32, blank=True, null=True)  # Field name made lowercase.
    brk_group = models.CharField(max_length=17, blank=True, null=True)  # Field name made lowercase.
    abbrev = models.CharField(max_length=16, blank=True, null=True)  # Field name made lowercase.
    postal = models.CharField(max_length=4, blank=True, null=True)  # Field name made lowercase.
    formal_en = models.CharField(max_length=52, blank=True, null=True)  # Field name made lowercase.
    formal_fr = models.CharField(max_length=35, blank=True, null=True)  # Field name made lowercase.
    name_ciawf = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    note_adm0 = models.CharField(max_length=16, blank=True, null=True)  # Field name made lowercase.
    note_brk = models.CharField(max_length=63, blank=True, null=True)  # Field name made lowercase.
    name_sort = models.CharField(max_length=36, blank=True, null=True)  # Field name made lowercase.
    name_alt = models.CharField(max_length=19, blank=True, null=True)  # Field name made lowercase.
    mapcolor7 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    mapcolor8 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    mapcolor9 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    mapcolor13 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    pop_est = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    pop_rank = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    pop_year = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    gdp_md = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    gdp_year = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    economy = models.CharField(max_length=26, blank=True, null=True)  # Field name made lowercase.
    income_grp = models.CharField(max_length=23, blank=True, null=True)  # Field name made lowercase.
    fips_10 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    iso_a2 = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    iso_a2_eh = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    iso_a3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    iso_a3_eh = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    iso_n3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    iso_n3_eh = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    un_a3 = models.CharField(max_length=4, blank=True, null=True)  # Field name made lowercase.
    wb_a2 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    wb_a3 = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    woe_id = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    woe_id_eh = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    woe_note = models.CharField(max_length=167, blank=True, null=True)  # Field name made lowercase.
    adm0_iso = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_diff = models.CharField(max_length=1, blank=True, null=True)  # Field name made lowercase.
    adm0_tlc = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_us = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_fr = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_ru = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_es = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_cn = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_tw = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_in = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_np = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_pk = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_de = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_gb = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_br = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_il = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_ps = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_sa = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_eg = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_ma = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_pt = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_ar = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_jp = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_ko = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_vn = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_tr = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_id = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_pl = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_gr = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_it = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_nl = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_se = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_bd = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_ua = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    adm0_a3_un = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    adm0_a3_wb = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(max_length=23, blank=True, null=True)  # Field name made lowercase.
    region_un = models.CharField(max_length=10, blank=True, null=True)  # Field name made lowercase.
    subregion = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    region_wb = models.CharField(max_length=26, blank=True, null=True)  # Field name made lowercase.
    name_len = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    long_len = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    abbrev_len = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    tiny = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    homepart = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    min_zoom = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    min_label = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    max_label = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    label_x = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    label_y = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    ne_id = models.BigIntegerField(blank=True, null=True)  # Field name made lowercase.
    wikidataid = models.CharField(max_length=8, blank=True, null=True)  # Field name made lowercase.
    name_ar = models.CharField(max_length=72, blank=True, null=True)  # Field name made lowercase.
    name_bn = models.CharField(max_length=148, blank=True, null=True)  # Field name made lowercase.
    name_de = models.CharField(max_length=46, blank=True, null=True)  # Field name made lowercase.
    name_en = models.CharField(max_length=44, blank=True, null=True)  # Field name made lowercase.
    name_es = models.CharField(max_length=44, blank=True, null=True)  # Field name made lowercase.
    name_fa = models.CharField(max_length=66, blank=True, null=True)  # Field name made lowercase.
    name_fr = models.CharField(max_length=54, blank=True, null=True)  # Field name made lowercase.
    name_el = models.CharField(max_length=86, blank=True, null=True)  # Field name made lowercase.
    name_he = models.CharField(max_length=78, blank=True, null=True)  # Field name made lowercase.
    name_hi = models.CharField(max_length=126, blank=True, null=True)  # Field name made lowercase.
    name_hu = models.CharField(max_length=52, blank=True, null=True)  # Field name made lowercase.
    name_id = models.CharField(max_length=46, blank=True, null=True)  # Field name made lowercase.
    name_it = models.CharField(max_length=48, blank=True, null=True)  # Field name made lowercase.
    name_ja = models.CharField(max_length=63, blank=True, null=True)  # Field name made lowercase.
    name_ko = models.CharField(max_length=47, blank=True, null=True)  # Field name made lowercase.
    name_nl = models.CharField(max_length=49, blank=True, null=True)  # Field name made lowercase.
    name_pl = models.CharField(max_length=47, blank=True, null=True)  # Field name made lowercase.
    name_pt = models.CharField(max_length=43, blank=True, null=True)  # Field name made lowercase.
    name_ru = models.CharField(max_length=86, blank=True, null=True)  # Field name made lowercase.
    name_sv = models.CharField(max_length=57, blank=True, null=True)  # Field name made lowercase.
    name_tr = models.CharField(max_length=42, blank=True, null=True)  # Field name made lowercase.
    name_uk = models.CharField(max_length=91, blank=True, null=True)  # Field name made lowercase.
    name_ur = models.CharField(max_length=67, blank=True, null=True)  # Field name made lowercase.
    name_vi = models.CharField(max_length=56, blank=True, null=True)  # Field name made lowercase.
    name_zh = models.CharField(max_length=33, blank=True, null=True)  # Field name made lowercase.
    name_zht = models.CharField(max_length=33, blank=True, null=True)  # Field name made lowercase.
    fclass_iso = models.CharField(max_length=24, blank=True, null=True)  # Field name made lowercase.
    tlc_diff = models.CharField(max_length=1, blank=True, null=True)  # Field name made lowercase.
    fclass_tlc = models.CharField(max_length=21, blank=True, null=True)  # Field name made lowercase.
    fclass_us = models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    fclass_fr = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_ru = models.CharField(max_length=14, blank=True, null=True)  # Field name made lowercase.
    fclass_es = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_cn = models.CharField(max_length=24, blank=True, null=True)  # Field name made lowercase.
    fclass_tw = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    fclass_in = models.CharField(max_length=14, blank=True, null=True)  # Field name made lowercase.
    fclass_np = models.CharField(max_length=24, blank=True, null=True)  # Field name made lowercase.
    fclass_pk = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    fclass_de = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_gb = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_br = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    fclass_il = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    fclass_ps = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    fclass_sa = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    fclass_eg = models.CharField(max_length=24, blank=True, null=True)  # Field name made lowercase.
    fclass_ma = models.CharField(max_length=24, blank=True, null=True)  # Field name made lowercase.
    fclass_pt = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_ar = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    fclass_jp = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_ko = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_vn = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    fclass_tr = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_id = models.CharField(max_length=24, blank=True, null=True)  # Field name made lowercase.
    fclass_pl = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_gr = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_it = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_nl = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_se = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.
    fclass_bd = models.CharField(max_length=24, blank=True, null=True)  # Field name made lowercase.
    fclass_ua = models.CharField(max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ne_countries'


class NeStatesProvinces(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    featurecla = models.CharField(max_length=24, blank=True, null=True)
    scalerank = models.IntegerField(blank=True, null=True)
    adm1_code = models.CharField(max_length=9, blank=True, null=True)
    diss_me = models.IntegerField(blank=True, null=True)
    iso_3166_2 = models.CharField(max_length=8, blank=True, null=True)
    wikipedia = models.CharField(max_length=84, blank=True, null=True)
    iso_a2 = models.CharField(max_length=2, blank=True, null=True)
    adm0_sr = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=44, blank=True, null=True)
    name_alt = models.CharField(max_length=129, blank=True, null=True)
    name_local = models.CharField(max_length=66, blank=True, null=True)
    type = models.CharField(max_length=38, blank=True, null=True)
    type_en = models.CharField(max_length=27, blank=True, null=True)
    code_local = models.CharField(max_length=5, blank=True, null=True)
    code_hasc = models.CharField(max_length=8, blank=True, null=True)
    note = models.CharField(max_length=114, blank=True, null=True)
    hasc_maybe = models.CharField(max_length=13, blank=True, null=True)
    region = models.CharField(max_length=43, blank=True, null=True)
    region_cod = models.CharField(max_length=15, blank=True, null=True)
    provnum_ne = models.IntegerField(blank=True, null=True)
    gadm_level = models.IntegerField(blank=True, null=True)
    check_me = models.IntegerField(blank=True, null=True)
    datarank = models.IntegerField(blank=True, null=True)
    abbrev = models.CharField(max_length=9, blank=True, null=True)
    postal = models.CharField(max_length=3, blank=True, null=True)
    area_sqkm = models.IntegerField(blank=True, null=True)
    sameascity = models.IntegerField(blank=True, null=True)
    labelrank = models.IntegerField(blank=True, null=True)
    name_len = models.IntegerField(blank=True, null=True)
    mapcolor9 = models.IntegerField(blank=True, null=True)
    mapcolor13 = models.IntegerField(blank=True, null=True)
    fips = models.CharField(max_length=5, blank=True, null=True)
    fips_alt = models.CharField(max_length=9, blank=True, null=True)
    woe_id = models.IntegerField(blank=True, null=True)
    woe_label = models.CharField(max_length=64, blank=True, null=True)
    woe_name = models.CharField(max_length=44, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    sov_a3 = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3 = models.CharField(max_length=3, blank=True, null=True)
    adm0_label = models.IntegerField(blank=True, null=True)
    admin = models.CharField(max_length=36, blank=True, null=True)
    geonunit = models.CharField(max_length=40, blank=True, null=True)
    gu_a3 = models.CharField(max_length=3, blank=True, null=True)
    gn_id = models.IntegerField(blank=True, null=True)
    gn_name = models.CharField(max_length=72, blank=True, null=True)
    gns_id = models.IntegerField(blank=True, null=True)
    gns_name = models.CharField(max_length=80, blank=True, null=True)
    gn_level = models.IntegerField(blank=True, null=True)
    gn_region = models.CharField(max_length=1, blank=True, null=True)
    gn_a1_code = models.CharField(max_length=10, blank=True, null=True)
    region_sub = models.CharField(max_length=41, blank=True, null=True)
    sub_code = models.CharField(max_length=5, blank=True, null=True)
    gns_level = models.IntegerField(blank=True, null=True)
    gns_lang = models.CharField(max_length=3, blank=True, null=True)
    gns_adm1 = models.CharField(max_length=4, blank=True, null=True)
    gns_region = models.CharField(max_length=4, blank=True, null=True)
    min_label = models.FloatField(blank=True, null=True)
    max_label = models.FloatField(blank=True, null=True)
    min_zoom = models.FloatField(blank=True, null=True)
    wikidataid = models.CharField(max_length=9, blank=True, null=True)
    name_ar = models.CharField(max_length=85, blank=True, null=True)
    name_bn = models.CharField(max_length=134, blank=True, null=True)
    name_de = models.CharField(max_length=50, blank=True, null=True)
    name_en = models.CharField(max_length=47, blank=True, null=True)
    name_es = models.CharField(max_length=44, blank=True, null=True)
    name_fr = models.CharField(max_length=47, blank=True, null=True)
    name_el = models.CharField(max_length=85, blank=True, null=True)
    name_hi = models.CharField(max_length=134, blank=True, null=True)
    name_hu = models.CharField(max_length=47, blank=True, null=True)
    name_id = models.CharField(max_length=46, blank=True, null=True)
    name_it = models.CharField(max_length=47, blank=True, null=True)
    name_ja = models.CharField(max_length=96, blank=True, null=True)
    name_ko = models.CharField(max_length=54, blank=True, null=True)
    name_nl = models.CharField(max_length=46, blank=True, null=True)
    name_pl = models.CharField(max_length=45, blank=True, null=True)
    name_pt = models.CharField(max_length=43, blank=True, null=True)
    name_ru = models.CharField(max_length=85, blank=True, null=True)
    name_sv = models.CharField(max_length=41, blank=True, null=True)
    name_tr = models.CharField(max_length=44, blank=True, null=True)
    name_vi = models.CharField(max_length=71, blank=True, null=True)
    name_zh = models.CharField(max_length=61, blank=True, null=True)
    ne_id = models.BigIntegerField(blank=True, null=True)
    name_he = models.CharField(max_length=63, blank=True, null=True)
    name_uk = models.CharField(max_length=89, blank=True, null=True)
    name_ur = models.CharField(max_length=103, blank=True, null=True)
    name_fa = models.CharField(max_length=92, blank=True, null=True)
    name_zht = models.CharField(max_length=61, blank=True, null=True)
    fclass_iso = models.CharField(max_length=12, blank=True, null=True)
    fclass_us = models.CharField(max_length=12, blank=True, null=True)
    fclass_fr = models.CharField(max_length=1, blank=True, null=True)
    fclass_ru = models.CharField(max_length=12, blank=True, null=True)
    fclass_es = models.CharField(max_length=12, blank=True, null=True)
    fclass_cn = models.CharField(max_length=18, blank=True, null=True)
    fclass_tw = models.CharField(max_length=12, blank=True, null=True)
    fclass_in = models.CharField(max_length=12, blank=True, null=True)
    fclass_np = models.CharField(max_length=12, blank=True, null=True)
    fclass_pk = models.CharField(max_length=12, blank=True, null=True)
    fclass_de = models.CharField(max_length=12, blank=True, null=True)
    fclass_gb = models.CharField(max_length=12, blank=True, null=True)
    fclass_br = models.CharField(max_length=12, blank=True, null=True)
    fclass_il = models.CharField(max_length=12, blank=True, null=True)
    fclass_ps = models.CharField(max_length=12, blank=True, null=True)
    fclass_sa = models.CharField(max_length=12, blank=True, null=True)
    fclass_eg = models.CharField(max_length=12, blank=True, null=True)
    fclass_ma = models.CharField(max_length=1, blank=True, null=True)
    fclass_pt = models.CharField(max_length=12, blank=True, null=True)
    fclass_ar = models.CharField(max_length=12, blank=True, null=True)
    fclass_jp = models.CharField(max_length=12, blank=True, null=True)
    fclass_ko = models.CharField(max_length=12, blank=True, null=True)
    fclass_vn = models.CharField(max_length=12, blank=True, null=True)
    fclass_tr = models.CharField(max_length=1, blank=True, null=True)
    fclass_id = models.CharField(max_length=12, blank=True, null=True)
    fclass_pl = models.CharField(max_length=1, blank=True, null=True)
    fclass_gr = models.CharField(max_length=12, blank=True, null=True)
    fclass_it = models.CharField(max_length=12, blank=True, null=True)
    fclass_nl = models.CharField(max_length=1, blank=True, null=True)
    fclass_se = models.CharField(max_length=12, blank=True, null=True)
    fclass_bd = models.CharField(max_length=12, blank=True, null=True)
    fclass_ua = models.CharField(max_length=12, blank=True, null=True)
    fclass_tlc = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        db_table = 'ne_states_provinces'