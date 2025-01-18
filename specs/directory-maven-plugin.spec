Name:       directory-maven-plugin
Version:    1.0
Release:    4%{?dist}
Summary:    Establish locations for files in multi-module builds

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:    Apache-2.0
URL:        https://github.com/jdcasey/directory-maven-plugin

Source0:    https://github.com/jdcasey/directory-maven-plugin/archive/directory-maven-plugin-%{version}.tar.gz
# Fixes bz 2261062 - no mojo definition build error
# https://github.com/knight-of-ni/directory-maven-plugin/commit/ce51a6ea81b583c7b7b75e859bb1a508eb713fbe.patch
Patch0:     directory-maven-plugin-fix-no-mojo-definition.patch

BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(junit:junit)

%description
The Directory Plugin for Maven is used to discover various project-related 
paths, such as the execution root directory, the directory for a specific 
project in the current build session, or the highest project base directory 
(closest to the filesystem root directory) available in the projects loaded 
from disk (not resolved from a remote repository). The plugin will then reflect
this value to the console, and also inject it into each project's properties 
using the value of the property plugin parameter.

%package javadoc
Summary:  Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%autosetup -n directory-maven-plugin-directory-maven-plugin-%{version}

%pom_remove_parent

# Bump Java source option
sed -i 's/1.7/1.8/g' pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md
%license LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.0-1
- 1.0 release

* Thu Feb 29 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.3.1-14
- bump java source/target to 1.8, fixes 2266639
- patch pom.xml, fixes bz 2261062

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.3.1-13
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.3.1-7
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.3.1-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Jie kang <jkang@redhat.com> - 0.3.1-2
- Remove deprecated dependency: sonatype-oss-parent
- Use version macro. Add license to javadoc files

* Mon Oct 15 2018 Salman Siddiqui <sasiddiq@redhat.com> - 0.3.1-1
- Initial packaging
