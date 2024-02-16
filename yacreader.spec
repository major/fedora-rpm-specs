%global appname YACReader
%global versuf 2402143

Name:           yacreader
Version:        9.14.2
Release:        %autorelease
Summary:        Cross platform comic reader and library manager

# The entire source code is GPL-3.0-or-later except:
# BSD-3-Clause: QsLog
#               folder_model
# MIT:          pictureflow
License:        GPL-3.0-or-later AND BSD-3-Clause AND MIT
URL:            https://www.yacreader.com
Source0:        https://github.com/YACReader/%{name}/releases/download/%{version}/%{name}-%{version}.%{versuf}-src.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake3
BuildRequires:  mesa-libGLU-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5ScriptTools)
BuildRequires:  cmake(Qt5Svg)

# For YACReaderLibrary QR Code display
BuildRequires:  pkgconfig(libqrencode)

BuildRequires:  pkgconfig(libunarr)
BuildRequires:  pkgconfig(poppler-qt5)

Requires:       hicolor-icon-theme
Requires:       qt5-qtgraphicaleffects%{?_isa}
Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       qt5-qtsvg

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
# Translations
lrelease-qt5 %{appname}/%{appname}.pro
lrelease-qt5 %{appname}Library/%{appname}Library.pro

%qmake_qt5
%make_build


%install
%make_install \
    INSTALL_ROOT=%{buildroot}
# Translations
mkdir -p %{buildroot}%{_datadir}/%{name}/languages
find . -name \*.qm -exec cp {} %{buildroot}%{_datadir}/%{name}/languages/ \;
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
