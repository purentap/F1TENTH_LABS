;; Auto-generated. Do not edit!


(when (boundp 'lab1_pkg::scan_range)
  (if (not (find-package "LAB1_PKG"))
    (make-package "LAB1_PKG"))
  (shadow 'scan_range (find-package "LAB1_PKG")))
(unless (find-package "LAB1_PKG::SCAN_RANGE")
  (make-package "LAB1_PKG::SCAN_RANGE"))

(in-package "ROS")
;;//! \htmlinclude scan_range.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass lab1_pkg::scan_range
  :super ros::object
  :slots (_header _max_range _min_range ))

(defmethod lab1_pkg::scan_range
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:max_range __max_range) 0.0)
    ((:min_range __min_range) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _max_range (float __max_range))
   (setq _min_range (float __min_range))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:max_range
   (&optional __max_range)
   (if __max_range (setq _max_range __max_range)) _max_range)
  (:min_range
   (&optional __min_range)
   (if __min_range (setq _min_range __min_range)) _min_range)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _max_range
    8
    ;; float64 _min_range
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _max_range
       (sys::poke _max_range (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _min_range
       (sys::poke _min_range (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _max_range
     (setq _max_range (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _min_range
     (setq _min_range (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get lab1_pkg::scan_range :md5sum-) "695dacd2312207ace73c5166f2eaf0ec")
(setf (get lab1_pkg::scan_range :datatype-) "lab1_pkg/scan_range")
(setf (get lab1_pkg::scan_range :definition-)
      "Header header
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

")



(provide :lab1_pkg/scan_range "695dacd2312207ace73c5166f2eaf0ec")


