Summary:   Qt5 support library for PackageKit
Name:      PackageKit-Qt5
Version:   1.1.2
Release:   5%{?dist}

License:   LGPL-2.1-only
URL:       http://www.packagekit.org/

Source0:   https://github.com/hughsie/PackageKit-Qt/archive/v%{version}.tar.gz

# Upstream patches

BuildRequires: cmake
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Sql)
BuildRequires: gcc-c++
# required for /usr/share/dbus-1/interfaces/*.xml
BuildRequires: PackageKit >= 0.9.1

Recommends: PackageKit

%description
PackageKit-Qt is a Qt support library for PackageKit

%package devel
Summary: Development files for PackageKit-Qt5
Requires: PackageKit-Qt5%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -p1 -n PackageKit-Qt-%{version}


%build
%cmake -DBUILD_WITH_QT6=OFF
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/libpackagekitqt5.so.%{version}
%{_libdir}/libpackagekitqt5.so.1

%files devel
%{_libdir}/libpackagekitqt5.so
%{_libdir}/pkgconfig/packagekitqt5.pc
%{_includedir}/packagekitqt5/
%{_libdir}/cmake/packagekitqt5/

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Sep 25 2025 Steve Cossette <farchord@gmail.com> - 1.1.2-3
- Split off from PackageKit-Qt
