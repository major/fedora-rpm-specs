Name:           json-fortran
Version:        8.3.0
Release:        10%{?dist}
Summary:        A Modern Fortran JSON API
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://github.com/jacobwilliams/json-fortran
Source0:        https://github.com/jacobwilliams/json-fortran/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-gfortran

%description
JSON-Fortran is a user-friendly, thread-safe, and object-oriented API
for reading and writing JSON files, written in modern Fortran.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# For module dir ownership
Requires:       gcc-gfortran

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%cmake -DUSE_GNU_INSTALL_CONVENTION=TRUE
%cmake_build

%install
%cmake_install
# Move modules to correct directory
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}/
# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/libjsonfortran.so.8*

%files devel
%{_libdir}/cmake/jsonfortran-gnu-%{version}/
%{_libdir}/pkgconfig/json-fortran.pc
%{_libdir}/libjsonfortran.so
%{_fmoddir}/json_*.mod

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 2 2024 Miroslav Suchý <msuchy@redhat.com> - 8.3.0-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 26 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 8.3.0-2
- Require gcc-gfortran for directory ownership.

* Tue May 24 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 8.3.0-1
- Initial release.
