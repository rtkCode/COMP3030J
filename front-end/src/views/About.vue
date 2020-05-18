<template>
    <div class="about-card mt-5 p-4" id="#about">
        <div class="intro text-left text-white col">
            <p>{{$t("string.about.p1")}}</p>
            <ul>
                <li>{{$t("string.about.l1")}}</li>
                <li>{{$t("string.about.l2")}}</li>
                <li>{{$t("string.about.l3")}}</li>
                <li>{{$t("string.about.l4")}}</li>
                <li>{{$t("string.about.l5")}}</li>
                <li>{{$t("string.about.l6")}}</li>
            </ul>
            <p>{{$t("string.about.p2")}}</p>
        </div>
        <div :style="map" class="map col"></div>
        <div class="col-3 mr-2 cards">
            <div class="d-flex justify-content-around flex-column card border-radius10 status-card p-3 mr-4 mb-4 border-0">
                <span class="h2 m-0">3</span>
                <small>{{$t("string.about.hb")}}</small>
            </div>
            <div class="d-flex justify-content-around flex-column card border-radius10 status-card p-3 mr-4 mb-4 border-0">
                <span class="h2 m-0">600</span>
                <small>{{$t("string.about.vd")}}</small>
            </div>
            <div class="d-flex justify-content-around flex-column card border-radius10 status-card p-3 mr-4 mb-4 border-0">
                <span class="h2 m-0">100K</span>
                <small>{{$t("string.about.cc")}}</small>
            </div>
            <div class="d-flex justify-content-around flex-column card border-radius10 status-card p-3 mr-4 mb-4 border-0">
                <span class="h2 m-0">55K</span>
                <small>{{$t("string.about.cl")}}</small>
            </div>
        </div>
    </div>
</template>

<style scoped>
.about-card{
    width: 80%;
    border-radius: 10px !important;
    border: none !important;
    background: rgba(0, 110, 117, 0.7);
    max-height: 540px;
    overflow: hidden;
}

.map{
    width: 440px;
    height: 360px;
    opacity: 0.8;
}

.status-card{
    min-width: 200px;
    max-width: 220px;
    height: 100px;
}

@media (max-width: 1030px) {
  .map{
    display: none;
  }
}

@media (max-width: 735px) {
  .cards{
    display: none;
  }
}
</style>

<script>
export default {
    data(){
        return{
            map: {
                backgroundImage: "url(" + require("../../public/img/map.png") + ")",
                backgroundRepeat: "no-repeat",
                backgroundSize: "cover",
                backgroundPosition: "center"
            }
        }
    }
}
</script>