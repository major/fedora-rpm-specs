Name:           jaxb-api2
Version:        2.3.3
Release:        3%{?dist}
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

# Add compatibility aliases for old artifact coordinates
%mvn_file :jakarta.xml.bind-api glassfish-jaxb-api/jakarta.xml.bind-api

%mvn_compat_version jakarta*: %{version} 2.3.2
%mvn_file javax.xml.bind:jaxb-api JAXB-API jaxb-api

%build
%mvn_build

%install
%mvn_artifact javax.xml.bind:jaxb-api:%{version} jaxb-api/target/jakarta.xml.bind-api-%{version}.jar
cp jaxb-api/pom.xml jaxb-api2.pom
%mvn_artifact javax.xml.bind:jaxb-api:pom:%{version} jaxb-api2.pom

%mvn_install

rm %{buildroot}%{_javadir}/JAXB-API.jar
ln -s -f glassfish-jaxb-api/jakarta.xml.bind-api-%{version}.jar %{buildroot}%{_javadir}/jaxb-api.jar
rm %{buildroot}%{_datadir}/maven-poms/JAXB-API.pom
ln -s -f glassfish-jaxb-api/jakarta.xml.bind-api-%{version}.pom %{buildroot}%{_datadir}/maven-poms/jaxb-api.pom
sed -i /JAXB-API/d .mfiles
sed -i 's/JAXB-API/glassfish-jaxb-api\/jakarta.xml.bind-api-%{version}/' %{buildroot}%{_datadir}/maven-metadata/*

%files -f .mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Wed Jan 11 2023 Marian Koncek <mkoncek@redhat.com> - 2.3.3-3
- Provide a jaxb-api.jar symlink

* Thu Dec 22 2022 Marian Koncek <mkoncek@redhat.com> - 2.3.3-2
- Use correct BuildRequires on jakarta.activation-api

* Wed Nov 30 2022 Marian Koncek <mkoncek@redhat.com> - 2.3.3-1
- Initial package renamed from jaxb-api
