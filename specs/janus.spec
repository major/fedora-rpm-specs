%global __provides_exclude_from %{_includedir}/%{name}/events/.*\\.so$
%global __provides_exclude_from %{_includedir}/%{name}/loggers/.*\\.so$
%global __provides_exclude_from %{_includedir}/%{name}/plugins/.*\\.so$
%global __provides_exclude_from %{_includedir}/%{name}/transports/.*\\.so$

%global __requires_exclude_from %{_includedir}/%{name}/events/.*\\.so$
%global __requires_exclude_from %{_includedir}/%{name}/loggers/.*\\.so$
%global __requires_exclude_from %{_includedir}/%{name}/plugins/.*\\.so$
%global __requires_exclude_from %{_includedir}/%{name}/transports/.*\\.so$

%global api_version_major 2
%global api_version_minor 0
%global api_version_patch 7
%global api_version %{api_version_major}.%{api_version_minor}.%{api_version_patch}

Name: janus
Version: 1.3.2
Release: %autorelease
Summary: An open source WebRTC server designed and developed by Meetecho

License: GPL-3.0-only AND MIT AND BSD-3-Clause
URL: https://janus.conf.meetecho.com/
Source0: https://github.com/meetecho/%{name}-gateway/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.service
Source2: %{name}.sysusers

# this patch changes the use of TLS ciphers to use the system's default
patch0: janus-dtls.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: duktape-devel
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: jansson-devel

%if 0%{?rhel} == 8
BuildRequires: ffmpeg-devel
%endif

%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires: libavcodec-free-devel
BuildRequires: libavformat-free-devel
BuildRequires: libavutil-free-devel
%endif

BuildRequires: libconfig-devel
BuildRequires: libcurl-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libnice-devel
BuildRequires: libpcap-devel
BuildRequires: librabbitmq-devel
BuildRequires: libsrtp-devel
BuildRequires: libtool
BuildRequires: libwebsockets-devel
BuildRequires: lua-devel
BuildRequires: nanomsg-devel
BuildRequires: openssl-devel
BuildRequires: opus-devel
BuildRequires: paho-c-devel
BuildRequires: sofia-sip-devel
BuildRequires: speexdsp-devel
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
BuildRequires: usrsctp-devel
BuildRequires: zlib-devel

%description
Janus is an open source WebRTC server designed and developed by Meetecho.


%package devel
Summary: The %{name} header files and test scripts
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development package containing header files and what is required for %{name}
plugin development, as well as some test scripts.


%package eventhandlers-gelf
Summary: GELF event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-gelf
GELF event handler for %{name}.


%package eventhandlers-mqtt
Summary: MQTT event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-mqtt
MQTT event handler for %{name}.


%package eventhandlers-nanomsg
Summary: Nanomsg event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-nanomsg
Nanomsg event handler for %{name}.


%package eventhandlers-rabbitmq
Summary: RabbitMQ event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-rabbitmq
RabbitMQ event handler for %{name}.


%package eventhandlers-sample
Summary: Sample event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-sample
Sample event handler for %{name}.


%package eventhandlers-ws
Summary: WebSocket event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-ws
WebSocket event handler for %{name}.


%package loggers-json
Summary: A logger plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description loggers-json
This is a trivial logger plugin for %{name}.


%package plugins-audiobridge
Summary: An audio conference bridge plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-audiobridge
This is a plugin implementing an audio conference bridge for %{name}, specifically mixing Opus streams.


%package plugins-duktape
Summary: A simple bridge to JavaScript via Duktape for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-duktape
This is a plugin that implements a simple bridge to JavaScript via Duktape for
%{name}.


%package plugins-echotest
Summary: EchoTest plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-echotest
This is a trivial EchoTest plugin for %{name}, just used to showcase the plugin
interface.


%package plugins-lua
Summary: Simple bridge to Lua scripts for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lua-json
Requires: lua-term

%description plugins-lua
This is a plugin that implements a simple bridge to Lua scripts for %{name}.


%package plugins-nosip
Summary: Acts as an RTP bridge for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-nosip
This is quite a basic plugin, as it only takes care of acting as an RTP bridge
for %{name}.


%package plugins-recordplay
Summary: Record and playback of WebRTC messages for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-recordplay
This is a simple application that implements two different features for
%{name}: it allows you to record a message you send with WebRTC and
subsequently replay this recording (or other previously recorded) through
WebRTC as well.


%package plugins-sip
Summary: Allows WebRTC peers to register at a SIP server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-sip
This is a simple SIP plugin for Janus, allowing WebRTC peers to register at a
SIP server (e.g., Asterisk) and call SIP user agents through %{name}.


%package plugins-streaming
Summary: Streaming plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-streaming
This is a streaming plugin for %{name}, allowing WebRTC peers to watch/listen
to pre-recorded files or media generated by another tool.


%package plugins-textroom
Summary: A DataChannel only text room for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-textroom
This is a plugin implementing a DataChannel only text room for %{name}.


%package plugins-videocall
Summary: Allows two WebRTC peers to call each other through %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-videocall
This is a simple video call plugin for Janus, allowing two WebRTC peers to call
each other through %{name}.


%package plugins-videoroom
Summary: Videoconferencing SFU for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugins-videoroom
This is a plugin implementing a videoconferencing SFU (Selective Forwarding
Unit) for %{name}, that is an audio/video router.


%package tools
Summary: Janus' helper tools
Requires:%{name}%{?_isa} = %{version}-%{release}
Requires: gstreamer1-plugins-good%{?_isa}

%description tools
Janus' helper tools.


%package transports-http
Summary: RESTs transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}

%description transports-http
This is an implementation of a RESTs transport for the %{name} API, using the
libmicrohttpd library.


%package transports-mqtt
Summary: MQTT transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}

%description transports-mqtt
This is an implementation of a MQTT transport for the %{name} API, using the
Eclipse Paho C Client library.


%package transports-nanomsg
Summary: Nanomsg transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}

%description transports-nanomsg
This is an implementation of a Nanomsg transport for the %{name} API.


%package transports-pfunix
Summary: Unix Sockets transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}

%description transports-pfunix
This is an implementation of a Unix Sockets transport for the %{name} API.


%package transports-rabbitmq
Summary: RabbitMQ transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}

%description transports-rabbitmq
This is an implementation of a RabbitMQ transport for the %{name} API.


%package transports-websockets
Summary: WebSockets transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}

%description transports-websockets
This is an implementation of a WebSockets transport for the %{name} API.


%prep
%autosetup -p 1 -n %{name}-gateway-%{version}


%build
sh autogen.sh
%configure \
    --enable-docs \
    --enable-json-logger \
    --enable-plugin-audiobridge \
    --enable-plugin-duktape \
    --enable-plugin-lua \
    --enable-post-processing \
    --enable-systemd-sockets

%make_build

%check
make check


%install
%make_install

# generate configuration files
make DESTDIR=%{buildroot} configs

# make scripts executable
chmod 755 %{buildroot}%{_datadir}/%{name}/streams/*.sh

# systemd
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

# cleanup
rm -fr %{buildroot}%{_docdir}/%{name}-gateway
rm -fr %{buildroot}%{_datadir}/%{name}/html
rm -fr %{buildroot}%{_datadir}/%{name}/javascript
find %{buildroot} -type f -iname '*.la' -delete


%pre
%sysusers_create_compat %{SOURCE2}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
# licenses and docs
%license COPYING
%doc README.md
%doc SECURITY.md
%doc CHANGELOG.md

# binaries
%{_bindir}/%{name}
%{_bindir}/%{name}-cfgconv

# manuals
%{_mandir}/man1/%{name}-cfgconv.1.gz
%{_mandir}/man1/%{name}.1.gz

# samples
%doc %{_sysconfdir}/%{name}/%{name}.jcfg.sample

# configuration
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.jcfg

# systemd service unit
%{_unitdir}/%{name}.service

# systemd sysusers
%{_sysusersdir}/%{name}.conf

# lib filesystem
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/events
%dir %{_libdir}/%{name}/loggers
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/transports

# data filesystem
%dir %{_datadir}/%{name}


## event handlers
%files eventhandlers-gelf
%doc %{_sysconfdir}/%{name}/%{name}.eventhandler.gelfevh.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.eventhandler.gelfevh.jcfg
%{_libdir}/%{name}/events/libjanus_gelfevh.so
%{_libdir}/%{name}/events/libjanus_gelfevh.so.%{api_version_major}
%{_libdir}/%{name}/events/libjanus_gelfevh.so.%{api_version}


%files eventhandlers-mqtt
%doc %{_sysconfdir}/%{name}/%{name}.eventhandler.mqttevh.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.eventhandler.mqttevh.jcfg
%{_libdir}/%{name}/events/libjanus_mqttevh.so
%{_libdir}/%{name}/events/libjanus_mqttevh.so.%{api_version_major}
%{_libdir}/%{name}/events/libjanus_mqttevh.so.%{api_version}


%files eventhandlers-nanomsg
%doc %{_sysconfdir}/%{name}/%{name}.eventhandler.nanomsgevh.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.eventhandler.nanomsgevh.jcfg
%{_libdir}/%{name}/events/libjanus_nanomsgevh.so
%{_libdir}/%{name}/events/libjanus_nanomsgevh.so.%{api_version_major}
%{_libdir}/%{name}/events/libjanus_nanomsgevh.so.%{api_version}


%files eventhandlers-rabbitmq
%doc %{_sysconfdir}/%{name}/%{name}.eventhandler.rabbitmqevh.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.eventhandler.rabbitmqevh.jcfg
%{_libdir}/%{name}/events/libjanus_rabbitmqevh.so
%{_libdir}/%{name}/events/libjanus_rabbitmqevh.so.%{api_version_major}
%{_libdir}/%{name}/events/libjanus_rabbitmqevh.so.%{api_version}


%files eventhandlers-sample
%doc %{_sysconfdir}/%{name}/%{name}.eventhandler.sampleevh.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.eventhandler.sampleevh.jcfg
%{_libdir}/%{name}/events/libjanus_sampleevh.so
%{_libdir}/%{name}/events/libjanus_sampleevh.so.%{api_version_major}
%{_libdir}/%{name}/events/libjanus_sampleevh.so.%{api_version}


%files eventhandlers-ws
%doc %{_sysconfdir}/%{name}/%{name}.eventhandler.wsevh.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.eventhandler.wsevh.jcfg
%{_libdir}/%{name}/events/libjanus_wsevh.so
%{_libdir}/%{name}/events/libjanus_wsevh.so.%{api_version_major}
%{_libdir}/%{name}/events/libjanus_wsevh.so.%{api_version}


# loggers
%files loggers-json
%doc %{_sysconfdir}/%{name}/%{name}.logger.jsonlog.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.logger.jsonlog.jcfg
%{_libdir}/%{name}/loggers/libjanus_jsonlog.so
%{_libdir}/%{name}/loggers/libjanus_jsonlog.so.%{api_version_major}
%{_libdir}/%{name}/loggers/libjanus_jsonlog.so.%{api_version}


## plugins
%files plugins-audiobridge
%doc %{_sysconfdir}/%{name}/%{name}.plugin.audiobridge.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.audiobridge.jcfg
%{_libdir}/%{name}/plugins/libjanus_audiobridge.so
%{_libdir}/%{name}/plugins/libjanus_audiobridge.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_audiobridge.so.%{api_version}


%files plugins-duktape
%doc %{_sysconfdir}/%{name}/%{name}.plugin.duktape.jcfg.sample
%dir %{_datadir}/%{name}/duktape
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.duktape.jcfg
%{_datadir}/%{name}/duktape/echotest.js
%{_datadir}/%{name}/duktape/%{name}-sdp.js
%{_libdir}/%{name}/plugins/libjanus_duktape.so
%{_libdir}/%{name}/plugins/libjanus_duktape.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_duktape.so.%{api_version}


%files plugins-echotest
%doc %{_sysconfdir}/%{name}/%{name}.plugin.echotest.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.echotest.jcfg
%{_libdir}/%{name}/plugins/libjanus_echotest.so
%{_libdir}/%{name}/plugins/libjanus_echotest.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_echotest.so.%{api_version}


%files plugins-lua
%doc %{_sysconfdir}/%{name}/%{name}.plugin.lua.jcfg.sample
%dir %{_datadir}/%{name}/lua
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.lua.jcfg
%{_datadir}/%{name}/lua/echotest.lua
%{_datadir}/%{name}/lua/%{name}-logger.lua
%{_datadir}/%{name}/lua/%{name}-sdp.lua
%{_datadir}/%{name}/lua/videoroom.lua
%{_libdir}/%{name}/plugins/libjanus_lua.so
%{_libdir}/%{name}/plugins/libjanus_lua.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_lua.so.%{api_version}


%files plugins-nosip
%doc %{_sysconfdir}/%{name}/%{name}.plugin.nosip.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.nosip.jcfg
%{_libdir}/%{name}/plugins/libjanus_nosip.so
%{_libdir}/%{name}/plugins/libjanus_nosip.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_nosip.so.%{api_version}


%files plugins-recordplay
%doc %{_sysconfdir}/%{name}/%{name}.plugin.recordplay.jcfg.sample
%dir %{_datadir}/%{name}/recordings
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.recordplay.jcfg
%{_datadir}/%{name}/recordings/1234.nfo
%{_datadir}/%{name}/recordings/rec-sample-audio.mjr
%{_datadir}/%{name}/recordings/rec-sample-video.mjr
%{_libdir}/%{name}/plugins/libjanus_recordplay.so
%{_libdir}/%{name}/plugins/libjanus_recordplay.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_recordplay.so.%{api_version}


%files plugins-sip
%doc %{_sysconfdir}/%{name}/%{name}.plugin.sip.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.sip.jcfg
%{_libdir}/%{name}/plugins/libjanus_sip.so
%{_libdir}/%{name}/plugins/libjanus_sip.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_sip.so.%{api_version}


%files plugins-streaming
%doc %{_sysconfdir}/%{name}/%{name}.plugin.streaming.jcfg.sample
%dir %{_datadir}/%{name}/streams
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.streaming.jcfg
%{_datadir}/%{name}/streams/radio.alaw
%{_datadir}/%{name}/streams/remembrance.opus
%{_datadir}/%{name}/streams/test_gstreamer.sh
%{_datadir}/%{name}/streams/test_gstreamer1.sh
%{_datadir}/%{name}/streams/test_gstreamer1_multistream.sh
%{_datadir}/%{name}/streams/test_gstreamer_multistream.sh
%{_libdir}/%{name}/plugins/libjanus_streaming.so
%{_libdir}/%{name}/plugins/libjanus_streaming.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_streaming.so.%{api_version}


%files plugins-textroom
%doc %{_sysconfdir}/%{name}/%{name}.plugin.textroom.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.textroom.jcfg
%{_libdir}/%{name}/plugins/libjanus_textroom.so
%{_libdir}/%{name}/plugins/libjanus_textroom.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_textroom.so.%{api_version}


%files plugins-videocall
%doc %{_sysconfdir}/%{name}/%{name}.plugin.videocall.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.videocall.jcfg
%{_libdir}/%{name}/plugins/libjanus_videocall.so
%{_libdir}/%{name}/plugins/libjanus_videocall.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_videocall.so.%{api_version}


%files plugins-videoroom
%doc %{_sysconfdir}/%{name}/%{name}.plugin.videoroom.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.plugin.videoroom.jcfg
%{_libdir}/%{name}/plugins/libjanus_videoroom.so
%{_libdir}/%{name}/plugins/libjanus_videoroom.so.%{api_version_major}
%{_libdir}/%{name}/plugins/libjanus_videoroom.so.%{api_version}


# transports
%files transports-http
%doc %{_sysconfdir}/%{name}/%{name}.transport.http.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.transport.http.jcfg
%{_libdir}/%{name}/transports/libjanus_http.so
%{_libdir}/%{name}/transports/libjanus_http.so.%{api_version_major}
%{_libdir}/%{name}/transports/libjanus_http.so.%{api_version}


%files transports-mqtt
%doc %{_sysconfdir}/%{name}/%{name}.transport.mqtt.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.transport.mqtt.jcfg
%{_libdir}/%{name}/transports/libjanus_mqtt.so
%{_libdir}/%{name}/transports/libjanus_mqtt.so.%{api_version_major}
%{_libdir}/%{name}/transports/libjanus_mqtt.so.%{api_version}


%files transports-nanomsg
%doc %{_sysconfdir}/%{name}/%{name}.transport.nanomsg.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.transport.nanomsg.jcfg
%{_libdir}/%{name}/transports/libjanus_nanomsg.so
%{_libdir}/%{name}/transports/libjanus_nanomsg.so.%{api_version_major}
%{_libdir}/%{name}/transports/libjanus_nanomsg.so.%{api_version}


%files transports-pfunix
%doc %{_sysconfdir}/%{name}/%{name}.transport.pfunix.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.transport.pfunix.jcfg
%{_libdir}/%{name}/transports/libjanus_pfunix.so
%{_libdir}/%{name}/transports/libjanus_pfunix.so.%{api_version_major}
%{_libdir}/%{name}/transports/libjanus_pfunix.so.%{api_version}


%files transports-rabbitmq
%doc %{_sysconfdir}/%{name}/%{name}.transport.rabbitmq.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.transport.rabbitmq.jcfg
%{_libdir}/%{name}/transports/libjanus_rabbitmq.so
%{_libdir}/%{name}/transports/libjanus_rabbitmq.so.%{api_version_major}
%{_libdir}/%{name}/transports/libjanus_rabbitmq.so.%{api_version}


%files transports-websockets
%doc %{_sysconfdir}/%{name}/%{name}.transport.websockets.jcfg.sample
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.transport.websockets.jcfg
%{_libdir}/%{name}/transports/libjanus_websockets.so
%{_libdir}/%{name}/transports/libjanus_websockets.so.%{api_version_major}
%{_libdir}/%{name}/transports/libjanus_websockets.so.%{api_version}


%files devel
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/events
%dir %{_includedir}/%{name}/loggers
%dir %{_includedir}/%{name}/plugins
%dir %{_includedir}/%{name}/transports

# headers for plugin development
%{_includedir}/%{name}/apierror.h
%{_includedir}/%{name}/config.h
%{_includedir}/%{name}/debug.h
%{_includedir}/%{name}/events/eventhandler.h
%{_includedir}/%{name}/ip-utils.h
%{_includedir}/%{name}/log.h
%{_includedir}/%{name}/loggers/logger.h
%{_includedir}/%{name}/mutex.h
%{_includedir}/%{name}/plugins/plugin.h
%{_includedir}/%{name}/record.h
%{_includedir}/%{name}/refcount.h
%{_includedir}/%{name}/rtcp.h
%{_includedir}/%{name}/rtp.h
%{_includedir}/%{name}/rtpsrtp.h
%{_includedir}/%{name}/sdp-utils.h
%{_includedir}/%{name}/text2pcap.h
%{_includedir}/%{name}/transports/transport.h
%{_includedir}/%{name}/utils.h


%files tools
# binaries
%{_bindir}/%{name}-pp-rec
%{_bindir}/mjr2pcap
%{_bindir}/pcap2mjr

# manuals
%{_mandir}/man1/mjr2pcap.1.gz
%{_mandir}/man1/pcap2mjr.1.gz
%{_mandir}/man1/%{name}-pp-rec.1.gz


%changelog
%autochangelog
