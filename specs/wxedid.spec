Name:          wxedid
Version:       0.0.33
Release:       %autorelease
Summary:       Extended Display Identification Data editor
# src/rcode: LGPL-3.0-or-later
# src/*: GPL-3.0-or-later
License:       GPL-3.0-or-later AND LGPL-3.0-or-later
URL:           https://sourceforge.net/projects/wxedid
Source0:       https://downloads.sourceforge.net/wxedid/wxedid-%{version}.tar.gz
Source1:       wxedid.desktop
Source2:       wxedid.appdata.xml
Source3:       wxedid.png
Patch0:        wxedid-use-fedora-cflags.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: wxGTK-devel

%description
wxEDID is a wxWidgets - based EDID (Extended Display Identification Data)
editor.

Supported structures: EDID v1.3+ base structure and the CEA/CTA-861-H (as first
extension block).

Besides normal editor functionality, the app has been equipped with a DTD
constructor, which aims to ease timings selection/editing. It's also possible
to export and import EDID data to/from text files (hex ASCII format) and also
to export the structures as a human-readable text.

%prep
%autosetup -p1

%conf
autoreconf -fiv
%configure

%build
%make_build

%install
%make_install
install -dm755 %{buildroot}%{_mandir}/man1
install -pm644 man/wxedid.1 %{buildroot}%{_mandir}/man1
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
install -Dpm644 %{S:2} %{buildroot}%{_metainfodir}/wxedid.appdata.xml
install -Dpm644 %{S:3} %{buildroot}%{_datadir}/pixmaps/wxedid.png

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/wxedid.appdata.xml

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/wxedid
%{_datadir}/applications/wxedid.desktop
%{_datadir}/pixmaps/wxedid.png
%{_mandir}/man1/wxedid.1*
%{_metainfodir}/wxedid.appdata.xml

%changelog
%autochangelog
