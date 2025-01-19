Name: libkiwix
Version: 12.0.0
Release: 13%{?dist}

License: GPL-3.0-or-later
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: aria2
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libzim-devel
BuildRequires: meson
BuildRequires: mustache-devel
BuildRequires: ninja-build
BuildRequires: pugixml-devel
BuildRequires: zlib-devel

Provides: kiwix-lib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: kiwix-lib < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The Kiwix library provides the Kiwix software core. It contains
the code shared by all Kiwix ports.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%meson -Dwerror=false -Dcpp_std=c++14
%meson_build

%install
%meson_install

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/kiwix-compile-*
%{_libdir}/%{name}.so.12*
%{_mandir}/man1/kiwix*.1*

%files devel
%{_includedir}/kiwix
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/kiwix.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 12.0.0-11
- Rebuild for ICU 74

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 12.0.0-7
- Rebuilt for ICU 73.2

* Sat Apr 29 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 12.0.0-6
- Rebuilt due to libzim update.

* Sat Apr 01 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 12.0.0-5
- Rebuilt due to libzim package rename.

* Sun Jan 29 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 12.0.0-4
- Build with C++14 instead of C++11 for gtest-1.13.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 12.0.0-2
- Rebuild for ICU 72

* Thu Dec 01 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 12.0.0-1
- Updated to version 12.0.0.

* Thu Sep 08 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 11.0.0-4
- Rebuilt due to zimlib update.

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 11.0.0-3
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 11.0.0-1
- Updated to version 11.0.0.

* Mon Apr 18 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 10.1.1-1
- Updated to version 10.1.1.

* Sat Mar 26 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 10.1.0-1
- Updated to version 10.1.0.

* Wed Feb 09 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 10.0.1-1
- Updated to version 10.0.1.

* Mon Jan 24 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 10.0.0-1
- Updated to version 10.0.0.
- Renamed kiwix-lib package to libkiwix.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 9.4.1-4
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 9.4.1-3
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 9.4.1-1
- Updated to version 9.4.1.

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.4.0-1
- Updated to version 9.4.0.

* Wed Aug 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.3.1-3
- Fixed crash on exit.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.3.1-1
- Updated to version 9.3.1.

* Fri Jul 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.3.0-1
- Updated to version 9.3.0.

* Wed Jul 01 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.2.3-1
- Updated to version 9.2.3.

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 9.1.2-2
- Rebuild for ICU 67

* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.1.2-1
- Updated to version 9.1.2.

* Thu Apr 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.1.0-1
- Updated to version 9.1.0.

* Mon Feb 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 8.2.2-1
- Updated to version 8.2.2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 8.1.0-2
- Rebuild for ICU 65

* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 8.1.0-1
- Updated to version 8.1.0.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.2.0-1
- Updated to version 5.2.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.1.0-1
- Updated to version 5.1.0.

* Tue Apr 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.0-1
- Updated to version 5.0.0.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1.0-1
- Updated to version 4.1.0.

* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.1-1
- Initial SPEC release.
