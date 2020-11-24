import Base64 from './base64'
import iconsData from './icons-data'
Component({
  /**
   * Component properties
   */
  properties: {
    extClass: {
      type: String,
      value: ''
    },
    type: {
      type: String,
      value: 'outline',
      observer: '_genSrcByType'
    },
    icon: {
      type: String,
      value: '',
      observer: '_genSrcByIcon'
    },
    size: {
      type: Number,
      value: 20
    },
    color: {
      type: String,
      value: '#000000'
    }
  },

  /**
   * Component initial data
   */
  data: {
    src: '',
    height: 20,
    width: 20
  },

  /**
   * Component methods
   */
  methods: {
    _genSrcByIcon(v) {
      this._genSrc(iconsData[v][this.data.type])
    },
    _genSrcByType(v) {
      this._genSrc(iconsData[this.data.icon][v])
    },
    _genSrc(rawData) {
      if (!rawData) return
      const base64 = Base64.encode(rawData)
      this.setData({
        src: 'data:image/svg+xml;base64,' + base64
      })
    }
  }
})