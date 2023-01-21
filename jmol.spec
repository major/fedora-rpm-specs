Name:           jmol
Version:        14.32.83
Release:        2%{?dist}
Summary:        Java viewer for chemical structures in 3D

# JSpecView, JMol, and Sparsh-UI are all LGPL-2.0-or-later.
# src/javajs/img/GifEncoder.java is BSD-2-Clause.
# src/javajs/img/PpmEncoder.java is BSD-2-Clause.
# src/javajs/img/JpgEncoder.java and src/javajs/img/Jpg64Encoder.java are IJG.
# src/javajs/util/BS.java is GPL-2.0-only with the classpath exception.
# The icon is CC0-1.0.
# The Nuvola icons are GPL-2.0-only.
License:        LGPL-2.0-or-later AND BSD-2-Clause AND IJG AND GPL-2.0-only WITH Classpath-exception-2.0 AND CC0-1.0 AND GPL-2.0-only
URL:            http://www.jmol.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        http://downloads.sourceforge.net/%{name}/Jmol-%{version}-full.tar.gz
Source1:        http://biomodel.uah.es/Jmol/logos/Jmol_icon13.svg
Source2:        org.jmol.jmol.desktop
Source3:        org.jmol.jmol.metainfo.xml
# Fedora-specific patch to the ant build rules
Patch0:         %{name}-build.patch
# Use xsltproc instead of saxon
Patch1:         %{name}-xslt.patch
# Fix code that is invalid with JDK 9+
Patch2:         %{name}-java9.patch
# Fix javadoc errors
Patch3:         %{name}-javadoc.patch
# Avoid deprecated interfaces
Patch4:         %{name}-deprecated.patch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  apache-commons-cli
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jni-inchi
BuildRequires:  junit
BuildRequires:  libxslt
BuildRequires:  naga
BuildRequires:  web-assets-devel

Requires:       apache-commons-cli
Requires:       hicolor-icon-theme
Requires:       java
Requires:       javapackages-filesystem
Requires:       javapackages-tools
Requires:       jni-inchi
Requires:       naga

# The upstreams for JSpecView and JMol are the same.  The JSpecView site appears
# to have been abandoned.  Development of JSpecView has continued in the JMol
# source tree.  Note that JSpecView is now bundled in JMol.
Provides:       bundled(jspecview)

# A modified version of Sparsh-UI is bundled
Provides:       bundled(sparshui)

# Icons from Nuvola are included, but at different sizes than Fedora provides
Provides:       bundled(nuvola-icon-theme)

%description
Jmol is a free, open source molecule viewer for students, educators,
and researchers in chemistry and biochemistry.

%package -n jsmol
Summary:        JavaScript-Based Molecular Viewer From Jmol
License:        LGPLv2+
Requires:       web-assets-filesystem

Recommends:     js-jquery1

%description -n jsmol
JSmol is the extension of the Java-based molecular visualization
applet Jmol (jmol.sourceforge.net) as an HTML5 JavaScript-only
web app. It can be used in conjunction with the Java applet to
provide an alternative to Java when the platform does not support
that (iPhone/iPad) or does not support applets (Android). Used in
conjunction with the Jmol JavaScript Object
(http://wiki.jmol.org/index.php/Jmol_Javascript_Object ), JSmol
seamlessly offers alternatives to Java on these non-Applet platforms.

JSmol can read all the files that Jmol reads. You can do all the
scripting that Jmol does. You can create all the buttons and links
and such that you are used to creating for Jmol. All of the rendering
capability of the Jmol applet is there. JSmol has both a console and
a popup menu.

JSmol is integrated fully with JSME and JSpecView.

A "lite" version of JSmol provides minimal functionality
(balls and sticks only) for extremely small-bandwidth apps.

%package javadoc
Summary:        Java docs for %{name}
Requires:       javapackages-tools

%description javadoc
This package contains the API documentation for %{name}.

%package doc
Summary:     Documentation for %{name}

%description doc
The documentation for %{name}.

%prep
%autosetup -p0

# Remove binaries
find . \( -name \*.exe -o -name \*.jar -o -name \*.dll \) -delete
rm doc/*.zip

# Link the system jars
build-jar-repository -p -s jars commons-cli junit naga-3_0
ln -s %{_jnidir}/jni-inchi/jni-inchi.jar jars

# Fix EOL encoding
for doc in COPYRIGHT.txt LICENSE.txt README.txt; do
  sed -i.orig "s|\r||g" $doc
  touch -r $doc.orig $doc
  rm $doc.orig
done

# Fix character encoding
iconv -f ISO8859-1 -t UTF-8 CHANGES.txt > CHANGES.txt.utf8
touch -r CHANGES.txt CHANGES.txt.utf8
mv CHANGES.txt.utf8 CHANGES.txt

# Set the version without ant-contrib
sed -i 's,@version@,%{version},' build.xml

%build
export ANT_OPTS="-Dfile.encoding=utf-8"
export JAVAC=%{_bindir}/javac
ant jar doc

%install
# Install the JARs
mkdir -p %{buildroot}%{_javadir}/%{name}
install -D -p -m 644 build/{Jmol{,Data},Jvxl}.jar \
        %{buildroot}%{_javadir}/%{name}

# Install wrapper script
%jpackage_script org.openscience.jmol.app.Jmol "" "" naga:commons-cli:jni-inchi/jni-inchi:jmol/Jmol %{name} 1

# Install the icon
install -D -p -m 644 %{SOURCE1} \
        %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

# Install the metainfo file
mkdir -p %{buildroot}%{_metainfodir}
cp -p %{SOURCE3} %{buildroot}%{_metainfodir}
appstreamcli validate --no-net \
  %{buildroot}%{_metainfodir}/org.jmol.jmol.metainfo.xml

# Javadoc files
mkdir -p %{buildroot}%{_javadocdir}
cp -a build/doc %{buildroot}%{_javadocdir}/%{name}

# Install the parts of jsmol needed by sagemath
mkdir -p %{buildroot}%{_jsdir}/jsmol
cd appletweb
unzip jsmol.zip
cd jsmol
sed -i.orig "s|\r||g" README.TXT
touch -r README.TXT.orig README.TXT
cp -p JSmol*js %{buildroot}%{_jsdir}/jsmol
cp -a idioma j2s %{buildroot}%{_jsdir}/jsmol
cd ../..

%files
%doc README.txt ChangeLog.html CHANGES.txt
%license COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}
%{_javadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/org.jmol.jmol.desktop
%{_metainfodir}/org.jmol.jmol.metainfo.xml

%files -n jsmol
%doc appletweb/jsmol/README.TXT
%license COPYRIGHT.txt LICENSE.txt
%{_jsdir}/jsmol/

%files javadoc
%license COPYRIGHT.txt LICENSE.txt
%{_javadocdir}/%{name}/

%files doc
%doc %lang(en) build/doc/JmolAppletGuide.html
%doc %lang(en) build/doc/JmolDevelopersGuide.html
%doc %lang(en) build/doc/JmolHistory/ChangeLog.html
%doc %lang(en) build/doc/JmolUserGuide/
%doc %lang(de) build/doc/JmolAppletGuide_de.html
%doc %lang(de) build/doc/JmolDevelopersGuide_de.html
%doc %lang(de) build/doc/JmolUserGuide_de/
%doc %lang(fr) build/doc/JmolAppletGuide_fr.html
%doc %lang(fr) build/doc/JmolDevelopersGuide_fr.html
%doc %lang(fr) build/doc/JmolHistory/ChangeLog_fr.html
%doc %lang(fr) build/doc/JmolUserGuide_fr/
%doc %lang(nl) build/doc/JmolHistory/ChangeLog_nl.html
%doc %lang(ro) build/doc/JmolHistory/ChangeLog_ro.html
%license COPYRIGHT.txt LICENSE.txt

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.32.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Jerry James <loganjerry@gmail.com> - 14.32.83-1
- Version 14.32.83

* Fri Nov 25 2022 Jerry James <loganjerry@gmail.com> - 14.32.81-1
- Version 14.32.81
- Drop -lock patch

* Thu Oct 13 2022 Jerry James <loganjerry@gmail.com> - 14.32.77-1
- Version 14.32.77

* Thu Sep  8 2022 Jerry James <loganjerry@gmail.com> - 14.32.74-1
- Version 14.32.74
- Convert License tag to SPDX

* Sat Aug  6 2022 Jerry James <loganjerry@gmail.com> - 14.32.68-1
- Version 14.32.68

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.32.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 14.32.62-2
- Rebuilt for Drop i686 JDKs

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 14.32.62-1
- Version 14.32.62
- Add -lock patch to fix sagemath build hangs

* Thu Jun 30 2022 Jerry James <loganjerry@gmail.com> - 14.32.61-1
- Version 14.32.61

* Tue Apr 12 2022 Jerry James <loganjerry@gmail.com> - 14.32.47-1
- Version 14.32.47

* Tue Apr  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 14.32.22-2
- Rebuild with fixed msgfmt (in gettext) (bug 2062407)

* Wed Feb 16 2022 Jerry James <loganjerry@gmail.com> - 14.32.22-1
- Version 14.32.22

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 14.32.16-2
- Rebuilt for java-17-openjdk as system jdk

* Mon Jan 24 2022 Jerry James <loganjerry@gmail.com> - 14.32.16-1
- Version 14.32.16
- The applet code has been removed, so we can build with JDK 17

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.32.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Jerry James <loganjerry@gmail.com> - 14.32.6-1
- Version 14.32.6

* Mon Nov 29 2021 Jerry James <loganjerry@gmail.com> - 14.31.63-1
- Version 14.31.63
- Explicitly build with JDK 11 until the applet code can be removed

* Thu Nov 11 2021 Jerry James <loganjerry@gmail.com> - 14.31.61-1
- Version 14.31.61

* Thu Oct 21 2021 Jerry James <loganjerry@gmail.com> - 14.31.59-1
- Version 14.31.59

* Mon Oct 11 2021 Jerry James <loganjerry@gmail.com> - 14.31.57-1
- Version 14.31.57

* Thu Sep 16 2021 Jerry James <loganjerry@gmail.com> - 14.31.54-1
- Version 14.31.54

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 14.31.52-1
- Version 14.31.52

* Thu Aug 12 2021 Jerry James <loganjerry@gmail.com> - 14.31.51-1
- Version 14.31.51

* Mon Jul 26 2021 Jerry James <loganjerry@gmail.com> - 14.31.47-1
- Version 14.31.47
- Drop the ant-contrib dependency

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.31.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Jerry James <loganjerry@gmail.com> - 14.31.44-1
- Version 14.31.44
- Add a metainfo file

* Fri Jun 25 2021 Jerry James <loganjerry@gmail.com> - 14.31.42-1
- Version 14.31.42

* Tue Jun  1 2021 Jerry James <loganjerry@gmail.com> - 14.31.41-1
- Version 14.31.41

* Sat May  8 2021 Jerry James <loganjerry@gmail.com> - 14.31.38-1
- Version 14.31.38

* Thu Apr  1 2021 Jerry James <loganjerry@gmail.com> - 14.31.35-1
- Version 14.31.35

* Wed Mar 17 2021 Jerry James <loganjerry@gmail.com> - 14.31.34-1
- Version 14.31.34

* Mon Feb 22 2021 Jerry James <loganjerry@gmail.com> - 14.31.31-1
- Version 14.31.31

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.31.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Jerry James <loganjerry@gmail.com> - 14.31.18-1
- Version 14.31.18

* Sun Oct 25 2020 Jerry James <loganjerry@gmail.com> - 14.31.12-1
- Version 14.31.12

* Tue Sep 29 2020 Jerry James <loganjerry@gmail.com> - 14.31.8-1
- Bring back to Fedora

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.6.0-8.2016.06.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.6.0-7.2016.06.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.6.0-6.2016.06.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.6.0-5.2016.06.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.6.0-4.2016.06.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.6.0-3.2016.06.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.6.0-3.2016.06.30
- Fix FTBFS in rawhide.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.6.0-2.2016.06.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.6.0-1.2016.06.30
- Update to 14.6.0 snapshot 2016.06.30.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.4.0-2.2015.10.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.4.0-1.2015.10.13
- Update to 14.4.0 snapshot 2015.10.13.

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.2.15-1.2015.07.09
- Update to 14.2.15 snapshot 2015.07.09.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.2.12-3.2015.01.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 07 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 14.2.12-2.2015.01.22
- Create jsmol subpackage (#1190356)

* Mon Feb 02 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.2.12-1.2015.01.22
- Update to 14.2.12 snapshot 2015.01.22.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.0.13-2
- Don't bundle external libraries (BZ #1095315).

* Thu Apr 03 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.0.13-1
- Need full java because this is a GUI application.
- Update to 14.0.13.

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 14.0.11-2
- Use Requires: java-headless rebuild (#1067528)

* Thu Mar 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.0.11-1
- Update to 14.0.11.

* Wed Feb 12 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.0.7-1
- Added missing Requires: jspecview (BZ #1064335).
- Update to 14.0.7.

* Tue Jan 07 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.0.3-1
- Update to 14.0.4.

* Wed Jan 01 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 14.0.3-1
- Update to 14.0.3.
- Updated logo.

* Fri Aug 23 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 13.2.4-1
- Update to 13.2.4.

* Sat Aug 10 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 13.2.3-1
- Update to 13.2.3.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 13.0.15-1
- Update to 13.0.15.

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 12.0.48-10
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.48-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.48-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 12.0.48-7
- Remove exe file in %%prep.

* Mon May  7 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 12.0.48-6
- Add forgotten apache-commons BR/R

* Mon May  7 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 12.0.48-5
- Unbundle bundled libraries
- Fix javadoc encoding build problem
- Start using jpackage_script macro
- Fix up license tag somewhat

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 24 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 12.0.48-3
- Really fix build by not ignoring system classpath (thanks to omajid).

* Wed Aug 17 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 12.0.48-2
- Try to fix build on rawhide and F16 by adding CLASSPATH definition.

* Wed Aug 17 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 12.0.48-1
- Update to 12.0.48.

* Thu Apr 28 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 12.0.41-1
- Update to 12.0.41.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 6 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.26-1
- Update to 11.8.26.

* Sat Jul 24 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.25-1
- Update to 11.8.25.

* Tue May 18 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.24-1
- Update to 11.8.24.

* Sun Apr 25 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.23-1
- Update to 11.8.23.

* Fri Mar 26 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.22-1
- Update to 11.8.22.

* Tue Mar 23 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.21-1
- Update to 11.8.21.

* Thu Mar 11 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.20-1
- Update to 11.8.20.

* Fri Mar 05 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.19-1
- Update to 11.8.19.

* Sat Feb 06 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.18-1
- Update to 11.8.18.

* Sat Jan 16 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.17-1
- Update to 11.8.17.

* Thu Jan 14 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.16-1
- Update to 11.8.16.

* Tue Jan 05 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.15-1
- Update to 11.8.15.

* Wed Dec 23 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8.14-1
- Build from stable release tarballs works now, switch to using stable
releases.
- Update to 11.8.14.

* Fri Oct 02 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8-1.11581
- Switch back to tar.bz2 source since xz doesn't work in EL-5.
- Update to svn revision 11581.

* Tue Sep 22 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.8-1.11564
- Update to 11.8 series, svn revision 11564.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.6-12.11223svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-11.11223svn
- Include desktop file in the spec.

* Thu Jul 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-10.11223svn
- Bump release to be able to rebuild in koji.

* Thu Jul 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-9.11223svn
- Update to svn revision 11223.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.6-8.10506svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-7.10506svn
- Remove jpackage-utils from the Requires of the documentation packages.

* Fri Oct 24 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-6.10137svn
- Fix build on EPEL 5.

* Fri Oct 24 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-5.10137svn
- Disable JAR signing.

* Fri Oct 24 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-4.10137svn
- Add gettext-devel to BR and fix desktop-file-install.

* Thu Oct 23 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-3.10137svn
- Update to svn revision 10137.

* Tue Oct 14 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-2.10081svn
- Review fixes.

* Mon Oct 13 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 11.6-1.10081svn
- First release.
