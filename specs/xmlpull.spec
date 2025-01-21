Name:           xmlpull
Version:        1.2.0
Release:        11%{?dist}
Summary:        XML Pull Parsing API

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            https://github.com/xmlpull-xpp3/%{name}-xpp3
Source0:        %{url}/archive/%{name}-xpp3-parent-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(junit:junit)

%description
XmlPull v1 API is a simple to use XML pull parsing API that was
designed for simplicity and very good performance both in constrained
environment such as defined by J2ME and on server side when used in
J2EE application servers.

%javadoc_package

%prep
%autosetup -n %{name}-xpp3-%{name}-xpp3-parent-%{version}

find \( -name \*.jar -o -name \*.class \) -delete

%pom_disable_module xpp3_min

# using java 8, we need to remove the java module
rm xmlpull/src/main/java/module-info.java

%mvn_package :%{name}-xpp3-parent __noinstall

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license %{name}/LICENSE.txt
%doc %{name}/README.adoc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.2.0-9
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.0-4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.0-3
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Didik Supriadi <didiksupriadi41@gmail.com> - 1.2.0-1
- Initial package
