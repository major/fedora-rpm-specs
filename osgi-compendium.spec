%bcond_with bootstrap

Name:           osgi-compendium
Version:        7.0.0
Release:        16%{?dist}
Summary:        Interfaces and Classes for use in compiling OSGi bundles
License:        Apache-2.0
URL:            http://www.osgi.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://osgi.org/download/r7/osgi.cmpn-%{version}.jar

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.core)
%endif

%description
OSGi Compendium, Interfaces and Classes for use in compiling bundles.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -c

# Delete pre-built binaries
rm -r org
find -name '*.class' -delete

mkdir -p src/main/{java,resources}
mv OSGI-OPT/src/org src/main/java/
mv xmlns src/main/resources

# J2ME stuff
rm -r src/main/java/org/osgi/service/io

mv META-INF/maven/org.osgi/osgi.cmpn/pom.xml .

%pom_xpath_inject pom:project '
<packaging>bundle</packaging>
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-Name>${project.artifactId}</Bundle-Name>
          <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>'

%pom_add_dep org.osgi:osgi.annotation::provided
%pom_add_dep org.osgi:osgi.core::provided
# Don't compile in Servlet, Jax RS and JPA support
rm -r src/main/java/org/osgi/service/http
rm -r src/main/java/org/osgi/service/jaxrs
rm -r src/main/java/org/osgi/service/jpa
rm -r src/main/java/org/osgi/service/transaction/control/jpa

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install


%files -f .mfiles
%license LICENSE
%doc about.html

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 7.0.0-16
- Convert License tag to SPDX format

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 7.0.0-12
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 7.0.0-9
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Mat Booth <mat.booth@redhat.com> - 7.0.0-7
- Rebuild to regenerate OSGi metadata

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 7.0.0-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 7.0.0-4
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 7.0.0-3
- Mass rebuild for javapackages-tools 201901

* Tue Mar 19 2019 Mat Booth <mat.booth@redhat.com> - 7.0.0-2
- Allow conditionally compiling in support for Jax RS and JPA

* Wed Mar 06 2019 Mat Booth <mat.booth@redhat.com> - 7.0.0-1
- Update to OSGi R7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 6.0.0-2
- Fix scopes of injected Maven dependencies

* Mon Oct 12 2015 Michael Simacek <msimacek@redhat.com> - 6.0.0-1
- Initial packaging
