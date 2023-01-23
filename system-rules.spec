Name:           system-rules
Version:        1.19.0
Release:        5%{?dist}
Summary:        A collection of JUnit rules for testing code which uses java.lang.System
License:        CPL
URL:            https://stefanbirkner.github.io/system-rules
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/stefanbirkner/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  maven-local-openjdk8
BuildRequires:  mvn(com.github.stefanbirkner:fishbowl)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.mockito:mockito-core)

%description
System Rules is a collection of JUnit rules for testing code which uses
java.lang.System.

%{?javadoc_package}

%prep
# -n: base directory name
%autosetup -n %{name}-%{name}-%{version}
# delete precompiled jar and class files
find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete
# remove parent dep
%pom_remove_parent
# add groupId as consequences of removing parent
# see: https://maven.apache.org/guides/introduction/introduction-to-the-pom.html#the-solution
%pom_xpath_inject pom:project '<groupId>com.github.stefanbirkner</groupId>'
# add version to remove warning about unversioned plugin
%pom_xpath_inject 'pom:plugin[pom:artifactId = "maven-surefire-plugin"]' '<version>3.0.0-M5</version>'
# remove forkMode (deprecated)
%pom_xpath_remove 'pom:plugin[pom:artifactId = "maven-surefire-plugin"]/pom:configuration/pom:forkMode'
# alias for junit
# this PR will solve this in the future: https://src.fedoraproject.org/rpms/junit/pull-request/4
%pom_change_dep junit:junit-dep junit:junit
# add surefire deps
# see: https://bugzilla.redhat.com/show_bug.cgi?id=2007791#c15
%pom_add_dep org.apache.commons:commons-lang3:3.8.1:test
# remove unnecessary plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.19.0-3
- Rebuilt for Drop i686 JDKs

* Fri Oct 22 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.19.0-2
- Fix tests
- Remove deprecated forkMode

* Mon Aug 30 2021 Didik Supriadi <didiksupriadi41@gmail.com> - 1.19.0-1
- Initial package
