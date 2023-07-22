Name:           jakarta-mail
Version:        1.6.7
Release:        5%{?dist}
Summary:        Jakarta Mail API
License:        EPL-2.0 or GPLv2 with exceptions
URL:            https://github.com/eclipse-ee4j/mail
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/mail/archive/%{version}/mail-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.activation:jakarta.activation)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# javadoc package is currently not built
Obsoletes:      javamail-javadoc  < 1.5.2-16

%description
The Jakarta Mail API provides a platform-independent and
protocol-independent framework to build mail and messaging applications.

%prep
%setup -q -n mail-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

# disable unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :osgiversion-maven-plugin
%pom_remove_plugin :directory-maven-plugin

# disable android-specific code
%pom_disable_module android

# remove profiles that only add unnecessary things
%pom_xpath_remove "pom:project/pom:profiles"

# inject OSGi bundle versions manually instead of using osgiversion-maven-plugin
find -name pom.xml -exec sed -i "s/\${mail\.osgiversion}/%{version}/g" {} +

# -Werror is considered harmful
sed -i "/-Werror/d" mail/pom.xml

# add aliases for old maven artifact coordinates
%mvn_alias com.sun.mail:mailapi \
    javax.mail:mailapi
%mvn_alias com.sun.mail:jakarta.mail \
    com.sun.mail:javax.mail \
    javax.mail:mail \
    org.eclipse.jetty.orbit:javax.mail.glassfish
%mvn_alias jakarta.mail:jakarta.mail-api \
    javax.mail:javax.mail-api

# add symlinks for compatibilty with old classpaths
%mvn_file com.sun.mail:jakarta.mail \
    %{name}/jakarta.mail \
    javamail/mail \
    javamail/javax.mail \
    javax.mail/javax.mail

%build
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
#
# XXX 2022-01-05 disable tests for now due to issue with DNS resolution caused by glibc change.
# Tests fail with: java.net.UnknownHostException: myhostname: Temporary failure in name resolution
# Simple reproducer: echo 'java.net.InetAddress.getLocalHost();' | jshell -s
# Until glibc-2.34.9000-27.fc36 jakarta-mail tests pass.
# Starting with glibc-2.34.9000-28.fc36 jakarta-mail tests fail.
# Related bugs:
# https://bugzilla.redhat.com/show_bug.cgi?id=2023741
# https://bugzilla.redhat.com/show_bug.cgi?id=2033020
#
# define the variable ${main.basedir} to avoid using directory-maven-plugin
%mvn_build -j -f -- -Dmain.basedir=${PWD}

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
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

