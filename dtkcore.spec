Name:           dtkcore
Version:        5.6.13
Release:        %autorelease
Summary:        Deepin tool kit core modules
# migrated to SPDX
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  dtkcommon-devel
BuildRequires:  libicu-devel
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  gtest-devel
BuildRequires:  cmake
BuildRequires:  qt5-doctools
BuildRequires:  %{_bindir}/doxygen

# Qt5 private headers needed
BuildRequires:  qt5-qtbase-private-devel

Requires:       dtkcommon%{_isa}
Requires:       deepin-desktop-base
Requires:       lshw


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
sed -i 's|/etc/os-version|/etc/uos-version|' src/dsysinfo.cpp

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DBUILD_DOCS=ON \
       -DBUILD_EXAMPLES=OFF \
       -DQCH_INSTALL_DESTINATION=%{_qt5_docdir}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libexecdir}/dtk5/

%files devel
%doc docs/Specification.md
%{_includedir}/dtk5/
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_libdir}/cmake/DtkCore/
%{_libdir}/cmake/DtkCMake/
%{_libdir}/cmake/DtkDConfig/
%{_libdir}/cmake/DtkTools/
%{_libdir}/pkgconfig/dtkcore.pc
%{_libdir}/lib%{name}.so
%{_qt5_docdir}/%{name}.qch

%changelog
%autochangelog
