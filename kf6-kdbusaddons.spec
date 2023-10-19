%global gitdate		20230829.232927
%global cmakever	5.240.0
%global commit0		fbb85588c24d0f118959c530022cab2833cf5a39
%global shortcommit0	%(c=%{commit0}; echo ${c:0:7})
%global framework	kdbusaddons

Name:			kf6-%{framework}
Version:		%{cmakever}^%{gitdate}.%{shortcommit0}
Release:		3%{?dist}
Summary:		KDE Frameworks 6 Tier 1 addon with various classes on top of QtDBus
License:		CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:			https://invent.kde.org/frameworks/%{framework}
Source0:		https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:		extra-cmake-modules >= %{cmakever}
BuildRequires:		kf6-rpm-macros
BuildRequires:		cmake
BuildRequires:		gcc-c++
BuildRequires:		qt6-qtbase-devel
BuildRequires:		qt6-qtbase-private-devel
BuildRequires:		qt6-qttools-devel
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

%prep
%autosetup -n %{framework}-%{commit0} -p1

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
%{_kf6_archdatadir}/mkspecs/modules/qt_KDBusAddons.pri


%changelog
* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230829.232927.fbb8558-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.232927.fbb8558-2
- Rebuild for Qt Private API

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232927.fbb8558-1
- Initial Release
