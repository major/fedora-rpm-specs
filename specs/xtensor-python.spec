%undefine __cmake_in_source_build

Name:           xtensor-python
Version:        0.26.0
Release:        8%{?dist}
Summary:        Python bindings for xtensor
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://xtensor-python.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor-python
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

# because xtensor does so for armv7hl, ppc64le and s390x
ExcludeArch:    armv7hl ppc64le s390x

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  python3-pytest
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  xtensor-devel
BuildRequires:  python3-numpy


# there is no actual arched content - this is a header only library
%global debug_package %{nil}

%global _description %{expand:
xtensor-python enables in-place use of Numpy arrays in C++ with all the
benefits from xtensor:
- C++ universal function and broadcasting.
- STL-compliant APIs.
- A broad coverage of NumPy APIs.}


%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       pybind11-devel
Requires:       python3-devel
Requires:       xtensor-devel
Requires:       python3-numpy

%description devel %_description

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%make_build -C %{_vpath_builddir} xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 4 2024 Miroslav Suchý <msuchy@redhat.com> - 0.26.0-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 sguelton@redhat.com - 0.26.0-1
- Upstream release

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 sguelton@redhat.com - 0.24.1-0
- Upstream release

* Tue Sep 3 2019 sguelton@redhat.com - 0.23.1-0
- Initial package
