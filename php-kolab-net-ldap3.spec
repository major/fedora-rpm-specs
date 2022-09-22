# spec file for php-kolab-net-ldap3
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global git_commit    ec4f0d6918aa
%global git_short     %(c=%{git_commit}; echo ${c:0:7})

Name:           php-kolab-net-ldap3
Version:        1.1.4
Release:        3%{?dist}
Summary:        Advanced functionality for accessing LDAP directories

License:        GPLv3+
URL:            http://git.kolab.org/pear/Net_LDAP3/
Source0:        %{name}-%{version}-%{git_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch

# From composer.json
#               "php": ">=5.3.3",
#               "pear-pear/Net_LDAP2": ">=2.0.12"
Requires:       php(language) >= 5.3.3
Requires:       php-pear-Net-LDAP2 >= 2.0.12
# From phpcompatinfo report for version 1.1.0
Requires:       php-json
Requires:       php-ldap
Requires:       php-pcre
Requires:       php-spl

Provides:       php-composer(kolab/Net_LDAP3) = %{version}
Provides:       php-composer(kolab/net_ldap3) = %{version}


%description
A successor of the PEAR:Net_LDAP2 module providing advanced functionality
for accessing LDAP directories.


%prep
%setup -q -n %{name}-%{git_commit}


%build
# Nothing to build


%install
mkdir -p       %{buildroot}%{_datadir}/php
cp -pr lib/Net %{buildroot}%{_datadir}/php/Net


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%{_datadir}/php/Net


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Thu Aug 29 2019 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Remi Collet <remi@fedoraproject.org> - 1.0.7-2
- provide php-composer(kolab/net_ldap3)

* Mon Sep 17 2018 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- update to 1.0.7
- sources from git snapshot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3

* Tue Feb 24 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-2
- add upstream patch for License clarification

* Sun Feb 22 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- initial package, version 1.0.2