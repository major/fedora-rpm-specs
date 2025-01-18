%global centos_git_common_url https://git.centos.org/centos-git-common
%global centos_git_common_commit 28b610e9fb79594c49bc64c7c331d0aaab382e7e

Name:           centos-packager
Version:        0.7.0
Release:        16%{?dist}
Summary:        Tools and files necessary for building CentOS packages
Group:          Applications/Productivity

License:        GPL-2.0-or-later
URL:            https://git.centos.org/centos/centos-packager
Source0:        cbs-koji.conf
Source1:        COPYING
Source2:        centos-cert
Source3:        %{centos_git_common_url}/raw/%{centos_git_common_commit}/f/lookaside_upload
Source4:        %{centos_git_common_url}/raw/%{centos_git_common_commit}/f/lookaside_upload_sig
Source5:        %{centos_git_common_url}/raw/%{centos_git_common_commit}/f/get_sources.sh

Requires:       koji
Requires:       rpm-build rpmdevtools rpmlint
Requires:       mock curl openssh-clients
Requires:       redhat-rpm-config
Requires:       bc
Requires:       krb5-workstation
Requires:       openssl
Requires:       fasjson-client python3-fasjson-client

BuildArch:      noarch

%description
Tools to help set up a CentOS packaging environment and interact with the
Community Build System (CBS).


%prep
cp %{SOURCE1} .

%build
# Nothing here

%install
mkdir -p %{buildroot}%{_sysconfdir}/koji.conf.d
install -p -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/koji.conf.d/cbs-koji.conf

mkdir -p %{buildroot}/%{_bindir}
ln -s koji %{buildroot}%{_bindir}/cbs
install -p -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/centos-cert
install -p -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/centos-lookaside-upload
install -p -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/centos-lookaside-upload-sig
install -p -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/centos-get-sources

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/koji.conf.d/cbs-koji.conf
%{_bindir}/cbs
%{_bindir}/centos-cert
%{_bindir}/centos-lookaside-upload
%{_bindir}/centos-lookaside-upload-sig
%{_bindir}/centos-get-sources

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Davide Cavalca <dcavalca@centosproject.org> - 0.7.0-14
- Import lookaside_upload, lookaside_upload_sig and get_sources.sh from
  centos-git-common
- Convert license tag to SPDX

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May  4 2021 Davide Cavalca <dcavalca@fb.com> - 0.7.0-6
- Use the correct macro for the license file
- Preserve timestamps on install

* Fri Apr 23 2021 Davide Cavalca <dcavalca@fb.com> - 0.7.0-5
- Clean up macros usage
- Fix changelog inconsistencies and formatting
- Update description

* Wed Apr 21 2021 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.7.0-4
- Added openssl as Requires (missing on some fedora install)

* Sat Mar 27 2021 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.7.0-3
- Bumped centos-cert for additional verification with CA

* Mon Feb  1 2021 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.7.0-2
- Fixed the cbs call for correct profile

* Thu Nov 19 2020 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.7.0-1
- added Requires: on fasjson-client (talking to IPA and not FAS anymore)
- replaced centos-cert script with just a wrapper around fasjson-client for TLS cert

* Tue Aug 11 2020 Brian Stinson <bstinson@centosproject.org> - 0.6.0-1
- Cut a new release

* Wed Nov 27 2019 Jan Staněk <jstanek@redhat.com> - 0.5.5-2
- Use Python3 on F28+ and EL 8+

* Mon Nov 28 2016 Brian Stinson <brian@bstinson.com> - 0.5.5-1
- Update more references to ACO
- Make sure Exception messages don't print credentials to the screen

* Thu Oct 20 2016 Brian Stinson <brian@bstinson.com> - 0.5.4-1
- Update to point at the trust ca-bundle.crt #12110
- Update the help text to mention ACO

* Tue Oct 11 2016 Brian Stinson <brian@bstinson.com> - 0.5.3-1
- Rebuild to fix #12011

* Tue Nov 10 2015 Brian Stinson <brian@bstinson.com> - 0.5.2-1
- Fix a typo pointing to the ca-bundle in the cbs koji profile

* Thu Oct 29 2015 Brian Stinson <brian@bstinson.com> - 0.5.1-1
- Refactor to be more friendly if the http request fails
- Move centos_cert to centos-cert

* Wed Oct 28 2015 Brian Stinson <brian@bstinson.com> - 0.5.0-1
- The centos-cert utility now downloads the correct certificate, and sets up the
  CA certificate properly
- Updated the koji config to point to the downloaded certificates

* Sun Jul 26 2015 Brian Stinson <brian@bstinson.com> - 0.2.0-1
- Added the centos_cert utility
- Remove the dep on centpkg
- Add a dep for python-centos

* Sun Dec 14 2014 Brian Stinson <bstinson@ksu.edu> - 0.1.0-1
- initial build
