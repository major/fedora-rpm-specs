Summary:        A GUI front-end to CHMlib
Name:           xchm
Version:        1.37
Release:        %autorelease
License:        GPL-2.0-or-later
URL:            https://github.com/rzvncj/xCHM
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  chmlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  wxGTK-devel

%description
xCHM is a wxWidgets-based .chm viewer. xCHM can show the contents tree if
one is available, print the displayed page, change fonts faces and size,
work with bookmarks, do the usual history stunts (forward, back, home),
provide a searchable index and seach for text in the whole book. The
search is a fast B-tree search, based on the internal $FIftiMain file
found inside indexed .chm archives, and it can be customized to search in
content or just the topics' titles.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README
%license AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
