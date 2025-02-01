Summary: SELinux binary policy manipulation library
Name: libsepol
Version: 3.8
Release: 1%{?dist}
License: LGPL-2.1-or-later
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsepol-%{version}.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsepol-%{version}.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
URL: https://github.com/SELinuxProject/selinux/wiki
# $ git clone https://github.com/fedora-selinux/selinux.git
# $ cd selinux
# $ git format-patch -N libsepol-3.8 -- libsepol
# $ i=1; for j in 0*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
# Patch list start
# Patch list end
BuildRequires: make
BuildRequires: gcc
BuildRequires: flex
BuildRequires: gnupg2
Obsoletes: %{name}-compat = 3.1-4

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%package devel
Summary: Header files and libraries used to build policy manipulation tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The libsepol-devel package contains the libraries and header files
needed for developing applications that manipulate binary policies. 

%package static
Summary: static libraries used to build policy manipulation tools
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libsepol-static package contains the static libraries and header files
needed for developing applications that manipulate binary policies. 

%package utils
Summary: SELinux libsepol utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
The libsepol-utils package contains the utilities

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n libsepol-%{version}

# sparc64 is an -fPIC arch, so we need to fix it here
%ifarch sparc64
sed -i 's/fpic/fPIC/g' src/Makefile
%endif

%build
%set_build_flags
CFLAGS="$CFLAGS -fno-semantic-interposition"
%make_build LIBDIR="%{_libdir}"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir} 
mkdir -p ${RPM_BUILD_ROOT}%{_includedir} 
mkdir -p ${RPM_BUILD_ROOT}%{_bindir} 
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man3
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
%make_install LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}"
rm -rf ${RPM_BUILD_ROOT}%{_mandir}/man8/gen*
rm -rf ${RPM_BUILD_ROOT}%{_mandir}/ru/man8

%files static
%{_libdir}/libsepol.a

%files devel
%{_libdir}/libsepol.so
%{_libdir}/pkgconfig/libsepol.pc
%{_includedir}/sepol/*.h
%{_mandir}/man3/*.3.gz
%dir %{_includedir}/sepol
%dir %{_includedir}/sepol/policydb
%{_includedir}/sepol/policydb/*.h
%dir %{_includedir}/sepol/cil
%{_includedir}/sepol/cil/*.h

%files
%license LICENSE
%{_libdir}/libsepol.so.2

%files utils
%{_bindir}/chkcon
%{_bindir}/sepol_check_access
%{_bindir}/sepol_compute_av
%{_bindir}/sepol_compute_member
%{_bindir}/sepol_compute_relabel
%{_bindir}/sepol_validate_transition
%{_mandir}/man8/chkcon.8.gz

%changelog
%autochangelog
