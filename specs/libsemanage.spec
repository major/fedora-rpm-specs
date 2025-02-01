%define libsepolver 3.8-1
%define libselinuxver 3.8-1

Summary: SELinux binary policy manipulation library
Name: libsemanage
Version: 3.8
Release: 1%{?dist}
License: LGPL-2.1-or-later
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsemanage-%{version}.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsemanage-%{version}.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
# git format-patch -N 3.8 -- libsemanage
# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
# Patch list start
# Patch list end
URL: https://github.com/SELinuxProject/selinux/wiki
Source3: semanage.conf

BuildRequires: gcc make
BuildRequires: libselinux-devel >= %{libselinuxver} swig
BuildRequires: libsepol-devel >= %{libsepolver} 
BuildRequires: audit-libs-devel
BuildRequires: bison flex bzip2-devel
BuildRequires: gnupg2

BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: bzip2-libs audit-libs
Requires: libselinux%{?_isa} >= %{libselinuxver}
Obsoletes: libsemanage-compat = 3.1-4

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

libsemanage provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%package static
Summary: Static library used to build policy manipulation tools
Requires: libsemanage-devel%{_isa} = %{version}-%{release}

%description static
The semanage-static package contains the static libraries 
needed for developing applications that manipulate binary policies. 

%package devel
Summary: Header files and libraries used to build policy manipulation tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The semanage-devel package contains the libraries and header files
needed for developing applications that manipulate binary policies. 

%package -n python3-libsemanage
Summary: semanage python 3 bindings for libsemanage
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libselinux-python3
%{?python_provide:%python_provide python3-libsemanage}
# Remove before F30
Provides: %{name}-python3 = %{version}-%{release}
Provides: %{name}-python3%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}

%description -n python3-libsemanage
The libsemanage-python3 package contains the python 3 bindings for developing
SELinux management applications.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n libsemanage-%{version}


%build
%set_build_flags
CFLAGS="$CFLAGS -fno-semantic-interposition"

# To support building the Python wrapper against multiple Python runtimes
# Define a function, for how to perform a "build" of the python wrapper against
# a specific runtime:
BuildPythonWrapper() {
  BinaryName=$1

  # Perform the build from the upstream Makefile:
  make \
    PYTHON=$BinaryName \
    LIBDIR="%{_libdir}" SHLIBDIR="%{_lib}" \
    pywrap
}

make clean
make swigify
%make_build LIBDIR="%{_libdir}" SHLIBDIR="%{_lib}" all

BuildPythonWrapper \
  %{__python3}

%install
InstallPythonWrapper() {
  BinaryName=$1

  make \
    PYTHON=$BinaryName \
    DESTDIR="${RPM_BUILD_ROOT}" LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}" \
    install-pywrap
}

mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir} 
mkdir -p ${RPM_BUILD_ROOT}%{_sharedstatedir}/selinux
mkdir -p ${RPM_BUILD_ROOT}%{_sharedstatedir}/selinux/tmp
%make_install LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}"

InstallPythonWrapper \
  %{__python3} \
  $(python3-config --extension-suffix)
  
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/selinux/semanage.conf

%files
%license LICENSE
%dir %{_sysconfdir}/selinux
%config(noreplace) %{_sysconfdir}/selinux/semanage.conf
%{_libdir}/libsemanage.so.2
%{_mandir}/man5/*
%dir %{_libexecdir}/selinux
%dir %{_sharedstatedir}/selinux
%dir %{_sharedstatedir}/selinux/tmp

%ldconfig_scriptlets

%files static
%{_libdir}/libsemanage.a

%files devel
%{_libdir}/libsemanage.so
%{_libdir}/pkgconfig/libsemanage.pc
%dir %{_includedir}/semanage
%{_includedir}/semanage/*.h
%{_mandir}/man3/*

%files -n python3-libsemanage
%{python3_sitearch}/*.so
%{python3_sitearch}/semanage.py*
%{python3_sitearch}/__pycache__/semanage*
%{_libexecdir}/selinux/semanage_migrate_store

%changelog
%autochangelog
