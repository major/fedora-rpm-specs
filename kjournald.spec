Name:          kjournald
Version:       23.08.1
Release:       2%{?dist}
Summary:       Framework for interacting with systemd-journald

License:       BSD-3-Clause and CC0-1.0 and MIT and LGPL-2.1-or-later and MIT
URL:           https://invent.kde.org/system/%{name}

Source:        https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: systemd-devel
BuildRequires: kf5-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
%{summary}.

%package       libs
Summary:       Library files for kjournald
Requires:      %{name} = %{version}
%description   libs

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.kjournaldbrowser.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kjournaldbrowser.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/kjournaldbrowser
%{_datadir}/applications/org.kde.kjournaldbrowser.desktop
%{_datadir}/metainfo/org.kde.kjournaldbrowser.appdata.xml
%{_datadir}/qlogging-categories5/kjournald.categories

%files libs
%{_libdir}/libkjournald.so
%{_libdir}/libkjournald.so.0
%{_libdir}/libkjournald.so.%{version}

%changelog
* Sat Sep 23 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-2
- Rebuild(extra-cmake-modules)

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Thu Jun 8 2023 Steve Cossette <farchord@gmail.com> - 23.04.2-1
- Initial release
