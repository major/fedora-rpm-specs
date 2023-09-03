Name:           jaxb-stax-ex
Version:        2.1.0
Release:        4%{?dist}
Summary:        Extended StAX API
License:        BSD-3-Clause

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
%setup -q

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.0-4
- Convert License tag to SPDX format

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Marian Koncek <mkoncek@redhat.com> - 2.1.0-1
- Update to upstream version 2.1.0

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
