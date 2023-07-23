# Version of scala-altered objectweb-asm
%global asmver 9.5.0
%global asmrel 1

# Version of jquery bundled in scaladoc
%global jqueryver 3.6.4

# Version of jline to use
%global jlinever 3.22.0

%global scaladir %{_datadir}/scala

# Scala needs itself to compile.  Use this if the version in the repository
# cannot build the current version.
%bcond_with bootstrap

Name:           scala
Version:        2.13.11
Release:        2%{?dist}
Summary:        Hybrid functional/object-oriented language for the JVM
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# Used to generate OSGi data
%global date    20230531
%global seqnum  233414
%global commit  f113b1ab477ae2052725fe0b7ba5ae2796903807
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global osgiver %{version}.v%{date}-%{seqnum}-VFINAL-%{shortcommit}
%global majver  %(cut -d. -f1-2 <<< %{version})

# The project as a whole is Apache-2.0.
# The bundled ASM is BSD-3-Clause.
# The bundled jquery is MIT.
License:        Apache-2.0 and BSD-3-Clause and MIT
URL:            https://www.scala-lang.org/
# Source code
Source0:        https://github.com/scala/scala/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with bootstrap}
# Binary form, used to bootstrap
Source1:        https://downloads.lightbend.com/scala/%{version}/%{name}-%{version}.tgz
%endif
# Scala-modified version of objectweb-asm
Source2:        https://github.com/scala/scala-asm/archive/v%{asmver}-scala-%{asmrel}.tar.gz

# POMs from maven central
Source3:        https://repo1.maven.org/maven2/org/scala-lang/scala-library/%{version}/scala-library-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/scala-lang/scala-reflect/%{version}/scala-reflect-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/scala-lang/scala-compiler/%{version}/scala-compiler-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/scala-lang/scalap/%{version}/scalap-%{version}.pom

# Bundled version of jquery for scaladoc
Source7:        https://code.jquery.com/jquery-%{jqueryver}.min.js
Source8:        https://code.jquery.com/jquery-%{jqueryver}.slim.min.js

# OSGi properties for the reflect jar
Source9:        scala-reflect-bnd.properties
# OSGi properties for the library jar
Source10:       scala-library-bnd.properties
# OSGi properties for the compiler jar
Source11:       scala-compiler-bnd.properties

# Properties file for scala-compiler
Source12:       compiler.properties
# Properties file for scala-asm
Source13:       asm.properties
# Properties file for scala-buildcharacter
Source14:       buildcharacter.properties

# MIME information
Source15:       scala.keys
Source16:       scala.mime
Source17:       scala-mime-info.xml

# Use the Fedora way of finding the JVM to invoke
Patch0:         %{name}-tooltemplate.patch

# Unbundle fonts from scaladoc
Patch1:         %{name}-unbundle-fonts.patch

BuildRequires:  aqute-bnd
BuildRequires:  font(lato)
BuildRequires:  font(materialicons)
BuildRequires:  font(opensans)
BuildRequires:  font(sourcecodepro)
BuildRequires:  maven-local
BuildRequires:  mvn(io.github.java-diff-utils:java-diff-utils)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(org.jline:jline-builtins)
BuildRequires:  mvn(org.jline:jline-terminal-jna)
BuildRequires:  mvn(org.openjdk.jol:jol-core)

%if %{without bootstrap}
BuildRequires:  scala
%endif

Requires:       %{name}-reflect = %{version}-%{release}
Requires:       javapackages-tools

# scaladoc depends on a specific version of jquery, which may differ from the
# version in the js-jquery package
Provides:       bundled(js-jquery) = %{jqueryver}

# The bundled version of objectweb-asm has been altered for Scala purposes.
Provides:       bundled(objectweb-asm) = %{asmver}

# This can be removed when Fedora 36 reaches EOL
Obsoletes:      ant-%{name} < 2.13.4
Obsoletes:      %{name}-swing < 2.13.4

%global _desc %{expand:
Scala is a general purpose programming language designed to express
common programming patterns in a concise, elegant, and type-safe way.
It smoothly integrates features of object-oriented and functional
languages.  It is also fully interoperable with Java.}

%description %_desc

This package contains the Scala compiler and bytecode parser.

%package        library
Summary:        Scala standard library

%description    library %_desc

This package contains the standard library for the Scala programming
language.

%package        reflect
Summary:        Scala reflection library
Requires:       %{name}-library = %{version}-%{release}

%description    reflect %_desc

This package contains the reflection library for the Scala programming
language.

%package        apidoc
Summary:        Documentation for the Scala programming language
Requires:       font(lato)
Requires:       font(materialicons)
Requires:       font(opensans)
Requires:       font(sourcecodepro)

%description    apidoc %_desc

This package provides reference and API documentation for the Scala
programming language.

%prep
%autosetup -p1
%if %{with bootstrap}
%setup -T -D -a 1
%endif
%setup -T -D -a 2

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use env
for fil in scripts/stability-test.sh \
  src/compiler/templates/tool-unix.tmpl \
  test/script-tests/jar-manifest/run-test \
  tools/scaladoc-diff; do
  sed -i.orig 's,%{_bindir}/env bash,%{_bindir}/bash,' $fil
  fixtimestamp $fil
done

# Unbundle fonts
# The CSS uses local() references, so these should not be needed anyway.
rm src/scaladoc/scala/tools/nsc/doc/html/resource/lib/{lato,MaterialIcons,open-sans,source-code-pro}*

# Fetch upstream's POMs
cp -p %{SOURCE3} src/library/pom.xml
cp -p %{SOURCE4} src/reflect/pom.xml
cp -p %{SOURCE5} src/compiler/pom.xml
cp -p %{SOURCE6} src/scalap/pom.xml

# Fedora has a split jline3, so split up the dependency
%pom_change_dep org.jline:jline org.jline:jline-terminal-jna src/compiler
%pom_add_dep org.jline:jline-reader:%{jlinever} src/compiler
%pom_add_dep org.jline:jline-style:%{jlinever} src/compiler
%pom_add_dep org.jline:jline-builtins:%{jlinever} src/compiler

%build
export LC_ALL=C.UTF-8

%if %{with bootstrap}
PATH=$PATH:$PWD/%{name}-%{version}/bin
COMPJAR=$PWD/%{name}-%{version}/lib/scala-compiler.jar
%else
COMPJAR=%{_javadir}/scala/scala-compiler.jar
%endif

JAVA_VER=$(java -version 2>&1 | sed -n 's/.*"\([[:digit:]]*\)[.[:digit:]]*[^[:digit:]]*".*/\1/p')
JLINE_JARS=$(build-classpath jna jline/jline-terminal jline/jline-terminal-jna \
    jline/jline-reader jline/jline-style jline/jline-builtins)
JAVAC_FLAGS="-g -parameters -source 11 -target 11"
SCALAC_FLAGS="-g:vars -release $JAVA_VER -J-Xmx512M -J-Xms32M"
SCALADOC_FLAGS='-J-Xmx512M -J-Xms32M -doc-footer epfl -diagrams -implicits -groups -doc-version %{version} -doc-source-url https://github.com/scala/scala/blob/v%{version}/src/€{FILE_PATH_EXT}#L€{FILE_LINE}'
DIFFUTILS_JAR=$(build-classpath java-diff-utils)

mkdir -p target/{compiler,library,manual,reflect,scalap,tastytest,testkit}
mkdir -p target/html/{compiler,library,reflect}

# Build the bundled objectweb-asm
cd scala-asm-%{asmver}-scala-%{asmrel}
javac $JAVAC_FLAGS -d ../target/compiler $(find src -name \*.java)
cd -

# Build the library
cd src
javac $JAVAC_FLAGS -d ../target/library -cp $(build-classpath junit) \
    $(find library -name \*.java)
scalac $SCALAC_FLAGS -d ../target/library -classpath ../target/library \
    $(find library -name \*.scala | sort)
scaladoc $SCALADOC_FLAGS -doc-title 'Scala Standard Library' \
    -sourcepath $PWD/library -doc-no-compile $PWD/library-aux \
    -skip-packages scala.concurrent.impl \
    -doc-root-content $PWD/library/rootdoc.txt \
    $(find library -name \*.scala | sort)
mv scala ../target/html/library

# Build the reflection library
javac $JAVAC_FLAGS -d ../target/reflect $(find reflect -name \*.java)
scalac $SCALAC_FLAGS -d ../target/reflect -classpath ../target/reflect \
    $(find reflect -name \*.scala | sort)
scaladoc $SCALADOC_FLAGS -doc-title 'Scala Reflection Library' \
    -sourcepath $PWD/reflect \
    -skip-packages scala.reflect.macros.internal:scala.reflect.internal:scala.reflect.io \
    $(find reflect -name \*.scala | sort)
mv scala ../target/html/reflect

# Build the compiler
javac $JAVAC_FLAGS -d ../target/compiler -cp $COMPJAR \
    $(find compiler -name \*.java)
scalac $SCALAC_FLAGS -d ../target/compiler \
    -classpath ../target/compiler:$DIFFUTILS_JAR \
    -feature $(find compiler -name \*.scala)

# Build the interactive compiler
scalac $SCALAC_FLAGS -d ../target/compiler -classpath ../target/compiler \
    -feature $(find interactive -name \*.scala)

# Build the REPL
scalac $SCALAC_FLAGS -d ../target/compiler -classpath ../target/reflect \
    -feature $(find repl -name \*.scala)

# Build the REPL frontend
javac $JAVAC_FLAGS -d ../target/compiler $(find repl-frontend -name \*.java)
scalac $SCALAC_FLAGS -d ../target/compiler \
    -classpath ../target/compiler:$JLINE_JARS \
    -feature $(find repl-frontend -name \*.scala)
scaladoc $SCALADOC_FLAGS -doc-title 'Scala Compiler' \
    -sourcepath $PWD/compiler:$PWD/interactive:$PWD/repl:$PWD/repl-frontend \
    -doc-root-content $PWD/compiler/rootdoc.txt \
    -classpath $PWD/../target/library:$PWD/../target/reflect:$JLINE_JARS:$DIFFUTILS_JAR \
    $(find compiler -name \*.scala) $(find interactive -name \*.scala) \
    $(find repl -name \*.scala) $(find repl-frontend -name \*.scala)
mv scala ../target/html/compiler

# Build the documentation generator
# The order of the source files matters!  Some orderings end with this error:
# error: scala.reflect.internal.Symbols$CyclicReference: illegal cyclic reference involving <refinement of scala.tools.nsc.doc.model.ModelFactory with scala.tools.nsc.doc.model.ModelFactoryImplicitSupport with scala.tools.nsc.doc.model.ModelFactoryTypeSupport with scala.tools.nsc.doc.model.diagram.DiagramFactory with scala.tools.nsc.doc.model.CommentFactory with scala.tools.nsc.doc.model.TreeFactory with scala.tools.nsc.doc.model.MemberLookup>
# I do not know why that happens.  This is one order that works.  There are
# no doubt many more.
scalac $SCALAC_FLAGS -d ../target/compiler \
    $(find scaladoc -name \*.scala | sort)

# Build the bytecode parser
scalac $SCALAC_FLAGS -d ../target/scalap $(find scalap -name \*.scala)

# Build the testing tool
javac $JAVAC_FLAGS -d ../target/testkit \
    -cp ../target/library:$(build-classpath junit) \
    $(find testkit -name \*.java)
scalac $SCALAC_FLAGS -d ../target/testkit \
    -classpath ../target/testkit:$(build-classpath junit) -feature \
    $(find testkit -name \*.scala)

# TODO: build the parser testing tool.  This cannot be done without some sbt
# classes.  If we have sbt, then we don't need to build manually anyway.

# Build the integration tests
scalac $SCALAC_FLAGS -d ../target/tastytest -classpath $DIFFUTILS_JAR \
    $(find tastytest -name \*.scala)

# Build the man page builder
scalac $SCALAC_FLAGS -d ../target/manual -classpath ../target/library \
    $(find manual -name \*.scala)
cd -

# Copy source files into target before constructing jars
for dir in reflect library compiler scalap; do
  cp -p LICENSE NOTICE target/$dir
done
cp -p src/library/rootdoc.txt target/library
cp -p src/compiler/rootdoc.txt target/compiler
cp -a src/compiler/templates target/compiler
cp -a src/scaladoc/scala/tools/nsc/doc/html/resource \
      target/compiler/scala/tools/nsc/doc/html
cp -p src/scalap/decoder.properties target/scalap

# Build the compiler jar
cd target
mkdir -p compiler/META-INF/services
cat > compiler/META-INF/services/javax.script.ScriptEngineFactory << EOF
scala.tools.nsc.interpreter.shell.Scripted\$Factory
EOF
propdate=$(date -u -d %{date})
jnaver=$(sed -n 's,^  <version>\(.*\)</version>,\1,p' %{_datadir}/maven-poms/jna.pom)
cp -p %{SOURCE7} compiler/jquery.min.js
cp -p %{SOURCE8} compiler/jquery.slim.min.js
sed -e "s/@@DATE@@/$propdate/;s/@@VER@@/%{version}/;s/@@OSGI@@/%{osgiver}/" \
  %{SOURCE12} > compiler/compiler.properties
cp -p compiler/compiler.properties compiler/interactive.properties
cp -p compiler/compiler.properties compiler/repl.properties
cp -p compiler/compiler.properties compiler/replFrontend.properties
cp -p compiler/compiler.properties compiler/scaladoc.properties
sed -e "s/@@DATE@@/$propdate/;s/@@VER@@/%{version}/;s/@@MAJVER@@/%{majver}/" \
  -e "s/@@ASMVER@@/%{asmver}/;s/@@ASMREL@@/%{asmrel}/" \
  %{SOURCE13} > compiler/scala-asm.properties
sed -e "s/@@DATE@@/$propdate/;s/@@VER@@/%{version}/;s/@@OSGI@@/%{osgiver}/" \
  -e "s/@@ASMVER@@/%{asmver}/;s/@@ASMREL@@/%{asmrel}/" \
  -e "s/@@JLINEVER@@/%{jlinever}/;s/@@JNAVER@@/$jnaver/" \
  %{SOURCE14} > compiler/scala-buildcharacter.properties
jar cf scala-compiler.jar.no -C compiler .
bnd wrap --properties %{SOURCE11} --output scala-compiler.jar \
    --version "%{osgiver}" scala-compiler.jar.no

# Build the reflect jar
cp -p compiler/compiler.properties reflect/reflect.properties
jar cf scala-reflect.jar.no -C reflect .
bnd wrap --properties %{SOURCE9} --output scala-reflect.jar \
    --version "%{osgiver}" scala-reflect.jar.no

# Build the library jar
cp -p compiler/compiler.properties library/library.properties
jar cf scala-library.jar.no -C library .
bnd wrap --properties %{SOURCE10} --output scala-library.jar \
    --version "%{osgiver}" scala-library.jar.no

# Build the decoder jar
cp -p compiler/compiler.properties scalap/scalap.properties
jar cf scalap-%{version}.jar -C scalap .
cd -

# Build the man pages
mkdir -p html man/man1
cd src
scala -classpath ../target/manual:../target/scala-library.jar scala.tools.docutil.ManMaker 'fsc, scala, scalac, scaladoc, scalap' ../html ../man
cd -

# Prepare to install
%mvn_artifact src/library/pom.xml target/scala-library.jar
%mvn_artifact src/reflect/pom.xml target/scala-reflect.jar
%mvn_artifact src/compiler/pom.xml target/scala-compiler.jar
%mvn_artifact src/scalap/pom.xml target/scalap-%{version}.jar

%mvn_package org.scala-lang:scala-library library
%mvn_package org.scala-lang:scala-reflect reflect

%install
%mvn_install

# Create the binary scripts
mkdir -p %{buildroot}%{_bindir}
CLASSPATH=$(build-classpath jna jline/jline-terminal \
            jline/jline-terminal-jna jline/jline-reader jline/jline-style \
            jline/jline-builtins)\
:%{_javadir}/scala/scala-library.jar\
:%{_javadir}/scala/scala-reflect.jar\
:%{_javadir}/scala/scala-compiler.jar
JAVAFLAGS="-Xmx256M -Xms32M"

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.fsc.CompileClient," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/fsc

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.MainGenericRunner," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scala

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.Main," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scalac

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.ScalaDoc," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scaladoc

sed -e "s,@classpath@,$CLASSPATH:$(build-classpath scala/scalap)," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.scalap.Main," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scalap

chmod 0755 %{buildroot}%{_bindir}/{fsc,scala*}

# Install the MIME info
install -d %{buildroot}%{_datadir}/mime-info
install -p -m 644 %{SOURCE15} %{SOURCE16} %{buildroot}%{_datadir}/mime-info/

install -d %{buildroot}%{_datadir}/mime/packages/
install -p -m 644 %{SOURCE17} %{buildroot}%{_datadir}/mime/packages/

# Install the man pages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/man1/* %{buildroot}%{_mandir}/man1

%files -f .mfiles
%{_bindir}/fsc
%{_bindir}/scala*
%{_datadir}/mime-info/scala.*
%{_datadir}/mime/packages/scala-mime-info.xml
%{_mandir}/man1/fsc.1*
%{_mandir}/man1/scala*

%files library -f .mfiles-library
%license LICENSE NOTICE doc/LICENSE.md doc/License.rtf

%files reflect -f .mfiles-reflect

%files apidoc
%doc target/html/*
%license LICENSE NOTICE doc/LICENSE.md doc/License.rtf

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Jerry James <loganjerry@gmail.com> - 2.13.11-1
- Version 2.13.11
- Fix bad scaladoc output (rhbz#2215780)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Jerry James <loganjerry@gmail.com> - 2.13.10-1
- Expand overly generic file globs

* Mon Oct 10 2022 Jerry James <loganjerry@gmail.com> - 2.13.10-1
- Version 2.13.10
- Remove font dependencies from main package

* Tue Sep 20 2022 Jerry James <loganjerry@gmail.com> - 2.13.9-1
- Version 2.13.9
- Drop upstreamed -difflib patch
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.13.8-2
- Rebuilt for Drop i686 JDKs

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 2.13.8-1
- Version 2.13.8

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.13.7-3
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Jerry James <loganjerry@gmail.com> - 2.13.7-1
- Version 2.13.7
- Support building with OpenJDK 17

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Jerry James <loganjerry@gmail.com> - 2.13.6-1
- Version 2.13.6

* Mon Feb 22 2021 Jerry James <loganjerry@gmail.com> - 2.13.5-1
- Version 2.13.5

* Fri Feb 19 2021 Jerry James <loganjerry@gmail.com> - 2.13.4-3
- Require javapackages-tools for the binary wrappers (bz 1930755)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Jerry James <loganjerry@gmail.com> - 2.13.4-1
- Version 2.13.4
- Massive changes, too many to list

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.6-14
- Re-enable docs generation during build

* Fri Oct 12 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.6-13
- Stop scaladoc from trying to bundle non-existent resources
- Temporarly disable docs generation during build

* Tue Jul 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 2.10.6-12
- Require full javapackages-tools for scripts.

* Tue Jul 31 2018 Michael Simacek <msimacek@redhat.com> - 2.10.6-11
- Correct license tag to include CC0 and Public Domain
- Repack tarball to remove possibly proprietary binaries
- Use %%license macro

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.6-9
- Include bootstrap sources in SRPM

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Michael Simacek <msimacek@redhat.com> - 2.10.6-7
- Port from deprecated add_maven_depmap to mvn_install
- Remove unused BR felix-framework
- Fix unowned directory

* Thu Dec  7 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.6-6
- Add missing BR on javapackages-local
- Resolves: rhbz#1512883

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.10.6-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan  5 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.6-2
- Update to current packaging guidelines
- Remove legacy build conditionals
- Remove file requires
- Remove usage of shutil (not available on RHEL)

* Wed Nov 16 2016 William Benton <willb@redhat.com> - 2.10.6-1
- upstream version bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Michael Simacek <msimacek@redhat.com> - 2.10.4-8
- Use aqute-bnd-2.4.1

* Thu Jul 9 2015 William Benton <willb@redhat.com> - 2.10.4-7
- non-bootstrap build

* Thu Jul 9 2015 William Benton <willb@redhat.com> - 2.10.4-6
- bootstrap build

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.10.4-4
- Drop ExcludeArch for ARM, can't be both noarch and arch exclusive

* Wed Oct 1 2014 William Benton <willb@redhat.com> - 2.10.4-3
- non-bootstrap build

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 2.10.4-2
- update/optimize mime scriptlets

* Mon Sep 15 2014 William Benton <willb@redhat.com> - 2.10.4-1
- updated to upstream version 2.10.4
- fixes for Java 8 compatibility:  use scala 2.10.4 for bootstrapping

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-11
- Implenting usage of headless java (#1068518)
- Fix rpmdeps version sanity check issue

* Mon Dec  9 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-10
- Activate compiler-pom patch again

* Sun Dec  8 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-9
- Put the swing library into a seperate subpackage

* Wed Nov 27 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-8
- Filter osgi(org.apache.ant) Req. (#975598)

* Thu Oct 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-7
- Fix wrong condition for jline Req.

* Wed Oct 30 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-6
- Jline2 is now jline in Rawhide
- Fix an issue with jansi.jar in F-20 (#1025062)

* Tue Oct 22 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-5
- Fix typo

* Mon Oct 21 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-4
- Fix jline2.jar path for Rawhide (#1021465)
- Add jpackage-utils as a BR

* Tue Oct 15 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-3
- Fix change classpath of jansi.jar
- Dynamicly setting of version in bnd.properties
- automatic generation of gitdate and gitsha

* Sun Oct 13 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-2
- Fix REPL crash issue when entering an exclaimation mark (#890069)

* Thu Oct 10 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.3-1
- New upstream release

* Thu Sep 26 2013 William Benton <willb@redhat.com> - 2.10.2-1
- upstream version 2.10.2

* Thu Sep 12 2013 William Benton <willb@redhat.com> - 2.10.1-4
- updated upstream source location (thanks to Antoine Gourlay for the observation)

* Wed Sep 11 2013 William Benton <willb@redhat.com> - 2.10.1-3
- Fixes to build and install on F19

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 16 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.1-1
- New upstream releae

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.0-1
- New upstream release
- Add patch to use system aQuate-bnd.jar file

* Thu Dec 13 2012 Jochen Schmitt <s4504kr@omega.in.herr-schmitt.de> - 2.10.0-0.5
- New upstream release

* Fri Dec  7 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.10.0-0.3
- New upstream release

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 2.9.2-1
- update to 2.9.2
- added maven poms
- adapted to current guideline
- built with java 7 support
- removed ant-nodeps from buildrequires
- disabled swing module

* Sat Jul 21 2012 Fedora Release Engineering <JOchen herr-schmitt de> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.9.1-2
- Build explicit agains java-1.6.0

* Thu Nov  3 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.9.1-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  9 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.8.1-1
- New upstream release (#661853)

* Sun Aug 15 2010 Geoff Reedy <geoff@programmer-monk.net> - 2.8.0-1
- Update to upstream 2.8.0 release

* Thu Oct 29 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.7-1
- Update to upstream 2.7.7 release

* Sat Sep 19 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.5-1
- Update to upstream 2.7.5 release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.4-5
- fix problem in tooltemplate patch

* Mon May 18 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.4-4
- make jline implicitly available to match upstream behavior

* Mon May 18 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.4-3
- fix problem with substitutions to scripts in %%install

* Mon May 18 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.4-2
- fix launcher scripts by modifying template, not overriding them

* Tue May 12 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.4-1
- update to 2.7.4 final

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Geoff Reedy <geoff@programmer-monk.net> - 2.7.3-1
- update to 2.7.3 final

* Sun Nov 09 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.2-1
- update to 2.7.2 final

* Mon Nov 03 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.2-0.3.RC6
- bump release to fix upgrade path

* Sat Nov 01 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.2-0.1.RC6
- update to 2.7.2-RC6

* Thu Oct 30 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.2-0.1.RC5
- update to 2.7.2-RC5

* Sat Sep 06 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.2-0.2.RC1
- All code is now under BSD license
- Remove dll so and exe binaries in prep
- Add BuildRequires required by Java packaging guidelines
- Add missing defattr for examples and ant-scala

* Wed Aug 20 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.2-0.1.RC1
- update to 2.7.2-RC1

* Wed Aug 13 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.1-3
- regenerate classpath in manifest patch to apply cleanly to 2.7.1

* Wed Aug 13 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.1-2
- no changes, accidental release bump

* Mon May 05 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.1-1
- Update to 2.7.1

* Fri May 02 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.0-2
- Use java-sdk-openjdk for non-fc8 builds

* Mon Mar 10 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.7.0-1
- Update to 2.7.0
- License now correctly indicated as BSD and LGPLv2+
- Include LICENSE file in apidoc subpackage

* Mon Feb 11 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-8
- Adhere more strongly to the emacs package guidelines
- Include some comments regarding the boot-strapping process

* Wed Jan 16 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-7
- Add dist tag to release
- Fix directory ownership issues in %%_datadir/scala
- Remove source code from -devel package
- Rename -devel package to ant-scala
- Fix packaging of gtksourceview2 language spec
- Preserve timestamps when installing and cping
- Add patch to remove Class-Path entries from jar manifests
- Fix line endings in enscript/README
 
* Sun Jan 13 2008 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-6
- Include further information about inclusion of binary distribution
- Unpack only those files needed from the binary distribution
- Include note about license approval

* Thu Dec 27 2007 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-5
- Add emacs(bin) BR
- Patch out call to subversion in build.xml
- Add pkgconfig to BuildRequires

* Thu Dec 27 2007 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-4
- Reformat emacs-scala description
- Expand tabs to spaces
- Fix -devel symlinks
- Better base package summary

* Wed Dec 26 2007 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-3
- Add ant config to devel package
- Require icedtea for build
- Move examples to %%{_datadir}/scala/examples
- Clean up package descriptions
- Add base package requirement for scala-examples and scala-devel

* Wed Dec 26 2007 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-2
- Fix post scripts
- Use spaces instead of tabs

* Wed Dec 26 2007 Geoff Reedy <geoff@programmer-monk.net> - 2.6.1-1
- Initial build.
