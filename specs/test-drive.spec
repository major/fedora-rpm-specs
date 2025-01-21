Name:           test-drive
Version:        0.4.0
Release:        9%{?dist}
Summary:        The simple testing framework
# Automatically converted from old format: ASL 2.0 or MIT - review is highly recommended.
License:        Apache-2.0 OR LicenseRef-Callaway-MIT
URL:            https://github.com/fortran-lang/test-drive
Source0:        https://github.com/fortran-lang/test-drive/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-gfortran
BuildRequires:  cmake

%description
This project offers a lightweight, procedural unit testing framework
based on nothing but standard Fortran.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
# Move module files
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/test-drive/*/*.mod %{buildroot}%{_fmoddir}
rm -rf %{buildroot}%{_includedir}/test-drive/

%files
%license LICENSE-Apache LICENSE-MIT
%doc README.md
%{_libdir}/libtest-drive.so.0*

%files devel
%{_fmoddir}/testdrive*.mod
%{_libdir}/pkgconfig/test-drive.pc
%{_libdir}/cmake/test-drive/
%{_libdir}/libtest-drive.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 09 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.4.0-2
- Use %%{_fmoddir} macro.

* Tue May 24 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.4.0-1
- Initial release.
