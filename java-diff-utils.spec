Name:           java-diff-utils
Version:        4.12
Release:        4%{?dist}
Summary:        Java library for performing diff operations

License:        Apache-2.0
URL:            https://java-diff-utils.github.io/java-diff-utils/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-parent-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%global _desc %{expand:
Diff Utils library is an OpenSource library for performing the comparison / diff operations 
between texts or some kind of data: computing diffs, applying patches, generating unified 
diffs or parsing them, generating diff output for easy future displaying (like side-by-side 
view) and so on.}

%description %_desc

%package        parent
Summary:        Java Diff Utils parent POM

%description    parent %_desc

This package contains the parent POM for Java Diff Utils.

%package        jgit
Summary:        Java Diff Utils extension using jgit difference algorithms
Requires:       %{name} = %{version}-%{release}

%description    jgit %_desc

This package contains an extension to the main package that uses jgit's
difference algorithms.

%{?javadoc_package}

%prep
%autosetup -n %{name}-%{name}-parent-%{version}

# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-java-diff-utils
%license LICENSE

%files parent -f .mfiles-java-diff-utils-parent
%license LICENSE

%files jgit -f .mfiles-java-diff-utils-jgit

%changelog
* Tue Oct 03 2023 Christiano Anderson <chris@christiano.dev> - 4.12-4
- Updated description and rebuilt for fc40 

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Jerry James <loganjerry@gmail.com> - 4.12-1
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 4.12-1
- Version 4.12

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 4.11-4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.11-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep  8 2021 Jerry James <loganjerry@gmail.com> - 4.11-1
- Version 4.11
- Drop upstreamed -javadoc patch

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  1 2021 Jerry James <loganjerry@gmail.com> - 4.10-1
- Version 4.10
- Drop upstreamed -unchecked patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Jerry James <loganjerry@gmail.com> - 4.9-1
- Initial RPM
