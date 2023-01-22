#For git snapshots, set to 0 to use release instead:
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 4e881ab49b26f82eb3e66e1ffe73f4f23af7b4a3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif

Summary: Qt6 - Configuration Tool
Name:    qt6ct
Version: 0.7
%if 0%{?usesnapshot}
Release: 0.2%{?snapshottag}%{?dist}
%else
Release: 2%{?dist}
%endif

# The entire source code is under BSD-2-Clause License
License: BSD
Url:     https://github.com/trialuser02/qt6ct

%if 0%{?usesnapshot}
Source0: https://github.com/trialuser02/qt6ct/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0: https://github.com/trialuser02/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

ExcludeArch:   s390x

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-linguist
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: chrpath
BuildRequires:  desktop-file-utils
Requires: qt6-qtsvg

%description
This program allows users to configure Qt6 settings (theme, font, icons, etc.)
under DE/WM without Qt integration.

%prep
%if 0%{?usesnapshot}
%setup -q -n %{name}-%{commit0}
%else
%autosetup -n %{name}-%{version} -p1
%endif


%build
# Create translation files.
lrelease-qt6 src/qt6ct/translations/*.ts
%{_qt6_qmake} %{_qt6_qmake_flags}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
# /usr/bin/qt6ct' contains a standard rpath '/usr/lib64' in [/usr/lib64]
chrpath --delete %{buildroot}%{_bindir}/%{name}
chrpath --delete %{buildroot}%{_qt6_plugindir}/styles/libqt6ct-style.so
chrpath --delete %{buildroot}%{_qt6_plugindir}/platformthemes/libqt6ct.so

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc AUTHORS README ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_qt6_plugindir}/platformthemes/libqt6ct.so
%{_qt6_plugindir}/styles/libqt6ct-style.so
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/colors/
%{_datadir}/%{name}/colors/*.conf
%dir %{_datadir}/%{name}/qss/
%{_datadir}/%{name}/qss/*.qss

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.7-1
- Update to 0.7-1

* Sat Oct 22 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.7-0.1.git4e881ab
- Fix crash with a segmentation fault when closing the tool

* Wed Sep 21 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.6-0.1.git6abd586
- New Snapshot version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5-1
- Update to 0.5
- Add ExcludeArch s390x

* Sat Aug 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4-2
- Add missing desktop file validation
- Add BR desktop-file-utils

* Wed Aug 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4-1
- Update to 0.4
- Fix unowned directories

* Thu Jul 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3-1
- Update to 0.3

* Mon Feb 08 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2-1
- initial Build
