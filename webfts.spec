Name:           webfts
Version:        2.2.11
Release:        14%{?dist}
Summary:        Web Interface for FTS 
License:        ASL 2.0
URL:            https://gitlab.cern.ch/fts/webfts
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone https://gitlab.cern.ch/fts/webfts.git webfts-2.2.5
#  tar --exclude-vcs -zcvf webfts-2.2.5.tar.gz webfts-2.2.5
Source:         %{name}-%{version}.tar.gz
BuildArchitectures: noarch

Requires:	httpd
Requires:	php


%description
The package provides the WEB Interface for the FTS3 service

%prep
%setup -c -n %{name}

%install
rm -rf %{buildroot}
mkdir -p -m0755 %{buildroot}/var
mkdir -p -m0755 %{buildroot}/var/www
mkdir -p -m0755 %{buildroot}/var/www/%{name}

cp -rp %{name}-%{version}/* %{buildroot}/var/www/%{name}

mkdir -p -m0755 %{buildroot}/etc
mkdir -p -m0755 %{buildroot}/etc/httpd
mkdir -p -m0755 %{buildroot}/etc/httpd/conf.d

cp -rp %{name}-%{version}/conf/%{name}.conf %{buildroot}/etc/httpd/conf.d/

%post
service httpd restart

%files
%config(noreplace) /etc/httpd/conf.d/%{name}.conf
%config(noreplace) /var/www/%{name}/config.xml
%defattr(-,root,root,-)
/var/www/%{name}

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Andrea Manzi <amanzi@cern.ch> - 2.2.11-1
- change default port
* Fri Dec 16 2016 Andrea Manzi <amanzi@cern.ch> - 2.2.10-1
- removed beta version
* Fri Jul 29 2016 Andrea Manzi <amanzi@cern.ch> - 2.2.9-1
- fix selectAll Files
* Mon Jul 04 2016 Andrea Manzi <amanzi@cern.ch> - 2.2.8-1
- fix date filter and displayed date
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Fri Nov 27 2015 Andrea Manzi <amanzi@cern.ch> - 2.2.7-1
- fix text typos
* Tue Nov 24 2015 Andrea Manzi <amanzi@cern.ch> - 2.2.6-1
- fix endpoints content not ordered
- fix resubmission with dropbox
* Fri Nov 6 2015 Andrea Manzi <amanzi@cern.ch> - 2.2.5-1
- correct escaping url when list endpoints
- fix reload of SE endpoints
* Fri Jun 27 2015 Andrea Manzi <amanzi@cern.ch> - 2.2.4-1
- fix for FINISHEDDIRTY jobs not displayed
* Wed Jun 25 2015 Andrea Manzi <amanzi@cern.ch> - 2.2.3-1
- fix for file Attributes columns wrongly ordered
* Fri Feb 27 2015 Andrea Manzi <amanzi@cern.ch> - 2.2.2-1
- fix for XSS vulnerability
* Fri Feb 13 2015 Andrea Manzi <amanzi@cern.ch> - 2.2.1-1
- moved to sha512
- added dropbox revoke tokens button
* Thu Nov 27 2014 Andrea Manzi <amanzi@cern.ch> - 2.2.0-1
- data management support
* Thu Nov 13 2014 Andrea Manzi <amanzi@cern.ch> - 2.1.0-1
- cernbox support
- added voname to proxy
* Tue Aug 27 2014 Andrea Manzi <amanzi@cern.ch> - 2.0.0-1
- dropbox support
* Tue Jul 22 2014 Andrea Manzi <amanzi@cern.ch> - 1.4.0-1
- added support for LFC registration, overwrite and checksums
- added resubmission of failed files only
