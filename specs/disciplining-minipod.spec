%global libname liboscillator-disciplining
%global _description %{expand:
Library providing C disciplining algorithm used with oscillatord to discipling
oscillators using the minipod algorithm developed by Matthias Lorentz.}

Name:           disciplining-minipod
Version:        3.10.5
Release:        %autorelease
Summary:        Disciplining algorithm for Atomic Reference Time Card

License:        LGPL-2.0-or-later
URL:            https://github.com/leoleovich/disciplining-minipod
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  sed

%description    %{_description}

%package -n     %{libname}
Summary:        %{summary}

%description -n %{libname} %{_description}

%package -n     %{libname}-devel
Summary:        Development files for %{libname}
Requires:       %{libname} = %{version}-%{release}

%description -n %{libname}-devel
This package contains development headers and files for %{libname}.

%prep
%autosetup -p1
# Drop forced optimization flag
sed -i 's/-O3//' CMakeLists.txt
# Do not install static library
sed -i 's/^install.*-static.*$//' src/CMakeLists.txt

%build
# TODO: Please submit an issue to upstream (rhbz#2380544)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

%check
%set_build_flags
%if 0%{?el8}
export CC="%{__cc}"
%endif
# build tests
%cmake -DBUILD_TESTS=true -DCMAKE_PREFIX_PATH="%{buildroot}%{_prefix}"
%cmake_build
# run tests
for t in test-checks test-utils test-minipod-lib test-fine-circular-buffer; do
# work around newer cmake and %{_vpath_builddir} difference
%if 0%{?el8}
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test/$t
%else
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./%{_vpath_builddir}/test/$t
%endif
done

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/%{libname}.so.3*

%files -n %{libname}-devel
%{_includedir}/oscillator-disciplining
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
* Fri Nov 13 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.5-1
- Update to 3.10.5

* Fri Sep 04 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.4-1
- Update to 3.10.4

* Fri Aug 14 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.3-1
- Update to 3.10.3

* Fri Aug 14 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Fri Aug 14 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.0-3
- New repository

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue Jun 23 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0

* Wed Jun 03 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.9.3-3
- Update to 3.9.3

* Wed Jun 03 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.9.3-2
- Update to 3.9.3

* Wed Jun 03 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.9.3-1
- Update to 3.9.3

* Thu May 21 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.2-1
- Update to 3.9.2

* Fri May 08 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.1-1
- Update to 3.9.1

* Wed Apr 15 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.0-2
- Update sources for 3.9.0

* Wed Apr 15 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Nov 10 2025 Cristian Le <git@lecris.dev> - 3.8.4-5
- Allow to build with CMake 4.0 (rhbz#2380544)

* Wed Aug 20 2025 Patrick Cullen <cullenptrck@gmail.com> - 3.8.4-4
- Update to 3.8.4

* Wed Aug 20 2025 Patrick Cullen <cullenptrck@gmail.com> - 3.8.4-3
- Update to 3.8.4

* Wed Aug 20 2025 Patrick Cullen <cullenptrck@gmail.com> - 3.8.4-2
- Update to 3.8.4

* Wed Aug 20 2025 Patrick Cullen <cullenptrck@gmail.com> - 3.8.4-1
- Update to 3.8.4

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Apr 01 2025 Vadim Fedorenko <vadfed@fb.com> - 3.8.3-1
- Update to 3.8.3

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.8.2-2
- convert license to SPDX

* Thu Aug 22 2024 Yaroslav Kolomiiets <yarek@fedoraproject.org> - 3.8.2-1
- Update to 3.8.2

* Wed Aug 21 2024 Yaroslav Kolomiiets <yarek@fedoraproject.org> - 3.8.1-4
- Update to 3.8.1

* Wed Aug 21 2024 Yaroslav Kolomiiets <yarek@fedoraproject.org> - 3.8.1-3
- Update to 3.8.1

* Wed Aug 21 2024 Yaroslav Kolomiiets <yarek@fedoraproject.org> - 3.8.1-2
- Update to 3.8.1

* Wed Aug 21 2024 Yaroslav Kolomiiets <yarek@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1

* Tue Aug 06 2024 Vadim Fedorenko <vadfed@fb.com> - 3.8.0-1
- Update to v3.8.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 08 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Tue Feb 13 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.6.3-1
- Update to 3.6.3

* Fri Feb 02 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Wed Jan 31 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Patrick Cullen <cullenptrck@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Oct 11 2023 Patrick Cullen <cullenptrck@gmail.com> - 3.5.6-1
- Update to 3.5.6

* Tue Sep 26 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.4-1
- Update to 3.5.4

* Tue Sep 05 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.3-1
- Update to 3.5.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1

* Tue Feb 21 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0

* Tue Feb 14 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.4.5-1
- Update to 3.4.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Alexander Bulimov <abulimov@fedoraproject.org> - 3.4.3-1
- Update to 3.4.3

* Tue Jan 03 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.4.2-1
- Update to 3.4.2

* Wed Oct 26 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1

* Fri Oct 07 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Mon Sep 12 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.9-1
- Update to 3.3.9

* Mon Sep 05 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.8-1
- Update to 3.3.8

* Wed Aug 10 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.7-1
- Update to 3.3.7

* Thu Aug 04 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.6-1
- Update to 3.3.6

* Tue Aug 02 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.5-1
- Update to 3.3.5

* Mon Aug 01 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4

* Fri Jul 29 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.3-1
- Update to 3.3.3

* Fri Jul 22 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Wed Jul 13 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Tue Jul 05 2022 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.2.6-1
- Update to 3.2.6

* Fri Jun 17 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.2.4-1
- Update to 3.2.4

* Thu Jun 16 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3

* Tue Jun 07 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Fri Jun 03 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.2.0-2
- Skip test-fine-circular-buffer

* Fri Jun 03 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Wed May 25 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Fri May 20 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Thu May 12 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.0.10-1
- Update to 3.0.10

* Thu May 05 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.0.8-1
- Update to 3.0.8

* Wed Apr 27 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 3.0.3-1
- Update to v3.0.3

* Fri Mar 25 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 2.1.0-1
- Update to v2.1.0

* Fri Mar 25 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Mar 25 2022 Alexander Bulimov <abulimov@fedoraproject.org> - 1.3.0-1
- Update to v1.3.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Alexander Bulimov <alexander.bulimov@gmail.com> - 1.2.0-1
- Update to v1.2.0

* Tue Aug 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.1-2
- Ensure the CC env variable is set on el8

* Tue Aug 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.1-1
- Initial import; Fixes: RHBZ#1992232
