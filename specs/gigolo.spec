# VCS   https://gitlab.xfce.org/apps/gigolo.git/

%global minorversion 0.6

Name:           gigolo
Version:        0.6.0
Release:        %autorelease
Summary:        GIO/GVFS management application

License:        GPL-2.0-only
URL:            https://docs.xfce.org/apps/gigolo/start
Source0:        https://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  meson
Requires:       gvfs-fuse

%description
A frontend to easily manage connections to remote filesystems using GIO/GVFS. 
It allows you to quickly connect/mount a remote filesystem and manage
bookmarks of such. 

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

# remove duplicate docs
rm -rf %{buildroot}%{_docdir}/%{name}

# Rename invalid hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO THANKS
%{_bindir}/gigolo
%{_datadir}/icons/hicolor/*/apps/org.xfce.gigolo.*
%{_datadir}/applications/gigolo.desktop
%{_mandir}/man1/gigolo.1.gz

%changelog
%autochangelog
