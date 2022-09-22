Name:           edflib
Version:        1.22
# Upstream has been encouraged to provide a shared library with proper ABI
# versioning (https://gitlab.com/Teuniz/EDFlib/-/issues/6#note_732772193).
#
# For now, we must make do with downstream .so name versioning
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/#_downstream_so_name_versioning).
# Make sure to increment the following integer each time there is an ABI change
# upstream.
%global downstream_so_number 2
Release:        %autorelease
Summary:        C/C++ library to read/write EDF+ and BDF+ files

# The entire source is BSD-3-Clause, except:
#   - The executable sources sine_generator.c, sweep_generator.c,
#     test_edflib.c, and test_generator.c are all BSD-2-Clause, but the
#     binaries built from these sources are not installed; therefore these
#     sources do not contribute to the license of the binary RPMs.
#   - The contents of unittest/ are GPL-3.0-or-later, but the binaries that
#     link these sources are for testing only and are not installed; therefore
#     these sources do not contribute to the license of the binary RPMs.
License:        BSD-3-Clause
URL:            https://gitlab.com/Teuniz/EDFlib/
%global tar_version %(echo '%{version}' | tr -d .)
Source0:        https://www.teuniz.net/edflib/edflib_%{tar_version}.tar.gz
# Upstream intends this library primarily as a copylib. The following is based
# on a sample Makefile from
# https://gitlab.com/Teuniz/EDFlib/-/issues/6#note_628056608, with
# modifications to pass LDFLAGS and to implement downstream .so name
# versioning.
Source1:        Makefile

# Add support for big-endian platforms (fixes #9)
# https://gitlab.com/Teuniz/EDFlib/-/merge_requests/1
# See also: https://gitlab.com/Teuniz/EDFlib/-/issues/9
#
# Since upstream decided against supporting big-endian platforms, this patch is
# applied *only* on s390x to keep the other architectures closer to upstream.
Patch:          0001-Add-support-for-big-endian-platforms.patch

BuildRequires:  make
BuildRequires:  gcc

%global common_description %{expand:
EDFlib is a programming library for C/C++ for reading and writing EDF+ and BDF+
files. It also reads “old style” EDF and BDF files. EDF means European Data
Format. BDF is the 24-bits version of EDF.

Documentation is available at https://www.teuniz.net/edflib/index.html.}

%description %common_description

Documentation is available at https://www.teuniz.net/edflib/index.html.


%package devel
Summary:        Development files for edflib
Requires:       edflib%{?_isa} = %{version}-%{release}

%description devel %common_description

The edflib-devel package contains libraries and header files for developing
applications that use edflib.


%prep
%setup -n edflib_%{tar_version} -q
%ifarch s390x
%patch0 -p1
%endif
cp -p '%{SOURCE1}' Makefile.shared


%build
%set_build_flags
%make_build -f Makefile.shared DOWNSTREAM_SO_NUMBER='%{downstream_so_number}'
%make_build -C unittest CC="${CC-gcc}" \
    CFLAGS="${CFLAGS} -D_LARGEFILE64_SOURCE -D_LARGEFILE_SOURCE ${LDFLAGS}"


%install
%make_install -f Makefile.shared \
    DOWNSTREAM_SO_NUMBER='%{downstream_so_number}' \
    PREFIX='%{_prefix}' \
    INCLUDEDIR='%{_includedir}' \
    LIBDIR='%{_libdir}'

%check
./unittest/edflib_test


%files
%license LICENSE
%doc README.md
%{_libdir}/libedf.so.0.%{downstream_so_number}


%files devel
%{_includedir}/edflib.h
%{_libdir}/libedf.so


%changelog
%autochangelog
