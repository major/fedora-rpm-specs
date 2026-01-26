%global abi_ver 9

Name:           nghttp3
Version:        1.15.0
Release:        %autorelease
Summary:        HTTP/3 library written in C

License:        MIT
URL:            https://github.com/ngtcp2/nghttp3
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source:         https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf4f3b91474d1eb29889bd0ef7e8403d5d673c366#/tatsuhiro-t.asc

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gpgverify
BuildRequires:  libtool
BuildRequires:  make

%global _description %{expand:
nghttp3 is an implementation of RFC 9114 HTTP/3 mapping over QUIC
and RFC 9204 QPACK in C.
It does not depend on any particular QUIC transport implementation.}

%description %{_description}


%package -n     libnghttp3
Summary:        HTTP/3 library written in C

%description -n libnghttp3 %{_description}


%package -n     libnghttp3-devel
Summary:        Development files for libnghttp3
Requires:       libnghttp3%{?_isa} = %{version}-%{release}

%description -n libnghttp3-devel %{_description}

The libnghttp3-devel package contains libraries and header files for
developing applications that use libnghttp3.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
autoreconf -fiv
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# will be installed via %%doc
rm -f %{buildroot}%{_docdir}/nghttp3/README.rst


%check
%make_build check


%files -n libnghttp3
%license COPYING
%doc README.rst
%{_libdir}/libnghttp3.so.%{abi_ver}{,.*}

%files -n libnghttp3-devel
%{_includedir}/nghttp3
%{_libdir}/libnghttp3.so
%{_libdir}/pkgconfig/libnghttp3.pc


%changelog
%autochangelog
