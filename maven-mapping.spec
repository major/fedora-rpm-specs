%bcond_with bootstrap

Name:           maven-mapping
Version:        3.0.0
Release:        21%{?dist}
Summary:        Apache Maven Mapping
License:        ASL 2.0

URL:            https://maven.apache.org/shared/maven-mapping/
Source0:        https://repo.maven.apache.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
%endif

%description
Maven shared component that implements file name mapping.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q
%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.target" "1.7" pom.xml
%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.source" "1.7" pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-19
- Implement bootstrap mode

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.0-17
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.0-16
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 07 2021 Markku Korkeala <markku.korkeala@iki.fi> - 3.0.0-14
- Change maven compiler target and source to 1.7, update Source0 url

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fabio Valentini <decathorpe@gmail.com> - 3.0.0-11
- Consistently use HTTPS URLs for both URL and Sources.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan  5 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-2
- Update to current packaging guidelines

* Mon Nov 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-1
- Initial packaging

