%global upstream_name kdev-python

Name:           kdevelop-python
Version:        26.04.3
Release:        2%{?dist}
Summary:        KDevelop Python language support

License:        CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:            https://kdevelop.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{upstream_name}-%{version}.tar.xz

# Fixes to build against python 3.15
Patch0:         65.patch

# kdevelop depends on qt6-qtwebengine, which is only available on some arches
ExclusiveArch:  %{qt6_qtwebengine_arches}
 
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# Needs to track kdevelop
BuildRequires:  kdevelop-devel = 9:%{version}
BuildRequires:  libappstream-glib

BuildRequires:  python3-devel
BuildRequires:  pkgconfig(cups)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)


%description
%{summary}.

%prep
%autosetup -n %{upstream_name}-%{version} -p1

%conf
%cmake_kf6

%build
%cmake_build

%install
%cmake_install

%check
%find_lang kdevpython --all-name
# • tag-invalid           : stock icon is not valid [kdevelop]
# Reported Upstream: https://bugs.kde.org/show_bug.cgi?id=522338
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdev-python.metainfo.xml ||:

%files -f kdevpython.lang
%license LICENSES/*
%doc DESIGN INSTALL README README.packagers
%{_kf6_libdir}/libkdevpython*.so
%{_kf6_qtplugindir}/kdevplatform/65/kdevpdb.so
%{_kf6_qtplugindir}/kdevplatform/65/kdevpythonlanguagesupport.so
%{_kf6_datadir}/kdevappwizard/templates/*.tar.bz2
%{_kf6_datadir}/kdevpythonsupport/
%{_kf6_metainfodir}/org.kde.kdev-python.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/kdevpythonsupport.categories

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 26.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jul 03 2026 Steve Cossette <farchord@gmail.com> - 26.04.3-1
- 26.04.3

* Sat Jun 27 2026 Steve Cossette <farchord@gmail.com> - 26.04.2-1
- Initial Import
