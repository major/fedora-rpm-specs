Name:           sigil
Version:        2.4.2
Release:        1%{?dist}
Summary:        WYSIWYG ebook editor
# Automatically converted from old format: GPL-3.0-or-later AND Apache-2.0 - review is highly recommended.
License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://sigil-ebook.com/
Source0:        https://github.com/Sigil-Ebook/Sigil/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch1:         %{name}-0.8.0-system-dicts.patch
Patch2:         %{name}-0.9.3-global-plugin-support.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1632199
# port to minizip 2.x for F-30+
Patch3:         %{name}-1.9.20-minizip2.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libpcre2-16)
BuildRequires:  cmake(minizip)
BuildRequires:  pkgconfig(python3)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# For the plugins
Requires:       python3-pillow python3-cssselect python3-cssutils
Requires:       python3-html5lib python3-lxml python3-qt5
Requires:       python3-regex python3-chardet python3-six
Requires:       hicolor-icon-theme
Recommends:     FlightCrew-sigil-plugin
# See internal/about.md for rationale for this
Provides:       bundled(gumbo) = 0.9.2
Provides:       bundled(nodejs-mathjax) = 2.75

ExclusiveArch: %{qt5_qtwebengine_arches}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}


%description
Sigil is a multi-platform WYSIWYG ebook editor. It is designed to edit books
in ePub format.

Now what does it have to offer...

    * Full Unicode support: everything you see in Sigil is in UTF-16
    * Full EPUB spec support
    * WYSIWYG editing
    * Multiple Views: Book View, Code View and Split View
    * Metadata editor with full support for all possible metadata entries with
      full descriptions for each
    * Table Of Contents editor
    * Multi-level TOC support
    * Book View fully supports the display of any XHTML document possible under
      the OPS spec
    * SVG support
    * Basic XPGT support
    * Advanced automatic conversion of all imported documents to Unicode
    * Currently imports TXT, HTML and EPUB files; more will be added with time
    * Embedded HTML Tidy; all imported documents are thoroughly cleaned;
      changing views cleans the document so no matter how much you screw up
      your code, it will fix it (usually) 


%package doc
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
Summary:        Documentation for Sigil ebook editor
BuildArch:      noarch

%description doc
%{summary}.


%prep
%autosetup -p1 -n Sigil-%{version}


# Fix hunspell library lookup from python
hver=$(ls -1 %{_libdir}/libhunspell*.so | sed 's/.*hunspell\(-.*\)\.so/\1/')
sed "s/find_library('hunspell')/find_library('hunspell$hver')/" \
  src/Resource_Files/plugin_launchers/python/pluginhunspell.py

#fixtimestamp src/Resource_Files/plugin_launchers/python/pluginhunspell.py

# remove unbundled libs
rm -rf 3rdparty/{minizip,zlib,hunspell,pcre2}


%build
%cmake -DUSE_QT5=1 -DUSE_SYSTEM_LIBS=1 -DSYSTEM_LIBS_REQUIRED=1 \
  -DDISABLE_UPDATE_CHECK=1 -DINSTALL_HICOLOR_ICONS=1 \
  -DINSTALL_BUNDLED_DICTS=0 -DSHARE_INSTALL_PREFIX:PATH=%{_prefix}
%cmake_build


%install
%cmake_install

# Make rpmlint happy
#chmod +x %{buildroot}%{_datadir}/%{name}/python3lib/*.py
#chmod +x %{buildroot}%{_datadir}/%{name}/plugin_launchers/python/*.py
#chmod -x %{buildroot}%{_datadir}/%{name}/plugin_launchers/python/sigil_gumbo_bs4_adapter.py

# fix shebang and byte compile
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/plugin_launchers/
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/python3lib/
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/plugin_launchers/
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/python3lib/

# desktop-file and appdata
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc ChangeLog.txt README.md
%license COPYING.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%files doc
%doc docs/*.epub


%changelog
* Tue Feb 11 2025 Marek Kasik <mkasik@redhat.com> - 2.4.2-1
- New upstream release 2.4.2
- Resolves: rhbz#2307477

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.1-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Dan Horák <dan[at]danny.cz> - 2.2.1-1
- New upstream release 2.2.1 (rhbz#2292574)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.13

* Mon Apr 08 2024 Dan Horák <dan[at]danny.cz> - 2.1.0-1
- New upstream release 2.1.0 (rhbz#2272660)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 2.0.2-2
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Sun Nov 19 2023 Dan Horák <dan[at]danny.cz> - 2.0.2-1
- New upstream release 2.0.2 (#1724109)
- Resolves: rhbz#1724109 rhbz#2128371 rhbz#2245795

* Mon Oct 30 2023 Dan Horák <dan[at]danny.cz> - 1.9.20-1
- New upstream release 1.9.20 (#1724109)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.14-17
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 0.9.14-15
- Rebuild (minizip-ng)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.14-13
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.14-10
- Rebuilt for Python 3.10

* Tue Feb 09 2021 Miro Hrončok <mhroncok@redhat.com> - 0.9.14-9
- Rebuilt for minizip 3.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 0.9.14-6
- Use __cmake_in_source_build

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.14-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.14-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Dan Horák <dan[at]danny.cz> - 0.9.14-1
- New upstream release 0.9.14 (#1719405)

* Tue Jun 04 2019 Dan Horák <dan[at]danny.cz> - 0.9.13-2
- switch to minizip2 on F-30+ (#1632199)

* Thu Mar 21 2019 Dan Horák <dan[at]danny.cz> - 0.9.13-1
- New upstream release 0.9.13 (#1690914)

* Tue Feb 19 2019 Dan Horák <dan[at]danny.cz> - 0.9.12-1
- New upstream release 0.9.12 (#1678503)

* Sun Feb 17 2019 Dan Horák <dan[at]danny.cz> - 0.9.11-1
- New upstream release 0.9.11 (#1677953)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 0.9.10-3
- rebuild for hunspell 1.7.0

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com> - 0.9.10-2
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Tue Jul 31 2018 Dan Horák <dan[at]danny.cz> - 0.9.10-1
- New upstream release 0.9.10 (#1608388)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 23 2017 Dan Horák <dan[at]danny.cz> - 0.9.9-1
- New upstream release 0.9.9 (#1528492)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Jerry James <loganjerry@gmail.com> - 0.9.8-1
- New upstream release 0.9.8 (rhbz#1389961)
- Add -pluginrunner patch to fix a small code typo
- Drop unneeded boost and xerces-c BRs
- Add pkgconfig BR
- Fix more wrong executable bits and end of line encodings
- Don't use /usr/bin/env to find python
- Drop obsolete update-desktop-database invocations
- Use ls and sed to insert the right hunspell version instead of patching it
- Minor appdata updates

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.6-4
- Rebuilt for Boost 1.63

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-3
- Rebuild for Python 3.6

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.6-2
- Rebuild for hunspell 1.5.x

* Fri Aug 12 2016 Hans de Goede <hdegoede@redhat.com> - 0.9.6-1
- New upstream release 0.9.6 (rhbz#1330501)

* Mon Apr 18 2016 Caolán McNamara <caolanm@redhat.com> - 0.9.3-2
- rebuild for hunspell 1.4.0

* Wed Feb 24 2016 Hans de Goede <hdegoede@redhat.com> - 0.9.3-1
- New upstream release 0.9.3 (rhbz#1219489)
- Use high-res icons
- Add appdata

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Jonathan Wakely <jwakely@redhat.com> 0.8.1-8
- Patched and rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.8.1-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.8.1-5
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.8.1-2
- Rebuild for boost 1.57.0

* Sat Oct 18 2014 Dan Horák <dan[at]danny.cz> - 0.8.1-1
- New upstream release 0.8.1
- Add doc subpackage for user guide and plugin guide

* Tue Sep 30 2014 Dan Horák <dan[at]danny.cz> - 0.8.0-1
- New upstream release 0.8.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Petr Machata <pmachata@redhat.com> - 0.7.4-5
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.7.4-4
- rebuild for boost 1.55.0

* Sun Apr 20 2014 Dan Horák <dan[at]danny.cz> - 0.7.4-3
- dropping old conditionals will allow build on EL-7

* Mon Nov 11 2013 Rex Dieter <rdieter@fedoraproject.org> 0.7.4-2
- rebuild (qt5 qreal/arm)

* Mon Oct 28 2013 Dan Horák <dan[at]danny.cz> - 0.7.4-1
- New upstream release 0.7.4 (#1023931)

* Wed Sep 11 2013 Dan Horák <dan[at]danny.cz> - 0.7.3-1
- New upstream release 0.7.3 (#907398)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.6.2-3
- Rebuild for boost 1.54.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.2-2
- Rebuild for Boost-1.53.0

* Tue Dec 18 2012 Dan Horák <dan[at]danny.cz> - 0.6.2-1
- New upstream release 0.6.2

* Sun Nov 25 2012 Hans de Goede <hdegoede@redhat.com> - 0.6.0-3
- Add Provides: bundled(libtidy)  (rhbz#772362)

* Mon Nov 19 2012 Hans de Goede <hdegoede@redhat.com> - 0.6.0-2
- Call desktop-file-validate on the desktop-file (rhbz#772362)

* Wed Oct 31 2012 Dan Horák <dan[at]danny.cz> - 0.6.0-1
- New upstream release 0.6.0

* Sun Oct 21 2012 Dan Horák <dan[at]danny.cz> - 0.5.907-1
- New upstream release 0.5.907 (beta)

* Fri Oct 05 2012 Dan Horák <dan[at]danny.cz> - 0.5.906-2
- allow use of bundled pcre on Fedora < 18
- use system spelling dictionaries

* Thu Oct 04 2012 Dan Horák <dan[at]danny.cz> - 0.5.906-1
- New upstream release 0.5.906 (beta)

* Mon Jan 23 2012 Hans de Goede <hdegoede@redhat.com> - 0.5.0-1
- New upstream release 0.5.0
- Add patches to use system hunspell and pcre libs

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 0.4.2-3
- Drop buildroot and defattr boilerplate (no longer needed with recent rpm)
- Use system FlightCrew and XercesExtensions
- Drop support for building for F-15, having a buildin xerces-c with a shared
  system XercesExtensions is asking for trouble

* Tue Dec 13 2011 Dan Horák <dan[at]danny.cz> - 0.4.2-2
- don't require SSE2 in xerces

* Mon Dec 12 2011 Dan Horák <dan[at]danny.cz> - 0.4.2-1
- initial Fedora version
