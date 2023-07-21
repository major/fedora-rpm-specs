%bcond_with bootstrap

Name:           extra-enforcer-rules
Version:        1.5.1
Release:        5%{?dist}
Summary:        Extra rules for maven-enforcer-plugin
License:        ASL 2.0
URL:            https://github.com/mojohaus/extra-enforcer-rules
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/mojohaus/extra-enforcer-rules/archive/refs/tags/extra-enforcer-rules-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.enforcer:enforcer-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif

%description
Apache's Maven Enforcer Plugin is used to apply and enforce rules on Maven
projects. The Enforcer plugin ships with a set of standard rules. This project
provides extra rules which are not part of the standard rule set.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n extra-enforcer-rules-extra-enforcer-rules-%{version}

# Integration tests fetch upstream poms
%pom_remove_plugin :maven-invoker-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 05 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.1-2
- Implement bootstrap mode

* Mon May 02 2022 Marian Koncek <mkoncek@redhat.com> - 1.5.1-1
- Initial release
