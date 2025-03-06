Name:           xsimd
Version:        13.2.0
Release:        %autorelease
Summary:        C++ wrappers for SIMD intrinsic
License:        BSD-3-Clause
URL:            https://xsimd.readthedocs.io/
%global github  https://github.com/xtensor-stack/xsimd
Source:         %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doctest-devel

# there is no actual arched content - this is a header only library
%global debug_package %{nil}

%global _description \
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that \
has been available for many years. SIMD instructions perform a single operation \
on a batch of values at once, and thus provide a way to significantly \
accelerate code execution. However, these instructions differ between \
microprocessor vendors and compilers. \
 \
xsimd provides a unified means for using these features for library authors. \
Namely, it enables manipulation of batches of numbers with the same arithmetic \
operators as for single values. It also provides accelerated implementation \
of common mathematical functions operating on batches. \

%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

Patch0: https://github.com/xtensor-stack/xsimd/pull/1091.patch

%description devel %_description

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
# Explicitly not supported upstream for simd mode. Still valuable for scalar mode layer.
%ifnarch ppc64le s390x
%cmake_build -- xtest
%endif

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
