Name:          kde-inotify-survey
Version:       24.12.2
Release:       1%{?dist}
Summary:       Monitors inotify limits and lets the user know when exceeded

# Complete license breakdown can be found in the "LICENSE-BREAKDOWN" file
License:       BSD-3-Clause and CC0-1.0 and FSFAP and GPL-2.0-only and GPL-3.0-only
URL:           https://invent.kde.org/system/%{name}

Source:        https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Updates the dbus service config to use the right policies to satisfy a rpmlint error
# Merge Request: https://invent.kde.org/frameworks/kauth/-/merge_requests/44
Source1:       org.kde.kded.inotify.conf

Requires:      kf6-kded
Requires:      dbus-common
Requires:      polkit
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: qt6-qtbase-devel
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Auth)

%description
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name
rm %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
install -m644 -p -D %{SOURCE1} %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf

%files -f %{name}.lang
%license LICENSES/* screenshot.png.license
%doc README.md screenshot.png
%{_bindir}/kde-inotify-survey
%{_kf6_plugindir}/kded/inotify.so
%{_kf6_libexecdir}/kauth/kded-inotify-helper
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
%{_datadir}/knotifications6/org.kde.kded.inotify.notifyrc
%{_datadir}/metainfo/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy

%changelog
* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Sun Nov 19 2023 Steve Cossette <farchord@gmail.com> - 24.01.75-1
- 24.01.75

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Thu Jun 8 2023 Steve Cossette <farchord@gmail.com> - 23.04.2-3
- Update to 23.04.2
- Fixed changelog mistake

* Mon May 29 2023 Steve Cossette <farchord@gmail.com> - 23.04.1-1
- Initial release
