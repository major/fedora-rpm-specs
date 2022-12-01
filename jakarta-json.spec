Name:           jakarta-json
Version:        2.1.1
Release:        1%{?dist}
Summary:        Jakarta JSON Processing

License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://projects.eclipse.org/projects/ee4j.jsonp
Source0:        https://github.com/jakartaee/jsonp-api/archive/%{version}-RELEASE.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# These can be removed when Fedora 36 reaches EOL
Obsoletes:      jsonp < 1.0.4-12
Provides:       jsonp = %{version}-%{release}
Obsoletes:      jsonp-javadoc < 1.0.4-12

# These can be removed when Fedora 38 reaches EOL
Obsoletes:      jakarta-json-jaxrs < 1.1.6-5
Obsoletes:      jakarta-json-jaxrs-1x < 1.1.6-5

# These can be removed when Fedora 41 reaches EOL
Obsoletes:      jakarta-json-impl < 2.0.0
Obsoletes:      jakarta-json-api < 2.0.0
Provides:       jakarta-json-api = %{version}-%{release}

%description
Jakarta JSON Processing provides portable APIs to parse, generate,
transform, and query JSON documents.

%{?javadoc_package}

%prep
%autosetup -n jsonp-api-%{version}-RELEASE

# org.eclipse.ee4j:project is not available in Fedora
%pom_remove_parent api

# Unnecessary plugins for an RPM build
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin api
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin api

# This plugin is not available in Fedora
%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin api

%build
cd api
%mvn_build
cd -

%install
cd api
%mvn_install
cd -
ln -s api/.mfiles-javadoc .

%files -f api/.mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%changelog
* Tue Nov 29 2022 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Version 2.1.1
- New URLs
- Drop obsolete -deprecated patch
- Drop subpackages since there is only 1 jar now

* Thu Nov 24 2022 Jerry James <loganjerry@gmail.com> - 1.1.6-9
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.6-8
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.6-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct  8 2021 Jerry James <loganjerry@gmail.com> - 1.1.6-5
- Drop the jaxrs and jaxrs-1x subpackages, since they depend on jaxb

* Fri Oct  8 2021 Jerry James <loganjerry@gmail.com> - 1.1.6-4
- Remove dependency on jaxb, which has been retired

* Sat Aug 14 2021 Jerry James <loganjerry@gmail.com> - 1.1.6-3
- Add jakarta-annotation and junit BuildRequires

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Jerry James <loganjerry@gmail.com> - 1.1.6-1
- Change name from "jsonp"
- Version 1.1.6
- Split into subpackages to manage dependencies
