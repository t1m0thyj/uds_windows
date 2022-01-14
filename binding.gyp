{
  "targets": [
    {
      "target_name": "uds_windows",
      "sources": [
        "src/binding.cc",
        "src/native-emitter.cc"
      ],
      "include_dirs": ["<!@(node -p \"require('node-addon-api').include\")"],
      "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      }
    }
  ]
}
