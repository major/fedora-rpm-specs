%global forgeurl https://github.com/Nitrokey/nitrokey-app
Version:        1.4.2
%forgemeta

Name:           nitrokey-app
Release:        %autorelease
Summary:        Nitrokey's Application
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

# Non-upstreamable, required to unbundle libraries
Patch:          0001-don-t-show-information-about-3rd-party-licenses.patch

# Based on https://github.com/Nitrokey/nitrokey-app/issues/498
Patch:          cmake4.patch

BuildRequires:  cmake
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cppcodec-1)
BuildRequires:  pkgconfig(libnitrokey-1) >= 3.5

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup %{forgesetupargs} -p1
# Remove 3rdparty libraries
rm -vr 3rdparty
# Unbundle libnitrokey
rm -vr libnitrokey

%build
# TODO: Please submit an issue to upstream (rhbz#2380934)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -GNinja -DADD_GIT_INFO=FALSE
%cmake_build

%install
%cmake_install

# We don't need ubuntu icons
rm -vr %{buildroot}%{_datadir}/icons/ubuntu*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.nitrokey.%{name}.appdata.xml

%files
%license LICENSES/GPLv3
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/com.nitrokey.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
