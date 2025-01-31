Summary: SELinux Translation Daemon
Name: mcstrans
Version: 3.8
Release: 0.rc3.1%{?dist}.1
License: GPL-2.0-or-later
Url: https://github.com/SELinuxProject/selinux/wiki
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}-rc3/mcstrans-%{version}-rc3.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}-rc3/mcstrans-%{version}-rc3.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
Source3: secolor.conf.8
# fedora-selinux/selinux: git format-patch -N 3.8 -- mcstrans
# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
# Patch list start
# Patch list end
BuildRequires: gcc
BuildRequires: make
BuildRequires: libselinux-devel >= %{version}
BuildRequires: libcap-devel pcre2-devel libsepol-devel libsepol-static
BuildRequires: systemd
BuildRequires: gnupg2
Requires: pcre2
%{?systemd_requires}
Provides: setransd
Provides: libsetrans

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

mcstrans provides an translation daemon to translate SELinux categories 
from internal representations to user defined representation.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n mcstrans-%{version}-rc3

%build
%set_build_flags

%make_build LIBDIR="%{_libdir}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}%{_usr}/share/mcstrans
mkdir -p %{buildroot}%{_sysconfdir}/selinux/mls/setrans.d

%make_install LIBDIR="%{_libdir}" SHLIBDIR="%{_lib}" SBINDIR="%{_sbindir}"
rm -f %{buildroot}%{_libdir}/*.a
cp -r share/* %{buildroot}%{_usr}/share/mcstrans/
# Systemd 
mkdir -p %{buildroot}%{_unitdir}
ln -s mcstrans.service %{buildroot}/%{_unitdir}/mcstransd.service
rm -rf %{buildroot}/%{_sysconfdir}/rc.d/init.d/mcstrans
install -m644 %{SOURCE3} %{buildroot}%{_mandir}/man8/

%post 
%systemd_post mcstransd.service

%preun
%systemd_preun mcstransd.service

%postun 
%systemd_postun mcstransd.service

%files
%{_mandir}/man8/mcs.8.gz
%{_mandir}/man8/mcstransd.8.gz
%{_mandir}/man5/setrans.conf.5.gz
%{_mandir}/man8/secolor.conf.8.gz
%{_sbindir}/mcstransd
%{_unitdir}/mcstrans.service
%{_unitdir}/mcstransd.service
%dir %{_sysconfdir}/selinux/mls/setrans.d

%dir %{_usr}/share/mcstrans

%defattr(0644,root,root,0755)
%dir %{_usr}/share/mcstrans/util
%dir %{_usr}/share/mcstrans/examples
%{_usr}/share/mcstrans/examples/*

%defattr(0755,root,root,0755)
%{_usr}/share/mcstrans/util/*

%changelog
%autochangelog
