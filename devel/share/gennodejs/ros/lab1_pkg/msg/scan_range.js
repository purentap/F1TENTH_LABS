// Auto-generated. Do not edit!

// (in-package lab1_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class scan_range {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.max_range = null;
      this.min_range = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('max_range')) {
        this.max_range = initObj.max_range
      }
      else {
        this.max_range = 0.0;
      }
      if (initObj.hasOwnProperty('min_range')) {
        this.min_range = initObj.min_range
      }
      else {
        this.min_range = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type scan_range
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [max_range]
    bufferOffset = _serializer.float64(obj.max_range, buffer, bufferOffset);
    // Serialize message field [min_range]
    bufferOffset = _serializer.float64(obj.min_range, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type scan_range
    let len;
    let data = new scan_range(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [max_range]
    data.max_range = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [min_range]
    data.min_range = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lab1_pkg/scan_range';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '695dacd2312207ace73c5166f2eaf0ec';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    float64 max_range
    float64 min_range
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new scan_range(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.max_range !== undefined) {
      resolved.max_range = msg.max_range;
    }
    else {
      resolved.max_range = 0.0
    }

    if (msg.min_range !== undefined) {
      resolved.min_range = msg.min_range;
    }
    else {
      resolved.min_range = 0.0
    }

    return resolved;
    }
};

module.exports = scan_range;
