Summary:    Daemon that can spin idle disks down
Name:       spindown
Version:    0.4.0
Release:    41%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
Url:        http://code.google.com/p/spindown
Source0:    http://spindown.googlecode.com/files/spindown-%{version}.tar.gz
Source1:    spindown.service
Source2:    01spindown

Patch0:     spindown-0.4.0-Makefile.patch
Patch1:     spindown-0.4.0-iniparser.patch
Patch2:     spindown-0.4.0-iniparser-3.0-1.patch
Patch3:     spindown-0.4.0-bz1037334.patch
Patch4:     spindown-0.4.0-gcc-14.x.patch

Requires(preun): systemd-units

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: iniparser-devel >= 4.2.2
BuildRequires: systemd-units

%description
Spindown is a daemon that can spin idle disks down and thus save energy and
improve disk lifetime. It periodically checks for read or written blocks. When
no blocks are read or written the disk is idle. When a disk stays idle long
enough, spindown uses custom command like sg_start or hdparm to spin it down.
It also works with USB disks and hot-swappable disks because it doesn't watch
the device name (hda, sdb, ...), but the device ID. This means that it doesn't
matter if the disk is swapped while the daemon is running.

%prep
%autosetup -p1
rm -rf src/ininiparser3.0b
cp -pf %{SOURCE1} spindown.service
cp -pf %{SOURCE2} 01spindown

%build
%make_build OPT="$RPM_OPT_FLAGS"

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/pm-utils/sleep.d
mkdir -p %{buildroot}%{_unitdir}
install -p -m 755 01spindown %{buildroot}%{_libdir}/pm-utils/sleep.d/01spindown
install -p -m 755 spindown.service %{buildroot}%{_unitdir}/spindown.service

%preun
%systemd_preun spindown.service

%files
%doc CHANGELOG README
%license COPYING
%{_unitdir}/spindown.service
%{_sbindir}/spindownd
%{_libdir}/pm-utils/sleep.d/01spindown
%config(noreplace) %{_sysconfdir}/spindown.conf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-40
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 David Cantrell <dcantrell@redhat.com> - 0.4.0-38
- Rebuild against iniparser-4.2.4

* Thu May 30 2024 David Cantrell <dcantrell@redhat.com> - 0.4.0-37
- Rebuild against latest iniparser
- Update spec file macro use
- Fix compile issues with latest gcc

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Martin Cermak <mcermak@redhat.com> - 0.4.0-29
- NVR Bump and rebuild for CI gating updates

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.0-17
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 02 2014 Martin Cermak <mcermak@redhat.com> 0.4.0-14
- Use new systemd-rpm macros in spindown spec file (resolves bz850324)

* Tue Dec 03 2013 Martin Cermak <mcermak@redhat.com> 0.4.0-13
- Build correctly with -Werror=format-security (resolves bz1037334)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for c++ ABI breakage

* Tue Feb 21 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-8
- Improved fix for bz787231 as discussed in bz769059#c7
- Fixed systemd unit installation

* Fri Feb 03 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-7
- Behave correctly after waking from suspend (resolves bz787231)

* Tue Jan 31 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-6
- Fixed against iniparser-3.0-1

* Thu Jan 26 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-5
- Replaced sysvinitscript with a systemd unit

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May  6 2011 Martin Cermak <mcermak@redhat.com> 0.4.0-3
- Initscript changed according to comment #5 in bz700571

* Wed May  4 2011 Martin Cermak <mcermak@redhat.com> 0.4.0-2
- Multiple changes described in the comment #3 in bz700571

* Thu Apr 28 2011 Martin Cermak <mcermak@redhat.com> 0.4.0-1
- Packaged for Fedora 


