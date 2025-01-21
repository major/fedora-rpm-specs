%global __cmake_in_source_build 1
%global prerel beta2
%global stable 1
%global stable_ver stable1

Summary:        A lightweight Qt Audio player
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://sayonara-player.com
Name:           sayonara

%if 0%{?stable}
Version:        1.10.0
Release:        4.%{stable_ver}%{?dist}
#Release:        3%%{?dist}
Source0:        https://gitlab.com/luciocarreras/sayonara-player/-/archive/%{version}-%{stable_ver}/sayonara-player-%{version}-%{stable_ver}.tar.bz2
%else
Version:        1.10.0
Release:        0.3.%{prerel}%{?dist}
Source0:        https://gitlab.com/luciocarreras/sayonara-player/-/archive/%{version}-%{prerel}/sayonara-player-%{version}-%{prerel}.tar.bz2
%endif

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libnotify-devel
BuildRequires:  taglib-devel
BuildRequires:  libmtp-devel
Requires:       qt5-qtsvg
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-bad-free
ExcludeArch:    %{ix86}

%description
%{name} is a small, clear, not yet platform-independent music player. Low 
CPU usage, low memory consumption and no long loading times are only three 
benefits of this player. Sayonara should be easy and intuitive to use and 
therefore it should be able to compete with the most popular music players.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
%if 0%{?stable}
%autosetup -p0 -n %{name}-player-%{version}-%{stable_ver}
%else
%autosetup -p1 -n %{name}-player-%{version}-%{prerel}
%endif

rm -rf .gitignore .gitlab-ci.yml debian
# use system taglib
rm -rf src/3rdParty/Taglib

%build
%cmake . -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
         -DWITH_DOC=ON                       \
         -DWITH_SYSTEM_TAGLIB=ON             \
         -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

# build docs
# update Doxyfile
doxygen -u docs/doxygen.cfg
# build docs
doxygen docs/doxygen.cfg

%install
%cmake_install

# remove menu dir, because it's not necessary
rm -rf %{buildroot}/%{_datadir}/menu

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc MANUAL README.md INSTALL.md
%{_bindir}/%{name}
%{_bindir}/%{name}-ctl
%{_bindir}/%{name}-query
%{_datadir}/applications/com.%{name}-player.Sayonara.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/com.%{name}-player.Sayonara.appdata.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/translations/icons
%{_datadir}/%{name}/translations/icons/*.png
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-ctl.1.gz
%{_mandir}/man1/%{name}-query.1.gz

%files doc
#doc docs/html
%{_datadir}/doc/%{name}/doxygen/html

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4.stable1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.0-3.stable1
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2.stable1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 27 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.10.0-1.stable1
- Update to 1.10.0 stable1

* Mon May 06 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.10.0-0.1.beta2
- Update to 1.10.0 beta2

* Thu Apr 18 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.10.0-0.1.beta1
- Update to 1.10.0 beta1

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.9.0-0.1.beta1
- Update to 1.9.0 beta1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 31 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.8.0-0.1.beta1
- Update to 1.8.0 beta1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6.stable3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5.stable3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4.stable3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.7.0-3
- Update to 1.7.0 stable3

* Thu Jul 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.7.0-2
- Update to 1.7.0 stable2
- Add sayonara-namespace.patch

* Tue May 18 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 stable1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.8.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.6.0-0.7.beta7
- Update to 1.6.0-0.7.beta7

* Tue Aug 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.6.0-0.6.beta6
- Use %%cmake_build and %%cmake_install macros instead of %%make_build and %%make_install
- Add "%%global __cmake_in_source_build 1" due sayonara doesn't support out-of-src tree builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.5.beta6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.4.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.6.0-0.3.beta6
- Update to 1.6.0-0.3.beta6

* Wed May 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.6.0-0.2.beta4
- Use system taglib

* Wed May 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.6.0-0.1.beta4
- Update to 1.6.0-0.1.beta4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-0.3.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.5.2-0.2.beta3
- Add Patch0 to Fix (BZ#1770426)

* Fri Oct 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.5.2-0.1.beta3
- Update to 1.5.2-0.1.beta3

* Tue Aug 27 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1-1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1-1

* Thu May 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-1.git20190428
- Update to 1.3.0-1.git20190428

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2.git20180828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-1.git20180828
- Update to 1.1.1-1.git20180828

* Sat Jul 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-7.git20180115
- Fix FTBFS add %{name}-qt.patch (RHBZ#1606300)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6.git20180115
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.git20180115
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-4.git20180115
- Remove obsolete scriptlets

* Tue Jan 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-3.git20180115
- Update to 1.0.0-git5-20180115

* Mon Jan 01 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-2.git20171231
- Update to 1.0.0-git1-20171231

* Sun Dec 31 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1.git20171230
- Update to 1.0.0-git0-20171230

* Wed Oct 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.3-5.git20171018
- Rebuild for sayonara (git tag 0.9.3-git3-20171018)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4.git20170509
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3.git20170509
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.3-2.git20170509
- Rebuild for sayonara (git tag 0.9.3-git2-20170509)

* Fri May 05 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.3-1.git20170502
- Rebuild for sayonara (git tag 0.9.3-git1-20170502)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5.git20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.2-4.git20161030
- Rebuild for sayonara (git tag 0.9.2-git11-20161030)

* Mon Oct 10 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.2-3.git20161009
- Rebuild for sayonara (git tag 0.9.2-git5-20161009)

* Tue Sep 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.2-2.git20160920
- Add Requires gstreamer1-plugins-bad-free
- Rebuild for sayonara (git tag 0.9.2-git4-20160920)
- Spec file cleanup
- Changed git revision tag

* Wed Sep 14 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.2-1.20160920git
- Update to 0.9.2-1.20160920git

* Wed Sep 14 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.1-1.20160913git
- Update to 0.9.1-1.20160913git

* Wed Jun 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.0-2.20160607git
- Update to 0.9.0-2.20160607git

* Tue May 17 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.0-1.20160517git
- Update to 0.9.0

* Mon May 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.8.3-2.20160501git
- Update to new git release

* Mon Apr 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.8.3-1.20160424git
- Update to 0.8.3
- Added BR doxygen
- Added subpackage doc

* Tue Feb 16 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.8.2-1.20160214git
- Update to 0.8.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2.svn324
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.8.1-1.svn324
- Update to 0.8.1
- Added xpm icon path
- Added manual page

* Thu Dec 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-1.svn289
- Update to 0.8.0
- added BR libmtp-devel

* Thu Nov 26 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-4.svn257
- rebuild for new svn release

* Fri Oct 23 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-3.svn223
- rebuild for new svn release

* Sat Oct 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-2.svn211
- rebuild for new svn release

* Sun Oct 11 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-1.svn200
- Update to 0.7.1

* Wed Aug 26 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.0-2.svn151
- fixed trailing spaces in Helper/MetaData/LibraryItem.cpp
- fixed soundcloud install dir issues
- fixed QObject dependencies neccessary under Fedora 22 in certain source files
- made Gstreamer mandatory

* Sat Aug 22 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-1.svn144
- rebuild for new svn release

* Fri Aug 14 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.6-6.svn119
- rebuild for new svn release

* Fri Jul 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.6-5.svn80
- rebuild for new svn release

* Thu Jul 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.6-4.svn73
- rebuild for new svn release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-3.svn62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.6.6-2.svn62
- added new CMake Build type option: RelWithDebInfo
- removed screenshots from sayonara.appdata.xml

* Sun May 24 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.6.6-1.svn52
- changed server adress
- changed cmake call
- added -fPIC compiler flag for debug mode in CMakeLists.txt
- added sayonara.appdata.xml on SVN

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.5-2.svn1037
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.5-1.svn1037
- rebuild for new svn release
- added 'if' conditions to fix f23 build

* Tue Feb 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-4.svn1021
- rebuild for new svn release

* Mon Feb 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-3.svn1018
- rebuild for new svn release
- cosmetic changes
- take ownership of unowned directory %%{_datadir}/%%{name}/translations
- take ownership of unowned directory %%{_datadir}/%%{name}/translations/icons

* Mon Feb 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-2.svn1016
- deleted BR  gstreamer1-devel because its redundant
- deleted RR svn isn't needed
- corrected license tag to GPLv3+
- added RR hicolor-icon-theme
- mark license files as %%license where available
- added appdata.xml file
- modified desktop file Categories
- removed java stuff
- added BR libappstream-glib

* Fri Feb 13 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-1.svn1016
- rebuild for new svn release
- cleanup spec file

* Mon Sep 01 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-1.4.svn878
- enabled debugging informations
- rebuild for new svn release
- set correct file permisson

* Fri Aug 29 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-1.3.svn870
- rebuild for new svn release
- added more comments

* Tue Jun 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.2.svn851
- removed unecessary BR glib2-devel
- removed unecessary BR alsa-lib-devel
- removed unecessary BR libxml2-devel

* Tue Jun 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.2.svn851
- rebuild for new svn release
- added svn Requirement
- corrected svn path

* Mon Jun 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.1.svn850
- added download instructions
- rebuild for new svn release

* Tue Oct 29 2013 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.0-1.0.svn695
- Inital release.
