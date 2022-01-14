const { EventEmitter } = require("events");
const { inherits } = require("util");
const { NativeEmitter } = require("bindings")("uds_windows");

inherits(NativeEmitter, EventEmitter);

const emitter = new NativeEmitter();

emitter.on("start", () => {
    console.log("### START ...");
});

emitter.on("data", (evt) => {
    console.log(evt);
});

emitter.on("end", () => {
    console.log("### END ###");
});

emitter.callAndEmit();
