%define _lto_cflags %{nil}

Name:       libfaketime
Version:    0.9.12
Release:    %autorelease
Summary:    Manipulate system time per process for testing purposes
# most of the code is GPL-2.0-or-later AND GPL-3.0-only
# part of src/libfaketime.c is GPLv3
License:    GPL-2.0-or-later AND GPL-3.0-only
URL:        https://github.com/wolfcw/libfaketime
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Provides:   faketime = %{version}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-Time-HiRes

# https://github.com/wolfcw/libfaketime/pull/525
Patch0: libfaketime-0.9.12-isoc23.patch

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
