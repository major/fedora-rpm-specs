%bcond_without  portlet

Name:           apache-commons-fileupload
Version:        1.4
Release:        12%{?dist}
Summary:        API to work with HTML file upload
License:        ASL 2.0
URL:            http://commons.apache.org/fileupload/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://archive.apache.org/dist/commons/fileupload/source/commons-fileupload-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
%if %{with portlet}
BuildRequires:  mvn(javax.portlet:portlet-api)
%endif

%description
The javax.servlet package lacks support for RFC-1867, HTML file
upload.  This package provides a simple to use API for working with
such data.  The scope of this package is to create a package of Java
utility classes to read multipart/form-data within a
javax.servlet.http.HttpServletRequest.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n commons-fileupload-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' NOTICE.txt

%if %{with portlet}
# fix gId
sed -i "s|<groupId>portlet-api</groupId>|<groupId>javax.portlet</groupId>|" pom.xml
%else
%pom_remove_dep portlet-api:portlet-api
%pom_xpath_remove pom:properties/pom:commons.osgi.import
%pom_xpath_remove pom:properties/pom:commons.osgi.dynamicImport
rm -r src/main/java/org/apache/commons/fileupload/portlet
%endif

# -----------------------------------------------------------------------------

%mvn_file ":{*}" @1 %{name}
%mvn_alias : org.apache.commons:

%build
# tests fail to compile because they use an obsolete version of servlet API (2.4)
%mvn_build -f -- -Dcommons.osgi.symbolicName=org.apache.commons.fileupload

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

# -----------------------------------------------------------------------------

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.4-10
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4-9
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.4-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Mat Booth <mat.booth@redhat.com> - 1.4-1
- Update to latest upstream release
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Michael Simacek <msimacek@redhat.com> - 1.3.3-1
- Update to upstream version 1.3.3

* Wed Mar 15 2017 Michael Simacek <msimacek@redhat.com> - 1.3.2-3
- Convert conditional

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 1.3.2-2
- Remove unused BR release-plugin

* Wed Jun 01 2016 Michael Simacek <msimacek@redhat.com> - 1.3.2-1
- Update to upstream version 1.3.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  8 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-6
- Update to current packaging guidelines

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-3
- Use .mfiles generated during build

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.1-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Feb 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-1
- Update to upstream version 1.3.1
- Remove unused patched

* Thu Feb  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-5
- Add backported upstream patch to fix DoS vulnerability
- Resolves: CVE-2014-0050

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3
- Remove unneeded BR: maven-idea-plugin

* Thu Apr 18 2013 Severin Gehwolf <sgehwolf@redhat.com> 1.3-2
- Use pom macros over patch.
- Remove surefire maven plugin since tests are skipped anyway.

* Thu Mar 28 2013 Michal Srb <msrb@redhat.com> - 1.3-1
- Update to upstream version 1.3

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.2-11
- Disable tests (they use obsolete servlet API 2.4)
- Resolves: rhbz#913878

* Thu Feb 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.2-10
- Add missing BR: maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.2.2-8
- Conditionally build portlet-2.0-api support in Fedora only

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.2-6
- Fix up patches to apply, cleanup spec old coments
- Fix surefire plugin dependency to use new name

* Tue May 29 2012 gil cattaneo <puntogil@libero.it> 1.2.2-5
- Add portlet-2.0-api support (required by springframework).

* Fri Mar  2 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> 1.2.2-4
- Fix build and update to latest guidelines

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Chris Spike <chris.spike@arcor.de> 1.2.2-1
- Updated to 1.2.2
- Fixed License tag
- tomcat5 -> tomcat6 BRs/Rs
- Fixed wrong EOL encodings

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.1-4
- Add license to javadoc subpackage

* Thu May 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.1-3
- Added Requires on jpackage-utils for javadoc

* Thu May 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.1-2
- Rename package (jakarta-commons-fileupload->apache-commons-fileupload)
- Re-did whole spec file

* Wed Jan  6 2010 Mary Ellen Foster <mefoster at gmail.com> - 1:1.2.1-1
- Update to newest version; include Maven metadata

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.0-7.3
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.0-7jpp.2
- Autorebuild for GCC 4.3

* Tue Apr 17 2007 Permaine Cheung <pcheung@redhat.com> - 1:1.0-6jpp.2
- Update spec file as per fedora review

* Thu Aug 10 2006 Deepak Bhole <dbhole@redhat.com> - 1:1.0-6jpp.1
- Added missing requirements.

* Thu Aug 10 2006 Karsten Hopp <karsten@redhat.de> 1.0-5jpp_3fc
- Requires(post/postun): coreutils

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 1:1.0-5jpp_2fc
- Rebuilt

* Thu Jul 20 2006 Deepak Bhole <dbhole@redhat.com> - 1:1.0-5jpp_1fc
- Added conditional native compilation.

* Wed Apr 26 2006 Fernando Nasser <fnasser@redhat.com> - 1:1.0-4jpp
- First JPP 1.7 build

* Fri Oct 22 2004 Fernando Nasser <fnasser@redhat.com> - 1:1.0-3jpp
- Patch to build with servletapi5
- Add missing dependency on ant-junit

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 1:1.0-2jpp
- Rebuild with ant-1.6.2

* Sat Jun 28 2003 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-1jpp
- Update to 1.0.
- Add Epochs to dependencies.
- Nuke beanutils dependency.
- Versionless javadoc dir symlinks.

* Tue Mar 25 2003 Nicolas Mailhot <Nicolas.Mailhot (at) JPackage.org> - 1:1.0-0.beta1.4jpp
- for jpackage-utils 1.5

* Mon Mar 10 2003 Henri Gomez <hgomez@users.sourceforge.net> - 1:1.0-0.beta1.3jpp
- rebuild with correct ant (avoid corrupted archive)

* Fri Mar 07 2003 Henri Gomez <hgomez@users.sourceforge.net> - 1:1.0-0.beta1.2jpp
- replace servlet23 requirement by servlet4api

* Wed Feb 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-0.beta1.1jpp
- Update to 1.0 beta 1 (no code changes from cvs20030115).
- Fix requirements.

* Wed Jan 15 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.0-1jpp
- 1.0 (cvs 20030115)
- first jPackage release
