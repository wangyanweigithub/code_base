#include <stdio.h>
extern "C" {
#include "libavcodec/avcodec.h"
#include "libavformat/avformat.h"
#include "libavutil/avutil.h"
}


int main(int argc,char* argv[])
{
    if(argc<2)
{
	printf("input a video file!\r\n");
}
    av_register_all();
    printf("the video file is %s\r\n",argv[1]);

    AVFormatContext *pFormatCtx;

    if(av_open_input_file(&pFormatCtx,argv[1],NULL,0,NULL)!=0)
    return -1;
    if(av_find_stream_info(pFormatCtx)<0)
        return -1;
    dump_format(pFormatCtx,0,argv[1],0);

    int i;
AVCodecContext *pCodecCtx;
    int videoStream = -1;
    for(i=0;i<pFormatCtx->nb_streams;i++)
    {
        if(pFormatCtx->streams[i]->codec->codec_type==CODEC_TYPE_VIDEO)
        {
            videoStream = i;
            break;
        }
    }
    if(videoStream==-1)
    {
        return -1;
    }
    pCodecCtx = pFormatCtx->streams[videoStream]->codec;

    AVCodec *pCodec;
    pCodec=avcodec_find_decoder(pCodecCtx->codec_id);
    if(pCodec==NULL){
        printf("Unspported codec!\n");
        return -1;
    }
    if(avcodec_open(pCodecCtx,pCodec)<0)
		return -1;
    printf("open file successed!\n");

    return 0;
}
