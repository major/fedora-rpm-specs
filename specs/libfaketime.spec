%define _lto_cflags %{nil}

Name:       libfaketime
Version:    0.9.12
Release:    %autorelease
Summary:    Manipulate system time per process for testing purposes
# COPYING:                  GPLv2 text
# man/faketime.1:           "GNU General Public License, see COPYING"
# README:                   "GNU General Public License, see COPYING"
# src/faketime.c:           GPL-2.0-only
# src/faketime_common.h:    GPL-2.0-only
# src/libfaketime.c:        GPL-2.0-only AND GPL-3.0-only
# src/time_ops.h:           GPL-2.0-only
# src/uthash.h:             BSD-1-Clause
## Not in any binary package
# src/timeprivacy:          BSD-2-Clause
# test/libmallocintercept.c:    GPL-2.0-only
# test/timetest.c:          GPL-2.0-or-later
License:    GPL-3.0-only AND GPL-2.0-only AND BSD-1-Clause
SourceLicense:  %{license} AND GPL-2.0-or-later AND BSD-2-Clause
URL:        https://github.com/wolfcw/libfaketime
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/wolfcw/libfaketime/pull/525
Patch0:     libfaketime-0.9.12-isoc23.patch
# Make the libraires executable, needed for stripping them. Not suitable for
# upstream, e.g. Debian does not like it.
Patch1:     libfaketime-0.9.12-Dynamic-libraries-are-expected-to-be-executable-on-F.patch
# Adapt to GCC 16, posted upstream,
# <https://github.com/wolfcw/libfaketime/pull/528>
Patch2:     libfaketime-0.9.12-tests-Silence-an-unused-but-set-variable-warning-wit.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
# Tests:
BuildRequires:  bash
BuildRequires:  perl-interpreter
BuildRequires:  perl(Time::HiRes)
Provides:   faketime = %{version}-%{release}

%description
libfaketime intercepts various system calls that programs use to retrieve the
current date and time. It then reports modified (faked) dates and times (as
specified by you, the user) to these programs. This means you can modify the
system time a program sees without having to change the time system-wide.

%prep
%autosetup -p1

%build
%ifarch ppc64le
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif
%ifarch riscv64
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
%endif

%set_build_flags
%make_build PREFIX=%{_prefix} LIBDIRNAME=/%{_lib} all

%check
%ifarch ppc64le
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif
%ifarch riscv64
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
%endif

make PREFIX=%{_prefix} LIBDIRNAME=/%{_lib} -C test

%install
%make_install PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}

# Pick up docs in the files section
rm -fr %{buildroot}/%{_docdir}/faketime

%files
%license COPYING
%doc README NEWS README.developers
%{_bindir}/faketime
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}MT.so.1
%{_mandir}/man1/faketime.1*

%changelog
%autochangelog
