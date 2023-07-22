Name:           jaxb-api
Version:        4.0.0
Release:        4%{?dist}
Summary:        Jakarta XML Binding API
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
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
%setup -q

# Remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Marian Koncek <mkoncek@redhat.com> - 4.0.0-2
- Rebuild

* Fri Jan 06 2023 Marian Koncek <mkoncek@redhat.com> - 4.0.0-1
- Update to upstream version 4.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.3-7
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.3-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.3-2
- Initial package renamed from glassfish-jaxb-api.
