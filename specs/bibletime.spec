Name:           bibletime
Version:        3.0.3
Release:        7%{?dist}
Summary:        An easy to use Bible study tool
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.bibletime.info/
Source0:        http://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  clucene-core-devel >= 2.0
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(QtGui) >= 4.5.0
BuildRequires:  sword-devel >= 1.8.1-15
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  po4a
BuildRequires:  libxslt

# fop is java_arches exclusive
ExclusiveArch:  %{java_arches}
BuildRequires:  fop

BuildRequires:  docbook-style-xsl
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  qt5-qtwebengine-devel
%else
BuildRequires:  qt5-qtwebkit-devel
%endif
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  make

%description
BibleTime is a free and easy to use cross-platform bible study tool. It
provides easy handling of digitalized texts (Bibles, commentaries and
lexicons) and powerful features to work with these texts (search in
texts, write own notes, save, print etc.). BibleTime is a frontend for
the SWORD Bible Framework.

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -B %{_target_platform}

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# rename wrongly-named locale
mv %{buildroot}%{_docdir}/%{name}/handbook/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/handbook/pdf/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/pdf/{br,BR} || :

# locale's
%find_lang %{name} || touch %{name}.lang
BT_DOC_DIR=%{_docdir}/%{name}/
for doctype in handbook howto ; do
	for fmt in html pdf; do
		for lang_dir in %{buildroot}/$BT_DOC_DIR/$doctype/$fmt/* ; do
			lang=$(basename $lang_dir)
			echo "%lang($lang) $BT_DOC_DIR/$doctype/$fmt/$lang/*" >> %{name}.lang
		done
	done
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/info.%{name}.BibleTime.desktop

%files -f %{name}.lang
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/info.%{name}.BibleTime.desktop
%dir %{_datadir}/%{name}
%dir %{_docdir}/%{name}/handbook/
%dir %{_docdir}/%{name}/howto/
%{_datadir}/%{name}/display-templates/
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/license/
%{_datadir}/%{name}/locale/
%{_datadir}/%{name}/pics/
%{_datadir}/metainfo/info.%{name}.BibleTime.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/info.%{name}.BibleTime.svg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.3-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 12 2023 Filipe Rosset <rosset.filipe@gmail.com> - 3.0.3-1
- Update to 3.0.3 fixes FTBFS rhbz#2113119 and rhbz#2163514

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Greg Hellings <greg.hellings@gmail.com> - 3.0.2-1
- New upstream release 3.0.2

* Mon Aug 9 2021 Greg Hellings <greg.hellings@gmail.com> - 3.0.1-1
- New upstream release 3.0.1
- Never relased as builds are sketchy

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Greg Hellings <greg.hellings@gmail.com> - 3.0-4
- Rebuild for new Sword

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 1 2020 Greg Hellings <greg.hellings@gmail.com> - 3.0-2
- Force rebuild against SWORD 1.9.0

* Sun Aug 02 2020 Greg Hellings <greg.hellings@gmail.com> - 3.0-1
- Upstream release 3.0
- Drop patch
- Adjust BRs for 3.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Greg Hellings <greg.hellings@gmail.com> - 2.11.2-5
- Set minimum Sword version to 1.8.1-15 for ppc64le build errors

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Greg Hellings <greg.hellings@gmail.com> - 2.11.2-2
- Rebuild for SWORD 1.8.1-7

* Mon Jun 18 2018 Greg Hellings <greg.hellings@gmail.com> - 2.11.2-1
- Upstream version 2.11.2
- Added patch to fix compiling in Rawhide with missing Qt headers

* Wed Mar 07 2018 Greg Hellings <greg.hellings@gmail.com> - 2.11.1-4
- Add gcc-c++ build requires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Greg Hellings <greg.hellings@gmail.com> - 2.11.1-2
- Rebuild for Sword 1.8

* Mon Oct 02 2017 Greg Hellings <greg.hellings@gmail.com> - 2.11.1-1
- Upstream version 2.11.1
- Removed patch for old Qt builds, as no long applies

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.11.0-3
- Rebuilt for Boost 1.63

* Mon Jan 16 2017 Dan Horák <dan[at]danny.cz> - 2.11.0-2
- Build with qtwebkit on platforms where qtwebengine is not available

* Tue Jan 10 2017 Greg Hellings <greg.hellings@gmail.com> - 2.11.0-1
- New upstream release
- Moved LICENSE file to license macro
- Added the name macro in a few file paths
- Excluded from PPC64-le and PPC64 builds due to missing deps

* Tue Aug 16 2016 Greg Hellings <greg.hellings@gmail.com> - 2.11_rc2-1
- New upstream test build

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 2.10.1-12
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.10.1-11
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.10.1-9
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.10.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.10.1-6
- Rebuild for boost 1.57.0

* Sun Dec 14 2014 Rex Dieter <rdieter@fedoraproject.org> 2.10.1-5
- rebuild (sword)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Rex Dieter <rdieter@fedoraproject.org> 2.10.1-3
- fix regressions introduced in recent "cleanup SPEC" commit
- trailing whitespace in %%description
- changes in %%build: lost CMAKE_BUILD_TYPE, %%{make_build} undefined in on older rpm
- %%install: lost 'make install/fast'

* Wed Jul 09 2014 Jakub Čajka <jcajka@redhat.com> - 2.10.1-2
- Replaced -fpie with -fPIE to fix build on s390

* Mon Jul 07 2014 Greg Hellings <greg.hellings@gmail.com> - 2.10.1-1
- New upstream release
- Should address bug #1113320

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 2.10.0-3
- Rebuild for boost 1.55.0

* Mon May 19 2014 Deji Akingunola <dakingun@gmail.com> - 2.10.0-2
- Rebuild for sword-1.7.3

* Wed Jan 29 2014 Greg Hellings <greg.hellings@gmail.com> - 2.10.0-1
- Updated to bibletime-2.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.9.1-7
- Rebuild for boost 1.54.0

* Fri Apr 19 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.1-6
- No text visible in main window when using qtwebkit-2.3 (#952390)

* Thu Apr 18 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.9.1-5
- clean .spec of deprecated tags (Group, %%clean, %%defattr)
- use %%cmake macro
- drop extraneous explicit sword-related deps (curl, zlib)
- bibletime.desktop: don't remove Qt category, patch to pass validation
- fix unowned dirs %%_datadir/bibletime/docs/{handbook,howto}

* Sun Feb 03 2013 Kevin Fenzi <kevin@scrye.com> - 2.9.1-4
- Rebuild for broken deps in rawhide

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 20 2012 Deji Akingunola <dakingun@gmail.com> - 2.9.1-2
- Rebuild for icu soname change

* Thu Feb 23 2012 Deji Akingunola <dakingun@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Deji Akingunola <dakingun@gmail.com> - 2.8.2-1
- Update to 2.8.2

* Mon Oct 17 2011 Jonathan Dieter <jdieter@lesbg.com> - 2.8.1-2
- Add patch so it builds again CLucene 2.0+

* Thu Jun 02 2011 Deji Akingunola <dakingun@gmail.com> - 2.8.1-1
- Update to 2.8.1

* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> - 2.8.0-3
- rebuild for icu 4.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2011 Deji Akingunola <dakingun@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Fri Oct 22 2010 Deji Akingunola <dakingun@gmail.com> - 2.7.3-3
- Rebuild for sword-1.6.2

* Wed Sep 29 2010 jkeating - 2.7.3-2
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Deji Akingunola <dakingun@gmail.com> - 2.7.3-1
- Update to 2.7.3, fixes a potential data loss bug

* Mon Jun 21 2010 Deji Akingunola <dakingun@gmail.com> - 2.7-1
- Update to 2.7

* Sat Apr 03 2010 Caolán McNamara <caolanm@redhat.com> - 2.5-3
- rebuild for icu 4.4

* Thu Jan 14 2010 Deji Akingunola <dakingun@gmail.com> - 2.5-2
- Rebuild for sword-1.6.1

* Tue Dec 29 2009 Deji Akingunola <dakingun@gmail.com> - 2.5-1
- New upstream version

* Wed Dec 02 2009 Deji Akingunola <dakingun@gmail.com> - 2.4-1
- Update to 2.4
- Update the description and summary.

* Wed Sep 30 2009 Deji Akingunola <dakingun@gmail.com> - 2.2-1
- Update to 2.2

* Wed Aug 12 2009 Deji Akingunola <dakingun@gmail.com> - 2.1-1
- Update to 2.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 06 2009 Deji Akingunola <dakingun@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Tue Mar 17 2009 Deji Akingunola <dakingun@gmail.com> - 1.7-1
- Update to 1.7

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 26 2008 Deji Akingunola <dakingun@gmail.com> - 1.6.5.1-1
- Update to 1.6.5.1

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6.5-4
- Autorebuild for GCC 4.3

* Wed Feb 13 2008 Deji Akingunola <dakingun@gmail.com> 1.6.5-3
- Rebuild for gcc-4.3

* Wed Jan 02 2008 David Anderson <fedora-packaging@dw-perspective.org.uk> 1.6.5-2
- BR kdelibs3-devel

* Tue Nov 06 2007 Deji Akingunola <dakingun@gmail.com> 1.6.5-1
- 1.6.5

* Fri May 04 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 1.6.4-2
- 1.6.4

* Mon Feb 05 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 1.6.3b-3
- 1.6.3b

* Sat Jan 27 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 1.6.2-5
- Correct wrong location of pt_BR files

* Mon Jan 15 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 1.6.2-4
- Added internationalisation

* Fri Jan 12 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 1.6.2-2
- Cleanups (thanks to Deji Akingunola)

* Fri Jan 12 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 1.6.2-1
- First attempt for Fedora Extras
- (Credits to Joachim Ansorg and Brook Humphrey for previous
- version from bibletime tarball)
