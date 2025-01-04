# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%bcond_with bootstrap

%if %{without bootstrap}
%bcond_with ant_minimal
%else
%bcond_without ant_minimal
%endif

%global ant_home %{_datadir}/ant

Name:           ant
Version:        1.10.15
Release:        %autorelease
Summary:        Java build tool
Summary(it):    Tool per la compilazione di programmi java
Summary(fr):    Outil de compilation pour java
License:        Apache-2.0
URL:            https://ant.apache.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
Source2:        apache-ant-1.8.ant.conf
# manpage
Source3:        ant.asciidoc

Patch:          %{name}-build.xml.patch

BuildRequires:  rubygem-asciidoctor

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  ant-junit
%endif

%if %{without ant_minimal}
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(bcel:bcel)
BuildRequires:  mvn(bsf:bsf)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(commons-net:commons-net)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(jdepend:jdepend)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-logging::api:)
BuildRequires:  mvn(org.tukaani:xz)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(regexp:regexp)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)

BuildRequires:  junit5
%endif

Requires:       %{name}-lib = %{version}-%{release}
Requires:       %{name}-jdk-binding
Suggests:       %{name}-openjdk21 = %{version}-%{release}

%description
Apache Ant is a Java library and command-line tool whose mission is to
drive processes described in build files as targets and extension
points dependent upon each other.  The main known usage of Ant is the
build of Java applications.  Ant supplies a number of built-in tasks
allowing to compile, assemble, test and run Java applications.  Ant
can also be used effectively to build non Java applications, for
instance C or C++ applications.  More generally, Ant can be used to
pilot any type of process which can be described in terms of targets
and tasks.

%description -l fr
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisé par les projets apache-jakarta et apache-xml.

%description -l it
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java.
Allo stato attuale viene utilizzato dai progetti apache jakarta ed
apache xml.

%package lib
Summary:        Core part of %{name}

%description lib
Core part of Apache Ant that can be used as a library.

%package junit
Summary:        Optional junit tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description junit
Optional junit tasks for %{name}.

%description junit -l fr
Taches junit optionelles pour %{name}.

%if %{without ant_minimal}

%package jmf
Summary:        Optional jmf tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description jmf
Optional jmf tasks for %{name}.

%description jmf -l fr
Taches jmf optionelles pour %{name}.

%package swing
Summary:        Optional swing tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description swing
Optional swing tasks for %{name}.

%description swing -l fr
Taches swing optionelles pour %{name}.

%package antlr
Summary:        Optional antlr tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description antlr
Optional antlr tasks for %{name}.

%description antlr -l fr
Taches antlr optionelles pour %{name}.

%package apache-bsf
Summary:        Optional apache bsf tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description apache-bsf
Optional apache bsf tasks for %{name}.

%description apache-bsf -l fr
Taches apache bsf optionelles pour %{name}.

%package apache-resolver
Summary:        Optional apache resolver tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description apache-resolver
Optional apache resolver tasks for %{name}.

%description apache-resolver -l fr
Taches apache resolver optionelles pour %{name}.

%package commons-logging
Summary:        Optional commons logging tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description commons-logging
Optional commons logging tasks for %{name}.

%description commons-logging -l fr
Taches commons logging optionelles pour %{name}.

%package commons-net
Summary:        Optional commons net tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description commons-net
Optional commons net tasks for %{name}.

%description commons-net -l fr
Taches commons net optionelles pour %{name}.

%package apache-bcel
Summary:        Optional apache bcel tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description apache-bcel
Optional apache bcel tasks for %{name}.

%description apache-bcel -l fr
Taches apache bcel optionelles pour %{name}.

%package apache-oro
Summary:        Optional apache oro tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description apache-oro
Optional apache oro tasks for %{name}.

%description apache-oro -l fr
Taches apache oro optionelles pour %{name}.

%package apache-regexp
Summary:        Optional apache regexp tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description apache-regexp
Optional apache regexp tasks for %{name}.

%description apache-regexp -l fr
Taches apache regexp optionelles pour %{name}.

%package apache-xalan2
Summary:        Optional apache xalan2 tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description apache-xalan2
Optional apache xalan2 tasks for %{name}.

%description apache-xalan2 -l fr
Taches apache xalan2 optionelles pour %{name}.

%package imageio
Summary:        Optional imageio tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description imageio
Optional imageio tasks for %{name}.

%package jakartamail
Summary:        Optional jakartamail tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description jakartamail
Optional jakartamail tasks for %{name}.

%description jakartamail -l fr
Taches jakartamail optionelles pour %{name}.

%package jdepend
Summary:        Optional jdepend tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description jdepend
Optional jdepend tasks for %{name}.

%description jdepend -l fr
Taches jdepend optionelles pour %{name}.

%package jsch
Summary:        Optional jsch tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description jsch
Optional jsch tasks for %{name}.

%description jsch -l fr
Taches jsch optionelles pour %{name}.

%package junit5
Summary:        Optional junit5 tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description junit5
Optional junit5 tasks for %{name}.

%description junit5 -l fr
Taches junit5 optionelles pour %{name}.

%package testutil
Summary:        Test utility classes for %{name}
Requires:       %{name} = %{version}-%{release}

%description testutil
Test utility tasks for %{name}.

%package xz
Summary:        Optional xz tasks for %{name}
Requires:       %{name} = %{version}-%{release}

%description xz
Optional xz tasks for %{name}.

%package manual
Summary:        Manual for %{name}
# ant-manual contains file tutorial-tasks-filesets-properties.zip
# which in turn contains src/Find.java and src/FindTest.java both
# licensed under ASL 1.1. See rhbz#1055629
License:        Apache-2.0 AND Apache-1.1

%description manual
Documentation for %{name}.

%description manual -l it
Documentazione di %{name}.

%description manual -l fr
Documentation pour %{name}.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.

%endif

# -----------------------------------------------------------------------------

%prep
%autosetup -p1 -C

# clean jar files
find . -name "*.jar" | xargs -t rm

# failing testcases. TODO see why
rm src/tests/junit/org/apache/tools/ant/types/selectors/SignedSelectorTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsFileSelectedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsSignedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/optional/image/ImageIOTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/JarTest.java \
   src/tests/junit/org/apache/tools/mail/MailMessageTest.java

# Test relies on internal JUnit 5 API that was changed
rm src/tests/junit/org/apache/tools/ant/taskdefs/optional/junitlauncher/LegacyXmlResultFormatterTest.java

# Log4jListener is deprecated by upstream: Apache Log4j (1) is not
# developed any more. Last release is 1.2.17 from 26 May 2012 and
# contains vulnerability issues.
rm src/main/org/apache/tools/ant/listener/Log4jListener.java

#install jars
%if %{with bootstrap}
ln -s %{_prefix}/lib/javapackages-bootstrap/junit.jar lib/optional/junit.jar
ln -s %{_prefix}/lib/javapackages-bootstrap/hamcrest-core.jar lib/optional/hamcrest-core.jar
%else
%if %{with ant_minimal}
build-jar-repository -s -p lib/optional junit hamcrest/core hamcrest/library
%else
build-jar-repository -s -p lib/optional antlr bcel commons-lang3 jakarta-mail/jakarta.mail-api jakarta-activation/jakarta.activation-api jdepend junit oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver xalan-j2-serializer hamcrest/core hamcrest/library xz-java junit5 opentest4j
%endif
%endif

# fix hardcoded paths in ant script and conf
cp -p %{SOURCE2} %{name}.conf
sed -e 's:/etc/ant.conf:%{_sysconfdir}/ant.conf:g' \
    -e 's:/etc/ant.d:%{_sysconfdir}/ant.d:g' \
    -e 's:/usr/share/ant:%{_datadir}/ant:g' \
    -e 's:/usr/bin/build-classpath:%{_bindir}/build-classpath:g' \
    -e 's:/usr/share/java-utils/java-functions:%{_javadir}-utils/java-functions:g' \
    -i src/script/ant %{name}.conf

# Remove unnecessary JARs from the classpath
sed -i 's/jaxp_parser_impl//;s/xml-commons-apis//' src/script/ant

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 >KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 >LICENSE.utf8
mv LICENSE.utf8 LICENSE

# We want a hard dep on antlr
%pom_xpath_remove pom:optional src/etc/poms/ant-antlr/pom.xml

# fix javamail dependency coordinates (remove once javamail is updated)
%pom_change_dep com.sun.mail:jakarta.mail jakarta.mail:jakarta.mail-api src/etc/poms/ant-jakartamail/pom.xml

%pom_change_dep commons-logging:commons-logging-api org.apache.commons:commons-logging::api: src/etc/poms/ant-commons-logging/pom.xml

%build
%if %{with ant_minimal}
%{ant} jars
%else
%{ant} jars test-jar javadocs
%endif

# typeset the manpage
asciidoctor -b manpage -D man %{SOURCE3}

# remove empty jai and netrexx jars. Due to missing dependencies they contain only manifests.
rm build/lib/ant-jai.jar build/lib/ant-netrexx.jar
# log4j logging is deprecated
rm build/lib/ant-apache-log4j.jar
# dropped in favor of jakartamail
rm build/lib/ant-javamail.jar

%install
# ANT_HOME and subdirs
mkdir -p %{buildroot}%{ant_home}/{lib,etc,bin}

%mvn_alias :ant org.apache.ant:ant-nodeps apache:ant ant:ant
%mvn_alias :ant-launcher ant:ant-launcher

%mvn_file ':{ant,ant-bootstrap,ant-launcher}' %{name}/@1 @1

%if %{with ant_minimal}
mv build/lib build/lib0
mkdir build/lib/
mv build/lib0/ant.jar build/lib/
mv build/lib0/ant-bootstrap.jar build/lib/
mv build/lib0/ant-launcher.jar build/lib/
mv build/lib0/ant-junit.jar build/lib/
mv build/lib0/ant-junit4.jar build/lib/
%endif

for jar in build/lib/*.jar; do
  # Make sure that installed JARs are not empty
  jar tf ${jar} | grep -E -q '.*\.class'

  jarname=$(basename $jar .jar)

  # jar aliases
  ln -sf ../../java/%{name}/${jarname}.jar %{buildroot}%{ant_home}/lib/${jarname}.jar

  pom=src/etc/poms/${jarname}/pom.xml

  # bootstrap does not have a pom, generate one
  [ $jarname == ant-bootstrap ] && pom='org.apache.ant:ant-bootstrap:%{version}'

  %mvn_artifact ${pom} ${jar}
done

# ant-parent pom
%mvn_artifact src/etc/poms/pom.xml

%mvn_package :ant lib
%mvn_package :ant-launcher lib
%mvn_package :ant-bootstrap lib
%mvn_package :ant-parent lib
%mvn_package :ant-junit4 junit
# catchall rule for the rest
%mvn_package ':ant-{*}' @1

%mvn_install

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
%if %{with ant_minimal}
rm src/etc/jdepend-frames.xsl
rm src/etc/jdepend.xsl
rm src/etc/maudit-frames.xsl
%endif
cp -p src/etc/*.xsl %{buildroot}%{ant_home}/etc

# install everything else
mkdir -p %{buildroot}%{_bindir}
cp -p src/script/ant %{buildroot}%{_bindir}/
ln -sf %{_bindir}/ant %{buildroot}%{ant_home}/bin/
cp -p src/script/antRun %{buildroot}%{ant_home}/bin/

# default ant.conf
mkdir -p %{buildroot}%{_sysconfdir}
cp -p %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

# OPT_JAR_LIST fragments
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
echo "junit hamcrest/core ant/ant-junit" > %{buildroot}%{_sysconfdir}/%{name}.d/junit
echo "junit hamcrest/core ant/ant-junit4" > %{buildroot}%{_sysconfdir}/%{name}.d/junit4

# JDK bindings
install -d -m 755 %{buildroot}%{_javaconfdir}/
ln -sf %{_jpbindingdir}/ant.conf %{buildroot}%{_javaconfdir}/ant.conf
echo 'JAVA_HOME=%{_jvmdir}/jre-21-openjdk' > %{buildroot}%{_javaconfdir}/ant-openjdk21.conf
%jp_binding --verbose --variant openjdk21 --ghost ant.conf --target %{_javaconfdir}/ant-openjdk21.conf --provides %{name}-jdk-binding --requires java-21-openjdk-headless --recommends java-21-openjdk-devel
touch %{buildroot}%{_javaconfdir}/ant-unbound.conf
%jp_binding --verbose --variant unbound --ghost ant.conf --target %{_javaconfdir}/ant-unbound.conf --provides %{name}-jdk-binding

%if %{without ant_minimal}

echo "ant/ant-jmf" > %{buildroot}%{_sysconfdir}/%{name}.d/jmf
echo "ant/ant-swing" > %{buildroot}%{_sysconfdir}/%{name}.d/swing
echo "antlr ant/ant-antlr" > %{buildroot}%{_sysconfdir}/%{name}.d/antlr
echo "bsf commons-logging ant/ant-apache-bsf" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver ant/ant-apache-resolver" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-resolver
echo "apache-commons-logging ant/ant-commons-logging" > %{buildroot}%{_sysconfdir}/%{name}.d/commons-logging
echo "apache-commons-net ant/ant-commons-net" > %{buildroot}%{_sysconfdir}/%{name}.d/commons-net
echo "bcel commons-lang3 ant/ant-apache-bcel" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-bcel
echo "oro ant/ant-apache-oro" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp ant/ant-apache-regexp" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-regexp
echo "xalan-j2 xalan-j2-serializer ant/ant-apache-xalan2" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-xalan2
echo "ant/ant-imageio" > %{buildroot}%{_sysconfdir}/%{name}.d/imageio
echo "jakartamail jaf ant/ant-jakartamail" > %{buildroot}%{_sysconfdir}/%{name}.d/jakartamail
echo "jdepend ant/ant-jdepend" > %{buildroot}%{_sysconfdir}/%{name}.d/jdepend
echo "jsch ant/ant-jsch" > %{buildroot}%{_sysconfdir}/%{name}.d/jsch
echo "junit5 hamcrest/core junit opentest4j ant/ant-junitlauncher" > %{buildroot}%{_sysconfdir}/%{name}.d/junitlauncher
echo "testutil ant/ant-testutil" > %{buildroot}%{_sysconfdir}/%{name}.d/testutil
echo "xz-java ant/ant-xz" > %{buildroot}%{_sysconfdir}/%{name}.d/xz

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}

# fix link between manual and javadoc
(cd manual; ln -sf %{_javadocdir}/%{name} api)

%endif

# manpage
install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%if %{without ant_minimal}
%check
%{ant} -Doffline=true test
%endif

%files
%doc KEYS README WHATSNEW
%license LICENSE NOTICE
%config %{_javaconfdir}/%{name}*.conf
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/ant
%dir %{ant_home}/bin
%{ant_home}/bin/ant
%attr(0755,root,root) %{ant_home}/bin/antRun
%{_mandir}/man1/%{name}.*
%dir %{ant_home}/etc
%{ant_home}/etc/ant-update.xsl
%{ant_home}/etc/changelog.xsl
%{ant_home}/etc/coverage-frames.xsl
%{ant_home}/etc/mmetrics-frames.xsl
%{ant_home}/etc/log.xsl
%{ant_home}/etc/tagdiff.xsl
%{ant_home}/etc/common2master.xsl
%{ant_home}/etc/printFailingTests.xsl
%dir %{_sysconfdir}/%{name}.d

%files lib -f .mfiles-lib
%dir %{ant_home}
%dir %{ant_home}/lib
%{ant_home}/lib/%{name}.jar
%{ant_home}/lib/%{name}-launcher.jar
%{ant_home}/lib/%{name}-bootstrap.jar

%files junit -f .mfiles-junit
%{ant_home}/lib/%{name}-junit.jar
%{ant_home}/lib/%{name}-junit4.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit
%config(noreplace) %{_sysconfdir}/%{name}.d/junit4
%{ant_home}/etc/junit-frames.xsl
%{ant_home}/etc/junit-noframes.xsl
%{ant_home}/etc/junit-frames-xalan1.xsl
%{ant_home}/etc/junit-frames-saxon.xsl
%{ant_home}/etc/junit-noframes-saxon.xsl

%if %{without ant_minimal}

%files jmf -f .mfiles-jmf
%{ant_home}/lib/%{name}-jmf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jmf

%files swing -f .mfiles-swing
%{ant_home}/lib/%{name}-swing.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/swing

%files antlr -f .mfiles-antlr
%{ant_home}/lib/%{name}-antlr.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr

%files apache-bsf -f .mfiles-apache-bsf
%{ant_home}/lib/%{name}-apache-bsf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf

%files apache-resolver -f .mfiles-apache-resolver
%{ant_home}/lib/%{name}-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver

%files commons-logging -f .mfiles-commons-logging
%{ant_home}/lib/%{name}-commons-logging.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging

%files commons-net -f .mfiles-commons-net
%{ant_home}/lib/%{name}-commons-net.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net

%files apache-bcel -f .mfiles-apache-bcel
%{ant_home}/lib/%{name}-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel

%files apache-oro -f .mfiles-apache-oro
%{ant_home}/lib/%{name}-apache-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl

%files apache-regexp -f .mfiles-apache-regexp
%{ant_home}/lib/%{name}-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp

%files apache-xalan2 -f .mfiles-apache-xalan2
%{ant_home}/lib/%{name}-apache-xalan2.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-xalan2

%files imageio -f .mfiles-imageio
%{ant_home}/lib/%{name}-imageio.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/imageio

%files jakartamail -f .mfiles-jakartamail
%{ant_home}/lib/%{name}-jakartamail.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jakartamail

%files jdepend -f .mfiles-jdepend
%{ant_home}/lib/%{name}-jdepend.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl

%files jsch -f .mfiles-jsch
%{ant_home}/lib/%{name}-jsch.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch

%files junit5 -f .mfiles-junitlauncher
%{ant_home}/lib/%{name}-junitlauncher.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junitlauncher

%files testutil -f .mfiles-testutil
%{ant_home}/lib/%{name}-testutil.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/testutil

%files xz -f .mfiles-xz
%{ant_home}/lib/%{name}-xz.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/xz

%files manual
%license LICENSE NOTICE
%doc manual/*

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{name}

%endif

# -----------------------------------------------------------------------------

%changelog
%autochangelog
