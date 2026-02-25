Name:       gsmartcontrol
Version:    2.0.2
Release:    %autorelease
Summary:    Graphical user interface for smartctl

# Note that the "Whatever" license is effectively the MIT license.  See email
# from Tom Callaway to Fedora-legal-list on 18-APR-2011.
# Automatically converted from old format: (GPLv2 or GPLv3) and BSD and zlib and Boost and MIT - review is highly recommended.
License:    (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Callaway-BSD AND Zlib AND BSL-1.0 AND LicenseRef-Callaway-MIT

URL:        http://gsmartcontrol.sourceforge.net
Source0:    https://github.com/ashaduri/gsmartcontrol/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtkmm30-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make
Requires:       smartmontools >= 5.43
Requires:       hicolor-icon-theme
Requires:       xterm

%description
GSmartControl is a graphical user interface for smartctl (from
smartmontools package), which is a tool for querying and controlling
SMART (Self-Monitoring, Analysis, and Reporting Technology) data on
modern hard disk drives. It allows you to inspect the drive's SMART
data to determine its health, as well as run various tests on it.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE.txt LICENSE.LGPL3.txt
%{_bindir}/%{name}-root
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/polkit-1/actions/org.%{name}.policy
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-root.1.*
%{_pkgdocdir}
%{_datadir}/metainfo/gsmartcontrol.appdata.xml

%changelog
%autochangelog
