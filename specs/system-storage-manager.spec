%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           system-storage-manager
Version:        1.3
Release:        22%{?dist}
Summary:        A single tool to manage your storage

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://system-storage-manager.github.io/
Source0:        https://github.com/system-storage-manager/ssm/archive/%{name}-%{version}.tar.gz

Patch1:         python3-sphinx.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pwquality
Requires:       util-linux
Requires:       which
Requires:       xfsprogs
Requires:       e2fsprogs
Requires:       python3-pwquality


%description
System Storage Manager provides an easy to use command line interface to manage
your storage using various technologies like lvm, btrfs, encrypted volumes and
more.

In more sophisticated enterprise storage environments, management with Device
Mapper (dm), Logical Volume Manager (LVM), or Multiple Devices (md) is becoming
increasingly more difficult.  With file systems added to the mix, the number of
tools needed to configure and manage storage has grown so large that it is
simply not user friendly.  With so many options for a system administrator to
consider, the opportunity for errors and problems is large.

The btrfs administration tools have shown us that storage management can be
simplified, and we are working to bring that ease of use to Linux file systems
in general.

You should install the ssm if you need to manage your storage with various
technologies via a single unified interface.


%prep
%setup -q -n ssm-%{name}-%{version}

# fedora-specific issue with the name of python3-sphinx binaries
%patch -P1 -p1

# there is no assert_ method in Python 3.12+
sed -i 's/assert_/assertTrue/' tests/unittests/test_ssm.py

%build
make docs


%install
rm -rf ${RPM_BUILD_ROOT}
%{__python3} setup.py install --root=${RPM_BUILD_ROOT}
if [ "%{_pkgdocdir}" != "%{_docdir}/%{name}-%{version}" ]; then
    mv ${RPM_BUILD_ROOT}/{%{_docdir}/%{name}-%{version},%{_pkgdocdir}}
fi

%check
%{__python3} test.py || :


%files
%{_bindir}/ssm
%{_pkgdocdir}/
%{_mandir}/man8/ssm.8*
%{python3_sitelib}/ssmlib/
%{python3_sitelib}/*.egg-info


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3-19
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.3-16
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3-13
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Jan Tulak <jtulak@redhat.com> - 1.3-1
- New upstream stable version 1.3

* Mon Aug 13 2018 Jan Tulak <jtulak@redhat.com> - 1.2-1
- New upstream stable version 1.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-1
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Jan Tulak <jtulak@redhat.com> - 1.0-0
- New upstream stable version 1.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-2
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Jan Tulak <jtulak@redhat.com> - 0.5-0
- New upstream stable version 0.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5


* Mon Jul 27 2015 Lukas Czerner <lczerner@redhat.com> 0.4-7
- Big upstream update
- Python3 support (#1239016)
- Error out if file system is not supported (#1196428)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Lukas Czerner <lczerner@redhat.com> 0.4-4
- Update to a new upstream release v0.4
- Remove btrfs resize support
- Unmount all btrfs subvolumes when removing a filesystem
- Fix size argument parsing for create and snapshot command
- Fix list output for some cases
- Add support to create encrypted volumes with crypt backend
- Add dry-run option
- Fix removing volumes with crypt backend
- Add raid1 and raid10 support for lvm backend
- Allow to check btrfs volumes
- Fix error handling when trying to resize btrfs subvolume
- Fix ssm mount command so it detects directory properly
- Suppress backtrace when a command fails
- Fix ssm to recognize units in new btrfs output properly
- Use correct sysfs file to get size for a partition
- Fix ssm to be able add a device with signature to btrfs file system
- Resognize btrfs devices from new btrfs output properly


* Mon Dec 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.2-4
- Install docs to %%{_pkgdocdir} where available (#994122).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jun  1 2012 Lukas Czerner <lczerner@redhat.com> 0.2-1
- Initial version of the package
