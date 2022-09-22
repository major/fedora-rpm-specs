%undefine __cmake_in_source_build
%global sover   2

Name:           toxcore
Version:        0.2.13
Release:        %autorelease
Summary:        Peer to peer instant messenger

# GPLv3+: main library
# BSD: toxencryptsave/crypto_pwhash_scryptsalsa208sha256
# ISC: toxcore/crypto_core_mem.c
License:        GPLv3+ and BSD and ISC
URL:            https://github.com/TokTok/c-toxcore
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/TokTok/c-toxcore/issues/1144
Patch0:         toxcore-0.2.12-install_libmisc.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)

%description
Tox is a peer to peer (serverless) instant messenger aimed at making
security and privacy easy to obtain for regular users. It uses NaCl
for its encryption and authentication.

%package devel
Summary:        Development files for Toxcore
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Tox is a peer to peer (serverless) instant messenger aimed at making
security and privacy easy to obtain for regular users. It uses NaCl
for its encryption and authentication.

This package contains Toxcore development files.

%prep
%autosetup -p1 -n c-%{name}-%{version}

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake -DSTRICT_ABI=ON
%cmake_build

%install
%cmake_install
rm -v %{buildroot}/%{_libdir}/*.a

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/DHT_bootstrap
%{_libdir}/libtoxcore.so.%{sover}*
%{_libdir}/libmisc_tools.so

%files devel
%{_includedir}/tox/
%{_libdir}/libtoxcore.so
%{_libdir}/pkgconfig/toxcore.pc

%changelog
%autochangelog
