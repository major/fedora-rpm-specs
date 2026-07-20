%if 0%{?fedora} >= 44
%bcond python 1
%else
# on Fedora 43 a .egg is generated
# probably not worth fixing the layout for a distro EOL
# at the end of the year
%bcond python 0
%endif
%bcond test 1

%ifarch %{ix86}
%global _cython_cpu i386
%elifarch ppc64le
%global _cython_cpu powerpc64le
%else
%global _cython_cpu %{_host_cpu}
%endif

Name:           libseccomp
Version:        2.6.1
Release:        %autorelease
Summary:        Enhanced seccomp library

%global soname_version %%(echo %%{version}} | cut -d. -f1)

License:        LGPL-2.1-only
URL:            https://github.com/seccomp/libseccomp
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  make

%ifnarch riscv64 s390
# Versions prior to 3.13.0-4 do not work on ARM with newer glibc 2.25.0-6
# See https://bugzilla.redhat.com/show_bug.cgi?id=1466017
BuildRequires:  valgrind >= 1:3.13.0-4
%endif

%global _description %{expand:
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.}

%description %{_description}


%package devel
Summary:        Development files used to build applications with libseccomp support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %{_description}

The %{name}-devel package contains the dynamic library and header files for
developing applications that use %{name}.


%package static
Summary:        Enhanced seccomp static library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static %{_description}

The %{name}-static package contains the static library for developing 
applications that statically link against %{name}.


%if %{with python}
%package python
Summary:        Python bindings for %{name}
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)
BuildRequires:  sed
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description python %{_description}

The %{name}-python package contains Python bindings for %{name}.

%files python
%{python3_sitearch}/seccomp-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/seccomp.cpython-%{python3_version_nodots}-%{_cython_cpu}-linux-gnu.so
%endif


%prep
%autosetup -p1
%if %{with python}
sed -ie 's|$cmd /usr/bin/env python|$cmd %{python3}|g' tests/regression
%endif

%conf
%configure %{?with_python:--enable-python}

%build
%make_build

%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_mandir}

%make_install

rm -f %{buildroot}/%{_libdir}/libseccomp.la
%if %{with python}
# this file is not necessary, and the files listed are prefixed with
# %%{buildroot} so we'd have to clean it up or delete it
rm -f %{buildroot}%{python3_sitearch}/install_files.txt
%endif

%check
%if %{with tests}
%make_build check
%endif


%files
%license LICENSE
%doc CREDITS README.md CHANGELOG CONTRIBUTING.md
%{_libdir}/libseccomp.so.%{soname_version}
%{_libdir}/libseccomp.so.%{version}

%files devel
%{_includedir}/seccomp.h
%{_includedir}/seccomp-syscalls.h
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%{_bindir}/scmp_sys_resolver
%{_mandir}/man1/*
%{_mandir}/man3/*

%files static
%{_libdir}/libseccomp.a


%changelog
%autochangelog
