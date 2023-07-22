Name:           jakarta-activation
Version:        2.1.1
Release:        4%{?dist}
Summary:        Jakarta Activation API
# the whole project is licensed under (EPL-2.0 or BSD)
# the source code additionally can be licensed under GPLv2 with exceptions
# we only ship built source code
License:        EPL-2.0 or BSD or GPLv2 with exceptions
URL:            https://jakartaee.github.io/jaf-api/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/jaf-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaf-api-%{version}

pushd api
%pom_remove_parent

# remove custom doclet configuration
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
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
%doc README.md
%license LICENSE.md NOTICE.md

%files javadoc -f api/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Marian Koncek <mkoncek@redhat.com> - 2.1.1-3
- Change license, reduce dependencies

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Marian Koncek <mkoncek@redhat.com> - 2.1.1-1
- Update to upstream version 2.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.2-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.2-3
- Temporarily disable javadoc generation

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.2-1
- Update to version 1.2.2.
- Drop custom maven-compiler-plugin overrides in favor of upstream settings.

* Wed Jul 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-7
- Override javac source / target versions with 1.8 to fix build with Java 11.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-5
- Package unretired and renamed from jaf.
