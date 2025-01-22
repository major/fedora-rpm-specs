Name:           librcd
Version:        0.1.14
Release:        27%{?dist}
Summary:        Library for autodetection charset of Russian and Ukrainian text

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://rusxmms.sourceforge.net
Source0:        http://dside.dyndns.org/files/rusxmms/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires: make

%description
LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized
to handle very short titles, like ID3 tags, file names and etc, and provides
very high accuracy even for short 3-4 letter words. Current version supports
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251,
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection
accuracy on short titles and is able to detect ISO8859-1 (non-Cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized
to handle very short titles, like ID3 tags, file names and etc, and provides
very high accuracy even for short 3-4 letter words. Current version supports
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251,
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection
accuracy on short titles and is able to detect ISO8859-1 (non-Cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure --disable-static
%make_build


%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -delete


%ldconfig_scriptlets


%files
%doc AUTHORS README
%license COPYING
%{_libdir}/librcd.so.*

%files devel
%doc ChangeLog
%{_includedir}/librcd.h
%{_libdir}/librcd.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.14-26
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Ivan Romanov <drizt72@zoho.eu> - 0.1.14-12
- Explicity add gcc to BR (fix #1604655)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 16 2013 Ivan Romanov <drizt@land.ru> - 0.1.14-2
- added ChangeLog to devel subpackage
- fixed typo in Summary

* Sat Nov 16 2013 Ivan Romanov <drizt@land.ru> - 0.1.14-1
- initial version of package
