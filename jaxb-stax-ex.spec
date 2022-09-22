Name:           jaxb-stax-ex
Version:        1.8.3
Release:        10%{?dist}
Summary:        Extended StAX API
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-stax-ex
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
This project contains a few extensions to complement JSR-173 StAX API in
the following areas:

- Enable parser instance reuse (which is important in the
  high-performance environment like Eclipse Implementation of JAXB and
  Eclipse Metro)
- Improve the support for reading from non-text XML infoset, such as
  FastInfoset.
- Improve the namespace support.

%{?javadoc_package}

%prep
%autosetup

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin


%build
%mvn_build -- -Dmaven.compiler.source=1.8  -Dmaven.compiler.target=1.8


%install
%mvn_install


%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.8.3-9
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.8.3-8
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.8.3-6
- Remove workaround for SUREFIRE-1897

* Tue Oct 19 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.8.3-5
- Enable test and javadoc package
- Simplified module-info.class build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Dogtag PKI Team <pki-devel@redhat.com> - 1.8.3-3
- Disable tests

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.3-1
- Initial package renamed from stax-ex.

