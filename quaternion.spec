%global appid com.github.quaternion
%global forgeurl    https://github.com/quotient-im/Quaternion
%global commit      3d7083aad02b8892b2ba6843d64ff9766095f52f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate    20230827

Name:       quaternion
Version:    0.0.95.50~%{snapdate}g%{shortcommit}
Release:    %autorelease

%forgemeta

Summary:    A Qt5-based IM client for Matrix
License:    GPL-3.0-or-later
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Quotient)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Keychain)

Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}
Requires:       hicolor-icon-theme

%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.

%prep
%forgesetup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_WITH_QT6=NO \
    -DUSE_INTREE_LIBQMC=NO
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt
cp -p linux/%{appid}.appdata.xml %{buildroot}%{_metainfodir}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{appid}.appdata.xml

%changelog
%autochangelog
