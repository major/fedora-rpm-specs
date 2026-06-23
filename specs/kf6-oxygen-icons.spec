%global framework oxygen-icons

Name:           kf6-oxygen-icons
Version:        6.27.0
Release:        2%{?dist}
Summary:        Oxygen icon theme

License:        CC0-1.0 AND LGPL-3.0-or-later
URL:            https://invent.kde.org/frameworks/oxygen-icons
Source0:        http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  libappstream-glib

%description
Oxygen Icons is a freedesktop.org compatible icon theme originally
developed for the KDE Plasma desktop environment in combination with
the Oxygen Style. It features smooth gradients, soft shadows, and a
slightly glossy look.

%package -n oxygen-icon-theme
Epoch:       1
Summary:     Oxygen icon theme
License:     CC0-1.0 AND LGPL-3.0-or-later
BuildArch:   noarch
Requires:    hicolor-icon-theme
# Needed for proper Fedora logo
Requires:    system-logos
# Renamed from oxygen-icon-theme
Obsoletes:   oxygen-icon-theme < 1:6.27.0-1
Conflicts:   oxygen-icon-theme < 1:6.27.0-1

%description -n oxygen-icon-theme
Oxygen Icons is a freedesktop.org compatible icon theme originally
developed for the KDE Plasma desktop environment in combination with
the Oxygen Style. It features smooth gradients, soft shadows, and a
slightly glossy look.


%prep
%autosetup -n %{framework}-%{version} -p1

%conf
%cmake_kf6

%build
%cmake_build


%install
%cmake_install

## icon optimizations
du -s .
hardlink -c -v %{buildroot}%{_datadir}/icons/
du -s .

# %%ghost icon.cache
touch %{buildroot}%{_kf6_datadir}/icons/oxygen/icon-theme.cache

## trigger-based scriptlets
%transfiletriggerin -n oxygen-icon-theme -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :

%transfiletriggerpostun -n oxygen-icon-theme -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.oxygenicon.metainfo.xml

%files -n oxygen-icon-theme
%license LICENSES/*
%doc README.md AUTHORS
%ghost %{_datadir}/icons/oxygen/icon-theme.cache
%{_datadir}/icons/oxygen/index.theme
%{_datadir}/icons/oxygen/*/
%{_metainfodir}/org.kde.oxygenicon.metainfo.xml



%changelog
* Sun Jun 21 2026 Steve Cossette <farchord@gmail.com> - 6.27.0-2
- Changed conflicts/obsoletes as the previous package had an epoch

* Sun Jun 14 2026 Steve Cossette <farchord@gmail.com> - 6.27.0-1
- Initial Release
