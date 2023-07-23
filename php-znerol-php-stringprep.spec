# remirepo/fedora spec file for php-znerol-php-stringprep
#
# Copyright (c) 2014-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    fe3f274cb0a862e7e511a7f2033301a06cbfb4f1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      20150618
%global gh_owner     znerol
%global gh_project   Stringprep
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%global topdir       %{_datadir}/php/Znerol
%global basedir      %{topdir}/Component/Stringprep

Name:           php-znerol-php-stringprep
Version:        0
Release:        0.18.%{gh_date}git%{gh_short}%{?dist}
Summary:        Implementation of RFC 3454 Preparation of Internationalized Strings

License:        LGPLv3
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) > 5.3
BuildRequires:  php-iconv
BuildRequires:  php-intl
BuildRequires:  php-spl
BuildRequires:  php-phpunit-PHPUnit
%endif
BuildRequires:  php-theseer-autoload

# From documentation
Requires:       php(language) > 5.3
Requires:       php-iconv
Requires:       php-intl
# From phpcompatinfo
Requires:       php-spl

Provides:       php-composer(znerol/php-stringprep) = %{version}


%description
Implementation of RFC 3454 Preparation of Internationalized Strings.

See: http://tools.ietf.org/html/rfc3454


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate a simple autoloader
%{_bindir}/phpab \
   --exclude *Test.php \
   --output autoload.php \
   .


%install
mkdir -p %{buildroot}%{basedir}
cp -pr Profile RFC3454 *php \
         %{buildroot}%{basedir}


%check
%if %{with_tests}
%{_bindir}/phpunit --bootstrap %{buildroot}%{basedir}/autoload.php --verbose
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md doc
%{topdir}


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20150618gitfe3f274
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul  3 2016 Remi Collet <remi@fedoraproject.org> - 0-0.4.20150618gitfe3f274
- new snapshot
- drop patch merges upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20150519git804b0d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Remi Collet <remi@fedoraproject.org> - 0-0.2.20150519git804b0d5
- add patch for autoload issue
  https://github.com/znerol/Stringprep/pull/6

* Tue May 19 2015 Remi Collet <remi@fedoraproject.org> - 0-0.1.20150519git804b0d5
- new snapshot (License PR merged)

* Sun Nov  9 2014 Remi Collet <remi@fedoraproject.org> - 0-0.1.20141109gita23ef29
- initial package (git snapshot)