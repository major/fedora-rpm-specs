# Header-only package
%global debug_package %{nil}

Name:           frozen
Version:        1.2.0
Release:        2%{?dist}
Summary:        A header-only, constexpr alternative to gperf for C++14 users

License:        Apache-2.0
URL:            https://github.com/serge-sans-paille/frozen
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.2.0-1
- 1.2.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-3
- Drop main package.

* Tue Jul 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-2
- review fixes.

* Mon Jul 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.1-1
- Initial package.
