%define     UpstreamName Validator

Name:       mediawiki-validator
Version:    0.5.1
Release:    17%{?dist}
Summary:    MediaWiki extension Validator
License:    GPLv3+
URL:        http://www.mediawiki.org/wiki/Extension:Validator
#  git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Validator.git
#  git archive -9 --prefix Validator/ --format tgz --output mediawiki-validator-0.5.1.tar.gz 0.5.1
# Source0:    https://github.com/JeroenDeDauw/Validator/archive/0.5.tar.gz
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch
Requires:   mediawiki >= 1.17.0
Requires:   php >= 5.2.3


%description
Validator is an extension that makes parameter validation functionality
available to other MediaWiki extensions. This enables other extensions to
validate parameters, set them to their defaults, and generate error messages,
while only defining the parameters and their criteria.


%prep
%setup -q -n %{UpstreamName}


%build


%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}%{_datadir}/mediawiki/extensions/%{UpstreamName}

cat <<EOF>README.fedora
To complete installation of %{name}: add the following two lines to
LocalSettings.php:

  # Validator
  require_once( "$IP/extensions/%{UpstreamName}/%{UpstreamName}.php" );

for each MediaWiki instance you wish to install %{name} on

Additional instructions may be detailed in the online installation guide
available at http://www.mediawiki.org/wiki/Extension:Validator#Installation
EOF
%{__cp} -pa * %{buildroot}%{_datadir}/mediawiki/extensions/%{UpstreamName}/



%files
%{_datadir}/mediawiki/extensions/%{UpstreamName}
%doc COPYING INSTALL README README.fedora releasenotes/RELEASE-NOTES RELEASE-NOTES*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 06 2013 James Laska <jlaska@redhat.com> - 0.5.1-3
- Update to Validator-0.5.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 23 2012 James Laska <jlaska@redhat.com> 0.4.13-1
- Initial packaging of 0.4.13
