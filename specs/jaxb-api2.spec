Name:           jaxb-api2
Version:        2.3.3
Release:        %autorelease
Summary:        Jakarta XML Binding API
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api:1.2.2)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# TODO Remove in Fedora 47
Obsoletes:      %{name}-javadoc < 2.3.3-15

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%prep
%autosetup -p1 -C

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
%mvn_build -j

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

%autochangelog
