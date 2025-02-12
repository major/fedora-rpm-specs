Name:           cdsclient
Version:        4.07
Release:        %autorelease
Summary:        Tools to query databases at CDS

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://cdsarc.u-strasbg.fr/doc/cdsclient.html
Source0:        https://cdsarc.cds.unistra.fr/ftp/pub/sw/cdsclient-%{version}.tar.gz
# Patch to get useful debuginfo. strip was called in Makefile before and compiler
# flags were ignored, submitted upstream by email
Patch0:         fix_makefile_debuginfo.patch
# Upstream places abibcode.awk in /usr/bin although it is not an executable but
# arch independent data
Patch1:         abibcode_share_location_trim.patch

BuildRequires:  gcc
BuildRequires: make

# wget is used by some of the shell scripts to fetch data from servers
Requires:       wget

%description
The cdsclient package is a set of C and shell routines which can be built on
Unix stations or PCs running Linux, which once compiled allow to query some 
databases located at CDS or on mirrors over the network.

The cdsclient package includes two generic query programs:
- vizquery, a program to remotely query VizieR. It connects the VizieR server
  via the HTTP protocol (requires an access to the port 80)
- find_cats, a program for fast access to large surveys from a list of 
  positions, via a dedicated client (requires an access to the port 1660)
  Specific programs like find2mass or finducac3 are connecting directly to one
  of the very large surveys available from CDS (a very large survey has 107 
  or more rows).
  

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
sed -i -e '1 s|python|python3|' catClient.py


%build
# Compile with an older std until upstream fixes it
# Mail to upstream on 2025-02-12
CFLAGS="$CFLAGS --std=gnu17"
%configure 
make %{?_smp_mflags}


%install
# make install doesn't create directories
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_datadir}/%{name}
%make_install PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}
# Remove this unneeded stuff
rm -f %{buildroot}%{_prefix}/versions
rm -f %{buildroot}%{_bindir}/find_cats.gz
# Move abibcode.awk (non executable called by abibcode) to /usr/share/cdsclient/
mv %{buildroot}%{_bindir}/abibcode.awk %{buildroot}%{_datadir}/%{name}/abibcode.awk
%{_fixperms} %{buildroot}/*


%files
%if 0%{?fedora} >= 21
%license COPYING COPYRIGHT
%else
%doc COPYING COPYRIGHT
%endif
%dir %{_datadir}/%{name}
%dir %{_mandir}/mantex
%{_bindir}/*
%{_datadir}/%{name}/abibcode.awk
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/mantex/*


%changelog
%autochangelog
