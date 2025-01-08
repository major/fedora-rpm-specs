%global _hardened_build 1
#global snapshot 0
%global OWNER Drive-Trust-Alliance
%global PROJECT sedutil
%global commit 5bbe4ff75b9416926d157a755d9760f7ff4e3904
%global commitdate 20241211
%global gittag %{version}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		sedutil
Version:	1.49.6
Release:	2%{?dist}
Summary:	Tools to manage the activation and use of self encrypting drives

# Everything is GPLv3+ except:
# - Common/pbkdf2/* which is CC0, a bundled copy of Cifra: https://github.com/ctz/cifra
License:	GPL-3.0-or-later AND CC0-1.0 AND BSD-4-Clause-UC AND Unlicense
URL:		https://github.com/%{OWNER}/%{PROJECT}/wiki
Source0:	https://github.com/%{OWNER}/%{PROJECT}/archive/%{gittag}/%{name}-%{gittag}.tar.gz

# sedutil does not work on big-endian architectures
ExcludeArch:	ppc ppc64 ppc64le s390 s390x

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	ncurses-devel
BuildRequires:	autoconf automake
BuildRequires:	systemd-devel
BuildRequires:	libnvme-devel

# This package uses a bundled copy of Cifra:
# https://github.com/ctz/cifra/commit/319fdb764cd12e12b8296358cfcd640346c4d0dd
Provides:	bundled(cifra)

# Replaces msed, but doesn't provide a compatible CLI command
Obsoletes:	msed <= 0.23-0.20

%description
The Drive Trust Alliance software (sedutil) is an Open Source (GPLv3)
effort to make Self Encrypting Drive technology freely available to
everyone. It is a combination of the two known available Open Source
code bases today: msed and OpalTool.

sedutil is a Self-Encrypting Drive (SED) management program and
Pre-Boot Authorization (PBA) image that will allow the activation and
use of self encrypting drives that comply with the Trusted Computing
Group Opal 2.0 SSC.

This package provides the sedutil-cli and linuxpba binaries, but not
the PBA image itself.

%prep
%autosetup
# Adjust the GitVersion.sh script to just use the git tag from the
# checkout so we don't need a full git tree or the git tool itself.
sed -i -e's/tarball/%{gittag}/' Customizations.OpenSource/linux/CLI/GitVersion.sh
sed -i -e's/tarball/%{gittag}/' linux/GitVersionPBA.sh


%build
autoreconf -iv
%configure
%make_build


%install
%make_install
mkdir -p %{buildroot}%{_libexecdir}/linuxpba
ln -sr %{buildroot}%{_sbindir}/linuxpba %{buildroot}%{_libexecdir}/linuxpba


%files
%doc README.md Common/Copyright.txt Common/ReadMe.txt linux/PSIDRevert_LINUX.txt
%license Common/LICENSE.txt
%{_sbindir}/sedutil-cli
%{_mandir}/man8/sedutil-cli.8*
%{_sbindir}/linuxpba
%{_libexecdir}/linuxpba


%changelog
* Mon Jan 06 2025 Charles R. Anderson <cra@alum.wpi.edu> - 1.49.6-2
- ExcludeArch: ppc64le

* Sun Jan 05 2025 Charles R. Anderson <cra@alum.wpi.edu> - 1.49.6-1
- Update to 1.49.6

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.20.0-7
- Convert to SPDX license string and add missing licenses
- Add macros for github owner/project/commit

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Charles R. Anderson <cra@alum.wpi.edu> - 1.20.0-4
- Upstream PR#428: fix build with GCC 13

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 06 2022 Filipe Brandenburger <filbranden@fedoraproject.org> - 1.20.0-2
- Make linuxpba symlink in libexec relative

* Fri Aug 12 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0
- Backport upstream PR for securemode and verifySIGPassword
- Use standard macros for building and installing

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.15.1-6.1
- Initial EPEL8 build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 Charles R. Anderson <cra@wpi.edu> - 1.15.1-1
- Update to 1.15.1
- Upstream swapped bundled gnulib GPLv2+ for bundled Cifra CC0

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 1.12-8
- add BR gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-4
- Update patch for epel7 build with older kernel version numbering

* Tue May  9 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-3
- Remove commented out macros
- Clarify multiple licensing scenario
- Provides: bundled(gnulib)
- Move sedutil-cli to /usr/sbin and linuxbpa to /usr/libexec
- Provide a manual page for sedutil-cli

* Wed May  3 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-2
- Obsolete msed package
- Remove stray execute permissions from source code

* Wed May  3 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-1
- Use nvme_ioctl.h for newer kernel versions (upstream pull request #56)

* Tue Jan  3 2017 Charles R. Anderson <cra@wpi.edu>
- update to 1.12
- sedutil-nvme_ioctl_h.patch for renamed linux/nvme.h header

* Wed Nov 11 2015 Charles R. Anderson <cra@wpi.edu> - 1.10-0.1.beta.git350b22c
- switch to DriveTrustAlliance/sedutil upstream where all further development
  of msed happens now.

* Fri Aug 07 2015 Rafael Fonseca <rdossant@redhat.com> - 0.23-0.7.beta.gite38a16d
- disable build on big endian architectures (rhbz#1251520)

* Mon Jul 27 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.6.beta.gite38a16d
- add comments about upstream pull requests for patches

* Sun Jul 26 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.5.beta.gite38a16d
- use Github Source0 URL and standard macros for git hash
- patch GitVersion.sh to use a static git tag so we do not need a
  full git tree or the git tool for building.
- preserve timestamps of installed files

* Tue Jul 21 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.4.beta.gite38a16d
- mark LICENSE.txt as a license text
- enable hardened build

* Tue Jul 21 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.3.beta.gite38a16d
- add more documentation

* Tue Jul 21 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.2.beta.gite38a16d
- add BR git to properly define GIT_VERSION 

* Mon Jul 20 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.1.beta.gite38a16d
- initial package
