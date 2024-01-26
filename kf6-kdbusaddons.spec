%global framework	kdbusaddons

Name:			kf6-%{framework}
Version:		5.248.0
Release:		3%{?dist}
Summary:		KDE Frameworks 6 Tier 1 addon with various classes on top of QtDBus
License:		CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:			https://invent.kde.org/frameworks/%{framework}
Source0:		https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:		extra-cmake-modules >= %{version}
BuildRequires:		kf6-rpm-macros
BuildRequires:		cmake
BuildRequires:		gcc-c++
BuildRequires:		qt6-qtbase-devel
BuildRequires:		qt6-qttools-devel
BuildRequires:          qt6-qtbase-private-devel
BuildRequires:		pkgconfig(xkbcommon)

Requires:		kf6-filesystem

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		qt6-qtbase-devel
%description		devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kdbusaddons6_qt

%files -f kdbusaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_bindir}/kquitapp6
%{_kf6_libdir}/libKF6DBusAddons.so.*

%files devel
%{_kf6_includedir}/KDBusAddons/
%{_kf6_libdir}/libKF6DBusAddons.so
%{_kf6_libdir}/cmake/KF6DBusAddons/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 5.247.0-2
- add doc package for KF6 API

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 5.245.0-2
- Rebuild (qt6)

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com>
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230829.232927.fbb8558-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.232927.fbb8558-2
- Rebuild for Qt Private API

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232927.fbb8558-1
- Initial Release
