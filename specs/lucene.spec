Name:           lucene
Version:        10.1.0
Release:        %autorelease
Epoch:          0
Summary:        High-performance, full-featured text search engine
# License breakdown is present in NOTICE.txt file
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND BSD-2-Clause
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

%package facet
Summary:        Lucene module: facet

%description facet
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
%files facet -f .mfiles-lucene-facet
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
%autochangelog
