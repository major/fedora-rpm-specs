Name:           jaxb-api2
Version:        2.3.3
Release:        12%{?dist}
Summary:        Jakarta XML Binding API
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api:1.2.2)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaxb-api-%{version}

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Test module depends on the package itself
%pom_disable_module jaxb-api-test

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Mark dependency on jakarta.activation as optional
%pom_xpath_inject "pom:dependency[pom:groupId='jakarta.activation']" "<optional>true</optional>" jaxb-api

%mvn_compat_version jakarta*: 2 %{version} 2.3.2

# TODO delete
%mvn_file javax.xml.bind:jaxb-api JAXB-API jaxb-api

%build
%mvn_build

%install
%mvn_artifact javax.xml.bind:jaxb-api:%{version} jaxb-api/target/jakarta.xml.bind-api-%{version}.jar
cp jaxb-api/pom.xml jaxb-api2.pom
%mvn_artifact javax.xml.bind:jaxb-api:pom:%{version} jaxb-api2.pom

%mvn_install

rm %{buildroot}%{_javadir}/JAXB-API.jar
ln -s -f jaxb-api2/jakarta.xml.bind-api-2.jar %{buildroot}%{_javadir}/jaxb-api.jar
rm %{buildroot}%{_datadir}/maven-poms/JAXB-API.pom
ln -s -f jaxb-api2/jakarta.xml.bind-api-2.pom %{buildroot}%{_datadir}/maven-poms/jaxb-api.pom
sed -i /JAXB-API/d .mfiles
sed -i 's/JAXB-API/jaxb-api2\/jakarta.xml.bind-api-2/' %{buildroot}%{_datadir}/maven-metadata/*

%files -f .mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.3.3-10
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 23 2023 Marian Koncek <mkoncek@redhat.com> - 2.3.3-6
- Fix wrong symlink targets

* Fri Jan 20 2023 Marian Koncek <mkoncek@redhat.com> - 2.3.3-5
- Add major compat version
- Remove glassfish alias

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Marian Koncek <mkoncek@redhat.com> - 2.3.3-3
- Provide a jaxb-api.jar symlink

* Thu Dec 22 2022 Marian Koncek <mkoncek@redhat.com> - 2.3.3-2
- Use correct BuildRequires on jakarta.activation-api

* Wed Nov 30 2022 Marian Koncek <mkoncek@redhat.com> - 2.3.3-1
- Initial package renamed from jaxb-api
