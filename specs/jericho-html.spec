Summary:       Java library allowing analysis and manipulation of parts of an HTML document
Name:          jericho-html
Version:       3.3
Release:       33%{?dist}
# Automatically converted from old format: EPL-1.0 or LGPLv2+ - review is highly recommended.
License:       EPL-1.0 OR LicenseRef-Callaway-LGPLv2+
URL:           http://jericho.htmlparser.net/
Source0:       http://downloads.sf.net/jerichohtml/%{name}-%{version}.zip
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: javapackages-local
BuildRequires: apache-commons-logging
BuildRequires: log4j
BuildRequires: slf4j
# For tests
BuildRequires: junit
%description
Jericho HTML Parser is a java library allowing analysis and
manipulation of parts of an HTML document, including server-side tags,
while reproducing verbatim any unrecognized or invalid HTML. It also
provides high-level HTML form manipulation functions.

It is an open source library released under both the Eclipse Public
License (EPL) and GNU Lesser General Public License (LGPL). You are
therefore free to use it in commercial applications subject to the
terms detailed in either one of these license documents.

%package       javadoc
Summary:       Javadoc for %{name}
%description   javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
find \( -name '*.class' -o -name '*.[jw]ar' \) -delete
find \( -name '*.java' -o -name '*.bat' -o -name '*.txt' -o -name '*.jsp' -o -name '*.css' -o -name '*.xml' \) \
    -exec sed -i 's/\r//' '{}' +

# fix non ASCII chars
for s in src/java/net/htmlparser/jericho/{Renderer,StreamEncodingDetector}.java ; do
    iconv -f WINDOWS-1252 -t UTF-8 ${s} > ${s}.new
    mv ${s}.new ${s}
done

%build
export CLASSPATH=$(build-classpath slf4j/api commons-logging log4j)

%javac -Xlint -g:none -d classes -encoding UTF-8 \
    src/java/net/htmlparser/jericho/*.java \
    src/java/net/htmlparser/jericho/nodoc/*.java
%jar -cf dist/%{name}.jar -C classes .

%javadoc -encoding UTF-8 -classpath classes:$CLASSPATH -quiet -Xdoclint:none \
    -windowtitle "Jericho HTML Parser %version" -use -d docs/javadoc \
    -subpackages net.htmlparser.jericho -exclude net.htmlparser.jericho.nodoc \
    -noqualifier net.htmlparser.jericho -sourcepath src/java -group "Core Package" \
    src/java/net/htmlparser/jericho/*.java \
    src/java/net/htmlparser/jericho/nodoc/*.java

cp -p docs/src/*.* docs/javadoc

%javac -Xlint -g -deprecation -classpath dist/%{name}.jar \
    -d samples/console/classes samples/console/src/*.java

%install
%mvn_file net.htmlparser.jericho:%{name}:%{version} %{name}
%mvn_artifact net.htmlparser.jericho:%{name}:%{version} dist/%{name}.jar
%mvn_install -J docs/javadoc

# Install link for web app
ln -s %{_javadir}/%{name}.jar samples/webapps/JerichoHTML/WEB-INF/lib

%check
mkdir -p test/classes
export CLASSPATH=classes:samples/console/classes:$(build-classpath junit hamcrest)
%javac -Xlint -g -d test/classes test/src/*.java test/src/samples/*.java \
    test/src/net/htmlparser/jericho/*.java
%java -classpath $CLASSPATH:test/classes \
    -Djava.util.logging.config.file=test/logging.properties \
    org.junit.runner.JUnitCore TestSuite

%files -f .mfiles
%license licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt
%doc project-description.txt release.txt
%doc samples

%files javadoc -f .mfiles-javadoc
%license licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.3-30
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.3-24
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.3-23
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Terje Rosten <terje.rosten@ntnu.no> - 3.3-18
- Add patch from Severin Gehwolf to fix JDK 11 build (rhbz#1857991)

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.3-17
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Feb 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 3.3-16
- Minor cleanup

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.3-9
- Have OpenJDK on PPC platforms now

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 gil cattaneo <puntogil@libero.it> 3.3-7
- adapt to current guideline
- switch encoding to utf8
- introduce license macro

* Thu Jun 18 2015 gil cattaneo <puntogil@libero.it> 3.3-6
- fix FTBFS: disable doclint in javadoc

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 3 2015 Orion Poplawski <orion@cora.nwra.com> 3.3-4
- Add hamcrest to classpath for tests

* Sun Jan 25 2015 gil cattaneo <puntogil@libero.it> 3.3-3
- add maven metadata

* Mon Jun 9 2014 Orion Poplawski <orion@cora.nwra.com> - 3.3-2
- Use BR junit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Orion Poplawski <orion@cora.nwra.com> - 3.3-1
- Update to 3.3
- Require java-headless (bug #1068266)

* Tue Oct 22 2013 Orion Poplawski <orion@cora.nwra.com> - 3.2-7
- Remove versioned jars (bug #1022118)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 21 2011 Orion Poplawski <orion@cora.nwra.com> - 3.2-2
- Specify Windows-1252 encoding
- Add src/java/net/htmlparser/jericho/nodoc/ to javadoc path

* Thu Apr 21 2011 Orion Poplawski <orion@cora.nwra.com> - 3.2-1
- Update to 3.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Orion Poplawski <orion@cora.nwra.com> - 3.1-5
- ExcludeArch ppc64 - no java >= 1:1.6.0 on ppc64

* Fri Jul 30 2010 Orion Poplawski <orion@cora.nwra.com> - 3.1-4
- Add licenses to javadoc file

* Mon Jun 28 2010 Orion Poplawski <orion@cora.nwra.com> - 3.1-3
- Fix Groups again
- Link to jar in sample webapp

* Fri Jun 25 2010 Orion Poplawski <orion@cora.nwra.com> - 3.1-2
- Fix spelling errors
- Change package groups
- Fix Requires and BuildRequires
- Fix Summary
- Don't need to copy library for tests

* Mon Oct 5 2009 Orion Poplawski <orion@cora.nwra.com> - 3.1-1
- Initial Fedora Package
