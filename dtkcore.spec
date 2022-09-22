Name:           dtkcore
Version:        5.5.30
Release:        %autorelease
Summary:        Deepin tool kit core modules
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  dtkcommon-devel
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  gtest-devel
BuildRequires:  make

# Qt5 private headers needed
BuildRequires:  qt5-qtbase-private-devel

Requires:       dtkcommon%{_isa}

# since f30
Obsoletes:      deepin-tool-kit <= 0.3.3
Obsoletes:      deepin-tool-kit-devel <= 0.3.3
Obsoletes:      dtksettings <= 0.1.7
Obsoletes:      dtksettings-devel <= 0.1.7

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel%{_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1

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
%dir %{_libexecdir}/dtk5/
%{_libexecdir}/dtk5/dtk-settings
%{_libexecdir}/dtk5/dtk-license.py
%{_libexecdir}/dtk5/dtk-translate.py
%{_libexecdir}/dtk5/deepin-os-release
%{_prefix}/bin/qdbusxml2cpp-fix

%files devel
%doc doc/Specification.md
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/DtkCore*/
%{_libdir}/cmake/DtkCMake*/
%{_libdir}/cmake/DtkTools*/
%{_libdir}/pkgconfig/dtkcore*.pc
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
