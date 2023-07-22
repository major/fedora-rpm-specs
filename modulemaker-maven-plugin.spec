%bcond_with bootstrap

Name:           modulemaker-maven-plugin
Version:        1.9
Release:        3%{?dist}
Summary:        A plugin for creating module-info.class files
License:        Apache-2.0
URL:            https://github.com/raphw/modulemaker-maven-plugin
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/raphw/modulemaker-maven-plugin/archive/refs/tags/modulemaker-maven-plugin-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
%endif

%description
This plugin allows the creation of a module-info.class for projects on Java 6
to Java 8 where a module-info.java file cannot be compiled.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n modulemaker-maven-plugin-modulemaker-maven-plugin-%{version}

cp -p %{SOURCE1} .

%pom_xpath_inject 'pom:dependency[pom:artifactId="maven-plugin-api"]' '<scope>provided</scope>'

%build
%mvn_build -- -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-2
- Implement bootstrap mode

* Thu Feb 16 2023 Marian Koncek <mkoncek@redhat.com> - 1.9-2
- Initial build
