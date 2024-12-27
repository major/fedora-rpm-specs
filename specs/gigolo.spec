%global minorversion 0.5

Name:           gigolo
Version:        0.5.4
Release:        %autorelease
Summary:        GIO/GVFS management application

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://goodies.xfce.org/projects/applications/gigolo/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make

Requires:       gvfs-fuse

Obsoletes: sion < 0.1.0-3

%description
A frontend to easily manage connections to remote filesystems using GIO/GVFS. 
It allows you to quickly connect/mount a remote filesystem and manage
bookmarks of such. 

%prep
%setup -q

%build
#rm -f waf
%configure
%make_build


%install
%make_install
%find_lang %{name}

# remove duplicate docs
rm -rf %{buildroot}/%{_datadir}/doc/gigolo

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO THANKS
%{_bindir}/gigolo
%{_datadir}/icons/hicolor/*/apps/org.xfce.gigolo.*
%{_datadir}/applications/gigolo.desktop
%{_mandir}/man1/gigolo.1.gz

%changelog
%autochangelog
