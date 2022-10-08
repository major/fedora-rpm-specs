%global sover   2

%global common_description %{expand:
Tox is a peer to peer (serverless) instant messenger aimed at making
security and privacy easy to obtain for regular users. It uses NaCl
for its encryption and authentication.}

Name:           toxcore
Version:        0.2.18
Release:        %autorelease
Summary:        Peer to peer instant messenger

# GPLv3+: main library
# BSD: toxencryptsave/crypto_pwhash_scryptsalsa208sha256
# ISC: toxcore/crypto_core_mem.c
License:        GPLv3+ and BSD and ISC
URL:            https://github.com/TokTok/c-toxcore
Source0:        %{url}/releases/download/v%{version}/c-%{name}-%{version}.tar.gz
# fix: #1144 by forcing misc_tools to be a static lib
Patch0:         https://github.com/Green-Sky/c-toxcore/commit/39f5c24e374226c83b4af46b43779882010c5d86.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)

%description %{common_description}

%package devel
Summary:        Development files for Toxcore
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{common_description}

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

%files devel
%{_includedir}/tox/
%{_libdir}/libtoxcore.so
%{_libdir}/pkgconfig/toxcore.pc

%changelog
%autochangelog
