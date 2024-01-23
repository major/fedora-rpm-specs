# Testing note: this package relies on an old version of mockito.  Compilation
# of the tests fails with the version of mockito currently in Fedora.  Porting
# to the new version is needed.

Name:           mojo-executor
Version:        2.4.0
Release:        7%{?dist}
Summary:        Execute other plugins within a maven plugin

License:        Apache-2.0
URL:            https://mojo-executor.github.io/mojo-executor/
Source0:        https://github.com/mojo-executor/mojo-executor/archive/%{name}-parent-%{version}.tar.gz
# Fix a javadoc comment
Patch0:         %{name}-javadoc.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)

%description
The Mojo Executor provides a way to to execute other Mojos (plugins)
within a Maven plugin, allowing you to easily create Maven plugins that
are composed of other plugins.

%package parent
Summary:        Parent POM for mojo-executor

%description parent
%{summary}.

%package maven-plugin
Summary:        Maven plugin for mojo-executor

%description maven-plugin
%{summary}.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%autosetup -n %{name}-%{name}-parent-%{version} -p1

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# We do not need jacoco since we do not run the tests
%pom_remove_plugin :jacoco-maven-plugin

# maven-release is not needed
%pom_remove_plugin :maven-release-plugin

# Modernize the junit dependency
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-no-plugin-version/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-null-maven-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-quiet/pom.xml

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-%{name}
%license LICENSE.txt
%doc README.md

%files parent -f .mfiles-%{name}-parent

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug  4 2023 Jerry James <loganjerry@gmail.com> - 2.4.0-6
- Bring back the ant-contrib dependency

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 2.4.0-3
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.4.0-2
- Rebuilt for Drop i686 JDKs

* Thu Mar 10 2022 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- Version 2.4.0
- Drop upstreamed -commons-lang3 patch

* Fri Feb 11 2022 Jerry James <loganjerry@gmail.com> - 2.3.3-1
- Version 2.3.3
- New URLs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.2-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 2.3.2-1
- Version 2.3.2
- Add -javadoc patch

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 2.3.1-8
- Remove build dependency on ant-contrib

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun  3 2021 Jerry James <loganjerry@gmail.com> - 2.3.1-6
- Remove dependency on jacoco

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug  2 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-4
- Add -commons-lang3 patch

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-2
- Drop unnecessary maven-release-plugin BR

* Sat Jan 18 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Initial RPM
