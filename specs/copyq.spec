%global forgeurl https://github.com/hluk/CopyQ/
%global commit 4aab252568347dbea3e8d7929d92ae2b7308aef2

Name:    copyq
Version: 9.1.0
Release: %autorelease
Summary: Advanced clipboard manager
License: GPL-3.0-or-later

%{forgemeta}

Url:     %{forgeurl}
Source0: %{forgesource}
Source1: %{name}.rpmlintrc

Patch0:  copyq-fix-qt6.9-build.patch

BuildRequires: cmake, extra-cmake-modules, gcc-c++
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils, git
BuildRequires: libXtst-devel, libXfixes-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kstatusnotifieritem-devel
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-qtbase-devel, qt6-qtbase-private-devel
BuildRequires: qt6-qtsvg-devel, qt6-qtdeclarative-devel
BuildRequires: qt6-qttools-devel, kf6-kstatusnotifieritem-devel
BuildRequires: qwt-qt6-devel
BuildRequires: wayland-devel, qt6-qtwayland-devel

%description
CopyQ is advanced clipboard manager with searchable and editable history with
support for image formats, command line control and more.

%prep
%{forgesetup}
%autosetup -p1 -n %{archivename}
sed -i '/DQT_RESTRICTED_CAST_FROM_ASCII/d' CMakeLists.txt

%build
%cmake_kf6 \
  -Wno-dev \
  -DWITH_QT6:BOOL=ON \
  -DWITH_TESTS:BOOL=ON \
  -DPLUGIN_INSTALL_PREFIX=%{_libdir}/%{name}/plugins \
  -DTRANSLATION_INSTALL_PREFIX:PATH=%{_datadir}/%{name}/locale

%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.github.hluk.%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/com.github.hluk.%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS CHANGES.md HACKING README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/metainfo/com.github.hluk.%{name}.appdata.xml
%{_datadir}/applications/com.github.hluk.%{name}.desktop
%{_datadir}/bash-completion/completions/copyq
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/locale/
%{_datadir}/%{name}/themes/
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
