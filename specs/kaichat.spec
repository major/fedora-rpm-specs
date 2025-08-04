Name:           kaichat
Version:        0.4.0
Release:        1%{?dist}
Summary:        Chat interface for AI models such as ollama

License:        CC0-1.0 AND LGPL-2.0-or-later AND MIT AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://apps.kde.org/kaichat/

Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules

# Fedora
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

# Qt
BuildRequires:  cmake(Qt6Widgets)

# KDE Frameworks
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6DBusAddons)

# KDE Libraries
BuildRequires:  cmake(KF6TextAutoGenerateText) >= 1.7.0

# Misc
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

# Runtime requirements


%description
%summary.

%prep
%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kaichat
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.kaichat.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/kaichat
%{_kf6_libdir}/libkaichatcore.so.%{version}
%{_kf6_libdir}/libkaichatwidgets.so.%{version}
%{_kf6_datadir}/applications/org.kde.kaichat.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kaichat.png
%{_metainfodir}/org.kde.kaichat.appdata.xml
%{_kf6_datadir}/qlogging-categories6/kaichat.categories

%changelog
* Sat Aug 2 2025 Steve Cossette <farchord@gmail.com> - 0.4.0-1
- 0.4.0
