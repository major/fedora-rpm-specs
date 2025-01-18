Name:           gau2grid
Version:        2.0.7
Release:        2%{?dist}
Summary:        Fast computation of a gaussian function and its derivative on a grid
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dgasmith/gau2grid
Source0:        https://github.com/dgasmith/gau2grid/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy

%description
A collocation code for computing gaussians on a grid of the form:
out_Lp = x^l y^m z^n \sum_i coeff_i e^(exponent_i * (|center - p|)^2)

%package devel
Summary:        Development headers for gau2grid
Requires:       cmake
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for gau2grid.

%prep
%autosetup

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DENABLE_XHOST=OFF
%{cmake_build}

%install
%{cmake_install}

%files
%license LICENSE
%doc README.md
%{_libdir}/libgg.so.2*

%files devel
%{_includedir}/gau2grid/ 
%{_datadir}/cmake/gau2grid/
%{_libdir}/libgg.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7.

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.1-8
- Turn off automatically enabled use of native instruction sets.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.1-5
- Adapt to new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5.25cf057git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.25cf057git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-3.25cf057git
- Update to 25cf057git to address FTBFS issues.

* Sun Sep 23 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-2
- Review fixes, including addition of soname.

* Sat Sep 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-1
- Initial release.
