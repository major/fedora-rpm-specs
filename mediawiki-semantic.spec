%define     UpstreamName SemanticMediaWiki

Name:       mediawiki-semantic
Version:    1.8.0.4
Release:    18%{?dist}
Summary:    An extension of MediaWiki that improves content organization
License:    GPLv2
URL:        http://semantic-mediawiki.org
# The following URRL works, but requires the '%' with the URL escape code '%25'
# Source0:    http://downloads.sourceforge.net/project/semediawiki/semediawiki/Semantic%2520MediaWiki%2520%{version}/Semantic%2520MediaWiki%2520%{version}.zip
#  git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/SemanticMediaWiki.git
#  git archive -9 --prefix SemanticMediaWiki/ --format zip --output mediawiki-semantic-%{version}.zip %{version}
Source0:    %{name}-%{version}.zip
# SemanticMediaWiki.zip also includes the Validator extension.  Validator is
# packaged separately as mediawiki-validator.  The following script removes
# Validator from the zip file.
# ./remove-validator.sh mediawiki-semantic-%{version}.tar.gz
Source1: remove-validator.sh
BuildArch:  noarch
Requires:   mediawiki >= 1.17.0
Requires:   mediawiki-validator >= 0.5
Requires:   php >= 5.2.3


%description
Semantic MediaWiki is also a full-fledged framework, in conjunction with many
spinoff extensions, that can turn a wiki into a powerful and flexible
“collaborative database”. All data created within SMW can easily be published
via the Semantic Web, allowing other systems to use this data seamlessly.


%prep
%setup -q -n %{UpstreamName}


%build


%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}/%{_datadir}/mediawiki/extensions/%{UpstreamName}

cat <<EOF> README.fedora
To complete installation of %{name}: add the following two lines to
LocalSettings.php:

  include_once("\$IP/extensions/%{UpstreamName}/%{UpstreamName}.php");
  enableSemantics('example.org');

for each MediaWiki instance you wish to install %{name} on.  Note that
example.org should be replaced by your server's name (or IP address).

Additional database changes are detailed in the online installation
instructions available at http://semantic-mediawiki.org/wiki/Help:Installation.
EOF

%{__cp} -a * %{buildroot}/%{_datadir}/mediawiki/extensions/%{UpstreamName}/


%files
%{_datadir}/mediawiki/extensions/%{UpstreamName}
%doc COPYING INSTALL README README.fedora RELEASE-NOTES-1.8 RELEASE-NOTES-1.8.0.4


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 James Laska <jlaska@redhat.com> - 1.8.0.4-2
- Updated requires for mediawiki and mediawiki-validator

* Mon Mar 04 2013 James Laska <jlaska@redhat.com> - 1.8.0.4-1
- Update to 1.8.0.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 James Laska <jlaska@redhat.com> 1.7.0.2-2
- Correct incomplete build section
- Replace RPM_BUILD_ROOT with buildroot macro

* Mon Jan 23 2012 James Laska <jlaska@redhat.com> 1.7.0.2-1
- Update to 1.7.0.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 James Laska <jlaska@redhat.com> 1.5.6-1
- Update to 1.5.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 11 2009 James Laska <jlaska@redhat.com> 1.4.2-1
- Initial packaging of 1.4.2
