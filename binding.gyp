{
  "targets": [
    {
      "target_name": "dhc",
      "cflags!": [ "-O2 -fno-exceptions" ],
      "cflags_cc!": [ "-O2 -fno-exceptions" ],
      "sources": [
        "dhc/*.c",
        "wrapper.cpp"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}