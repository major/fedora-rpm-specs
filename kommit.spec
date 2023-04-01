Name:           kommit
Version:        1.0.1
Release:        1%{?dist}
Summary:        Git gui client for KDE

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://apps.kde.org/kommit/
Source0:        https://invent.kde.org/sdk/kommit/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-syntax-highlighting-devel

Requires:       kf5-filesystem
Requires:       hicolor-icon-theme

Provides:       gitklient = %{version}-%{release}
Obsoletes:      gitklient < 1.0

%description
Git gui client for KDE.

%prep
%autosetup -n %{name}-v%{version}


%build
%cmake
%cmake_build


%install
%cmake_install
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}diff
%{_bindir}/%{name}merge
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.4.0
%{_libdir}/lib%{name}diff.so.0
%{_libdir}/lib%{name}diff.so.0.4.0
%{_libdir}/lib%{name}gui.so.0
%{_libdir}/lib%{name}gui.so.0.4.0
%{_libdir}/qt5/plugins/kf5/kfileitemaction/%{name}itemaction.so
%{_libdir}/qt5/plugins/kf5/overlayicon/%{name}overlayplugin.so
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/qlogging-categories5/kommit.categories
%{_defaultdocdir}/HTML/en/%{name}


%changelog
* Thu Mar 30 2023 Vasiliy Glazov <vascom2@gmail.com> 1.0.1-1
- renaming of gitklient
