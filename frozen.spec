# Header-only package
%global debug_package %{nil}

Name:           frozen
Version:        1.1.1
Release:        5%{?dist}
Summary:        A header-only, constexpr alternative to gperf for C++14 users

License:        Apache-2.0
URL:            https://github.com/serge-sans-paille/frozen
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fixes FTBFS, already present in upstream main branch.
Patch0:         includes.patch
Patch1:         079f73cc5c6413127d47f325cbb34a607e2cb030.patch
# related: https://github.com/serge-sans-paille/frozen/pull/167
Patch2:         frozen-fix-arch-in-cmake.patch

BuildRequires: gcc-c++
BuildRequires: cmake

%description
Header-only library that provides 0 cost initialization
for immutable containers, fixed-size containers, and
various algorithms.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Requires:       pkgconfig
Provides:       %{name}-static = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q

%patch -P 0 -p0
%patch -P 1 -p1
%patch -P 2 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
%ctest

%install
%cmake_install


%files devel
%license LICENSE
%doc examples/ AUTHORS README.rst
%{_includedir}/frozen/
%{_datadir}/cmake/%{name}/

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-3
- Drop main package.

* Tue Jul 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-2
- review fixes.

* Mon Jul 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-1
- Initial package.
