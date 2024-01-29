Name:           xeus-zmq
Version:        1.1.1
Release:        2%{?dist}
Summary:        ZeroMQ based middleware for xeus

License:        BSD-3-Clause
URL:            https://github.com/jupyter-xeus/xeus-zmq
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Xeus is not available for i686
# https://src.fedoraproject.org/rpms/xeus/blob/rawhide/f/xeus.spec
ExcludeArch: %{ix86}

BuildRequires:  cmake
BuildRequires:  cppzmq-devel
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  xeus-devel
BuildRequires:  xtl-devel
BuildRequires:  zeromq-devel
# Needed for tests
BuildRequires:  doctest-devel
BuildRequires:  python3-jupyter-kernel-test
BuildRequires:  python3-pytest

%description
xeus-zmq provides various implementations of the xserver API from
xeus, based on the ZeroMQ library. These implementations all
conform to the Jupyter Kernel Protocol specification.

%package devel
Summary:   ZeroMQ based middleware for xeus
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for xeus-zmq

%prep
%autosetup


%build
%cmake -DXEUS_ZMQ_BUILD_STATIC_LIBS=OFF \
       -DXEUS_ZMQ_BUILD_SHARED_LIBS=ON \
       -DXEUS_ZMQ_STATIC_DEPENDENCIES=OFF \
       -DXEUS_ZMQ_BUILD_TESTS=ON
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libxeus-zmq.so.2*

%files devel
%dir %{_includedir}/xeus-zmq
%{_includedir}/xeus-zmq/*.hpp
%dir %{_libdir}/cmake/xeus-zmq
%{_libdir}/cmake/xeus-zmq/*.cmake
%{_libdir}/libxeus-zmq.so

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 07 2023 Benson Muite <benson_muite@emailplus.org> - 1.1.1-1
- Initial package 
