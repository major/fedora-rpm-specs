Name:           fop
Summary:        XSL-driven print formatter
Version:        2.8
Release:        3%{?dist}
# ASL 1.1:
# several files in fop-core/src/main/resources/org/apache/fop/render/awt/viewer/resources
# rest is ASL 2.0
License:        ASL 2.0 and ASL 1.1
URL:            https://xmlgraphics.apache.org/fop
Source0:        https://www.apache.org/dist/xmlgraphics/%{name}/source/%{name}-%{version}-src.tar.gz
Source1:        %{name}.script
Source2:        batik-pdf-MANIFEST.MF
Source4:        https://www.apache.org/licenses/LICENSE-1.1.txt
Patch1:		0001-Main.patch
Patch2:		0002-Use-sRGB.icc-color-profile-from-colord-package.patch
Patch3:         0003-Port-to-QDox-2.0.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Requires:       java
Requires:       xalan-j2 >= 2.7.0
Requires:       xml-commons-apis >= 1.3.04
# Explicit requires for javapackages-tools since fop script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-logging
BuildRequires:  batik
BuildRequires:  fontbox
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-local
BuildRequires:  maven-plugin-build-helper
BuildRequires:  mvn(javax.servlet:servlet-api)
# For servlet, not packaged
#BuildRequires:  maven-war-plugin
BuildRequires:  pdfbox
BuildRequires:  qdox
BuildRequires:  xml-maven-plugin
BuildRequires:  xmlgraphics-commons >= 2.8
BuildRequires:  xmlunit
BuildRequires:  xmlunit-assertj
BuildRequires:  xmlunit-core

%description
FOP is the world's first print formatter driven by XSL formatting
objects. It is a Java application that reads a formatting object tree
and then turns it into a PDF document. The formatting object tree, can
be in the form of an XML document (output by an XSLT engine like XT or
Xalan) or can be passed in memory as a DOM Document or (in the case of
XT) SAX events.

%package javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}.

%prep
%autosetup -p1

cp %{SOURCE4} LICENSE-1.1

rm -f fop/lib/*.jar fop/lib/build/*.jar

# Not packaged
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_dep javax.media:jai-core fop-core
%pom_remove_dep com.sun.media:jai-codec fop-core
%pom_remove_dep net.sf.offo:fop-hyph fop-core
%pom_remove_dep net.sf.saxon:saxon fop-core
# Update to current xmlunit
%pom_change_dep xmlunit:xmlunit org.xmlunit:xmlunit-core fop-core
%pom_add_dep org.xmlunit:xmlunit-assertj3 fop-core
# Requires maven-war-plugin
%pom_disable_module fop-servlet
# Requires JAI, not packaged
rm fop-core/src/main/java/org/apache/fop/util/bitmap/JAIMonochromeBitmapConverter.java


%build
# Skip tests for now, make dirs needed by build but created by tests
mkdir -p fop-events/target/test-classes
%mvn_build -f


%install
%mvn_install
# inject OSGi manifest
jar ufm %{buildroot}%{_javadir}/%{name}/%{name}.jar %{SOURCE2}

# script
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/fop

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf
cp -rp fop/conf/* %{buildroot}%{_datadir}/%{name}/conf

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/xmvn-apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files -f .mfiles
%doc LICENSE LICENSE-1.1 README NOTICE
%{_datadir}/%{name}
%{_bindir}/fop

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE LICENSE-1.1


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.8-2
- Build from cleaned up tarball

* Wed Nov 16 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.8-1
- Update to 2.8

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.7-3
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.7-2
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 27 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.7-1
- Update to 2.7

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Mat Booth <mat.booth@gmail.com> - 2.6-3
- Remove unnecessary BR on servlet

* Thu Aug 26 2021 Peter Lemenkov <lemenkov@gmail.com> - 2.6-2
- Restore two patches

* Wed Aug 25 2021 Orion Poplawski <orion@nwra.com> - 2.6-1
- Update to 2.6, build with maven

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.5-1
- Ver. 2.5

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.4-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Feb 21 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.4-1
- Ver. 2.4
- No nonger requires avalon framework

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 2.2-3
- Add explicit javapackages-tools requirement since fop script
  uses java-functions. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.2-1
- Ver. 2.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-8
- Elimitate race condition when injecting JAR manifest
- Resolves: rhbz#1495235

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-7
- Add fontbox to classpath
- Resolves: rhbz#1413340

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Michael Simacek <msimacek@redhat.com> - 2.0-4
- Fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Michael Simacek <msimacek@redhat.com> - 2.0-2
- Add fix for FOP-2461 (rhbz#1251173)

* Tue Jul 14 2015 Michael Simacek <msimacek@redhat.com> - 2.0-1
- Update to upstream version 2.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-10
- Disable javadoc doclint

* Tue Mar 17 2015 Michael Simacek <msimacek@redhat.com> - 1.1-9
- Port to current QDox and xmlgraphics-commons

* Mon Jun 16 2014 Michal Srb <msrb@redhat.com> - 1.1-8
- Fix FTBFS

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 2 2014 Richard Hughes <rhughes@redhat.com> 1.1-6
- Drop the icc-profiles-openicc requirement and switch to using the colord sRGB
  profile filename.
- Resolves: #1042655

* Thu Nov 7 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1-5
- Fix the OSGi manifest.

* Wed Sep 18 2013 Michal Srb <msrb@redhat.com> - 1.1-4
- Fix license tag (Resolves: rhbz#979394)
- Add ASL 1.1 license text

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Michal Srb <msrb@redhat.com> - 1.1-2
- Build from clean tarball
- Spec file clean up

* Fri Apr 12 2013 Michal Srb <msrb@redhat.com> - 1.1-1
- Update to upstream version 1.1
- Replace proprietary color profile with free CP from icc-profiles-openicc package
- Resolves: rhbz#848659

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-20
- Add xml-commons-apis-ext to classpath

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-16
- Supply missing event-model.xml files

* Fri Jun 3 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-15
- Split avalon-framework into avalon-framework-api and avalon-framework-impl in classpath

* Thu Mar 10 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-14
- Reapply Fedora guidelines.
- Re-add pom.xml to unbreak Maven stack.
- Re-add OSGi manifest to unbreak Eclipse stack.
- Remove all bundled jars and classes and fix the build to work with our libs.

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-13
- reinstate updated manifest patch
- change define to global

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-12
- buildarch: noarch

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-11
- drop obsolete manifest patch

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-10
- import 1.0 into Fedora, based on Mandriva package

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 4 2011 Rüdiger Landmann <r.landmann@redhat.com> - 1.0-8
- BR qdox

* Tue Jan 4 2011 Rüdiger Landmann <r.landmann@redhat.com> - 1.0-7
- set BR on xmlgraphics-commons >= 1.4
- Add qdox classpath

* Thu Dec 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-0.0.3mdv2011.0
- Revision: 617684
- Resubmit after moving

* Fri Dec 3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-6
- Add LICENSE to javadoc sub-package
- Few other tweaks according to new guidelines
- Make jars and javadoc versionless
- Add pom file (Resolves rhbz#655804)

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-5
- We need servlet not jsp.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-4
- BR jsp.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-3
- Add more BRs.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-2
- BR ant-nodeps.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-1
- Update to 1.0.
- BR/R java 1.6.0 not openjdk (rhbz#620330).
- Remove jars in prep.

* Sat Sep 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.0.2mdv2011.0
- Revision: 576002
- rebuild for new xmlgraphics-commons

* Sun Aug 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.0.1mdv2011.0
- Revision: 574030
- update to new version 1.0
- disable patch 1
- disable gcj support

* Thu Apr 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.95-0.0.3mdv2010.1
- Revision: 540954
- rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.95-0.0.2mdv2010.0
- Revision: 437573
- rebuild

* Wed Dec 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.95-0.0.1mdv2009.1
- Revision: 315376
- update to new version 0.95
- drop patch0, not needed anymore
- spec file clean
- drop useles buildrequires
- use %%java_home

* Sat Dec 29 2007 David Walluck <walluck@mandriva.org> 0.94-0.2.1mdv2008.1
- Revision: 139372
- spec cleanup
- import fop


* Fri Dec  7 2007 Lillian Angel <langel at redhat.com> - 0.94-2
- Updated Release.

* Thu Dec  6 2007 Lillian Angel <langel at redhat.com> - 0.94-1
- Removed ppc/64 conditions since IcedTea is now available for ppc/64.

* Tue Nov 27 2007 Lillian Angel <langel at redhat.com> - 0.94-1
- Fixed to build with gcj on ppc/64.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0.94-1
- Fixed rpmlint errors.

* Tue Sep 18 2007 Joshua Sumali <jsumali at redhat.com> - 0:0.94-1
- Update to fop 0.94

* Thu Mar 30 2006 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-9jpp
- First build for JPP-1.7
- Replace avalon-framework, avalon-logkit with their new excalibur-*
  counterparts
- Drop non-free jimi and jai BRs

* Tue Oct 11 2005 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-8jpp
- Patch to Batik >= 1.5.1

* Fri Oct 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-7jpp
- Omit ant -d flag

* Mon Aug 23 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-6jpp
- Build with ant-1.6.2

* Fri Aug 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-5jpp
- Void change

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:0.20.5-4jpp
- Upgrade to Ant 1.6.X

* Thu Jan  8 2004 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-3jpp
- BuildRequires ant-optional.
- Crosslink with full J2SE javadocs instead of just JAXP/XML-commons.
- Add Main-Class back to manifest.

* Tue Sep 23 2003 Paul Nasrat <pauln at truemesh.com> - 0:0.20.5-2jpp
- Fix script and requires
- Remove class path in manifest
- New javadoc style

* Sat Jul 19 2003 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-1jpp
- Update to 0.20.5.
- Crosslink with xml-commons-apis and batik javadocs.
- BuildRequires jai, jce and jimi.

* Sat Jun  7 2003 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-0.rc3a.1jpp
- Update to 0.20.5rc3a.
- Include fop script.
- Non-versioned javadoc symlinks.

* Thu Apr 17 2003 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-0.rc2.1jpp
- Update to 0.20.5rc2 and JPackage 1.5.

* Sun Mar 10 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 0.20.3-1jpp
- 0.20.3 final
- fixed missing symlink

* Mon Jan 21 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 0.20.3-0.rc.1jpp
- 0.20.3rc
- first unified release
- javadoc into javadoc package
- no dependencies for manual package
- s/jPackage/JPackage
- adaptation to new xalan-j2 package
- requires and buildrequires avalon-logkit

* Thu Aug 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 0.20.1-1mdk
- first release
