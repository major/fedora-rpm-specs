# Maintenance has moved from SourceForge to GitHub, but there has never been a
# tagged release on GitHub. We package a post-release snapshot to get some
# minor fixes from the original 3.0.3 release on SourceForge.
%global commit b1d5212831842ee5869d99bc208a21837e4037d5
%global snapdate 20210820

# Should we re-generate Autoconf build files? Opinions vary wildly and strongly
# on this! We choose to do so.
%bcond autoreconf 1

Name:           libcsv
Version:        3.0.3^%{snapdate}git%{sub %{commit} 1 7}
%global so_version 3
Release:        %autorelease
Summary:        Fast and flexible CSV library written in pure ANSI C

# Upstream says in README:
#
#   The example programs are not covered under a license and can be used
#   without restriction.
#
# This resembles, but isn’t unambiguously, a public domain dedication. See also
# the “Freely redistributable without restrictions” License identifier
# described in the pre-SPDX licensing guidelines, which seems to be a close
# match for this language.
#
# We believe we can safely distribute these in the source RPM, but we choose
# not to package them as documentation in order to avoid dealing with their
# lack of a clear license.
#
# The “or any later version…” language that makes this LGPLv2+ rather than
# strictly LGPLv2 is not in the README or COPYING files, but in the comments in
# the source file headers.
#
# The following files under other licenses belong to the build system and
# therefore do not contribute to the license of the binary RPMs:
#   - aclocal.m4, m4/libtool.m4, m4/ltoptions.m4, m4/ltsugar.m4,
#     m4/ltversion.m4, and m4/lt~obsolete.m4 are FSFULLR
#   - compile, depcomp, ltmain.sh, missing, and test-driver are
#     GPL-2.0-or-later
#   - config.guess and config.sub are GPL-3.0-or-later
#   - configure is FSFUL, or, more likely, (FSFUL and LGPL-2.1-or-later)
#   - install-sh is X11
License:        LGPL-2.1-or-later
URL:            https://github.com/rgamble/libcsv
Source:         %{url}/archive/%{commit}/libcsv-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

%description
Fast and flexible CSV library written in pure ANSI C that can read and write
CSV data.


%package devel
Summary:        Development files for libcsv

Requires:       libcsv%{?_isa} = %{version}-%{release}

%description devel
The libcsv-devel package contains libraries and header files for
developing applications that use libcsv.


%prep
%autosetup -n libcsv-%{commit}


%build
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --disable-static
%make_build


%install
%make_install
find '%{buildroot}' -type f -name '*.la' -print -delete


%check
%make_build check


%files
%license COPYING
%doc README

%{_libdir}/libcsv.so.%{so_version}{,.*}


%files devel
%doc csv.pdf
%doc FAQ

%{_includedir}/csv.h
%{_libdir}/libcsv.so
%{_mandir}/man3/csv.3*


%changelog
%autochangelog
