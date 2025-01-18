%global version_no_dot 27

Name:           c2esp
Version:        2.7
Release:        34%{?dist}
Summary:        CUPS driver for Kodak AiO printers

License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/cupsdriverkodak/
Source0:        http://downloads.sourceforge.net/cupsdriverkodak/c2esp-%{version_no_dot}.tar.gz

Patch01: c2esp-ftbfs-gcc7.patch
Patch02: c2esp-gcc10.patch
Patch03: c2esp-c99.patch
Patch04: c2esp-use-libcupsfilters.patch


# for autoreconf
BuildRequires: autoconf
BuildRequires: automake
# _cups_serverbin macro
BuildRequires: cups-devel
# Needs gcc for compilation
BuildRequires: gcc
# for autosetup
BuildRequires: git-core
# JBIG1 lossless image compression
BuildRequires: jbigkit-devel
# cupsfilters/image.h
BuildRequires: libcupsfilters-devel
# for ppdCMYKLoad()
BuildRequires: libppd-devel
# uses make
BuildRequires: make
# postscriptdriver tags
BuildRequires: python3-cups

# directory structure
Requires: cups-filesystem

%description
CUPS filters and drivers for Kodak ESP and Hero all in one printers.

%prep
%autosetup -n c2esp-%{version_no_dot} -S git


%build
# c2esp-use-libcupsfilters.patch changes configure.ac, regenerate configure script
autoreconf -vfi

%configure
make %{_smp_mflags} -C src/

%install
# do not install doc/ or scripts/
make -C src/ install DESTDIR=%{buildroot}

%files
%license doc/COPYING
%doc doc/README
%{_cups_serverbin}/filter/c2esp
%{_cups_serverbin}/filter/c2espC
%{_cups_serverbin}/filter/command2esp
%{_datadir}/cups/drv/c2esp

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Zdenek Dohnal <zdohnal@redhat.com> - 2.7-30
- SPDX migration

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 15 2023 Zdenek Dohnal <zdohnal@redhat.com> - 2.7-28
- move to libcupsfilters-devel and libppd-devel

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 Florian Weimer <fweimer@redhat.com> - 2.7-26
- Port to C99 (#2152430)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 2.7-21
- make is no more in buildroot by default

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Zdenek Dohnal <zdohnal@redhat.com> - 2.7-19
- FTBFS with GCC 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 2.7-14
- gcc is no longer in buildroot by default

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Zdenek Dohnal <zdohnal@redhat.com> - 2.7-10
- 1423287 - c2esp: FTBFS in rawhide 

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Jiri Popelka <jpopelka@redhat.com> - 2.7-7
- BuildRequires: python3-cups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Jiri Popelka <jpopelka@redhat.com> - 2.7-4
- Rebuilt against jbigkit-2.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Jiri Popelka <jpopelka@redhat.com> - 2.7-2
- upstream updated tarball

* Sun Dec 29 2013 Jiri Popelka <jpopelka@redhat.com> - 2.7-1
- 2.7

* Thu Dec 19 2013 Jiri Popelka <jpopelka@redhat.com> - 2.7-0.1.rc1
- 2.7~rc1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Jiri Popelka <jpopelka@redhat.com> - 2.6-1
- initial build
