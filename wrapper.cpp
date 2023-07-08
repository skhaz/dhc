#include <nan.h>

NAN_METHOD(DHC)
{
}

NAN_MODULE_INIT(Init)
{
  Nan::Set(target, Nan::New("dhc_decompress").ToLocalChecked(),
           Nan::GetFunction(Nan::New<v8::FunctionTemplate>(DHC)).ToLocalChecked());
}

NODE_MODULE(addon, Init)