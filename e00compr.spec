Name:           e00compr
Version:        1.0.1
# Unless upstream accepts Source1, we will need to maintain an soversion
# downstream.
%global downstream_soversion 0.1
%global soversion %{downstream_soversion}
Release:        %autorelease
Summary:        Library to compress and uncompress E00 files

# SPDX
License:        MIT
URL:            http://avce00.maptools.org/e00compr
Source0:        http://avce00.maptools.org/dl/e00compr-%{version}.tar.gz
# Build a shared library instead of a static one, and version it with an
# appropriate SONAME.
#
# New account creation is broken on upstream bug tracker
# http://bugzilla.maptools.org/; Makefile.shared sent upstream by email
# 2022-01-05.
Source1:        Makefile.shared

# Fix possible buffer overflow due to strncpy() not null-terminating when it
# truncates:
#
# New account creation is broken on upstream bug tracker
# http://bugzilla.maptools.org/; patch sent upstream by email 2022-01-05.
Patch:          e00compr-1.0.1-strncpy-null-term.patch

# Unused variable
#
# New account creation is broken on upstream bug tracker
# http://bugzilla.maptools.org/; patch sent upstream by email 2022-01-05.
Patch:          e00compr-1.0.1-nDigits-unused.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  dos2unix

Requires:       e00compr-libs%{?_isa} = %{version}-%{release}
Requires:       e00compr-tools%{?_isa} = %{version}-%{release}

%global common_description %{expand:
E00compr is an ANSI C library that reads and writes Arc/Info compressed E00
files. Both “PARTIAL” and “FULL” compression levels are supported.

This package can be divided in three parts:

  • The ‘e00conv’ command-line program. This program takes a E00 file as input
    (compressed or not) and copies it to a new file with the requested
    compression level (NONE, PARTIAL or FULL).

  • A set of library functions to read compressed E00 files. These functions
    read a E00 file (compressed or not) and return a stream of uncompressed
    lines, making the E00 file appear as if it was not compressed.

  • A set of library functions to write compressed E00 files. These functions
    take one line after another from what should be a uncompressed E00 file,
    and write them to a file with the requested compression level, either NONE,
    PARTIAL or FULL.}

%description %{common_description}

This is a metapackage that installs both the command-line tools
(e00compr-tools) and the libraries (e00compr-libs).


%package libs
Summary:        Libraries for e00compr

%description libs %{common_description}

The e00compr-libs package contains the e00compr libraries.


%package devel
Summary:        Development files for e00compr

Requires:       e00compr-libs%{?_isa} = %{version}-%{release}

%description devel %{common_description}

The e00compr-devel package contains libraries and header files for developing
applications that use e00compr.


%package tools
Summary:        Command-line tools associated with e00compr

Requires:       e00compr-libs%{?_isa} = %{version}-%{release}

%description tools
This package provides the ‘e00conv’ command-line program, which takes a E00
file as input (compressed or not) and copies it to a new file with the
requested compression level (NONE, PARTIAL or FULL).


%prep
%autosetup
dos2unix --keepdate *.TXT *.txt
# Nothing in this package is a script; nothing should be executable.
find . -type f -perm /0111 -exec chmod -v a-x '{}' '+'

# Header name conflict with cpl (cpl_error.h)
# http://bugzilla.maptools.org/show_bug.cgi?id=2367
# Use actual header file locations in examples.
# Leave the upstream locations in the documentation since it assumes developers
# will use a static library or possibly copy sources into a dependent project’s
# source tree.
sed -r -i 's@"(e00compr)\.h"@<\1/\1.h>@' ex_*.c

# New account creation is broken on upstream bug tracker
# http://bugzilla.maptools.org/; suggested creation of a separate file by email
# to upstream on 2022-01-05.
awk 'toupper($0) ~ /(COPYRIGHT|LICENSE)/ { o=1 }; /[-]{3,}/ { o=0 }; o' \
    README.TXT | tee LICENSE

# Unless upstream accepts Source1, we will need to maintain an soversion
# downstream. Replace the suggested “1” with an “earlier” downstream version.
cp -p '%{SOURCE1}' Makefile.shared
sed -r -i 's/(SOVER=[[:blank:]]*)1/\1%{downstream_soversion}/' Makefile.shared


%build
%make_build \
    CC="${CC-gcc}" \
    CFLAGS="${CFLAGS}" \
    LFLAGS="${LDFLAGS}" \
    -f Makefile.shared


%install
# Upstream Makefile lacks an “install” target.
# Header name conflict with cpl (cpl_error.h)
# http://bugzilla.maptools.org/show_bug.cgi?id=2367
install -t '%{buildroot}%{_includedir}/e00compr' -D -p -m 0644 *.h
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 e00conv.1
install -d '%{buildroot}%{_libdir}'
# Use cp with an extra option, instead of install, to preserve symlinks
cp -p --no-dereference *.so *.so.* '%{buildroot}%{_libdir}'
install -t '%{buildroot}%{_bindir}' -D -p e00conv


%files
# Metapackage


%files libs
%license LICENSE
%doc README.TXT
%doc HISTORY.TXT
%{_libdir}/libe00compr.so.%{soversion}


%files tools
%doc e00compr.txt
%doc e00compr.html
%{_bindir}/e00conv
%{_mandir}/man1/e00conv.1.*


%files devel
# Examples:
%doc ex_*.c
%{_includedir}/e00compr/
%{_libdir}/libe00compr.so


%changelog
%autochangelog
