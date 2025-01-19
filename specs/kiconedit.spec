
Name:    kiconedit
Version: 4.4.0
Release: 34%{?dist}
Summary: An icon editor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/extragear/%{name}-%{version}.tar.bz2

BuildRequires: kdelibs4-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: make

%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}

%description
KIconEdit is designed to help create icons for 
KDE using the standard icon palette.


%prep
%setup -q

# update docbook version to make doc-translations build with kdelibs >= 4.5
sed -i -e 's#<!DOCTYPE book PUBLIC "-//KDE//DTD DocBook XML V4\.1\.2-Based Variant V1\.1//EN" "dtd/kdex\.dtd" \[#<!DOCTYPE book PUBLIC "-//KDE//DTD DocBook XML V4.2-Based Variant V1.1//EN" "dtd/kdex.dtd" [#g' doc-translations/*_kiconedit/*/index.docbook


%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-kde


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop



%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.DOC NEWS
%{_kde4_bindir}/kiconedit
%{_kde4_appsdir}/kiconedit/
%{_kde4_datadir}/applications/kde4/kiconedit.desktop
%{_kde4_iconsdir}/hicolor/*/*/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.0-33
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.4.0-17
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.4.0-11
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Rex Dieter <rdieter@fedoraproject.org> 4.4.0-5
- cleanup .spec, fix scriptlets

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 11 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-2
- update docbook version to make doc-translations build with kdelibs >= 4.5,
  fixes FTBFS (#599843)

* Fri Feb 12 2010 Sebastian Vahl <svahl@fedoraproject.org> - 4.4.0-1
- 4.4.0

* Thu Jan 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-3
- better Requires: kdelibs4 construct (using %%{_kde4_version})

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.3-2
- rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Thu Nov 05 2009 Sebastian Vahl <svahl@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Tue Sep 01 2009 Sebastian Vahl <svahl@fedoraproject.org> - 4.3.1-1
- 4.3.1

* Tue Aug 04 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 10 2009 Sebastian Vahl <fedora@deadbabylon.de> 4.2.4-1
- 4.2.4

* Mon May 11 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.3-2
- fix %%_docdir/HTML/<lang> ownership

* Fri May 08 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.3-1
- 4.2.3
- optimize scriptlets

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Mon Nov 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.3-2
- scriptlet, dependency fixes

* Sun Nov 09 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.1.3-1
- 4.1.3

* Fri Oct 03 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Thu Aug 28 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.1.0-1
- 4.1 (final)

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta 1

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-1
- update to 4.0.3
- rebuild for NDEBUG and _kde4_libexecdir

* Tue Mar 04 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.2-1
- new upstream version: 4.0.2

* Thu Feb 14 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.1-2
- remove reference to KDE 4 in summary

* Fri Feb 08 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.1-1
- new upstream version: 4.0.1

* Fri Jan 25 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.0-1
- Initial version of kde-4.0.0 version
