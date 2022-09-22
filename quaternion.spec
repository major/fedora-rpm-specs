%global appid com.github.quaternion
%global forgeurl    https://github.com/quotient-im/Quaternion
%global tag         %{version}

Name:       quaternion
Version:    0.0.95.1
Release:    %autorelease

%forgemeta

Summary:    A Qt5-based IM client for Matrix
License:    GPLv3
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
    -DUSE_INTREE_LIBQMC=NO
%make_build -C %{_vpath_builddir}

%install
%make_install -C %{_vpath_builddir}
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
