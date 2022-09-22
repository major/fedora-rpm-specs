%global commit0 8dc419c5644fc7305f757ec571406f5b2e0a96af
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name: pki-usgov-dod-cacerts
Version: 0.0.6
Release: 18%{?dist}
Summary: A collection of U.S. Government CA Certs that the DOD uses
BuildArch: noarch
License: Public Domain
# these certs are public domain for two reasons
#  1) 17 USC 105 -- US Government can't have copyright in things they create
#  2) they are highly constrained "facts"

URL: https://github.com/pollei/pki-usgov-dod-cacerts
Source0:  https://github.com/pollei/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires: perl-interpreter perl(MIME::Base64) perl(Digest::CRC) openssl
%description
A collection of U.S. Government CA Certs that the DOD uses.
Has Department of Defense, and Federal Common Policy certs.
Useful for Army, Navy, Air Force, and Marines.
%prep
%setup -qn %{name}-%{commit0}

%build
./extract_x509.sh
cat pki-usgov-dod/cacerts/*.txt > cacert-list.txt

%install
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/pki/pki-usgov-dod-cacerts/cacerts/
mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/pki-usgov-dod-cacerts/
cp -a pki-usgov-dod/cacerts/*.{pem,crt} ${RPM_BUILD_ROOT}/%{_sysconfdir}/pki/pki-usgov-dod-cacerts/cacerts/
cp -a cacert-list.txt ${RPM_BUILD_ROOT}/%{_datadir}/pki-usgov-dod-cacerts/

%files
%dir %{_sysconfdir}/pki/pki-usgov-dod-cacerts/
%config %{_sysconfdir}/pki/pki-usgov-dod-cacerts/cacerts/
%{_datadir}/pki-usgov-dod-cacerts/
%doc README

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.6-9
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.6-4
- use %%{_sysconfdir} instead of /etc/
- use `cp -a` to preserve build timestamps
- create cacert-list.txt at build time not install time
- properly own /etc/pki/pki-usgov-dod-cacerts/
* Tue Jan 12 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.6-3
- changed /etc/pki/usgov-dod/cacerts to /etc/pki/pki-usgov-dod-cacerts/cacerts
-       see https://bugzilla.redhat.com/show_bug.cgi?id=1274948#c5
* Mon Jan 11 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.6-2
- updated description with periods and a little better grammar
* Mon Jan 11 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.6-1
- lowered perl version to 5.10 to hopefully work in epel6
- added perl(MIME::Base64) to buildrequires to work in rawhide
* Mon Jan 11 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.5-1
- spec file white space removal
- changed /etc/pki/usgov_dod to /etc/pki/usgov-dod
- got rid of noreplace
- installs crt files in der format as well as pem
* Fri Oct 23 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.4-2
- added openssl to Buildrequires
* Fri Oct 23 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.4-1
- transitioned over to using github
* Thu Oct 22 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.3-1
- Changed name from usgov_pki_ca_certs to pki-usgov-dod-cacerts IAW Packaging:NamingGuidelines 
- moved human readable cert info into one big text file in /usr/share/pki-usgov-dod
* Wed Oct 21 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.2-1
- Noarch
- following https://fedoraproject.org/wiki/PackagingDrafts/Certificates
-   moved certs from /usr/share/foo to /etc/pki/usgov_dod/cacerts
