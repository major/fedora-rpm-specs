Name:           jaxb-dtd-parser
Version:        1.5.0
Release:        8%{?dist}
Summary:        SAX-like API for parsing XML DTDs
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
SAX-like API for parsing XML DTDs.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

pushd dtd-parser

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
popd

%build
pushd dtd-parser
%mvn_build
popd

%install
pushd dtd-parser
%mvn_install
popd

%files -f dtd-parser/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f dtd-parser/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-8
- Convert License tag to SPDX format

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Marian Koncek <mkoncek@redhat.com> - 1.5.0-6
- Remove provision of glassfish artifact

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Marian Koncek <mkoncek@redhat.com> - 1.5.0-4
- Reduce dependencies

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.0-2
- Rebuilt for Drop i686 JDKs

* Mon Apr 11 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.5.0-1
- New upstream release 1.5.0

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.5-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.5-1
- New upstream release 1.4.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Mat Booth <mat.booth@redhat.com> - 1.4.3-3
- Restore JDK 9+ bits for Jaxb

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.3-1
- Initial package renamed from glassfish-dtd-parser.
