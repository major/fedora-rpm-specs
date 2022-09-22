%global namedreltag .Final
%global oname hibernate-jpa-api
%global apiversion 2.1
%global minversion 0
%global pkgversion %{?apiversion}%{?minversion}%{?namedreltag}
%global namedversion %{version}%{?namedreltag}

Name:          hibernate-jpa-2.1-api
Version:       1.0.0
Release:       16%{?dist}
Summary:       Java Persistence 2.1 (JSR 338) API
License:       EPL and BSD
URL:           http://www.hibernate.org/
Source0:       https://github.com/hibernate/hibernate-jpa-api/archive/%{pkgversion}.tar.gz
Source1:       http://repo1.maven.org/maven2/org/hibernate/javax/persistence/%{name}/%{namedversion}/%{name}-%{namedversion}.pom
# fix mvn build, this project uses the default Gradle to build
# sets various mvn plugins properties
Patch0:        hibernate-jpa-api-2.10.Final-pom.patch

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
Hibernate definition of the Java Persistence 2.1 (JSR 338) API.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{pkgversion}
find . -name "*.jar" -delete

cp -p %{SOURCE1} pom.xml
%patch0 -p1

# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' src/main/javadoc/jdstyle.css

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.0-15
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.0-14
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.0-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 06 2016 gil cattaneo <puntogil@libero.it> 1.0.0-1
- update to 1.0.0.Final

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.9.Draft.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 gil cattaneo <puntogil@libero.it> - 1.0.0-0.8.Draft.16
- rebuilt

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.7.Draft.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 05 2015 gil cattaneo <puntogil@libero.it> 1.0.0-0.6.Draft.16
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.Draft.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.0-0.4.Draft.16
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.Draft.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 gil cattaneo <puntogil@libero.it> 1.0.0-0.2.Draft.16
- switch to XMvn
- minor changes to adapt to current guideline

* Thu May 09 2013 gil cattaneo <puntogil@libero.it> 1.0.0-0.1.Draft.16
- initial rpm
