Name:           apache-commons-net
Version:        3.8.0
Release:        3%{?dist}
Summary:        Internet protocol suite Java library
License:        ASL 2.0
URL:            http://commons.apache.org/net/
Source0:        http://archive.apache.org/dist/commons/net/source/commons-net-%{version}-src.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%package javadoc
Summary:    API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n commons-net-%{version}-src

# This test fails with "Connection timed out"
rm src/test/java/org/apache/commons/net/time/TimeTCPClientTest.java
# Fails in Koji with "Address already in use"
rm src/test/java/org/apache/commons/net/tftp/TFTPServerPathTest.java

%pom_remove_plugin :exec-maven-plugin

%pom_remove_dep org.apache.ftpserver:ftpserver-core
rm src/test/java/org/apache/commons/net/ftp/FTPSClientTest.java

%mvn_file  : commons-net %{name}
%mvn_alias : org.apache.commons:commons-net

%build
%mvn_build -- -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7 -Dcommons.osgi.symbolicName=org.apache.commons.net

%install
%mvn_install

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 07 2022 Marian Koncek <mkoncek@redhat.com> - 3.8.0-1
- Update to upstream version 3.8.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.6-16
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.6-14
- Set explicit Java compiler source/target levels to 1.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.6-12
- Remove build-dependency on exec-maven-plugin

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.6-6
- Remove build-dependency on exec-maven-plugin

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.6-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.6-5
- Mass rebuild for javapackages-tools 201902

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.6-4
- Mass rebuild for javapackages-tools 201901

* Thu Feb 07 2019 Mat Booth <mat.booth@redhat.com> - 3.6-6
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Michael Simacek <msimacek@redhat.com> - 3.6-1
- Update to upstream version 3.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May  5 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5-1
- Update to upstream version 3.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4-2
- Add workaround for suprious test failure (NET-586)

* Fri Nov 27 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4-1
- Update to upstream version 3.4

* Tue Aug 04 2015 Michael Simacek <msimacek@redhat.com> - 3.3-7
- Disable failing test

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3-5
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.3-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3-1
- Update to upstream version 3.3

* Wed Jun 05 2013 Michal Srb <msrb@redhat.com> - 3.2-5
- Enable tests
- Install README, RELEASE-NOTES.txt files
- Fix BR

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 3.2-2
- Build with xmvn

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-1
- Update to upstream version 3.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-1
- Update to upstream 3.1
- Remove RPM bug workaround
- Remove BR on maven-changes-plugin

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-3
- Use maven 3 to build
- Packaging fixes according to latest guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-1
- Replace maven plugins with apache-commons-parent for BR
- Versionless jars and javadocs
- Rebase to latest upstream version

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-6
- Add license to javadoc subpackage

* Thu May 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-5
- Fix maven depmap JPP name to short_name

* Wed May 19 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-4
- Ignore test failure

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-3
- Rename jakarta-commons-net to apache-commons-net and drop EPOCH
- Build with maven
- Clean up whole spec

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.0-2
- Set maven.repo.local.

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.0-1
- Update to upstream 2.0.
