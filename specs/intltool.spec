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

# Fix intltool-update to work with perl 5.26. Patch taken from
# Debian's intltool_0.51.0-4.debian.tar.xz
Patch: intltool-perl5.26-regex-fixes.patch
# https://bugs.launchpad.net/intltool/+bug/1505260
# https://bugzilla.redhat.com/show_bug.cgi?id=1249051
Patch: intltool-merge-Create-cache-file-atomically.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1318674
Patch: intltool_distcheck-fix.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2268342
# https://bugs.launchpad.net/intltool/+bug/1687644
Patch: intltool-cache-race.patch

%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.

%prep
%autosetup -p1

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
