Name:           dante
Version:        1.4.3
Release:        %autorelease
Summary:        A free SOCKS v4/v5 client implementation
License:        BSD-Inferno-Nettverk
URL:            https://www.inet.no/%{name}
Source0:        https://www.inet.no/%{name}/files/%{name}-%{version}.tar.gz
Source1:        sockd.service
Patch0:         dante-1.4.3-HAVE_SENDBUF_IOCTL.patch
Patch1:         dante-1.4.3-SETGROUPS.patch
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  miniupnpc-devel
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

%description
Dante is a free implementation of the SOCKS proxy protocol, version 4,
and version 5 (rfc1928). It can be used as a firewall between
networks. It is being developed by Inferno Nettverk A/S, a Norwegian
consulting company. Commercial support is available.

This package contains the dynamic libraries required to "socksify"
existing applications, allowing them to automatically use the SOCKS
protocol.

%package server
Summary:        A free SOCKS v4/v5 server implementation
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description server
This package contains "sockd", the SOCKS proxy daemon and its
documentation.  This is the server part of the Dante SOCKS proxy
package and allows SOCKS clients to connect through it to the external
network.

%package devel
Summary:        Development libraries for SOCKS
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Additional libraries required to compile programs that use SOCKS.

%prep
%autosetup -p1

%build
# Convert to utf-8
for file in CREDITS NEWS doc/socksify.1; do
  iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
  touch -r $file $file.new && \
  mv $file.new $file
done
# Set libc path
DANTELIBC=`find /%{_lib}/ -maxdepth 1 -iname "libc.so.*"`
# Add blank line because m4 does not like files ending with comments
echo >> acinclude.m4
# AM_CONFIG_HEADER macro is obsolete
sed -i -e 's!AM_CONFIG_HEADER!AC_CONFIG_HEADERS!' configure.ac
# Force reconf
autoreconf --force --install --verbose
# Change libdir because of unversionend libdsocks.so
# Disable static because libsocks has no debuginfo
# Disable libc_enable_secure rhbz#2271523
# Enable other features
%configure \
  --libdir=${exec_prefix}%{_libdir}/dante \
  --disable-static \
  --without-glibc-secure \
  --enable-preload \
  --enable-clientdl \
  --enable-serverdl \
  --enable-drt-fallback \
  --enable-shared \
  --with-libc=$DANTELIBC
# Fix unused-direct-shlib-dependency rpmlint error
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install

rm Makefile* SPECS/Makefile*
rm INSTALL

mkdir -p %{buildroot}/%{_sysconfdir} %{buildroot}/%{_unitdir}
install -m 644 example/socks.conf %{buildroot}/%{_sysconfdir}
install -m 644 example/sockd.conf %{buildroot}/%{_sysconfdir}
install -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/sockd.service

%post server
%systemd_post sockd.service

%preun server
%systemd_preun sockd.service

%postun server
%systemd_postun sockd.service

%files
%license LICENSE
%doc BUGS CREDITS NEWS README SUPPORT doc/README* example/socks.conf example/sockd.conf
%dir %{_libdir}/dante
%config(noreplace) %{_sysconfdir}/socks.conf
%{_libdir}/dante/libsocks.so.0.1.1
%{_libdir}/dante/libsocks.so.0
%{_libdir}/dante/libdsocks.so
%{_bindir}/socksify
%{_mandir}/man1/socksify.1*
%{_mandir}/man5/socks.conf.5*

%files server
%config(noreplace) %{_sysconfdir}/sockd.conf
%{_sbindir}/sockd
%{_mandir}/man5/sockd.conf.5*
%{_mandir}/man8/sockd.8*
%{_unitdir}/sockd.service

%files devel
%doc doc/rfc* doc/SOCKS4.protocol
%{_libdir}/dante/libsocks.so
%{_includedir}/socks.h
# Older RPM versions (<4.17) do not automatically remove *.la files
%if 0%{?rhel}
%exclude %{_libdir}/dante/*.la
%endif

%changelog
%autochangelog
