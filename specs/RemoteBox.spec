%global __requires_exclude perl\\(.*[.]pl\\)|^perl\\(vboxService\\)
%global __provides_exclude ^perl\\(vboxService\\)

Name:           RemoteBox
Version:        3.4
Release:        1%{?dist}
Summary:        Open Source VirtualBox Client with Remote Management
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only

URL:            http://remotebox.knobgoblin.org.uk/
Source0:        http://knobgoblin.org.uk/downloads/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  appdata-tools
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  perl-generators
BuildRequires:  sed

Requires:       perl-Gtk3
Requires:       perl-libwww-perl
Requires:       rdesktop
Requires:       xdg-utils

# let people find us
Provides:       remotebox

%description
VirtualBox is traditionally considered to be a virtualization solution aimed 
at the desktop as opposed to other solutions such as KVM, Xen and VMWare ESX 
which are considered more server oriented solutions. While it is certainly 
possible to install VirtualBox on a server, it offers few remote management 
features beyond using the vboxmanage command line. RemoteBox aims to fill 
this gap by providing a graphical VirtualBox client which is able to 
communicate with and manage a VirtualBox server installation. 

RemoteBox achieves this by using the vboxwebsrv feature of VirtualBox that 
allows its API to be accessed using a protocol called SOAP, even across a 
network. RemoteBox is very similar in look and feel to the native VirtualBox 
interface and allows you to perform most of the same tasks, including 
accessing the display of guests – completely remotely.


%prep
%autosetup -p0
# We need to tell RemoteBox where to find it's files
sed -i 's|$Bin/docs|%{_pkgdocdir}|g' remotebox
sed -i 's|$Bin/|%{_prefix}/|g' remotebox share/remotebox/*.pl

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/remotebox
cp -ar share/remotebox/* %{buildroot}%{_datadir}/remotebox/
install -pm755 remotebox %{buildroot}%{_bindir}

# Appdata file
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm644 packagers-readme/remotebox.appdata.xml %{buildroot}%{_datadir}/appdata

# Desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -pm644 packagers-readme/remotebox.desktop %{buildroot}%{_datadir}/applications

# Icon for .desktop
install -pm644 share/remotebox/icons/remotebox.png %{buildroot}%{_datadir}/pixmaps

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/remotebox.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/remotebox.desktop


%files
%doc docs/*
%{_bindir}/remotebox
%{_datadir}/appdata/remotebox.appdata.xml
%{_datadir}/applications/remotebox.desktop
%{_datadir}/pixmaps/remotebox.png
%{_datadir}/remotebox/


%changelog
* Tue Jan 14 2025 Pete Walter <pwalter@fedoraproject.org> - 3.4-1
- Update to 3.4 (rhbz#2326721)

* Thu Oct 03 2024 Pete Walter <pwalter@fedoraproject.org> - 3.3-1
- Update to 3.3

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Pete Walter <pwalter@fedoraproject.org> - 3.2-1
- Update to 3.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Pete Walter <pwalter@fedoraproject.org> - 3.1-1
- Update to 3.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-13
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-10
- Perl 5.34 rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-7
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-6
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Pete Walter <pwalter@fedoraproject.org> - 2.6-4
- Use validate-relax for appdata validation

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-2
- Perl 5.30 rebuild

* Sun Mar 24 2019 Pete Walter <pwalter@fedoraproject.org> - 2.6-1
- Update to 2.6

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.4-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Pete Walter <pwalter@fedoraproject.org> - 2.4-1
- Update to 2.4

* Mon Aug 14 2017 Pete Walter <pwalter@fedoraproject.org> - 2.3-1
- Update to 2.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Pete Walter <pwalter@fedoraproject.org> - 2.2-1
- Update to 2.2

* Fri Jul 08 2016 Pete Walter <pwalter@fedoraproject.org> - 2.1-1
- Update to 2.1
- Use upstream desktop file

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-3
- Perl 5.24 rebuild

* Fri Apr 01 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-2
- fix missing translation tag

* Tue Mar 01 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-1
- new version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-4
- Replace obsolete appdata-validate by appstream-util (bz#1277084)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-2
- Perl 5.22 rebuild

* Wed Jan 21 2015 Christopher Meng <rpm@cicku.me> - 1.9-1
- Update to 1.9

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.1-3
- Perl 5.20 rebuild

* Mon Jun 16 2014 Christopher Meng <rpm@cicku.me> - 1.8.1-2
- Update to 1.8.1
- Provide an appropriate appdata file.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Christopher Meng <rpm@cicku.me> - 1.8-1
- Update to 1.8

* Fri Feb 07 2014 Christopher Meng <rpm@cicku.me> - 1.7-1
- Update to 1.7

* Tue Oct 29 2013 Christopher Meng <rpm@cicku.me> - 1.6-2
- Correct the license.

* Fri Oct 25 2013 Christopher Meng <rpm@cicku.me> - 1.6-1
- Update to 1.6

* Thu Jun 06 2013 Christopher Meng <rpm@cicku.me> - 1.5-2
- SPEC cleanup.
- Fix errors of desktop file.

* Thu Apr 18 2013 Christopher Meng <rpm@cicku.me> - 1.5-1
- Initial Package.
