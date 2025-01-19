#%%global commit cf51167b55246b7f90ad4970d9686637e8bb0beb
#%%global commit_date 20180820
#%%global shortcommit %%(c=%%{commit};echo ${c:0:7})

Name:           grive2
Version:        0.5.3
Release:        10%{?dist}
#Release:        22.%%{commit_date}git%%{shortcommit}%%{?dist}
Summary:        Google Drive client

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://yourcmc.ru/wiki/Grive2
Source0:        https://github.com/vitalif/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
#Source0:        https://github.com/vitalif/%%{name}/archive/%%{commit}.tar.gz#/%%{name}-%%{commit}.tar.gz
# libgcrypt-config --libs or so returns the output with trailing newline, which now makes
# cmake 3.24 error. Remove traling newline using EXECUTE_PROCESS
Patch:          grive2-0.5.1-cmake-remove-newline.patch
# Add missing c++ include header
Patch:          grive2-0.5.1-cxx-missing-include.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  yajl-devel
BuildRequires:  zlib-devel
BuildRequires:  systemd
Requires(preun): systemd
Requires:       inotify-tools

%description
The purpose of this project is to provide an independent open source
implementation of Google Drive client for GNU/Linux. It uses Google Drive
REST API to talk to Google Drive service.

%prep
%autosetup -p1

%build
%cmake3
%cmake_build

%install
%cmake_install

%preun
%systemd_user_preun grive-changes@.service
%systemd_user_preun grive-timer@.service
%systemd_user_preun grive-timer@.timer


%files
%license COPYING
%doc README.md
%{_bindir}/grive
%{_mandir}/man1/*
%{_userunitdir}/grive*
%{_libexecdir}/grive

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-5
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-3
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 11 2022 Zamir SUN <sztsian@gmail.com> - 0.5.3-1
- Update to 0.5.3 to apply "loopback" flow authentication
- Fixes: RHBZ#2139494

* Wed Sep  7 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-15
- Fix FTBFS
  - Fix cmake invocation error with libgcrypt-config output
  - Fix missing c++ header inclusion

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.5.1-13
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-11
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-8
- Rebuilt for Boost 1.75

* Tue Aug 11 2020 Zamir SUN <sztsian@gmail.com> - 0.5.1-7
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-4
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Zamir SUN <sztsian@gmail.com> - 0.5.1-2
- Add dist back to release

* Sat Nov 23 2019 Zamir SUN <sztsian@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-22.20180820gitcf51167
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.5.0-21.20180820git%{shortcommit}%{?dist}
- Remove obsolete requirement for %%post scriptlet

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-20.20180820gitcf51167
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-19.20180820gitcf51167
- Rebuilt for Boost 1.69

* Fri Nov 30 2018 Zamir SUN <sztsian@gmail.com> - 0.5.0-18.20180820gitcf51167
- Update to most recent git head to merge in bugfixes

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5.0-17.20171122git84c57c1
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-16.20171122git84c57c1
- Rebuild for new binutils

* Thu Jul 26 2018 Zamir SUN <sztsian@gmail.com> - 0.5.0-15.20171122git84c57c1
- Fix RHBZ 1608667

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14.20171122git84c57c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Zamir SUN <sztsian@gmail.com> - 0.5.0-13.20171122git84c57c1
- Update to 84c57c121e03b070f80e1d8fd66749eead7a4d9e to apply bunch of fixes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12.20160114gitae06ecc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-11.20160114gitae06ecc
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10.20160114gitae06ecc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9.20160114gitae06ecc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-8.20160114gitae06ecc
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-7.20160114gitae06ecc
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6.20160114gitae06ecc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 0.5.0-5.20160114gitae06ecc
- Rebuilt for Boost 1.63

* Fri May 13 2016 Christian Dersch <lupinix@mailbox.org> - 0.5.0-4.20160114gitae06ecc
- Rebuilt for gcc 6.1.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3.20160114gitae06ecc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Christian Dersch <lupinix@mailbox.org> - 0.5.0-2.20160114gitae06ecc
- Rebuilt for boost 1.60.x

* Fri Jan 15 2016 Christian Dersch <lupinix@mailbox.org> - 0.5.0-1.20160115gitae06ecc
- new version 0.5.0

* Sun Jan 03 2016 Christian Dersch <lupinix@mailbox.org> - 0.4.2-1.20160102gitd2a6105
- Upgrade to 0.4.2 final

* Tue Dec 29 2015 Christian Dersch <lupinix@mailbox.org> - 0.4.2-0.2.20151227git5fb3c18
- Updated to newer git snapshot to include bugfixes

* Fri Dec 11 2015 Christian Dersch <lupinix@mailbox.org> - 0.4.2-0.1.20151208gitcc13b8b
- initial spec
