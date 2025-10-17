%bcond autoreconf 1

Name:           readosm
Version:        1.1.0a
%global so_version 1
Release:        %autorelease
Summary:        Library to extract valid data from within an Open Street Map input file

# The entire source is (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) (the
# “MPL-tri-license”),
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
# … except for certain build-system files that do not affect the license of the
# binary RPMs:
#
# FSFULLR:
#   - aclocal.m4
#   - m4/ltoptions.m4
#   - m4/ltsugar.m4
#   - m4/ltversion.m4
#   - m4/lt~obsolete.m4
# FSFUL AND FSFULLR AND GPL-2.0-or-later WITH Libtool-exception:
#   - m4/libtool.m4
# GPL-2.0-or-later WITH Libtool-exception:
#   - ltmain.sh
# GPL-2.0-or-later WITH Autoconf-exception-generic:
#   - compile
#   - config.guess
#   - config.sub
#   - depcomp
#   - missing
#   - test-driver
# FSFUL AND GPL-2.0-or-later WITH Libtool-exception AND (MPL-1.1 OR
# GPL-2.0-or-later OR LGPL-2.1-or-later):
# (The tri-license is because it is derived from configure.ac.)
#   - configure
# X11:
#   - install-sh
SourceLicense:  %{shrink:
                (%{license}) AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Libtool-exception AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                X11
                }
Source:         https://www.gaia-gis.it/gaia-sins/readosm-sources/readosm-%{version}.tar.gz
URL:            https://www.gaia-gis.it/fossil/readosm

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  make
BuildRequires:  gcc

BuildRequires:  expat-devel
BuildRequires:  zlib-devel

%description
ReadOSM is a simple library intended for extracting the contents from 
Open Street Map files: both input formats (.osm XML based and .osm.pbf based
on Google's Protocol Buffer serialization) are indifferently supported.

%package devel
Summary:        Development libraries and headers for ReadOSM

Requires:       readosm%{?_isa} = %{version}-%{release}

%description devel
The readosm-devel package contains libraries and header files for
developing applications that use ReadOSM.


%prep
%autosetup


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
%doc AUTHORS

%{_libdir}/libreadosm.so.%{so_version}{,.*}


%files devel
%{_libdir}/pkgconfig/readosm.pc
%{_libdir}/libreadosm.so
%{_includedir}/readosm.h


%changelog
%autochangelog
