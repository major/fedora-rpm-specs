Summary: Shared MIME information database
Name: shared-mime-info
Version: 2.5.1
Release: %autorelease
License: GPL-2.0-or-later
URL: http://freedesktop.org/Software/shared-mime-info
Source0: https://gitlab.freedesktop.org/xdg/shared-mime-info/-/archive/%{version}/shared-mime-info-%{version}.tar.bz2

Source1: mimeapps.list

%global xdgmime_commit 04ce4cd90cb3fa77d5348662de221a6f33b21b17
# Tarball for https://gitlab.freedesktop.org/xdg/xdgmime/-/tree/%%{xdgmime_commit}
Source6: https://gitlab.freedesktop.org/xdg/xdgmime/-/archive/%{xdgmime_commit}/xdgmime-%{xdgmime_commit}.tar.bz2

# Work-around for https://bugs.freedesktop.org/show_bug.cgi?id=40354
Patch0: 0001-Remove-sub-classing-from-OO.o-mime-types.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  xmlto
BuildRequires:  glib2-devel
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  git-core

# Disable pkgconfig autodep
%global __requires_exclude ^/usr/bin/pkg-config$

%description
This is the freedesktop.org shared MIME info database.

Many programs and desktops use the MIME system to represent the types of
files. Frequently, it is necessary to work out the correct MIME type for
a file. This is generally done by examining the file's name or contents,
and looking up the correct MIME type in a database.

%prep
%autosetup -S git_am

# xdgmime is expected under the subprojects directory
tar xjf %SOURCE6
mv xdgmime-%{xdgmime_commit}/ subprojects/xdgmime/

%build

# the updated mimedb is later owned as %%ghost to ensure proper file-ownership
# it also asserts it is possible to build it
%meson -Dupdate-mimedb=true
%meson_build

%install
%meson_install

find $RPM_BUILD_ROOT%{_datadir}/mime -type d \
| sed -e "s|^$RPM_BUILD_ROOT|%%dir |" > %{name}.files
find $RPM_BUILD_ROOT%{_datadir}/mime -type f -not -path "*/packages/*" \
| sed -e "s|^$RPM_BUILD_ROOT|%%ghost |" >> %{name}.files

# Install the distro fallback / DE-agnostic mimeapps.list. This is used whenever
# a DE-specific mimeapps.list file doesn't provide an app for a given type, or
# whenever the provided app isn't installed.
# See: https://specifications.freedesktop.org/mime-apps/latest/index.html
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/%{_datadir}/applications/mimeapps.list

## remove bogus translation files
## translations are already in the xml file installed
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*

%check
%meson_test --suite shared-mime-info

%post
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null ||:

%transfiletriggerin -- %{_datadir}/mime
update-mime-database -n %{_datadir}/mime &> /dev/null ||:

%transfiletriggerpostun -- %{_datadir}/mime
update-mime-database -n %{_datadir}/mime &> /dev/null ||:

%files -f %{name}.files
%license COPYING
%doc README.md NEWS CONTRIBUTING.md data/shared-mime-info-spec.xml
%{_bindir}/update-mime-database
%{_datadir}/mime/packages/*
%{_datadir}/applications/mimeapps.list
# better to co-own this dir than to pull in pkgconfig
%dir %{_datadir}/pkgconfig
%{_datadir}/pkgconfig/shared-mime-info.pc
%{_mandir}/man*/update-mime-database.*
# also co-own the gettext dirs, we don't require it
%dir %{_datadir}/gettext
%dir %{_datadir}/gettext/its
%{_datadir}/gettext/its/shared-mime-info.its
%{_datadir}/gettext/its/shared-mime-info.loc

%changelog
%autochangelog
