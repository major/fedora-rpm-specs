%global commit 7ed1368ef26d2b4ef752b35ae33a98ec372ef3f8
%global _buildNumber %(c=%{commit}; echo ${c:0:7})
%global _scmBranch %{version}

Name:           jaxb-istack-commons
Version:        3.0.12
Release:        5%{?dist}
Summary:        iStack Common Utility Code
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-istack-commons
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.glassfish.jaxb:codemodel)
BuildRequires:  mvn(org.testng:testng)

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package -n istack-commons-maven-plugin
Summary:        istack-commons Maven Mojo
%description -n istack-commons-maven-plugin
This package contains the istack-commons Maven Mojo.

%package -n import-properties-plugin
Summary:        istack-commons import properties plugin
%description -n import-properties-plugin
This package contains the istack-commons import properties Maven Mojo.

%package -n istack-commons-runtime
Summary:        istack-commons runtime
%description -n istack-commons-runtime
This package contains istack-commons runtime.

%package -n istack-commons-tools
Summary:        istack-commons tools
%description -n istack-commons-tools
This package contains istack-commons tools.

%package -n istack-commons-buildtools
Summary:        istack-commons buildtools
%description -n istack-commons-buildtools
This package contains istack-commons buildtools.

%package -n istack-commons-soimp
Summary:        istack-commons soimp
%description -n istack-commons-soimp
This package contains istack-commons soimp.

%package -n istack-commons-test
Summary:        istack-commons test
%description -n istack-commons-test
This package contains istack-commons test.

%prep
%autosetup

pushd istack-commons
# disable very verbose warnings
sed -i -e '/Xlint:all/d' pom.xml

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin . test tools
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%mvn_package :istack-commons __noinstall

# Compatibility
%mvn_alias :istack-commons-maven-plugin com.sun.istack:maven-istack-commons-plugin
popd

%build
pushd istack-commons
# - skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
# - ignore test
%mvn_build -f -j -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -DscmBranch=%{_scmBranch} -DbuildNumber=%{_buildNumber}
popd

%install
pushd istack-commons
%mvn_install
popd

%files -n istack-commons-maven-plugin -f istack-commons/.mfiles-istack-commons-maven-plugin
%license LICENSE.md NOTICE.md

%files -n import-properties-plugin -f istack-commons/.mfiles-import-properties-plugin
%license LICENSE.md NOTICE.md

%files -n istack-commons-runtime -f istack-commons/.mfiles-istack-commons-runtime
%license LICENSE.md NOTICE.md

%files -n istack-commons-tools -f istack-commons/.mfiles-istack-commons-tools
%license LICENSE.md NOTICE.md

%files -n istack-commons-buildtools -f istack-commons/.mfiles-istack-commons-buildtools
%license LICENSE.md NOTICE.md

%files -n istack-commons-test -f istack-commons/.mfiles-istack-commons-test
%license LICENSE.md NOTICE.md

%files -n istack-commons-soimp -f istack-commons/.mfiles-istack-commons-soimp
%license LICENSE.md NOTICE.md

%changelog
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

