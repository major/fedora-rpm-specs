%global common_description %{expand:
This package provides a set of C++ libraries for multimedia streaming, using
using open standard protocols (RTP/RTCP, RTSP, SIP). These libraries can be
used  to build streaming applications.

The libraries can also be used to stream, receive, and process MPEG, H.263+ or
JPEG video, and several audio codecs. They can easily be extended to support
additional (audio and/or video) codecs, and can also be used to build basic
RTSP or SIP clients and servers, and have been used to add streaming support to
existing media player applications.}

Name:           live555
Version:        2025.05.08
Release:        %autorelease
Summary:        RTP/RTCP/RTSP/SIP multimedia streaming libraries

License:        LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            http://live555.com/liveMedia
Source:         %{url}/public/live.%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel

%description    %{common_description}

%package        devel
Summary:        Development files for live555.com streaming libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains development headers and libraries for live555.

%package        tools
Summary:        RTSP streaming tools using live555.com streaming libraries

%description    tools %{common_description}

This package contains the live555.com streaming server (live555MediaServer),
the example programs (openRTSP, playSIP, sapWatch, vobStreamer) and a variety
of test tools.

%prep
%setup -q -n live

%build
# C++20 is because of:
# BasicTaskScheduler.cpp:191:40: error: 'struct std::atomic_flag' has no member named 'test'
export CXXFLAGS="-std=c++20 %{optflags}"

./genMakefiles %{_target_os}-with-shared-libraries
%make_build

%install
%make_install PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

# Fix library dependency detection
chmod +x %{buildroot}%{_libdir}/*.so*

%files
%license COPYING COPYING.LESSER
%doc README
%{_libdir}/libBasicUsageEnvironment.so.2{,.*}
%{_libdir}/libgroupsock.so.30{,.*}
%{_libdir}/libliveMedia.so.116{,.*}
%{_libdir}/libUsageEnvironment.so.3{,.*}

%files tools
%{_bindir}/live555HLSProxy
%{_bindir}/live555MediaServer
%{_bindir}/live555ProxyServer
%{_bindir}/mikeyParse
%{_bindir}/MPEG2TransportStreamIndexer
%{_bindir}/openRTSP
%{_bindir}/playSIP
%{_bindir}/registerRTSPStream
%{_bindir}/sapWatch
%{_bindir}/testAMRAudioStreamer
%{_bindir}/testDVVideoStreamer
%{_bindir}/testH264VideoStreamer
%{_bindir}/testH264VideoToHLSSegments
%{_bindir}/testH264VideoToTransportStream
%{_bindir}/testH265VideoStreamer
%{_bindir}/testH265VideoToTransportStream
%{_bindir}/testMKVSplitter
%{_bindir}/testMKVStreamer
%{_bindir}/testMP3Receiver
%{_bindir}/testMP3Streamer
%{_bindir}/testMPEG1or2AudioVideoStreamer
%{_bindir}/testMPEG1or2ProgramToTransportStream
%{_bindir}/testMPEG1or2Splitter
%{_bindir}/testMPEG1or2VideoReceiver
%{_bindir}/testMPEG1or2VideoStreamer
%{_bindir}/testMPEG2TransportReceiver
%{_bindir}/testMPEG2TransportStreamer
%{_bindir}/testMPEG2TransportStreamSplitter
%{_bindir}/testMPEG2TransportStreamTrickPlay
%{_bindir}/testMPEG4VideoStreamer
%{_bindir}/testOggStreamer
%{_bindir}/testOnDemandRTSPServer
%{_bindir}/testRelay
%{_bindir}/testReplicator
%{_bindir}/testRTSPClient
%{_bindir}/testWAVAudioStreamer
%{_bindir}/vobStreamer

%files devel
%{_libdir}/libBasicUsageEnvironment.so
%{_libdir}/libgroupsock.so
%{_libdir}/libliveMedia.so
%{_libdir}/libUsageEnvironment.so
%{_includedir}/BasicUsageEnvironment/
%{_includedir}/groupsock/
%{_includedir}/liveMedia/
%{_includedir}/UsageEnvironment/

%changelog
%autochangelog
