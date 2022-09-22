Name:           dtkgui
Version:        5.5.22
Release:        %autorelease
Summary:        Deepin dtkgui
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkgui

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  dtkcore-devel
BuildRequires:  librsvg2-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  make
%description
Dtkgui is the GUI module for DDE look and feel.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} \
           DTK_VERSION=%{version} \
           LIB_INSTALL_DIR=%{_libdir} \
           BIN_INSTALL_DIR=%{_libexecdir}/dtk5 \
           TOOL_INSTALL_DIR=%{_libexecdir}/dtk5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libexecdir}/dtk5/deepin-gui-settings
%{_libexecdir}/dtk5/dde-kwin-debug
%{_libexecdir}/dtk5/dnd-test-client
%{_libexecdir}/dtk5/dnd-test-server

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/dtkgui*.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkgui*.pri
%{_libdir}/cmake/DtkGui*/
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
