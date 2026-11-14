Name:           gpscorrelate
Version:        2.4
Release:        %autorelease
Summary:        A GPS photo correlation / geotagging tool

License:        GPL-2.0-or-later
URL:            https://dfandrich.github.io/gpscorrelate/
VCS:            https://github.com/dfandrich/gpscorrelate
Source:         %{vcs}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  exiv2
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       hicolor-icon-theme


%description
Gpscorrelate adds coordinates to the exif data of jpeg pictures based on a gpx
track file. The correlation is done by comparing the timestamp of the images
with the timestamp of the gps coordinates.


%prep
%autosetup -p1


%build
%make_build prefix=%{_prefix} CFLAGS="%{optflags}" OFLAGS="%{optflags}" docdir="%{_pkgdocdir}"


%install
%make_install prefix=%{_prefix}
make install-desktop-file DESTDIR=%{buildroot} prefix=%{_prefix}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
make check


%files
%doc %{_pkgdocdir}
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-gui.svg
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
