Name:           pomchecker
Version:        1.2.0
Release:        7%{?dist}
Summary:        POM syntax checker
License:        ASL 2.0
URL:            https://github.com/kordamp/pomchecker
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(info.picocli:picocli)
BuildRequires:  mvn(info.picocli:picocli-codegen)
BuildRequires:  mvn(org.apache.maven.enforcer:enforcer-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-spi)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-file)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-http)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-resolver-provider)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%description
Checks that a POM file has the required syntax for a given purpose.

%package -n %{name}-core
Summary:        POM validation core implementation
%description -n %{name}-core
Provides base behavior for other PomChecker projects.

%package -n %{name}-cli
Summary:        POM validation CLI runner

%if 0%{?fedora} >= 36
Requires:       mvn(org.codehaus.plexus:plexus-sec-dispatcher)
Requires:       mvn(org.codehaus.plexus:plexus-cipher)
Requires:       mvn(jakarta.enterprise:jakarta.enterprise.cdi-api)
Requires:       mvn(jakarta.inject:jakarta.inject-api)
Requires:       mvn(com.google.guava:failureaccess)
%else
Requires:       mvn(org.sonatype.plexus:plexus-sec-dispatcher)
Requires:       mvn(org.sonatype.plexus:plexus-cipher)
Requires:       mvn(javax.enterprise:cdi-api)
Requires:       mvn(javax.inject:javax.inject)
%endif

Requires:       javapackages-tools
Requires:       mvn(org.apache.maven:maven-artifact)
Requires:       mvn(org.codehaus.plexus:plexus-utils)
Requires:       mvn(org.apache.commons:commons-lang3)
Requires:       mvn(org.apache.maven:maven-compat)
Requires:       mvn(org.apache.maven:maven-settings-builder)
Requires:       mvn(org.apache.maven.resolver:maven-resolver-impl)
Requires:       mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
Requires:       mvn(jakarta.annotation:jakarta.annotation-api)
Requires:       mvn(org.codehaus.plexus:plexus-component-annotations)
Requires:       mvn(org.apache.maven:maven-core)
Requires:       mvn(org.apache.maven:maven-builder-support)
Requires:       mvn(org.apache.maven:maven-plugin-api)
Requires:       mvn(org.apache.maven.shared:maven-shared-utils)
Requires:       mvn(commons-io:commons-io)
Requires:       mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
Requires:       mvn(com.google.inject:guice::no_aop:)
Requires:       mvn(com.google.guava:guava)
Requires:       mvn(com.google.code.findbugs:jsr305)
Requires:       mvn(org.codehaus.plexus:plexus-classworlds)
Requires:       mvn(org.apache.maven:maven-model)
Requires:       mvn(org.apache.maven:maven-model-builder)
Requires:       mvn(org.apache.maven:maven-project)
Requires:       mvn(org.apache.maven:maven-profile)
Requires:       mvn(org.apache.maven:maven-artifact-manager)
Requires:       mvn(org.apache.maven:maven-plugin-registry)
Requires:       mvn(org.codehaus.plexus:plexus-container-default)
Requires:       mvn(org.apache.maven:maven-repository-metadata)
Requires:       mvn(org.apache.maven.resolver:maven-resolver-api)
Requires:       mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
Requires:       mvn(org.apache.maven:maven-resolver-provider)
Requires:       mvn(org.apache.maven.resolver:maven-resolver-spi)
Requires:       mvn(org.apache.maven.resolver:maven-resolver-transport-file)
Requires:       mvn(org.apache.maven.resolver:maven-resolver-transport-http)
Requires:       mvn(org.apache.httpcomponents:httpclient)
Requires:       mvn(commons-codec:commons-codec)
Requires:       mvn(org.apache.httpcomponents:httpcore)
Requires:       mvn(org.slf4j:jcl-over-slf4j)
Requires:       mvn(org.apache.maven.resolver:maven-resolver-util)
Requires:       mvn(org.apache.maven:maven-settings)
Requires:       mvn(info.picocli:picocli)
Requires:       mvn(org.codehaus.plexus:plexus-interpolation)
Requires:       mvn(org.slf4j:slf4j-api)
Requires:       mvn(org.apache.maven.wagon:wagon-provider-api)
Requires:       mvn(org.slf4j:slf4j-simple)
Requires:       mvn(aopalliance:aopalliance)

%description -n %{name}-cli
Command line tool for checking POM compliance.

%package -n %{name}-enforcer-rules
Summary:        POM validation enforcer rules
%description -n %{name}-enforcer-rules
Provides rules that can be used with the Maven Enforcer plugin.

%package -n %{name}-maven-plugin
Summary:        POM validation Maven plugin
%description -n %{name}-maven-plugin
The PomChecker Maven plugin provides goals to check the contents of a POM file.

%{?javadoc_package}

%prep
%autosetup

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

%pom_remove_plugin com.mycila:license-maven-plugin
%pom_remove_plugin org.codehaus.mojo:appassembler-maven-plugin %{name}-cli
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-site-plugin

%pom_remove_parent

%pom_xpath_inject pom:project '<groupId>org.kordamp.maven</groupId>'
%pom_xpath_inject 'pom:plugin[pom:artifactId = "maven-compiler-plugin"]' '<version>3.8.1</version>' %{name}-cli
%pom_xpath_inject 'pom:plugin[pom:artifactId = "maven-jar-plugin"]' '<version>3.2.0</version>' %{name}-cli

%pom_disable_module pomchecker-toolprovider
%pom_disable_module pomchecker-gradle-plugin

%mvn_package :%{name} __noinstall

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%jpackage_script org.kordamp.maven.checker.cli.Main "" "" pomchecker/pomchecker-cli:pomchecker/pomchecker-core:maven/maven-artifact:plexus/utils:apache-commons-lang3:maven/maven-compat:maven/maven-settings-builder:plexus/plexus-sec-dispatcher:plexus/plexus-cipher:maven-resolver/maven-resolver-impl:org.eclipse.sisu.plexus:cdi-api/jakarta.enterprise.cdi-api:jakarta-annotations/jakarta.annotation-api:plexus-containers/plexus-component-annotations:maven/maven-core:maven/maven-builder-support:maven/maven-plugin-api:maven-shared-utils/maven-shared-utils:apache-commons-io:org.eclipse.sisu.inject:guice/google-guice-no_aop:guava/guava:jsr-305:atinject:plexus/classworlds:maven/maven-model:maven/maven-model-builder:maven/maven-project:maven/maven-profile:maven/maven-artifact-manager:maven/maven-plugin-registry:plexus-containers/plexus-container-default:maven/maven-repository-metadata:maven-resolver/maven-resolver-api:maven-resolver/maven-resolver-connector-basic:maven/maven-resolver-provider:maven-resolver/maven-resolver-spi:maven-resolver/maven-resolver-transport-file:maven-resolver/maven-resolver-transport-http:httpcomponents/httpclient:apache-commons-codec:httpcomponents/httpcore:slf4j/jcl-over-slf4j:maven-resolver/maven-resolver-util:maven/maven-settings:picocli/picocli:plexus/interpolation:slf4j/slf4j-api:maven-wagon/provider-api:slf4j/slf4j-simple:guava/failureaccess:aopalliance pomchecker true

%files -n %{name}-core -f .mfiles-%{name}-core
%license LICENSE

%files -n %{name}-cli -f .mfiles-%{name}-cli
%license LICENSE
%{_bindir}/pomchecker

%files -n %{name}-enforcer-rules -f .mfiles-%{name}-enforcer-rules
%license LICENSE

%files -n %{name}-maven-plugin -f .mfiles-%{name}-maven-plugin
%license LICENSE

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.0-6
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.0-5
- Rebuilt for java-17-openjdk as system jdk

* Mon Jan 24 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.2.0-4
- Fix F34FailsToInstall: pomchecker-cli (rhbz#2044312)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.2.0-2
- Add requires in cli subpackage

* Fri Oct 08 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.2.0-1
- Initial package
