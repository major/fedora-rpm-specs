%global srcname JavadocOfflineSearch

Name:           javadocofflinesearch
Version:        2.2
Release:        20%{?dist}
Summary:        Tool for offline searching in your docs via browser
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/judovana/%{srcname}
Source0:        https://github.com/judovana/%{srcname}/archive/refs/tags/%{srcname}-%{version}.tar.gz
# already fixed in upstream https://github.com/judovana/JavadocOfflineSearch/commit/853285f3105506b860c762f534e1a7c2733a2c61
Patch1:         javadocFixes.patch
# fixed license https://github.com/judovana/JavadocOfflineSearch/commit/7d0c410d9ef215499f4fa4fb67e9a105f0a95ba7
Patch2:         7d0c410d9ef215499f4fa4fb67e9a105f0a95ba7.diff
# updated to pdfbox 2.x since f28
Patch3:         pdfbox2.patch
Patch4:         longLucene.patch
Patch5:         753213ae509495a70855369b3991493ac5bdbcc2.patch
Patch6:         lucene9.patch

ExclusiveArch: %{java_arches} noarch
 
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  tagsoup
BuildRequires:  lucene-core
#BuildRequires:  lucene-analyzers-common hidden in
BuildRequires:  lucene-analysis-common
BuildRequires:  lucene-queries
BuildRequires:  lucene-queryparser
BuildRequires:  apache-commons-cli
BuildRequires:  pdfbox
#BuildRequires:  apache-commons-logging-api included in:
BuildRequires:  apache-commons-logging
BuildRequires:  fontbox

Requires:  jpackage-utils
Requires:  java-headless
Requires:  tagsoup
Requires:  lucene-core
#Requires:  lucene-analyzers-common hidden in
Requires:  lucene-analysis-common
Requires:  lucene-queries
Requires:  lucene-queryparser
Requires:  apache-commons-cli
Requires:  lucene-backward-codecs
Recommends:  pdfbox
#Recommends:  apache-commons-logging-api included in:
Recommends:  apache-commons-logging
Recommends:  fontbox 

%description
The goal of this project was to make searching in your (java)docs as easy and
 comfortable as when you are browsing them online.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup -p1 -n %{srcname}-%{srcname}-%{version}
find -print -name '*.class' -or -name '*.jar'  -delete


%build
ant

#pack manually
pushd  build/classes
jar -cvf ../../dist/%{name}.jar *
popd

%install
install -m0644  dist/%{name}.jar -D $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT/%{_javadocdir}
cp -r  dist/javadoc  $RPM_BUILD_ROOT/%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_bindir}

cat <<EOF > $RPM_BUILD_ROOT/%{_bindir}/%{name}
#!/bin/bash
. /usr/share/java-utils/java-functions

MAIN_CLASS=javadocofflinesearch.JavadocOfflineSearch

set_classpath "javadocofflinesearch"
set_classpath "tagsoup"
set_classpath "lucene-core"
set_classpath "lucene-analysis"
set_classpath "lucene-queries"
set_classpath "lucene-queryparser"
set_classpath "apache-commons-cli"
set_classpath "pdfbox"
set_classpath "apache-commons-logging"
set_classpath "fontbox"
set_classpath "lucene-backward-codecs"

EOF
# ${@} in cat EOF is susbtitued by nothing
echo 'run ${@}' >> $RPM_BUILD_ROOT/%{_bindir}/%{name}




%files
%{_javadir}/*
%license LICENSE
%attr(755,root,root) %{_bindir}/%{name}


%files javadoc
%{_javadocdir}/%{name}
%license LICENSE


%changelog
* Fri Jul 15 2022 Jiri Vanek <jvanek@redhat.com> - 2.2-12
- fixed for freshly packed lucene; rhbz#2107600

* Sun Feb 23 2020 Jiri Vanek <jvanek@redhat.com> - 2.2-11
- fixed for new lucene

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Jiri Vanek <jvanek@redhat.com> - 2.2-7
- updated to pdfbox 2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Jiri Vanek <jvanek@redhat.com> - 2.2-2
- added lucene-backward-codecs depndences

* Thu Feb 25 2016 Jiri Vanek <jvanek@redhat.com> - 2.2-1
- initial commit

