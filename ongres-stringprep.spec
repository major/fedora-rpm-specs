%global     upstream_name   stringprep

Name:       ongres-%upstream_name
Version:    1.1
Release:    11%{?dist}
Summary:    RFC 3454 Preparation of Internationalized Strings in pure Java
License:    BSD-2-Clause AND Apache-2.0
URL:            https://github.com/ongres/%upstream_name
Source0:        https://github.com/ongres/%upstream_name/archive/%{version}/%upstream_name-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch

%description
The stringprep protocol does not stand on its own;
it has to be used by other protocols at precisely-defined 
places in those other protocols.

%package javadoc
Summary:    Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%prep
%autosetup -p1 -n "%upstream_name-%{version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

# velocity-2 dependencies
%pom_add_dep org.apache.commons:commons-lang3 stringprep
%pom_add_dep org.slf4j:slf4j-simple stringprep

%pom_remove_dep :velocity-tools codegenerator

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# codegenerator is only needed at build time, and has extra dependencies
%mvn_package com.ongres.stringprep:codegenerator __noinstall

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.1-11
- Rebuilt for java-21-openjdk as system jdk

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1-8
- Drop codegenerator from install

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.1-4
- Rebuilt for Drop i686 JDKs

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 1.1-1
- initial rpm
