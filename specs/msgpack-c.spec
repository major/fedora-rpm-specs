Name:           msgpack-c
Version:        7.0.0
Release:        %autorelease
Summary:        Binary-based efficient object serialization library

License:        BSL-1.0
URL:            https://msgpack.org
Source0:        https://github.com/msgpack/msgpack-c/releases/download/c-%{version}/%{name}-%{version}.tar.gz
# Fix INSTALL_INSTALL interface so users get the correct include directory
# https://github.com/msgpack/msgpack-c/pull/1177
Patch:          msgpack-c-interface.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doxygen
# for %%check
BuildRequires:  gtest-devel
BuildRequires:  zlib-devel

%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.


%package devel
Summary:        Libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for %{name}.


%prep
%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_INCLUDEDIR=include/msgpack-c -DMSGPACK_BUILD_TESTS=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%license LICENSE_1_0.txt COPYING
%doc ChangeLog NOTICE README README.md
%{_libdir}/libmsgpack-c.so.2{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libmsgpack-c.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
