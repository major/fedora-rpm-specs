# This package contains files under %%_libdir but no binary files
%global debug_package %{nil}

Name:           dtkcommon
Version:        5.5.22
Release:        %autorelease
Summary:        DTK common files

License:        GPLv3+
URL:            https://github.com/linuxdeepin/dtkcommon
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# glib2 provides %%{_datadir}/glib-2.0/schemas/
Requires:       glib2%{?_isa}

%description
This package contains common configuration files for DTK.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}

%description devel
This package contains common build configuration files for DTK.


%prep
%autosetup -p1
sed -r -i 's|/lib/\$\$ARCH|/%{_lib}|; s|/lib/\$\(ARCH\)|/%{_lib}|' dtkcommon.pro

%build
%qmake_qt5 VERSION=%{version} LIB_INSTALL_DIR=%_libdir
%make_build


%install
%make_install INSTALL_ROOT=%buildroot


%files
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/*

%files devel
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/Dtk/

%changelog
%autochangelog
