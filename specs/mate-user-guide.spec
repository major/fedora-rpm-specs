%global branch 1.28

Name:        mate-user-guide
Summary:     User Guide for MATE desktop
Version:     %{branch}.0
Release:     %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
URL:         http://mate-desktop.org
BuildArch:   noarch
Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: mate-common
BuildRequires: desktop-file-utils

Requires: yelp

%description
Documentations for MATE desktop.

%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
  --delete-original                                \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
$RPM_BUILD_ROOT%{_datadir}/applications/mate-user-guide.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog
%{_datadir}/applications/mate-user-guide.desktop


%changelog
%autochangelog
