Name:          kde-inotify-survey
Version:       23.04.3
Release:       2%{?dist}
Summary:       Monitors inotify limits and lets the user know when exceeded

# Complete license breakdown can be found in the "LICENSE-BREAKDOWN" file
License:       BSD-3-Clause and CC0-1.0 and FSFAP and GPL-2.0-only and GPL-3.0-only
URL:           https://invent.kde.org/system/%{name}

Source:        https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Updates the dbus service config to use the right policies to satisfy a rpmlint error
# Merge Request: https://invent.kde.org/frameworks/kauth/-/merge_requests/44
Source1:       org.kde.kded.inotify.conf

Requires:      kf5-kded
Requires:      dbus-common
Requires:      polkit
BuildRequires: kf5-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: qt5-qtbase-devel
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Auth)

%description
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%{cmake_kf5}
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
%{_kf5_plugindir}/kded/inotify.so
%{_kf5_libexecdir}/kauth/kded-inotify-helper
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
%{_datadir}/knotifications5/org.kde.kded.inotify.notifyrc
%{_datadir}/metainfo/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Thu Jun 8 2023 Steve Cossette <farchord@gmail.com> - 23.04.2-3
- Update to 23.04.2
- Fixed changelog mistake

* Mon May 29 2023 Steve Cossette <farchord@gmail.com> - 23.04.1-1
- Initial release
