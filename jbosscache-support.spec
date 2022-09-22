Name:    jbosscache-support
Version: 1.6
Release: 10%{?dist}
Summary: JBossCache support package

License: LGPL
URL:     http://www.jboss.org/jbosscache
# svn export http://anonsvn.jboss.org/repos/jbosscache/support/tags/1.6 jbosscache-support-1.6
# tar cJf jbosscache-support-1.6.tar.xz jbosscache-support-1.6
Source0: %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: java-devel
BuildRequires: jpackage-utils

Requires:      jpackage-utils

BuildArch:     noarch

%description
JBossCache support package is required by jbosscache.

%package -n jbosscache-common-parent
Summary:  Parent pom for jbosscache
Requires: %{name} = %{version}-%{release}

%description -n jbosscache-common-parent
The jbosscache-common-parent package contains the parent pom file
required by jbosscache.

%package xslt
Summary:  Xslt doc support for jbosscache
Requires: %{name} = %{version}-%{release}

%description xslt
The %{name}-xslt package contains xslt doc support for jbosscache.

%prep
%setup -q
find . -name \*.jar -exec rm -f {} \;

# webdav package was dropped from maven-wagon
%pom_xpath_remove "pom:build/pom:extensions/pom:extension[pom:artifactId = 'wagon-webdav']"

%build
# Does not include javadocs or tests
mvn-rpmbuild install -Dmaven.test.skip=true

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 xslt/target/jbosscache-doc-xslt-support-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-xslt.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -m 644 common/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jbosscache-common-parent.pom
install -m 644 xslt/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-xslt.pom

%add_maven_depmap JPP-%{name}-xslt.pom %{name}-xslt.jar
%add_maven_depmap JPP-jbosscache-common-parent.pom -a 'org.jboss.cache:jbosscache-common-parent'
%add_maven_depmap JPP-%{name}.pom -a 'org.jboss.cache:jbosscache-support'

%files
%doc README-Maven.txt
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files -n jbosscache-common-parent
%doc README-Maven.txt
%{_mavenpomdir}/JPP-jbosscache-common-parent.pom

%files xslt
%doc README-Maven.txt
%{_javadir}/%{name}-xslt.jar
%{_mavenpomdir}/JPP-%{name}-xslt.pom

%changelog
* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.6-8
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 11 2013 Matt Spaulding <mspaulding06@gmail.com> - 1.6-7
- Add BR for maven-install-plugin

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 02 2013 Matt Spaulding <mspaulding06@gmail.com> - 1.6-5
- Removed wagon-webdav dependency from pom.xml

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Aug 03 2012 Matt Spaulding <mspaulding06@gmail.com> - 1.6-2
- Removed define from file (was not being used)
- Fixed incorrect license type
- Renamed jbosscache-support-parent subpackage to jbosscache-common-parent to reflect artifactid
- Renamed pom files for parent subpackage name change

* Tue Jul 31 2012 Matt Spaulding <mspaulding06@gmail.com> - 1.6-1
- Initial package

