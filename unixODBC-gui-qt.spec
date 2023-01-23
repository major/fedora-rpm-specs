# currently we have to pull directly from upstream SVN
%global svn 132
%global checkout 20190111svn%{svn}

Summary: Several GUI (Qt) programs and plug-ins for unixODBC
Name: unixODBC-gui-qt
# There has not been a formal upstream release yet and we're not
# sure what the first formal release version number will be, so using 0
Version: 0
Release: 0.31.%{checkout}%{?dist}
URL: http://sourceforge.net/projects/unixodbc-gui-qt/
# Programs are GPL, libraries are LGPL
License: GPLv3 and LGPLv3

# Source code is available only in SVN by upstream, so using own
# tarball created from the last commit. SVN repository can be found at
# https://unixodbc-gui-qt.svn.sourceforge.net/svnroot/unixodbc-gui-qt
Source0: %{name}-%{checkout}.tar.gz
Source1: ODBCCreateDataSourceQ5.desktop
Source2: ODBCManageDataSourcesQ5.desktop

# We'd like to have the same soname version as former unixODBC-kde had
Patch0: 0001-Turn-on-soname-versioning.patch

BuildRequires: make
BuildRequires: git
BuildRequires: desktop-file-utils
BuildRequires: qt-assistant-adp-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: unixODBC-devel

# Since unixODBC-2.3.0 does not contain GUI tools anymore, we can say
# unixODBC-gui-qt obsoletes all versions of unixODBC-kde before 2.3.0
Provides: unixODBC-kde = 2.3.0-1
Obsoletes: unixODBC-kde < 2.3.0-1

%description
unixODBC-gui-qt provides several GUI (Qt) programs and plug-ins.
  * administrator (program)
  * create data source wizard (program)
  * test (program)
  * installer (plug-in)
  * auto test (plug-in)

%prep
%autosetup -S git -n %{name}

# Fix hardcoded installation paths
sed -Ei -e 's|(INSTALL_TARGET_BIN)\s*=.*$|\1 = %{_bindir}|' \
        -e 's|(INSTALL_TARGET_LIB)\s*=.*$|\1 = %{_libdir}|' \
        defines.pri

%build
export UNIXODBC_DIR="%{_prefix}" UNIXODBC_LIBDIR="%{_libdir}"

%{qmake_qt5}
%{make_build}

%install
export UNIXODBC_DIR="%{_prefix}" UNIXODBC_LIBDIR="%{_libdir}"

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps

%{make_install} INSTALL_ROOT="$RPM_BUILD_ROOT"

# install *.desktop files
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}

# install icons used for applications in *.desktop files
install -p -m 644 ODBCDataManagerQ4/ODBC64.xpm \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps/ODBCCreateDataSourceQ5.xpm
install -p -m 644 odbcinstQ5/ODBCManageDataSources64.xpm \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps/ODBCManageDataSourcesQ5.xpm

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING GPL.txt LGPL.txt
%doc AUTHORS ChangeLog NEWS doc
%{_bindir}/ODBCCreateDataSourceQ5
%{_bindir}/ODBCManageDataSourcesQ5
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_libdir}/libodbcinstQ*so*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Jan Staněk <jstanek@redhat.com> - 0-0.26.20190111svn132
- Add back dependency on qt5-qtbase-devel (pulls qmake and necessary macros)
- Use %%make_build and %%make_install macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20190111svn132
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Jeff Law <law@redhat.com> - 0-0.23.20190111svn132
- Drop dependency on qt5-devel

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20190111svn132
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Jan Staněk <jstanek@redhat.com> - 0-0.19.20190111svn132
- Update source tarball to revision r132
- Build Qt5 versions of the provided utilities

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.11.20120105svn98
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20120105svn98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Honza Horak <hhorak@redhat.com> - 0-0.5.20120105svn98
- desktop files minor fixes
  Related: #768986

* Tue Jan 10 2012 Tom Lane <tgl@redhat.com> - 0-0.4.20120105svn98
- minor specfile improvements

* Thu Jan 05 2012 Honza Horak <hhorak@redhat.com> - 0-0.3.20120105svn98
- fixed issues found by Package Review process (see #767622)

* Thu Dec 15 2011 Honza Horak <hhorak@redhat.com> - 0-0.2.20111208svn95
- add Provides: unixODBC-kde to indicate unixODBC-gui-qt fills the gap after
  GUI utils are no longer part of unixODBC

* Tue Dec 13 2011 Honza Horak <hhorak@redhat.com> - 0-0.1.20111208svn95
- initial build from svn commit 95 after detachment from unixODBC project
