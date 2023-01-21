%global srcname jax-ws-api

Name:           jakarta-xml-ws
Version:        2.3.3
Release:        2%{?dist}
Summary:        Jakarta XML Web Services API
License:        BSD

URL:            https://github.com/eclipse-ee4j/jax-ws-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  git
BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(jakarta.xml.soap:jakarta.xml.soap-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
#BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

%description
Jakarta XML Web Services defines a means for implementing XML-Based Web
Services based on Jakarta SOAP with Attachments and Jakarta Web Services
Metadata.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup -S git -n %{srcname}-%{version}

cd api
# remove unnecessary dependency on parent POM
  %pom_remove_parent
# remove unnecessary maven plugin
  %pom_remove_plugin :glassfish-copyright-maven-plugin
# removed temporary due to naming requirements
  %pom_remove_plugin :spec-version-maven-plugin
# not used
  %pom_remove_dep :jakarta.jws-api
cd -


%build
cd api
  %mvn_build
cd -


%install
cd api
  %mvn_install
cd -


%files -f api/.mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f api/.mfiles-javadoc


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.3.3-1
- Update to version 2.3.3
- Change License to BSD
- Change source url
- Change BuildRequires
- Remove Obsoletes and Provides
- Unpack as git directory (needed by buildnumber-maven-plugin)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.1-6
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.1-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-1
- Package renamed from glassfish-jaxws.

