%global srcname saaj-api

Name:           jakarta-saaj
Version:        3.0.0
Release:        5%{?dist}
Summary:        SOAP with Attachments API for Java
License:        BSD
URL:            https://github.com/eclipse-ee4j/saaj-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

%description
Jakarta SOAP with Attachments defines an API enabling developers to
produce and consume messages conforming to the SOAP 1.1, SOAP 1.2, and
SOAP Attachments Feature.

%package javadoc
Summary:        API documentation for %{name}
%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent
# remove unnecessary maven plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin
# add compatibility alias for old maven artifact coordinates
%mvn_alias jakarta.xml.soap:jakarta.xml.soap-api javax.xml.soap:saaj-api
# add compatibility symlink for old classpath
%mvn_file : %{name}/jakarta.xml.soap-api geronimo-saaj

# TODO remove when https://github.com/jakartaee/saaj-api/issues/134 is resolved
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:compilerArgs/pom:arg[text()="-Werror"]'
popd

%build
pushd api
# - skip tests because metro-saaj is not packaged for fedora yet:
#   https://github.com/eclipse-ee4j/metro-saaj
%mvn_build -f
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f api/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.0.0-5
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 3.0.0-1
- New upstream release 3.0.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.2-7
- Rebuilt for Drop i686 JDKs

* Tue Feb 22 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.2-6
- Cleanup spec

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.2-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 22 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.2-1
- Initial package renamed from geronimo-saaj.

