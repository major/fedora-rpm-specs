Name: pam_radius
Summary: PAM Module for RADIUS Authentication
Version: 3.0.0
Release: 2%{?dist}
License: GPL-2.0-or-later
URL: http://www.freeradius.org/pam_radius_auth/

%global underscored_v 3_0_0

Source0: https://github.com/FreeRADIUS/pam_radius/releases/download/release_%{underscored_v}/pam_radius-%{version}.tar.gz
Source1: https://github.com/FreeRADIUS/pam_radius/releases/download/release_%{underscored_v}/pam_radius-%{version}.tar.gz.sig
Requires: pam
BuildRequires: make
BuildRequires: pam-devel
BuildRequires: gcc

%description
pam_radius is a PAM module which allows user authentication using 
a radius server.

%prep
%setup -q -n pam_radius-%{version}

%build
%configure --enable-werror
make %{?_smp_mflags} CFLAGS="%{optflags} -Wall -fPIC -Wno-unused-but-set-variable -Wno-strict-aliasing"

%install
mkdir -p %{buildroot}/%{_lib}/security
install -p pam_radius_auth.so %{buildroot}/%{_lib}/security
mkdir -p %{buildroot}%{_sysconfdir}
install -p pam_radius_auth.conf %{buildroot}%{_sysconfdir}/pam_radius_auth.conf

%post
# Upstream changed the location of the configuration file everywhere, so it's
# time to align with them and remove all downstream only patches.
if [ -e "/etc/pam_radius.conf" ]; then
    mv "/etc/pam_radius.conf" "/etc/pam_radius_auth.conf"
fi

%files
%doc README.md INSTALL USAGE LICENSE Changelog
%config(noreplace) %attr(0600, root, root) %{_sysconfdir}/pam_radius_auth.conf
/%{_lib}/security/pam_radius_auth.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 27 2024 Iker Pedrosa <ipedrosa@redhat.com> - 3.0.0-1
- Rebase to version 3.0.0
- Remove all downstream patches as they are no longer needed

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May  2 2023 Iker Pedrosa <ipedrosa@redhat.com> - 2.0.0-6
- pam_radius_auth: allow "ipv4=no" and "ipv6=no" in the PAM file. Resolves: #2192547

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov  9 2022 Iker Pedrosa <ipedrosa@redhat.com> - 2.0.0-4
- SPDX license migration

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Iker Pedrosa <ipedrosa@redhat.com> - 2.0.0-2
- pam_radius_auth: stop printing password

* Thu May 26 2022 Iker Pedrosa <ipedrosa@redhat.com> - 2.0.0-1
- Rebase to version 2.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Alexander Scheel <ascheel@redhat.com> - 1.4.0-14
- Fix NULL-termination of password buffer, garbage contents prior to hashing

* Mon Apr 01 2019 Jason Taylor <jtfas90@gmail.com> - 1.4.0-13
- Fixed broken patch definition

* Mon Apr 01 2019 Jason Taylor <jtfas90@gmail.com> - 1.4.0-12
- Rebuild with gcc buildrequires

* Thu Mar 14 2019 Jason Taylor <jtfas90@gmail.com> - 1.4.0-11
- Rebuilt with patch for password length buffer overflow

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.0-2
- Update spec to guidelines and fix build on new arches

* Sun Dec 21 2014 Tim Lank <timlank@timlank.com> 1.4.0-1
- Many changes.  See USAGE for details.

* Sun Feb 21 2010 Tim Lank <timlank@timlank.com> 1.3.17-2
- everything it takes to get this accepted for Fedora 

* Mon Oct 26 2009 Richard Monk <rmonk@redhat.com> 1.3.17-0
- Bump for new version
- spec fixes for x86_64 builds

* Mon Jun 03 2002 Richie Laager <rlaager@wiktel.com> 1.3.15-0
- Inital RPM Version
