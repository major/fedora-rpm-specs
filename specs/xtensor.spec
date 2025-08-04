%undefine __cmake_in_source_build

Name:           xtensor
Version:        0.27.0
Release:        %autorelease
Summary:        C++ tensors with broadcasting and lazy computing
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://xtensor.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  xtl-devel
BuildRequires:  xsimd-devel
BuildRequires:  python3-numpy
BuildRequires:  doctest-devel
BuildRequires:  json-devel

# there is no actual arched content - this is a header only library
%global debug_package %{nil}

%global _description %{expand:
xtensor is a C++ library meant for numerical analysis with multi-dimensional
array expressions.

xtensor provides:
- an extensible expression system enabling lazy broadcasting.
- an API following the idioms of the C++ standard library.
- tools to manipulate array expressions and build upon xtensor.}


%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       xtl-devel
Requires:       xsimd-devel

%description devel %_description


%prep
%autosetup -p1

%ifarch s390x
find -name '*.npy' -exec %{__python3} -c "import numpy as np; arr = np.load('{}').byteswap() ; np.save('{}', arr.view(arr.dtype.newbyteorder()))" \;
%endif

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%cmake_build --target xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
