Name: dmapd
Version: 0.0.96
Release: %autorelease
Summary: A server that provides DAAP and DPAP shares

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.flyn.org/projects/dmapd/
Source0: http://www.flyn.org/projects/%name/%{name}-%{version}.tar.gz

%{?systemd_requires}
BuildRequires: libdmapsharing4-devel >= 3.9.3
BuildRequires: vips-devel >= 7.38
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: totem-pl-parser-devel
BuildRequires: systemd
BuildRequires: make
Requires(post): systemd-units systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units

%description 
The dmapd project provides a GObject-based, Open Source implementation 
of DMAP sharing with the following features:

 o Support for both DAAP and DPAP

 o Support for realtime transcoding of media formats not natively 
 supported by clients

 o Support for many metadata formats, such as those associated with Ogg 
 Vorbis and MP3 (e.g., ID3)

 o Detection of video streams so that clients may play them as video

 o Use of GStreamer to support a wide range of audio and video CODECs

 o Caching of photograph thumbnails to avoid regenerating them each time 
 the server restarts

Dmapd runs on Linux and other POSIX operating systems. It has been 
used on OpenWrt Linux-based systems with as little as 32MB of memory 
to serve music, video and photograph libraries containing thousands of 
files.

%prep
%autosetup -p1

# Create a sysusers.d config file
cat >dmapd.sysusers.conf <<EOF
u dmapd - 'dmapd Daemon' - -
EOF

%build
%configure                                      \
	--disable-static                        \
	--disable-tests                         \
	--with-systemdsystemunitdir=%{_unitdir} \

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/libdmapd.la
rm -f %{buildroot}%{_libdir}/dmapd/%{version}/modules/*.la
rm -f %{buildroot}%{_sbindir}/dmapd-test
mkdir -p %{buildroot}%{_localstatedir}/cache/dmapd/DAAP
mkdir -p %{buildroot}%{_localstatedir}/cache/dmapd/DPAP
mkdir -p %{buildroot}%{_localstatedir}/run/dmapd
install -D -p -m 644 distro/dmapd.conf %{buildroot}%{_sysconfdir}/dmapd.conf

install -m0644 -D dmapd.sysusers.conf %{buildroot}%{_sysusersdir}/dmapd.conf

%files 
%{_libdir}/*.so.0
%{_libdir}/*.so.%{version}
%{_libdir}/dmapd
%{_sbindir}/dmapd
%{_bindir}/dmapd-transcode
%{_bindir}/dmapd-hashgen
%config(noreplace) %{_sysconfdir}/dmapd.conf
%attr(0700,dmapd,root) %{_localstatedir}/cache/dmapd/
%attr(0700,dmapd,root) %{_localstatedir}/run/dmapd
%{_mandir}/*/*
%{_unitdir}/dmapd.service
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README FAQ 
%{_sysusersdir}/dmapd.conf


%post
/sbin/ldconfig
%systemd_post dmapd.service

%preun
%systemd_preun dmapd.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart dmapd.service

# FIXME: Remove once Fedora 15 EOL'ed.
# See http://fedoraproject.org/wiki/Packaging:ScriptletSnippets
%triggerun -- dmapd < 0.0.37-2
%{_bindir}/systemd-sysv-convert --save dmapd >/dev/null 2>&1 || :
/bin/systemctl --no-reload enable dmapd.service >/dev/null 2>&1 || :
/sbin/chkconfig --del dmapd >/dev/null 2>&1 || :
/bin/systemctl try-restart dmapd.service >/dev/null 2>&1 || :

%package devel
Summary: Files needed to develop modules using dmapd's libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the libraries, include files, and other 
resources needed for developing modules using dmapd's API.

%files devel
%{_libdir}/pkgconfig/dmapd.pc
%{_includedir}/dmapd-*/
%{_libdir}/*.so
%ghost %attr(0755,dmapd,dmapd) %dir %{_localstatedir}/run/dmapd
%ghost %attr(0600,root,root) %{_localstatedir}/lock/subsys/dmapd

%changelog
%autochangelog
