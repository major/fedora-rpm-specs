%global instdir %{_libdir}
%global baseinstdir %{instdir}/libreoffice
%global sdkinstdir %{baseinstdir}/sdk

Name:          openoffice.org-diafilter
Version:       1.7.6
Release:       22%{?dist}
Summary:       DIA diagram shape importer and gallery extension for LibreOffice
License:       GPL-3.0-or-later AND LGPL-3.0-or-later
URL:           http://fedorahosted.org/openoffice.org-diafilter
Source:        https://github.com/caolanm/diafilter/archive/%{version}.tar.gz

BuildRequires: make
BuildRequires: libreoffice-sdk, boost-devel, dia, pkgconfig(zlib), zip, gcc-c++
Requires:      libreoffice-draw%{?_isa}

%if 0%{?fedora} >= 37
# Fedora 37 dropped java for i686, so libreoffice-sdk isn't there either
ExclusiveArch: %{java_arches}
%endif

Patch0: fixbuild.patch

%description
This package contains an importer component for LibreOffice to enable importing
the "dia" diagram and shape formats. A gallery of the standard set of "dia"
shapes are made available from Gallery for convenience.

%prep
%autosetup -n diafilter-%{version} -p1

%build
. %{sdkinstdir}/setsdkenv_unix.sh
DIA_SHAPES_DIR=%{_datadir}/dia/shapes make %{?_smp_mflags} OPT_FLAGS="$RPM_OPT_FLAGS"

%install
install -d -m 755 $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/diafilter.oxt $RPM_BUILD_ROOT/%{_datadir}/applications
unzip -q build/diafilter.oxt -d $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/diafilter.oxt
install -p -m 644 openoffice.org-diafilter.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/openoffice.org-diafilter.desktop
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/appdata
install -p -m 644 openoffice.org-diafilter.metainfo.xml $RPM_BUILD_ROOT/%{_datadir}/appdata

%files
%{baseinstdir}/share/extensions/diafilter.oxt
%{_datadir}/appdata/%{name}.metainfo.xml
%{_datadir}/applications/openoffice.org-diafilter.desktop
%doc README NEWS TODO
%license gpl-3.0.txt lgpl-3.0.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 12 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.7.6-18
- libcmis rebuild

* Wed Jul 26 2023 Ian McInerney <ian.s.mcinerney@ieee.org> - 1.7.6-17
- Only build on architectures with Java/libreoffice-sdk (RHBZ 2226065)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Caolán McNamara <caolanm@redhat.com> - 1.7.6-15
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Caolán McNamara <caolanm@redhat.com> - 1.7.6-11
- Resolves: rhbz#1987775 FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Caolán McNamara <caolanm@redhat.com> - 1.7.6-3
- Resolves: rhbz#1605328 Remove_GCC_from_BuildRoot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Caolán McNamara <caolanm@redhat.com> - 1.7.6-1
- latest version

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 17 2017 Caolán McNamara <caolanm@redhat.com> - 1.7.5-3
- Resolves: rhbz#1424022 fix C++11 build

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 15 2016 Caolán McNamara <caolanm@redhat.com> - 1.7.5-1
- Resolves: rhbz#1307830 fix C++11 build

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 David Tardon <dtardon@redhat.com> - 1.7.4-2
- add appdata addon metadata

* Tue Sep 15 2015 Caolán McNamara <caolanm@redhat.com> - 1.7.4-1
- Resolves: rhbz#1261986 assert in string access

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.7.3-4
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Caolán McNamara <caolanm@redhat.com> - 1.7.3-2
- Resolves: rhbz#1222232 malformed .desktop file

* Wed Apr 29 2015 Caolán McNamara <caolanm@redhat.com> - 1.7.3-1
- Resolves: rhbz#1185566 SIGABRT in DIAFilter::detect

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.7.2-10
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.7.2-7
- Rebuild for boost 1.55.0

* Wed Jan 08 2014 Caolán McNamara <caolanm@redhat.com> - 1.7.2-6
- Resolves: rhbz#995762 not built with RPM_OPT_FLAGS

* Wed Aug 07 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.7.2-5
- Fix build failure as cpumaker dropped -BURC option
- Fix deprecated function call valueOf() to number()

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.7.2-3
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 26 2012 Caolán McNamara <caolanm@redhat.com> - 1.7.2-1
- Resolves: rhbz#843251 FTBFS

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Caolán McNamara <caolanm@redhat.com> - 1.7.1-1
- Resolves: rhbz#715925 FTBFS

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.0-6
- Resolves: rhbz#665512 Change package description

* Tue Dec 07 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.0-5
- Resolves: rhbz#660917 FTBFS

* Sat Oct 23 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.0-4
- rebuild for libreoffice

* Wed Sep 29 2010 jkeating - 1.7.0-3
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.0-2
- Resolves: rhbz#635286 build with $RPM_OPT_FLAGS

* Fri Sep 17 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.0-1
- latest version

* Thu Aug 26 2010 Caolán McNamara <caolanm@redhat.com> - 1.6.0-1
- Initial import
