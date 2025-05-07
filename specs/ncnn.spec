Name:           ncnn
Version:        20250503
Release:        %autorelease
Summary:        A high-performance neural network inference framework

License:        BSD-3-Clause AND BSD-2-Clause AND Zlib
URL:            https://github.com/Tencent/ncnn
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(glslang)
BuildRequires:  pkgconfig(protobuf)

%description
ncnn is a high-performance neural network inference computing framework
optimized for mobile platforms. ncnn is deeply considerate about deployment and
uses on mobile phones from the beginning of design. ncnn does not have third
party dependencies. It is cross-platform, and runs faster than all known open
source frameworks on mobile phone cpu. Developers can easily deploy deep
learning algorithm models to the mobile platform by using efficient ncnn
implementation, create intelligent APPs, and bring the artificial intelligence
to your fingertips. ncnn is currently being used in many Tencent applications,
such as QQ, Qzone, WeChat, Pitu and so on.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -GNinja \
    -DNCNN_SHARED_LIB=ON \
    -DNCNN_ENABLE_LTO=ON \
    -DNCNN_BUILD_EXAMPLES=ON \
    -DNCNN_VULKAN=ON \
    -DNCNN_SYSTEM_GLSLANG=ON \

%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libncnn.so.1*

%files devel
%{_includedir}/ncnn/
%{_bindir}/*2ncnn
%{_bindir}/ncnn*
%{_libdir}/cmake/ncnn/
%{_libdir}/libncnn.so
%{_libdir}/pkgconfig/ncnn.pc

%changelog
%autochangelog
