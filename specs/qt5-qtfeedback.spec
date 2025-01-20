%global qt_module qtfeedback

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Summary: Qt5 Tactile Feedback
Name:    qt5-qtfeedback
Version: 20180903gita14bd0b
Release: 11%{?dist}

License: GPL-2.0-or-later AND LGPL-3.0-only AND GFDL-1.3-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0 AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1
Url:     https://code.qt.io/cgit/qt/qtfeedback.git/
Source0: %{qt_module}-%{version}.tar.gz


BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel

%description
Qt5 tactile feedback libraries. This enables capabilities like vibrator feedback
for virtual keyboards.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.


%prep
%autosetup -n %{qt_module}-%{version} -p1
#  Taken from OpenSuse package (otherwise it fails to build)
touch .git # To make sure syncqt is used

%build
%{qmake_qt5} \
  CONFIG+=package multimedia_disabled=yes immersion_enabled=no meegotouchfeedback_enabled=no

%make_build

%install
make install INSTALL_ROOT=%{buildroot}
%if 0%{?flatpak}
# qtbase is part of runtime in /usr, this is built in /app
mv %{buildroot}/usr %{buildroot}%{_prefix}
sed -i -e "\|^libdir=|s|/usr/%{_lib}|%{_libdir}|" %{buildroot}%{_qt5_libdir}/*.la
sed -i -e "\|^prefix=|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/pkgconfig/*.pc
sed -i -e "\|^[^\#]|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/cmake/*/*.cmake
%endif

%ldconfig_scriptlets

%files
%license LICENSE* LGPL_EXCEPTION.txt
%{_qt5_libdir}/libQt5Feedback.so.*
%{_qt5_libdir}/qt5/qml/QtFeedback/*

%files devel
%{_qt5_libdir}/libQt5Feedback.so
%{_qt5_libdir}/libQt5Feedback.prl
%{_qt5_libdir}/libQt5Feedback.la
%{_qt5_libdir}/pkgconfig/Qt5Feedback.pc
%{_qt5_includedir}/QtFeedback/
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_feedback*.pri
%{_qt5_libdir}/cmake/Qt5Feedback/*.cmake

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 20180903gita14bd0b-4
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20180903gita14bd0b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Jan Grulich <jgrulich@redhat.com> - 20180903gita14bd0b-1
- Initial package from git snapshot
