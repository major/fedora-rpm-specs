Name:     inih
Version:  58
Release:  3%{?dist}
Summary:  Simple INI file parser library

License:  BSD-3-Clause
URL:      https://github.com/benhoyt/inih
Source0:  %{url}/archive/r%{version}/%{name}-r%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson


%description
The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.

%package cpp
Summary: INIReader C++ library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cpp
This package contains the INIReader C++ library which provides a C++ interface
for inih.

%package devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-cpp%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.


%prep
%autosetup -n %{name}-r%{version}


%build
%meson
%meson_build


%install
%meson_install


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}.so.0

%files cpp
%{_libdir}/libINIReader.so.0


%files devel
%{_includedir}/ini.h
%{_includedir}/INIReader.h
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/pkgconfig/INIReader.pc
%{_libdir}/lib%{name}.so
%{_libdir}/libINIReader.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Robert Scheck <robert@fedoraproejct.org> - 58-1
- New upstream release 58 (#2260272)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 57-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec  2 2023 Daan De Meyer <daan.j.demeyer@gmail.com> - 57-3
- Move INIReader C++ library to inih-cpp subpackage

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Robert Scheck <robert@fedoraproejct.org> - 57-1
- New upstream release 57 (#2221191)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Robert Scheck <robert@fedoraproejct.org> - 56-1
- New upstream release 56 (#2106574)

* Sat Apr 23 2022 Robert Scheck <robert@fedoraproejct.org> - 55-1
- New upstream release 55 (#1920254)
- Re-add ldconfig scriptlets for EPEL 7 (#2066538)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Christian Kellner <ckellner@redhat.com> - 49-1
- New upstream release 49
- Switch to meson build system.
- Ship the pkg-config file.
- Remove ldconfig scriptlets.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jan F. Chadima <jfch@jagda.eu> - 36-5
- implement license tag

* Wed Aug 31 2016 Jan F. Chadima <jfch@jagda.eu> - 36-4
- implement next review hints

* Tue Aug 30 2016 Jan F. Chadima <jfch@jagda.eu> - 36-3
- implement another review results

* Tue Aug 30 2016 Jan F. Chadima <jfch@jagda.eu> - 36-2
- implement review results

* Mon Aug 29 2016 Jan F. Chadima <jfch@jagda.eu> - 36-1
- initial version
