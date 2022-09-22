%global repo dde-network-utils


Name:           deepin-network-utils
Version:        5.4.13
Release:        %autorelease
Summary:        Deepin desktop-environment - network utils
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-network-utils
%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  make
BuildRequires:  gio-qt-devel
BuildRequires:  gtest-devel

%description
Deepin desktop-environment - network utils.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i 's|/lib$|/%{_lib}|' dde-network-utils/dde-network-utils.pro

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%{_libdir}/lib*.so.1
%{_libdir}/lib*.so.1.*
%{_datadir}/%{repo}/

%files devel
%{_includedir}/libddenetworkutils/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
%autochangelog
