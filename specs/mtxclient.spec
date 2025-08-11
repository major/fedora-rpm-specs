Name: mtxclient
Version: 0.10.1
Release: %autorelease

License: MIT
Summary: Client API library for Matrix, built on top of Boost.Asio
URL: https://github.com/Nheko-Reborn/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

BuildRequires: cmake(fmt) >= 9.1.0
BuildRequires: cmake(mpark_variant)
BuildRequires: cmake(nlohmann_json) >= 3.11.0
BuildRequires: cmake(Olm) >= 3.2.12
BuildRequires: cmake(spdlog) >= 1.0.0

BuildRequires: pkgconfig(coeurl) >= 0.3.1
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(zlib)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DHUNTER_ENABLED:BOOL=OFF \
    -DUSE_BUNDLED_COEURL:BOOL=OFF \
    -DUSE_BUNDLED_GTEST:BOOL=OFF \
    -DUSE_BUNDLED_JSON:BOOL=OFF \
    -DUSE_BUNDLED_LIBCURL:BOOL=OFF \
    -DUSE_BUNDLED_LIBEVENT:BOOL=OFF \
    -DUSE_BUNDLED_OLM:BOOL=OFF \
    -DUSE_BUNDLED_OPENSSL:BOOL=OFF \
    -DUSE_BUNDLED_SPDLOG:BOOL=OFF \
    -DASAN:BOOL=OFF \
    -DCOVERAGE:BOOL=OFF \
    -DIWYU:BOOL=OFF \
    -DBUILD_LIB_TESTS:BOOL=OFF \
    -DBUILD_LIB_EXAMPLES:BOOL=OFF
%cmake_build

%install
%cmake_install
ln -s libmatrix_client.so.%{version} %{buildroot}%{_libdir}/libmatrix_client.so.0

%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.0*

%files devel
%{_includedir}/%{name}
%{_includedir}/mtx
%{_includedir}/mtx.hpp
%{_libdir}/cmake/MatrixClient
%{_libdir}/*.so

%changelog
%autochangelog
