%global appname YACReader
%global versuf 2209046

Name:           yacreader
Version:        9.9.1
Release:        %autorelease
Summary:        Cross platform comic reader and library manager

# The entire source code is GPLv3+ except:
# BSD:          QsLog
#               folder_model
# MIT:          pictureflow
License:        GPLv3+ and BSD and MIT
URL:            https://www.yacreader.com
Source0:        https://github.com/YACReader/%{name}/releases/download/%{version}/%{name}-%{version}.%{versuf}-src.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(libunarr)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5Svg)
# For YACReaderLibrary QR Code display
BuildRequires:  pkgconfig(libqrencode)

Requires:       hicolor-icon-theme
Requires:       qt5-qtgraphicaleffects%{?_isa}
Requires:       qt5-qtquickcontrols%{?_isa}

%description
Best comic reader and comic manager with support for .cbr .cbz .zip .rar comic
files.


%prep
%autosetup -n %{name}-%{version}.%{versuf}

# wrong-file-end-of-line-encoding fix
sed -i 's/\r$//' INSTALL.md

# file-not-utf8 fix
iconv -f iso8859-1 -t utf-8 README.md > README.md.conv && mv -f README.md.conv README.md


%build
%qmake_qt5
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt
%find_lang %{name}library --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang -f %{name}library.lang
%license COPYING.txt
%doc CHANGELOG.md README.md INSTALL.md
%{_bindir}/%{appname}
%{_bindir}/%{appname}Library
%{_bindir}/%{appname}LibraryServer
%{_datadir}/%{name}/server/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
%{_userunitdir}/*.service
%dir %{_datadir}/%{name}/


%changelog
%autochangelog
