Name:           jaxb-api2
Version:        2.3.3
Release:        1%{?dist}
Summary:        Jakarta XML Binding API
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api) < 2
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

# Remove unnecessary maven plugins
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Mark dependency on jakarta.activation as optional
%pom_xpath_inject "pom:dependency[pom:groupId='jakarta.activation']" "<optional>true</optional>" jaxb-api

# Add compatibility aliases for old artifact coordinates
%mvn_alias jakarta.xml.bind:jakarta.xml.bind-api javax.xml.bind:jaxb-api
%mvn_file :jakarta.xml.bind-api glassfish-jaxb-api/jakarta.xml.bind-api jaxb-api

%mvn_compat_version 'javax.xml.bind:jaxb-api' %{version}
%mvn_compat_version 'jakarta.xml.bind:jakarta.xml.bind-api' %{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Wed Nov 30 2022 Marian Koncek <mkoncek@redhat.com> - 2.3.3-1
- Initial package renamed from jaxb-api
