%bcond_with bootstrap

Name:           jakarta-mail
Version:        2.1.5
Release:        1%{?dist}
Summary:        Jakarta Mail API
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/eclipse-ee4j/mail
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/mail/archive/%{version}/mail-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

%description
The Jakarta Mail API provides a platform-independent and
protocol-independent framework to build mail and messaging applications.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n mail-api-%{version}

pushd api
# Remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin

# Missing dependency
%pom_remove_dep :angus-activation
rm src/test/java/jakarta/mail/internet/NonAsciiFileNamesTest.java
popd

%build
pushd api
%mvn_build
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f api/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Sat Jan 17 2026 Andrew Bauer <zonexpertconsulting@outlook.com> - 2.1.5-1
- Update to 2.1.5 release

* Fri Sep 01 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 2.1.2-1
- Update to 2.1.2 release

* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.0-2
- Rebuild

* Mon Aug 21 2023 Marian Koncek <mkoncek@redhat.com> - 2.1.0-1
- Update to upstream version 2.1.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.6.7-2
- Rebuilt for Drop i686 JDKs

* Fri Apr 29 2022 Marian Koncek <mkoncek@redhat.com> - 1.6.7-1
- Update to upstream version 1.6.7

* Wed Apr 27 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.5-9
- Workaround build issue with RPM 4.18

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.6.5-8
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.5-6
- Disable tests failing due to glibc rhbz#2033020
- Remove obsoletes/provides on javamail

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.5-5
- Fix build with OpenJDK 17

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.5-3
- Add build-dependency on junit

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6.5-1
- Initial package renamed from javamail.
