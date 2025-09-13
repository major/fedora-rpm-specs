%bcond CHECK 1

Name:           ngtcp2
Version:        1.15.1
Release:        %autorelease
Summary:        Implementation of RFC 9000 QUIC protocol

License:        MIT
URL:            https://github.com/ngtcp2/ngtcp2
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf4f3b91474d1eb29889bd0ef7e8403d5d673c366#/tatsuhiro-t.asc
# Release does not contain all parts to build documentation
# https://github.com/ngtcp2/ngtcp2/pull/1404
Source3:        %{url}/raw/refs/tags/v%{version}/doc/mkapiref.py
Source4:        %{url}/raw/refs/tags/v%{version}/doc/source/index.rst
Source5:        %{url}/raw/refs/tags/v%{version}/doc/source/programmers-guide.rst

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gnutls-devel >= 3.7.5
BuildRequires:  libev-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  gnupg2

%description
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

%package devel
Summary:        The ngtcp2 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

Development headers and libraries.

%package doc
Summary:        The ngtcp2 API documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

Development API documentation.

%prep
%autosetup -p1
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
install -p -m 755 %{SOURCE3} doc/
install -p -m 644 %{SOURCE4} doc/source/
install -p -m 644 %{SOURCE5} doc/source/


%build
autoreconf -fsi
%configure --with-gnutls --with-libev --disable-static --enable-werror
%make_build
%make_build html

rm -f doc/build/html/.buildinfo


%install
%make_install
# Required on epel9
rm -f ${RPM_BUILD_ROOT}%{_libdir}/lib%{name}*.la

%check
%if %{with CHECK}
# does not yet compile: https://github.com/ngtcp2/ngtcp2/issues/1673
%make_build check
%endif

%files
%license COPYING
%doc README.rst
#doc SECURITY.md
%doc AUTHORS
%{_libdir}/libngtcp2.so.16*
%{_libdir}/libngtcp2_crypto_gnutls.so.8*


%files devel
%doc ChangeLog
%{_libdir}/libngtcp2.so
%{_libdir}/libngtcp2_crypto_gnutls.so
%{_libdir}/pkgconfig/libngtcp2.pc
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc
%{_includedir}/%{name}/


%files doc
%doc doc/build/html/


%changelog
%autochangelog
