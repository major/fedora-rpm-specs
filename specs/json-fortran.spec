Name:           json-fortran
Version:        9.3.1
Release:        1%{?dist}
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
# json_value_module.F90 passes internal procedures as actual arguments, for
# which gfortran emits stack trampolines. These mark the object as requiring an
# executable stack, which makes the resulting library undlopenable: glibc
# refuses to flip the stack to executable at dlopen time, so anything loading
# it indirectly from Python (e.g. python3-dftd4) fails to import. Allocate the
# trampolines on the heap instead (GCC >= 14).
# NB: CMake reads the Fortran flags from FFLAGS, not FCFLAGS, and %%cmake only
# fills in the defaults for variables that are still unset, so FFLAGS is the one
# that has to be set here for the flag to reach the compiler.
export FFLAGS="%{build_fflags} -I%{_fmoddir} -Wtrampolines -ftrampoline-impl=heap"
export FCFLAGS="$FFLAGS"
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
%{_libdir}/libjsonfortran.so.9*

%files devel
%{_libdir}/cmake/jsonfortran-gnu-%{version}/
%{_libdir}/pkgconfig/json-fortran.pc
%{_libdir}/libjsonfortran.so
%{_fmoddir}/json_*.mod

%changelog
* Thu Jul 23 2026 Susi Lehtola <jussilehtola@fedoraproject.org> - 9.3.1-1
- Update to 9.3.1.
- Build with -ftrampoline-impl=heap so that the library no longer requires an
  executable stack and can be dlopened.

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

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
