Name: kover
Summary: WYSIWYG CD cover printer with CDDB support
Version: 6
Release: 37%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://lisas.de/kover/kover-6.tar.bz2
URL: http://lisas.de/kover/
BuildRequires: desktop-file-utils
BuildRequires: libcdio-devel >= 0.90, libcddb-devel
BuildRequires: kdelibs4-devel >= 4
BuildRequires: cmake, gettext
BuildRequires: make

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support.

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%{__make} %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 21
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original \
%else
  --dir %{buildroot}%{_datadir}/applications/kde4 \
%endif
  --add-category Utility \
  --add-category AudioVideo \
  %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%{__install} -p -D %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-%{name}.png

%find_lang %{name} --with-kde

## unpackaged files
rm -rfv %{buildroot}%{_datadir}/icons/locolor


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README NEWS THANKS ChangeLog
%{_kde4_appsdir}/kover/
%{_kde4_iconsdir}/kover*
%{_kde4_iconsdir}/hicolor/*/*/*
%{_datadir}/mime/packages/*
%{_mandir}/man1/*
%if 0%{?fedora} && 0%{?fedora} < 21
%{_datadir}/applications/%{name}.desktop
%else
%{_datadir}/applications/kde4/%{name}.desktop
%endif
%{_kde4_bindir}/kover

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 6-36
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Adrian Reber <adrian@lisas.de> - 6-25
- Rebuilt for libcdio-2.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> - 6-19
- Rebuilt for libcdio-2.0.0

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6-18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Adrian Reber <adrian@lisas.de> - 6-14
- rebuilt for new libcdio

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6-11
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> - 6-10
- rebuilt for new libcdio

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 6-9
- .spec cleanup, update scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 17 2013 Adrian Reber <adrian@lisas.de> - 6-6
- rebuilt for new libcdio

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 6-4
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Adrian Reber <adrian@lisas.de> - 6-2
- only require libcdio >= 0.90

* Mon Jan 14 2013 Adrian Reber <adrian@lisas.de> - 6-1
- updated to 6

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> - 5-2
- rebuilt for new libcdio

* Thu Aug 02 2012 Adrian Reber <adrian@lisas.de> - 5-1
- updated to 5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-10
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Adrian Reber <adrian@lisas.de> - 4-8
- rebuilt for new libcdio

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> - 4-6
- rebuilt for new libcdio

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Adrian Reber <adrian@lisas.de> - 4-4
- included patch to build with gcc 4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Adrian Reber <adrian@lisas.de> - 4-2
- rebuilt for new libcdio

* Thu Nov 13 2008 Adrian Reber <adrian@lisas.de> - 4-1
- updated to 4

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3-4
- fix license tag

* Mon Feb 11 2008 Adrian Reber <adrian@lisas.de> - 3-3
- rebuilt for gcc43 and kde

* Thu Aug 23 2007 Adrian Reber <adrian@lisas.de> - 3-2
- rebuilt

* Fri Jul 06 2007 Adrian Reber <adrian@lisas.de> - 3-1
- updated to 3
- handle icons and mimetype
- added libcdio-devel and libcddb-devel as BR

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.9.6-8
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Adrian Reber <adrian@lisas.de> - 2.9.6-7
- rebuilt

* Mon Jul 24 2006 Adrian Reber <adrian@lisas.de> - 2.9.6-6
- disable -ansi to make it build with the newest kernel headers

* Sun Mar 12 2006 Adrian Reber <adrian@lisas.de> - 2.9.6-5
- rebuilt

* Sun Feb 12 2006 Adrian Reber <adrian@lisas.de> - 2.9.6-4
- rebuilt

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.9.6-3
- rebuild on all arches

* Tue Mar 29 2005 Adrian Reber <adrian@lisas.de> - 0:2.9.6-2
- add --disable-rpath to configure

* Sun Feb 13 2005 Adrian Reber <adrian@lisas.de> - 0:2.9.6-1
- updated to 2.9.6 to hopefully fix x86_64 build

* Thu May 01 2003 Adrian Reber <adrian@lisas.de> - 0:2.9.3-0.fdr.7
- added "Application" to desktop-file-install
- removed "KDE" from desktop-file-install
- changed "Multimedia" to "AudioVideo" at desktop-file-install

* Thu May 01 2003 Adrian Reber <adrian@lisas.de> - 0:2.9.3-0.fdr.6
- removed the INSTALL file from package and added the NEWS file

* Sat Apr 26 2003 Adrian Reber <adrian@lisas.de> - 0:2.9.3-0.fdr.5
- added the directories %%{_datadir}/apps/kover and
  %%{_datadir}/apps/kover/pics to the file list

* Wed Apr 23 2003 Adrian Reber <adrian@lisas.de> - 0:2.9.3-0.fdr.4
- added %%{?_smp_mflags}
- added --with-xinerama
- moved QTDIR and configure from prep to build
- changed X-Red-Hat-Extra to X-Fedora
- added %%{release} to BuildRoot

* Mon Mar 10 2003 Adrian Reber <adrian@lisas.de>
 - Changed Copyright: to License:

* Sun Nov 18 2001 Adrian Reber <adrian@lisas.de>
 - Included mime type

* Fri Jun 22 2001 Adrian Reber <adrian@lisas.de>
 - Integrated spec file in autoconf

* Fri May 11 2001 Adrian Reber <adrian@lisas.de>
 - Updated to kover 0.6

* Fri May 11 2001 Adrian Reber <adrian@lisas.de>
 - Initial release of kover-0.5 rpm
