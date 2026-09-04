#include <cstdio>
#include <cstdint>
#include <vector>
#include <fstream>
#include <cstring>
#include "lzham.h"
int main(int argc,char**argv){if(argc<3)return 2;std::ifstream f(argv[1],std::ios::binary);std::vector<uint8_t>b((std::istreambuf_iterator<char>(f)),{}); if(b.size()<16)return 3; uint32_t outlen=b[12]|(b[13]<<8)|(b[14]<<16)|(b[15]<<24); lzham_decompress_params p{};p.m_struct_size=sizeof(p);p.m_dict_size_log2=15;p.m_decompress_flags=LZHAM_DECOMP_FLAG_READ_ZLIB_STREAM;std::vector<uint8_t>out(outlen);size_t dst=out.size();uint32_t ad=0;auto s=lzham_decompress_memory(&p,out.data(),&dst,b.data()+16,b.size()-16,&ad);fprintf(stderr,"status=%d n=%zu ad=%08x\n",(int)s,dst,ad);if(s<0)return 4;std::ofstream o(argv[2],std::ios::binary);o.write((char*)out.data(),dst);return 0;}