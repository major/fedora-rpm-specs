Name:           R-fs
Version:        %R_rpm_version 1.6.6
Release:        %autorelease
Summary:        Cross-Platform File System Operations Based on 'libuv'

# Wasn't this so much nicer when it was just GPLv3?
# SPDX is currently missing this one:
# https://scancode-licensedb.aboutcode.org/bsd-credit.html
License:        GPL-3.0-only AND libutil-David-Nugent AND BSD-3-Clause AND BSD-2-Clause AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain AND Beerware
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libuv) >= 1.18.0

%description
A cross-platform interface to file system operations, built on top of the
'libuv' C library.

%prep
%autosetup -c
rm -f fs/tests/testthat/test-fs_*.R # unconditional suggest, should be fixed
rm -f fs/tests/testthat/test-file.R # unconditional suggest, should be fixed
# Remove bundled libuv
rm -rf fs/src/libuv-* fs/inst/COPYRIGHTS
cat << EOF > fs/src/Makevars
SOURCES = \$(wildcard *.cc unix/*.cc)
OBJECTS = \$(SOURCES:.cc=.o)
OBJECTS += bsd/setmode.o bsd/strmode.o bsd/reallocarray.o
PKG_LIBS = $(pkgconf --libs libuv)
PKG_CPPFLAGS = $(pkgconf --cflags libuv) -I.
EOF

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
