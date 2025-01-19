%global username guacd

# Manual FFmpeg support override by passing "--with(out)=ffmpeg" to mock/rpmbuild
%if 0%{?fedora} || 0%{?rhel} >= 9
%global _with_ffmpeg 1
%endif

Name:           guacamole-server
Version:        1.5.5
Release:        5%{?dist}
Summary:        Server-side native components that form the Guacamole proxy
License:        Apache-2.0
URL:            https://guacamole.apache.org/

Source0:        https://github.com/apache/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysusersd
# Add compatibility with FFMPEG 7.0
# https://github.com/apache/guacamole-server/pull/518
Patch1:         0001-Add-compatibility-with-FFMPEG-7.0.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freerdp-client2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtelnet)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(winpr2)

%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
}

%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

%package -n libguac
Summary:        The common library used by all C components of Guacamole

%description -n libguac
libguac is the core library for guacd (the Guacamole proxy) and any protocol
support plugins for guacd. libguac provides efficient buffered I/O of text and
base64 data, as well as somewhat abstracted functions for sending Guacamole
instructions.

%package -n libguac-devel
Summary:        Development files for %{name}
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-devel
The libguac-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libguac-client-kubernetes
Summary:        Kubernetes pods terminal support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-kubernetes
libguac-client-kubernetes is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for attaching to terminals of containers running
in Kubernetes pods.

%package -n libguac-client-rdp
Summary:        RDP support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-rdp
libguac-client-rdp is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for RDP, the proprietary remote desktop protocol used by
Windows Remote Deskop / Terminal Services, via the libfreerdp library.

%package -n libguac-client-ssh
Summary:        SSH support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-ssh
libguac-client-ssh is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for SSH, the secure shell.

%package -n libguac-client-vnc
Summary:        VNC support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-vnc
libguac-client-vnc is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for VNC via the libvncclient library (part of
libvncserver).

%package -n libguac-client-telnet
Summary:        Telnet support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-telnet
libguac-client-telnet is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for Telnet via the libtelnet library.

%package -n guacd
Summary:        Proxy daemon for Guacamole
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%{?systemd_requires}
%{?sysusers_requires_compat}

%description -n guacd
guacd is the Guacamole proxy daemon used by the Guacamole web application and
framework to translate between arbitrary protocols and the Guacamole protocol.

%prep
%autosetup -p1

%build
# Guacamole 1.5.0 doesn't build warning-free with FFmpeg
%{?_with_ffmpeg:
export CFLAGS="%{optflags} -Wno-error=discarded-qualifiers"
}

autoreconf -vif
%configure \
  --disable-silent-rules \
  --disable-static

%make_build

pushd doc/libguac/
  doxygen Doxyfile
popd

pushd doc/libguac-terminal/
  doxygen Doxyfile
popd

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

mkdir html
cp -a doc/libguac/doxygen-output/html/ html/libguac/
cp -a doc/libguac-terminal/doxygen-output/html/ html/libguac-terminal/

mkdir -p %{buildroot}%{_sharedstatedir}/guacd

# Systemd unit files
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/guacd.service
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_sysusersdir}/guacd.conf

%pre -n guacd
%sysusers_create_compat %{SOURCE2}

%post -n guacd
%systemd_post guacd.service

%preun -n guacd
%systemd_preun guacd.service

%postun -n guacd
%systemd_postun_with_restart guacd.service

%ldconfig_scriptlets -n libguac

%ldconfig_scriptlets -n libguac-client-kubernetes

%ldconfig_scriptlets -n libguac-client-rdp

%ldconfig_scriptlets -n libguac-client-ssh

%ldconfig_scriptlets -n libguac-client-vnc

%ldconfig_scriptlets -n libguac-client-telnet

%files -n libguac
%license LICENSE
%doc README CONTRIBUTING
%{_libdir}/libguac.so.24*
%{_libdir}/libguac-terminal.so.0*

%files -n libguac-devel
%doc html
%{_includedir}/guacamole/
%{_libdir}/libguac.so
%{_libdir}/libguac-terminal.so

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".

%files -n libguac-client-kubernetes
%{_libdir}/libguac-client-kubernetes.so
%{_libdir}/libguac-client-kubernetes.so.0*

%files -n libguac-client-rdp
%{_libdir}/libguac-client-rdp.so
%{_libdir}/libguac-client-rdp.so.0*
%{_libdir}/freerdp2/libguac-common-svc-client.so
%{_libdir}/freerdp2/libguacai-client.so

%files -n libguac-client-ssh
%{_libdir}/libguac-client-ssh.so
%{_libdir}/libguac-client-ssh.so.0*

%files -n libguac-client-vnc
%{_libdir}/libguac-client-vnc.so
%{_libdir}/libguac-client-vnc.so.0*

%files -n libguac-client-telnet
%{_libdir}/libguac-client-telnet.so
%{_libdir}/libguac-client-telnet.so.0*

%files -n guacd
%{_bindir}/guaclog
%{?_with_ffmpeg:
%{_bindir}/guacenc
%{_mandir}/man1/guacenc.1*
}
%{_mandir}/man1/guaclog.1*
%{_mandir}/man5/guacd.conf.5*
%{_mandir}/man8/guacd.8*
%{_sbindir}/guacd
%{_unitdir}/guacd.service
%{_sysusersdir}/guacd.conf
%attr(750,%{username},%{username}) %{_sharedstatedir}/guacd/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.5-4
- Add patch for FFMPEG 7 compatibility

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 1.5.5-3
- Rebuild for ffmpeg 7

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 06 2024 Robert Scheck <robert@fedoraproject.org> - 1.5.5-1
- Update to 1.5.5 (#2272293)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 09 2023 Robert Scheck <robert@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4 (#2223510)

* Wed Aug 02 2023 Robert Scheck <robert@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3 (#2223510)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 07 2023 Robert Scheck <robert@fedoraproject.org> - 1.5.2-2
- Added upstream patch to fix RDP related segfault (GUACAMOLE-1802)

* Sat May 27 2023 Robert Scheck <robert@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2 (#2208446)

* Sat Apr 15 2023 Robert Scheck <robert@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1 (#2185877)

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.5.0-2
- Rebuild for ffmpeg 6.0

* Sun Feb 19 2023 Robert Scheck <robert@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#2169593)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Simone Caronni <negativo17@gmail.com> - 1.4.0-6
- Rebuild for updated FreeRDP.

* Sat Jul 30 2022 Robert Scheck <robert@fedoraproject.org> - 1.4.0-5
- Added sysusers.d file to achieve user() and group() provides

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.0-3
- Rebuild for libwebsockets soname bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Robert Scheck <robert@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#2035998)

* Wed Nov 10 2021 Simone Caronni <negativo17@gmail.com> - 1.3.0-9
- Rebuild for updated FreeRDP.

* Tue Sep 14 2021 Robert Scheck <robert@fedoraproject.org> - 1.3.0-8
- Use -Wno-error=deprecated-declarations with OpenSSL 3.0.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.3.0-7
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 31 2021 Robert Scheck <robert@fedoraproject.org> - 1.3.0-6
- Rebuilt for libwebsockets 4.2.0 (#1997842)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 1.3.0-4
- Rebuild for updated FreeRDP.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 2021 Simone Caronni <negativo17@gmail.com> - 1.3.0-1
- Update to 1.3.0.

* Sat Dec 26 2020 Simone Caronni <negativo17@gmail.com> - 1.2.0-3
- Do not ship deprecated sysconfig file.
- Trim changelog.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Simone Caronni <negativo17@gmail.com> - 1.2.0-1
- Update to 1.2.0.

* Fri May 22 2020 Simone Caronni <negativo17@gmail.com> - 1.1.0-6
- Rebuild for updated FreeRDP.

* Sat Feb 08 2020 Simone Caronni <negativo17@gmail.com> - 1.1.0-5
- Update to final 1.1.0, switch to FreeRDP 2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4.20190711git1a9d1e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-3.20190711git1a9d1e8
- Rebuild for libwebsockets 3.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.20190711git1a9d1e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Simone Caronni <negativo17@gmail.com> - 1.1.0-1.20190711git1a9d1e8
- Update to 1.1.0 snapshot, enable Kubernetes plugin.
- Fix license.
- Drop RHEL 6 support.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- Update to version 1.0.0.
