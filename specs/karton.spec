%global gitcommit 07520e06f5a66e9cfe33a298a11e5482a2395aa0
%global gitdate 20251110.023853
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:           karton
Version:        0.1^%{gitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        A Libvirt-based Virtual Machine Manager for KDE

License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-3.0-or-later
# It'll change at some point
URL:            https://invent.kde.org/sitter/%{name}
Source0:        %{url}/-/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6IconThemes)

BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(libosinfo-1.0)
BuildRequires:  pkgconfig(spice-client-glib-2.0)
Requires:       kf6-kirigami
Requires:       hicolor-icon-theme


%description
%{summary}.

%prep
%autosetup -n %{name}-%{gitcommit} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
# Currently fails. Will make sure it's enabled by the time it goes stable.
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.karton.desktop ||:

%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/karton
%{_kf6_datadir}/applications/org.kde.karton.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/karton_logo.svg
%{_kf6_datadir}/qlogging-categories6/karton.categories

%changelog
* Wed Dec 31 2025 Steve Cossette <farchord@gmail.com> - 0.1^20251110.023853.07520e0-1
- Updated git snapshot

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1^20250502.060152.b318dca-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat May 24 2025 Steve Cossette <farchord@gmail.com> - 0.1^20250502.060152.b318dca-1
- Initial release
