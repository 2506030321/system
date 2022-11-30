// userInfo盒子中的Eharts图
document.write("<script src='../js/eharts.min.js'></script>")
var myChart1 = echarts.init(document.querySelector('.ehart'));
var myChart2 = echarts.init(document.querySelector('.s'));
var myChart3 = echarts.init(document.querySelector('.NightingaleRoseChart'));
var myChart4 = echarts.init(document.querySelector('.SankeyChart'));
var option1 = {
    title: {
        text: '标签分析'
        
    },
    radar: {
        // shape: 'circle',
        indicator: [
        { name: '景色', max: 100 },
        { name: '动物', max: 100 },
        { name: '食物', max: 100 },
        { name: '运动', max: 100 },
        { name: '文化', max: 100 },
        { name: '娱乐', max: 100 }
        ]
    },
    series: [
        {
        type: 'radar',
        data: [
            {
            value: [77, 23, 24, 98, 56, 76],
            
            }
        ]
        }
    ]
    }; 
// 南丁格尔玫瑰图
var option3 = { 
  // title: {
  //   text: '城市热度'
  //   }, 
    // legend: {
    //   top: 'bottom'
    // },
    series: [
      {
        name: 'Nightingale Chart',
        type: 'pie',
        radius: [20, 140],
        center: ['50%', '50%'],
        roseType: 'area',
        itemStyle: {
          borderRadius: 8
        },
        label:{
            fontSize:12,
            color:'rgb(166, 172, 204)'
        },
        labelLine:{
            length: 1,
            length2: 5
        },
        data: [
          { value: 40, name: '西安' },
          { value: 50, name: '渭南' },
          { value: 32, name: '铜川' },
          { value: 30, name: '宝鸡' },
          { value: 28, name: '汉中' },
          { value: 26, name: '延安' },
          { value: 22, name: '咸阳' },
          { value: 26, name: '安康' },
          { value: 22, name: '商洛' },
          { value: 18, name: '榆林' }
        ]
      }
    ]
  };
// 桑基图
 var option4 = {
    series: {
      type: 'sankey',
      layout: 'none',
      emphasis: {
        focus: 'adjacency'
      },
      data: [
        {
          name: 'a'
        },
        {
          name: 'b'
        },
        {
          name: 'a1'
        },
        {
          name: 'a2'
        },
        {
          name: 'b1'
        },
        {
          name: 'c'
        }
      ],
      links: [
        {
          source: 'a',
          target: 'a1',
          value: 5
        },
        {
          source: 'a',
          target: 'a2',
          value: 3
        },
        {
          source: 'b',
          target: 'b1',
          value: 8
        },
        {
          source: 'a',
          target: 'b1',
          value: 3
        },
        {
          source: 'b1',
          target: 'a1',
          value: 1
        },
        {
          source: 'b1',
          target: 'c',
          value: 2
        }
      ]
    }
  };
myChart1.setOption(option1);
myChart2.setOption(option1);
myChart3.setOption(option3);
myChart4.setOption(option4);
window.addEventListener("resize",function(){
  myChart1.resize();
  myChart2.resize();
  myChart3.resize();
  myChart4.resize();
})
