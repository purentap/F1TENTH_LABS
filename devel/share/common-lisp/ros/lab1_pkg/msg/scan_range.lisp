; Auto-generated. Do not edit!


(cl:in-package lab1_pkg-msg)


;//! \htmlinclude scan_range.msg.html

(cl:defclass <scan_range> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (max_range
    :reader max_range
    :initarg :max_range
    :type cl:float
    :initform 0.0)
   (min_range
    :reader min_range
    :initarg :min_range
    :type cl:float
    :initform 0.0))
)

(cl:defclass scan_range (<scan_range>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <scan_range>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'scan_range)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lab1_pkg-msg:<scan_range> is deprecated: use lab1_pkg-msg:scan_range instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <scan_range>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab1_pkg-msg:header-val is deprecated.  Use lab1_pkg-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'max_range-val :lambda-list '(m))
(cl:defmethod max_range-val ((m <scan_range>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab1_pkg-msg:max_range-val is deprecated.  Use lab1_pkg-msg:max_range instead.")
  (max_range m))

(cl:ensure-generic-function 'min_range-val :lambda-list '(m))
(cl:defmethod min_range-val ((m <scan_range>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab1_pkg-msg:min_range-val is deprecated.  Use lab1_pkg-msg:min_range instead.")
  (min_range m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <scan_range>) ostream)
  "Serializes a message object of type '<scan_range>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'max_range))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'min_range))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <scan_range>) istream)
  "Deserializes a message object of type '<scan_range>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_range) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'min_range) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<scan_range>)))
  "Returns string type for a message object of type '<scan_range>"
  "lab1_pkg/scan_range")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'scan_range)))
  "Returns string type for a message object of type 'scan_range"
  "lab1_pkg/scan_range")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<scan_range>)))
  "Returns md5sum for a message object of type '<scan_range>"
  "695dacd2312207ace73c5166f2eaf0ec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'scan_range)))
  "Returns md5sum for a message object of type 'scan_range"
  "695dacd2312207ace73c5166f2eaf0ec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<scan_range>)))
  "Returns full string definition for message of type '<scan_range>"
  (cl:format cl:nil "Header header~%float64 max_range~%float64 min_range~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'scan_range)))
  "Returns full string definition for message of type 'scan_range"
  (cl:format cl:nil "Header header~%float64 max_range~%float64 min_range~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <scan_range>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <scan_range>))
  "Converts a ROS message object to a list"
  (cl:list 'scan_range
    (cl:cons ':header (header msg))
    (cl:cons ':max_range (max_range msg))
    (cl:cons ':min_range (min_range msg))
))
