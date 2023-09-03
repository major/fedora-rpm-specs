Name:           jaxb-istack-commons
Version:        4.2.0
Release:        3%{?dist}
Summary:        iStack Common Utility Code
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-istack-commons
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package runtime
Summary:        istack-commons runtime

%description runtime
This package contains istack-commons runtime.

%package test
Summary:        istack-commons test

%description test
This package contains istack-commons test.

%package tools
Summary:        istack-commons tools

%description tools
This package contains istack-commons tools.

%prep
%setup -q

pushd istack-commons

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin . test tools
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# Missing dependency on args4j
%pom_disable_module soimp

%pom_disable_module buildtools
%pom_disable_module import-properties-plugin
%pom_disable_module maven-plugin

%mvn_package :istack-commons __noinstall
popd

%build
pushd istack-commons
# Javadoc fails on module.info files: "error: too many module declarations found"
%mvn_build -f -s -j
popd

%install
pushd istack-commons
%mvn_install
popd

%files runtime -f istack-commons/.mfiles-istack-commons-runtime
%license LICENSE.md NOTICE.md
%files test -f istack-commons/.mfiles-istack-commons-test
%license LICENSE.md NOTICE.md
%files tools -f istack-commons/.mfiles-istack-commons-tools
%license LICENSE.md NOTICE.md

%changelog
* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.0-3
- Convert License tag to SPDX format

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 17 2023 Marian Koncek <mkoncek@redhat.com> - 4.2.0-1
- Update to upstream version 4.2.0

* Wed Feb 08 2023 Marian Koncek <mkoncek@redhat.com> - 4.1.1-3
- Reorganize subpackages

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Marian Koncek <mkoncek@redhat.com> - 4.1.1-1
- Update to upstream version 4.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.12-4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.12-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 3.0.12-1
- New upstream release 3.0.12
- Remove workaround for SUREFIRE-1897

* Fri Oct 29 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 3.0.11-7
- Include buildtolls, test, and soimp module
- Don't install parent module

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Dogtag PKI Team <pki-devel@redhat.com> - 3.0.11-5
- Disable tests

* Mon May 24 2021 Dogtag PKI Team <pki-devel@redhat.com> - 3.0.11-4
- Drop jaxb-istack-commons-buildtools, jaxb-istack-commons-soimp,
  and jaxb-istack-commons-test

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 3.0.11-2
- Initial package renamed from istack-commons.
