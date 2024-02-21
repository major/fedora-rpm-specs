# currently we have to pull directly from upstream SVN
%global svn 144
%global checkout 20240219svn%{svn}

Summary: Several GUI (Qt) programs and plug-ins for unixODBC
Name: unixODBC-gui-qt
# There has not been a formal upstream release yet and we're not
# sure what the first formal release version number will be, so using 0
Version: 0^%{checkout}
Release: %autorelease
URL: http://sourceforge.net/projects/unixodbc-gui-qt/
# Programs are GPL, libraries are LGPL
License: GPL-3.0-only AND LGPL-3.0-only

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
install -p -m 644 odbcinstQ5/ODBCManageDataSources64.xpm \
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
%autochangelog
