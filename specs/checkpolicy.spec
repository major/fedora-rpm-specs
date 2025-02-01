%define libselinuxver 3.8-1
%define libsepolver 3.8-1

Summary: SELinux policy compiler
Name: checkpolicy
Version: 3.8
Release: 1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
# $ git clone https://github.com/fedora-selinux/selinux.git
# $ cd selinux
# $ git format-patch -N 3.8 -- checkpolicy
# $ i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
# Patch list start
# Patch list end
BuildRequires: gcc
BuildRequires: make
BuildRequires: byacc bison flex flex-static libsepol-static >= %{libsepolver} libselinux-devel  >= %{libselinuxver}
BuildRequires: gnupg2

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

This package contains checkpolicy, the SELinux policy compiler.  
Only required for building policies. 

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n checkpolicy-%{version}

%build

%set_build_flags

%make_build LIBDIR="%{_libdir}"
cd test
%make_build LIBDIR="%{_libdir}"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%make_install LIBDIR="%{_libdir}"
install test/dismod ${RPM_BUILD_ROOT}%{_bindir}/sedismod
install test/dispol ${RPM_BUILD_ROOT}%{_bindir}/sedispol

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/checkpolicy
%{_bindir}/checkmodule
%{_mandir}/man8/checkpolicy.8.gz
%{_mandir}/man8/checkmodule.8.gz
%{_bindir}/sedismod
%{_bindir}/sedispol

%changelog
%autochangelog
