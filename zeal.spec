%global commit 1cfa7c637f745be9d98777f06b4f8dec90892bf2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           zeal
Version:        0.6.2
Release:        5.20230618.%{shortcommit}%{?dist}
Summary:        Offline documentation browser inspired by Dash

License:        GPLv3+
URL:            https://zealdocs.org/
Source:         https://github.com/zealdocs/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         0001-apply-websettings.patch

# We should use %%qt6_qtwebengine_arches provided by qt6-srpm-macros
# but one of our dependency qt6-qtwebengine is available only
# for aarch64 and x86_64.
# BZ for the macro: https://bugzilla.redhat.com/show_bug.cgi?id=2215703
# Ticket about the arch supoort: https://bugreports.qt.io/browse/QTBUG-102143
ExclusiveArch:  aarch64 x86_64

BuildRequires:  cmake(Qt6Core) >= 6.2.0
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6Network)

BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires:       hicolor-icon-theme

%description
Zeal is a simple offline documentation browser inspired by Dash.


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
# turn off shared libs building:
# - it's only used from Zeal itself
# - build scripts not configured to install the lib
%cmake_qt6 \
  -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.zealdocs.zeal.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.zealdocs.zeal.appdata.xml


%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/org.zealdocs.zeal.desktop
%{_metainfodir}/org.zealdocs.zeal.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Wed Jul 26 2023 Björn Esser <besser82@fedoraproject.org> - 0.6.2-5.20230618.1cfa7c6
- Rebuild(qt6)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4.20230618.1cfa7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Lumír Balhar <lbalhar@redhat.com> - 0.6.2-3.20230618.1cfa7c6
- Rebuild

* Sun Jun 18 2023 Lumír Balhar <lbalhar@redhat.com> - 0.6.2-2.20230618.1cfa7c6
- Don't use obsoleted forge macros

* Sat Jun 10 2023 Zephyr Lykos <fedora@mochaa.ws> - 0.6.2-1.git1cfa7c6
- Update to commit 1cfa7c6
- Migrate to Qt 6
- Use forge macros
- Deprecate versioned cmake macros
- Clean up BuildRequires
- Reflect the actual version written in CMakeLists.txt

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-14.20220826.00d4b9c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 26 2022 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-13.20220826.00d4b9c
- Update to commit 00d4b9c

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-12.20200821.dbb8eb2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11.20200821.dbb8eb2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 21 2021 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-10.20210821.dbb8eb2
- Package the latest version from master branch to fix segfaults

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-8
- Fix build on rawhide
Resolves: rhbz#1923599

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-4
- Disable ads on the welcome page by default

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-2
- Specfile improved

* Wed Nov  7 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Fri Aug 24 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.0-3
- Fix missing dependency on libCore.so - don't build Zeal with shared libs flag

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Remove obsolete scriptlets

* Tue Jan 16 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0
- Switch to cmake; upstream is deprecating qmake
- and its rule for detecting Qt >= 5.5.1 breaks on F28's Qt 5.10

* Mon Sep  4 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Michel Alexandre Salim <michel@dellxps.localdomain> - 0.3.1-1
- Update to 0.3.1

* Sat Sep 24 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Mon Feb 22 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Michel Salim <salimma@fedoraproject.org> - 0.1.1-2
- Update license info, add bundled lib metadata

* Thu Sep 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1.1-1
- Initial package
