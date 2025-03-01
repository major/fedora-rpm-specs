Name: intltool
Summary: Utility for internationalizing various kinds of data files
Version: 0.51.0
Release: %autorelease
License: GPL-2.0-or-later WITH Autoconf-exception-generic
#VCS: bzr:https://code.edge.launchpad.net/~intltool/intltool/trunk
Source: https://edge.launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz
URL: https://launchpad.net/intltool
BuildArch: noarch
Requires: patch
# for /usr/share/aclocal
Requires: automake
Requires: gettext-devel
Requires: perl(Getopt::Long)
Requires: perl(XML::Parser)
BuildRequires: perl-generators
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(XML::Parser)
BuildRequires: gettext
BuildRequires: make
# http://bugzilla.gnome.org/show_bug.cgi?id=568845
# Dropping this patch per the last comment on that thread:
# Martin Pitt: As the reporter of the bug I close this, as the new API du jour is gsettings,
# which has a sensible gettext integration.
#Patch0: schemas-merge.patch
# Fix intltool-update to work with perl 5.26. Patch taken from
# Debian's intltool_0.51.0-4.debian.tar.xz
Patch1: intltool-perl5.26-regex-fixes.patch
# https://bugs.launchpad.net/intltool/+bug/1505260
# https://bugzilla.redhat.com/show_bug.cgi?id=1249051
Patch2: intltool-merge-Create-cache-file-atomically.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1318674
Patch3: intltool_distcheck-fix.patch

%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.

%prep
%setup -q
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

%build
%configure

%make_build

%install
%make_install

%check
if ! make check; then
    find . -type f -name 'test-suite.log' | while read trs; do
	echo "BEGIN " ${trs}; cat ${trs} 1>&2;
    done
    echo  "Exiting abnormally due to make check failure above" 1>&2
    exit 1
fi

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/intltool*
%{_datadir}/intltool
%{_datadir}/aclocal/intltool.m4
%{_mandir}/man8/intltool*.8*

%changelog
%autochangelog
