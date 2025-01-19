%define _legacy_common_support 1

%global forgeurl https://github.com/mricon/pam_url
%global commit 58e33bfaed3064ddc93f352b8272d42c17a20313
%forgemeta

Summary:        PAM module to authenticate with HTTP servers
Name:           pam_url
Version:        0.3.3
Release:        25%{?dist}
Epoch:          1
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{forgeurl}
Source:         %{forgesource}

Patch0:         pam_url-0.3.3-curl-timeout.patch
Patch1:         pam_url-0.3.3-nolibcheck.patch

Requires:       pam

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libcurl)

%description
The pam_url module enables you to authenticate users against a Web application,
such as totpcgi.

%prep
%forgesetup
%patch -P 0 -p 1
%patch -P 1 -p 1

%build
CFLAGS="%{optflags} -std=c99" make %{?_smp_mflags} pamlib=%{_lib}/security all

%install
make DESTDIR=%{buildroot} pamlib=%{_lib}/security install

%files
%doc AUTHOR COPYING INSTALL README examples
%config(noreplace) %{_sysconfdir}/pam_url.conf
/%{_lib}/security/pam_url.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.3.3-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 12 2023 Ralf Ertzinger <ralf@skytale.net> - 1:0.3.3-20
- Add patches to support connect and request timeouts

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Mattia Verga <mattia.verga@protonmail.com> - 1:0.3.3-14
- Update to latest available snapshot
- Fix libcurl headers detection
- Enable _legacy_common_support to try to fix build failure

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Konstantin Ryabitsev <icon@fedoraproject.org> - 1:0.3.3-1
- Upstream 0.3.3 with minor new features.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Dan Horák <dan[at]danny.cz> - 0.3.2-2
- fix build on all 64-bit arches

* Tue Dec 04 2012 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.3.2-1
- Upstream 0.3.2 with fixes for correct pam stacking.

* Wed Nov 28 2012 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.3.1-1
- Upstream 0.3.1 with fixes for memory corruption on 32-bit platforms.

* Wed Nov 28 2012 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.3-1
- Upstream 0.3 with support for CA_CERT, plus minor bugfixes.

* Mon Nov 19 2012 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.2-1
- Prepare for 0.2 release
- Set the epoch to 1 to solve branching issues with other releases
- Add doc files

* Tue May 08 2012 Andrew Wilcox <corgi@fedorapeople.org> 0.1-1
- Bring spec up to date with current guidelines (no clean/Buildroot)
- Modified CFLAGS
- Prettified description
- Set config file path

* Sun Mar 14 2010 Sascha Thomas Spreitzer <sspreitzer@fedoraproject.org>
- Added dependency to libconfig

* Tue Jun 09 2009 Sascha Thomas Spreitzer <sspreitzer@fedoraproject.org>
- Minor changes to description and summary. 
- Changed build step to common rpm optflags.

* Sun May 03 2009 Sascha Thomas Spreitzer <sspreitzer@fedoraproject.org>
- First shot of rpm spec.

