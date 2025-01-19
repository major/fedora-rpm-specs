Name:		libmetal
Version:	2024.10.0
Release:	2%{?dist}
Summary:	An abstraction layer across user-space Linux, baremetal, and RTOS environments 
License:	BSD-3-Clause OR Apache-2.0 OR GPL-2.0-only
URL:		https://github.com/OpenAMP/libmetal/

Source0:	https://github.com/OpenAMP/libmetal/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libmetal-add-additional-arches.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	libsysfs-devel

%description
An abstraction layer across user-space Linux, baremetal, and RTOS environments.

%package devel
Summary: 	Development files for libmetal
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.

%package doc
Summary:	Documentation files for libmetal
BuildArch:	noarch
%description doc
Documentation file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.


%prep
%autosetup -p1


%build
mkdir build
cd build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DWITH_STATIC_LIB=OFF ..
%cmake_build


%install
cd build
%cmake_install


%files
%license LICENSE.md
%doc README.md
%{_bindir}/test-metal-shared
%{_libdir}/libmetal.so.1
%{_libdir}/libmetal.so.1.*

%files devel
%{_libdir}/libmetal.so
%{_includedir}/metal/

%files doc
%license LICENSE.md
%doc README.md
%doc %{_datarootdir}/doc/metal/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2024.10.0-1
- Update to 2024.10.0

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2023.10.0-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 03 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.10.0-1
- Update to 2023.10.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 01 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.04.0-1
- Update to 2023.04.0 (lib 1.4.0)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  2 20:02:29 GMT 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10.0-1
- Update to 2020.10.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04.0-1
- Update to 2020.04.0

* Thu Mar 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.01.0-1
- Update to 2020.01.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2018.10-1
- Update to 2018.10 release

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2018.04-1
- Update to 2018.04 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-4
- Add patch to build on other arches

* Mon Feb 19 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-3
- Make -doc subpackage a noarch package

* Sat Feb 17 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-2
- Fix up issues identified in package review

* Tue Feb 13 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2017.10-1
- Initial packaging
