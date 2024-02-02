Summary:        High-performance, full-featured text search engine
Name:           lucene
Version:        9.9.2
Release:        1%{?dist}
Epoch:          0
# License breakdown is present in NOTICE.txt file
License:        ASL 2.0 and MIT and BSD
URL:            https://lucene.apache.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://dlcdn.apache.org/lucene/java/%{version}/lucene-%{version}-src.tgz
Source1:        aggregator.pom
Source2:        aggregator-analysis.pom

Source3:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-common/%{version}/lucene-analysis-common-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-icu/%{version}/lucene-analysis-icu-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-kuromoji/%{version}/lucene-analysis-kuromoji-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-morfologik/%{version}/lucene-analysis-morfologik-%{version}.pom
Source7:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-nori/%{version}/lucene-analysis-nori-%{version}.pom
Source8:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-opennlp/%{version}/lucene-analysis-opennlp-%{version}.pom
Source9:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-phonetic/%{version}/lucene-analysis-phonetic-%{version}.pom
Source10:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-smartcn/%{version}/lucene-analysis-smartcn-%{version}.pom
Source11:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-stempel/%{version}/lucene-analysis-stempel-%{version}.pom

Source12:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-backward-codecs/%{version}/lucene-backward-codecs-%{version}.pom
Source13:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-benchmark/%{version}/lucene-benchmark-%{version}.pom
Source14:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-classification/%{version}/lucene-classification-%{version}.pom
Source15:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-codecs/%{version}/lucene-codecs-%{version}.pom
Source16:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-core/%{version}/lucene-core-%{version}.pom
Source17:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-demo/%{version}/lucene-demo-%{version}.pom
Source18:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-expressions/%{version}/lucene-expressions-%{version}.pom
Source19:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-facet/%{version}/lucene-facet-%{version}.pom
Source20:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-grouping/%{version}/lucene-grouping-%{version}.pom
Source21:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-highlighter/%{version}/lucene-highlighter-%{version}.pom
Source22:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-join/%{version}/lucene-join-%{version}.pom
Source23:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-luke/%{version}/lucene-luke-%{version}.pom
Source24:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-memory/%{version}/lucene-memory-%{version}.pom
Source25:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-misc/%{version}/lucene-misc-%{version}.pom
Source26:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-monitor/%{version}/lucene-monitor-%{version}.pom
Source27:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-queries/%{version}/lucene-queries-%{version}.pom
Source28:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/%{version}/lucene-queryparser-%{version}.pom
Source29:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-replicator/%{version}/lucene-replicator-%{version}.pom
Source30:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-sandbox/%{version}/lucene-sandbox-%{version}.pom
Source31:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial3d/%{version}/lucene-spatial3d-%{version}.pom
Source32:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-suggest/%{version}/lucene-suggest-%{version}.pom
Source33:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-test-framework/%{version}/lucene-test-framework-%{version}.pom

Patch1:         0001-Use-antlr4-automatic-module-name.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)

BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)

Obsoletes:      %{name}-parent < 9
Obsoletes:      %{name}-solr-grandparent < 9

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package javadoc
Summary:        Javadoc for Lucene

%description javadoc
%{summary}.

%package analysis-common
Summary:        Lucene module: analysis-common
Obsoletes:      %{name}-analysis < 9

%description analysis-common
%{summary}.

%package analysis-icu
Summary:        Lucene module: analysis-icu
Obsoletes:      %{name}-analyzers-icu < 9

%description analysis-icu
%{summary}.

%package analysis-kuromoji
Summary:        Lucene module: analysis-kuromoji
Obsoletes:      %{name}-analyzers-kuromoji < 9

%description analysis-kuromoji
%{summary}.

%package analysis-nori
Summary:        Lucene module: analysis-nori
Obsoletes:      %{name}-analyzers-nori < 9

%description analysis-nori
%{summary}.

%package analysis-phonetic
Summary:        Lucene module: analysis-phonetic
Obsoletes:      %{name}-analyzers-phonetic < 9

%description analysis-phonetic
%{summary}.

%package analysis-smartcn
Summary:        Lucene module: analysis-smartcn
Obsoletes:      %{name}-analyzers-smartcn < 9

%description analysis-smartcn
%{summary}.

%package analysis-stempel
Summary:        Lucene module: analysis-stempel
Obsoletes:      %{name}-analyzers-stempel < 9

%description analysis-stempel
%{summary}.

%package backward-codecs
Summary:        Lucene module: backward-codecs

%description backward-codecs
%{summary}.

%package classification
Summary:        Lucene module: classification

%description classification
%{summary}.

%package codecs
Summary:        Lucene module: codecs

%description codecs
%{summary}.

%package core
Summary:        Lucene module: core
Obsoletes:      %{name} < 9

%description core
%{summary}.

%package expressions
Summary:        Lucene module: expressions

%description expressions
%{summary}.

%package grouping
Summary:        Lucene module: grouping

%description grouping
%{summary}.

%package highlighter
Summary:        Lucene module: highlighter

%description highlighter
%{summary}.

%package join
Summary:        Lucene module: join

%description join
%{summary}.

%package memory
Summary:        Lucene module: memory

%description memory
%{summary}.

%package misc
Summary:        Lucene module: misc

%description misc
%{summary}.

%package monitor
Summary:        Lucene module: monitor

%description monitor
%{summary}.

%package queries
Summary:        Lucene module: queries

%description queries
%{summary}.

%package queryparser
Summary:        Lucene module: queryparser

%description queryparser
%{summary}.

%package sandbox
Summary:        Lucene module: sandbox

%description sandbox
%{summary}.

%package spatial3d
Summary:        Lucene module: spatial3d

%description spatial3d
%{summary}.

%package suggest
Summary:        Lucene module: suggest

%description suggest
%{summary}.

%prep
%setup -q

find -mindepth 1 -maxdepth 1 ! -name lucene ! -name LICENSE.txt ! -name NOTICE.txt ! -name README.md -exec rm -rf {} +
mv -t . lucene/*
rmdir lucene

cp %SOURCE1 pom.xml

function add_pom {
  source=${1}
  prefix=${2}
  module=${source}
  module=${module##*/${prefix}}
  module=${module%%%%-%{version}.pom}
  cp ${source} ${module}/pom.xml
}

for source in $(echo %{sources} | tr ' ' '\n' | grep -v 'lucene-analysis-.*\.pom' | grep 'lucene-.*\.pom'); do
  add_pom ${source} "lucene-"
  %pom_add_parent org.fedoraproject.xmvn.lucene:aggregator:any ${module}
  %pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" "compile" ${module}
done

pushd analysis
cp %SOURCE2 pom.xml
%pom_add_parent org.fedoraproject.xmvn.lucene:aggregator:any

for source in $(echo %{sources} | tr ' ' '\n' | grep 'lucene-analysis-.*\.pom'); do
  add_pom ${source} "lucene-analysis-"
  %pom_add_parent org.fedoraproject.xmvn.lucene:aggregator-analysis:any ${module}
done
popd

%pom_disable_module benchmark
%pom_disable_module demo
%pom_disable_module facet
%pom_disable_module luke
%pom_disable_module replicator
%pom_disable_module test-framework

%pom_disable_module morfologik analysis
%pom_disable_module opennlp analysis

%mvn_package :aggregator __noinstall
%mvn_package :aggregator-analysis __noinstall

%build
# Tests have unpackaged dependencies
%mvn_build -s -f

%install
%mvn_install

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%files analysis-common -f .mfiles-lucene-analysis-common
%files analysis-icu -f .mfiles-lucene-analysis-icu
%files analysis-kuromoji -f .mfiles-lucene-analysis-kuromoji
%files analysis-nori -f .mfiles-lucene-analysis-nori
%files analysis-phonetic -f .mfiles-lucene-analysis-phonetic
%files analysis-smartcn -f .mfiles-lucene-analysis-smartcn
%files analysis-stempel -f .mfiles-lucene-analysis-stempel
%files backward-codecs -f .mfiles-lucene-backward-codecs
%files classification -f .mfiles-lucene-classification
%files codecs -f .mfiles-lucene-codecs

# core is a common dependency of all other modules
%files core -f .mfiles-lucene-core
%license LICENSE.txt NOTICE.txt
%doc README.md

%files expressions -f .mfiles-lucene-expressions
%files grouping -f .mfiles-lucene-grouping
%files highlighter -f .mfiles-lucene-highlighter
%files join -f .mfiles-lucene-join
%files memory -f .mfiles-lucene-memory
%files misc -f .mfiles-lucene-misc
%files monitor -f .mfiles-lucene-monitor
%files queries -f .mfiles-lucene-queries
%files queryparser -f .mfiles-lucene-queryparser
%files sandbox -f .mfiles-lucene-sandbox
%files spatial3d -f .mfiles-lucene-spatial3d
%files suggest -f .mfiles-lucene-suggest

%changelog
* Wed Jan 31 2024 Ding-Yi Chen <dchen@redhat.com> - 0:9.9.2-1
- Update to upstream version 9.9.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:9.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:9.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marian Koncek <mkoncek@redhat.com> - 0:9.9.1-1
- Update to upstream version 9.9.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:9.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 30 2023 Marian Koncek <mkoncek@redhat.com> - 0:9.5.0-1
- Update to upstream version 9.5.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:9.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Marian Koncek <mkoncek@redhat.com> - 0:9.4.0-1
- Update to upstream version 9.4.0

* Wed Oct 19 2022 Marian Koncek <mkoncek@redhat.com> - 0:9.2.0-3
- Do not ship parent poms

* Tue Aug 23 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:9.2.0-2
- Add missing Obsoletes
- Resolves: rhbz#2119506

* Tue Aug 16 2022 Marian Koncek <mkoncek@redhat.com> - 0:9.2.0-1
- Update to upstream version 9.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:8.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:8.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 Alexander Kurtakov <akurtako@redhat.com> 0:8.8.2-1
- Update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:8.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Mat Booth <mat.booth@redhat.com> - 0:8.6.3-1
- Update to latest upsteam release

* Thu Aug 06 2020 Mat Booth <mat.booth@redhat.com> - 0:8.4.1-9
- Add optional resolution on internal JDK APIs that might not be present on Java
  11

* Thu Aug 06 2020 Mat Booth <mat.booth@redhat.com> - 0:8.4.1-8
- Avoid requirement on com.sun.management package

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:8.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Mat Booth <mat.booth@redhat.com> - 0:8.4.1-6
- Fix NIO linkage error when running on Java 8 due to incorrect
  cross-compilation

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0:8.4.1-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed May 06 2020 Mat Booth <mat.booth@redhat.com> - 0:8.4.1-4
- Fix jp_minimal mode

* Tue May 5 2020 Alexander Kurtakov <akurtako@redhat.com> - 0:8.4.1-3
- Disable test-framework as its dependency (randomizedtesting) is removed.

* Sat Mar 21 2020 Mat Booth <mat.booth@redhat.com> - 0:8.4.1-2
- Fix deps for minimal mode

* Sat Mar 21 2020 Mat Booth <mat.booth@redhat.com> - 0:8.4.1-1
- Update to latest upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:8.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Mat Booth <mat.booth@redhat.com> - 0:8.1.1-3
- Drop spatial, morfologik, replicator, demo and benchmark modules due to missing deps
- Fix obsoletes when built in minimal mode

* Thu Jun 13 2019 Mat Booth <mat.booth@redhat.com> - 0:8.1.1-2
- Enable additional module in jp_minimal mode

* Wed Jun 12 2019 Mat Booth <mat.booth@redhat.com> - 0:8.1.1-1
- Update to latest upstream release

* Thu Feb 14 2019 Mat Booth <mat.booth@redhat.com> - 0:7.7.0-1
- Update to latest upstream release
- Drop deprecated uima analyzers sub-package
- Added nori Korean analyzers sub-package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Mat Booth <mat.booth@redhat.com> - 0:7.1.0-2
- Fix split package information in OSGi metadata

* Thu Apr 12 2018 Mat Booth <mat.booth@redhat.com> - 0:7.1.0-1
- Update to a newer upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:6.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Mat Booth <mat.booth@redhat.com> - 0:6.1.0-7
- Enable more modules in jp_minimal profile, rhbz#1455267

* Mon Oct 16 2017 Michael Simacek <msimacek@redhat.com> - 0:6.1.0-6
- Backport fix for CVE-2017-12629

* Thu Sep 21 2017 Mat Booth <mat.booth@redhat.com> - 0:6.1.0-5
- Rebuild to regenerate OSGi metadata due to objectweb-asm update

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:6.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Mat Booth <mat.booth@redhat.com> - 0:6.1.0-3
- Add better OSGi metadata for dealing with core/misc split packages
- Drop F24-specific hack

* Tue Mar 21 2017 Michael Simacek <msimacek@redhat.com> - 0:6.1.0-2
- Update jp_minimal conditional

* Mon Mar 20 2017 Mat Booth <mat.booth@redhat.com> - 0:6.1.0-1
- Update to lucene 6
- Add "spatial-extras" subpackage, this decouples dependencies on spatial4j.

* Thu Mar 16 2017 Michael Simacek <msimacek@redhat.com> - 0:5.5.0-7
- Add jp_minimal conditional

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 0:5.5.0-6
- Remove buildnumber-plugin

* Mon Aug 22 2016 Roman Vais <rvais@redhat.com> - 0:5.5.0-5
- Removed test dependency macros for lucene demo that caused conflict (duplicity)

* Wed Jul 13 2016 Roland Grunberg <rgrunber@redhat.com> - 0:5.5.0-4
- analyzers-common should have versioned requires on package from core.

* Fri Jul 08 2016 Mat Booth <mat.booth@redhat.com> - 0:5.5.0-3
- Misc module should require core module, the split package
  causes problems for OSGi consumers

* Mon Apr 18 2016 Mat Booth <mat.booth@redhat.com> - 0:5.5.0-2
- Add missing BR on ant, fixes FTBFS

* Wed Feb 24 2016 Michael Simacek <msimacek@redhat.com> - 0:5.5.0-1
- Update to upstream version 5.5.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:5.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Alexander Kurtakov <akurtako@redhat.com> 0:5.4.1-2
- Organize Sources numbering.
- Drop old jpackage header - package has nothing in common anymore.
- Drop 3+ years old provides/obsoletes.
- Move old changelog to separate file to ease working with the spec file.

* Mon Jan 25 2016 Alexander Kurtakov <akurtako@redhat.com> 0:5.4.1-1
- Update to upstream 5.4.1 release.

* Thu Jan 21 2016 Alexander Kurtakov <akurtako@redhat.com> 0:5.4.0-1
- Update to upstream 5.4.0 release.

* Tue Oct 6 2015 Alexander Kurtakov <akurtako@redhat.com> 0:5.3.1-1
- Update to upstream 5.3.1 release.

* Thu Aug 27 2015 Alexander Kurtakov <akurtako@redhat.com> 0:5.3.0-1
- Update to upstream 5.3.0 release.

* Wed Aug 26 2015 Mat Booth <mat.booth@redhat.com> - 0:5.2.1-4
- Remove forbidden SCL macros

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 0:5.2.1-3
- Disable generation of uses clauses in OSGi manifests.

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 0:5.2.1-2
- Drop old workarounds.

* Tue Jun 23 2015 Alexander Kurtakov <akurtako@redhat.com> 0:5.2.1-1
- Update to upstream 5.2.1.
