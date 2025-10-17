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

# The “or any later version…” language that makes this LGPLv2+ rather than
# strictly LGPLv2 is not in the README or COPYING files, but in the comments in
# the source file headers.
License:        LGPL-2.1-or-later
# The contents of examples/ are LicenseRef-Fedora-UltraPermissive:
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/618
# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/719
#
# From the README file:
#
#   The example programs are not covered under a license and can be used
#   without restriction.
#
# Examples are currently not packaged in the binary RPMs.
#
# The following files under other licenses belong to the build system and
# therefore do not contribute to the license of the binary RPMs:
#
# FSFUL AND GPL-2.0-or-later WITH Libtool-exception AND LGPL-2.1-or-later:
# (The LGPL-2.1-or-later is due to content from configure.ac.)
#   - configure
# FSFUL AND FSFULLR AND GPL-2.0-or-later WITH Libtool-exception:
#   - m4/libtool.m4
# FSFULLR:
#   - aclocal.m4
#   - m4/ltoptions.m4
#   - m4/ltsugar.m4
#   - m4/ltversion.m4
#   - m4/lt~obsolete.m4
# GPL-2.0-or-later WITH Autoconf-exception-generic:
#   - compile
#   - depcomp
#   - missing
#   - test-driver
# GPL-2.0-or-later WITH Libtool-exception:
#   - ltmain.sh
# GPL-3.0-or-later WITH Autoconf-exception-generic:
#   - config.guess
#   - config.sub
# X11:
#   - install-sh
SourceLicense:  %{shrink:
                %{license} AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-2.0-or-later WITH Libtool-exception AND
                GPL-3.0-or-later WITH Autoconf-exception-generic AND
                LicenseRef-Fedora-UltraPermissive AND
                X11
                }
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


%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --disable-static


%build
%make_build


%install
%make_install


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
