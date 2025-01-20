#in noarch? why...
%define debug_package %{nil}
%global remove_tests 1

%global commit 88a95fa93c58322393174f84543edc7a0a2ca44d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20220221

Name:       procyon
Version:    0.6.0
Release:    0.8.%{commitdate}.git%{shortcommit}%{?dist}
Summary:    procyon java decompiler and other tools
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:    Apache-2.0 
URL:        https://github.com/mstrobel/procyon
# ./generate-tarball.sh
# This script uses a fork of the original project
Source0:    %{name}-%{commit}.tar.gz
Source1:    procyon-decompiler
Patch3:     madeToPasXlint.patch


BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  javapackages-tools
BuildRequires:  java-devel
BuildRequires:  dos2unix
BuildRequires:  beust-jcommander
Requires:      java-headless
Requires:      javapackages-tools
# main package is just meta package for all subprojects and their artifacts
Recommends:   %{name}-compilertools = %{version}-%{release}
Recommends:   %{name}-core = %{version}-%{release}
Recommends:   %{name}-expressions = %{version}-%{release}
Recommends:   %{name}-reflection = %{version}-%{release}
Recommends:   %{name}-decompiler = %{version}-%{release}

%description
Procyon is a suite of Java metaprogramming tools focused on code generation and analysis.
It includes the following libraries: Core Framework, Reflection Framework,
Expressions Framework, Compiler Toolset (Experimental), Java Decompiler.
The Procyon libraries are available from Maven Central under group ID org.bitbucket.mstrobel.

%package compilertools
Summary:    The procyon-compilertools project
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Requires:      javapackages-tools

%description compilertools
The procyon-compilertools project is a work in progress that includes:
Class metadata and bytecode inspection/manipulation facilities based on Mono.Cecil and 
An optimization and decompiler framework based on ILSpy
The Compiler Toolset is still early in development and subject to change.

%package core
Summary:    The procyon-core framework contains common support classes
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Requires:      javapackages-tools

%description core
The procyon-core framework contains common support classes used by the other
Procyon APIs. Its facilities include string manipulation, collection extensions,
filesystem/path utilities, freezable objects and collections, attached data stores,
and some runtime type helpers.

%package expressions
Summary:    The procyon-expressions framework provides a more natural form of Linq-like code generation
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Requires:      javapackages-tools

%description expressions
The procyon-expressions framework provides a more natural form of code generation.
Rather than requiring bytecode to be emitted directly, as with procyon-reflection
and other popular libraries like ASM, procyon-expressions enables code composition
using declarative expression trees. These expression trees may then be compiled directly
into callbacks or coupled with a MethodBuilder. The procyon-expressions API is
almost a direct port of System.Linq.Expressions from .NET's Dynamic Language Runtime,
minus the dynamic callsite support (and with more relaxed rules regarding type conversions).

%package decompiler
Summary:    procyon-decompiler is a front-end for the Java decompiler
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Requires:   %{name}-core
Requires:   %{name}-compilertools
Requires:   beust-jcommander
Requires:      javapackages-tools

%description decompiler
procyon-decompiler is a front-end for the Java decompiler included in procyon-compilertools.
For more information about the decompiler, see the Java Decompiler wiki page - 
https://bitbucket.org/mstrobel/procyon/wiki/Java%20Decompiler

%package reflection
Summary:    The procyon-reflection framework provides a rich reflection and code generation API
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Requires:      javapackages-tools

%description reflection
The procyon-reflection framework provides a rich reflection and code generation API with full support for generics,
wildcards, and other high-level Java type concepts. It is based on .NET's System.Reflection and System.Reflection.
Emit APIs and is meant to address many of the shortcomings of the core Java reflection API, which offers rather
limited and cumbersome support for generic type inspection. Its code generation facilities include a TypeBuilder,
MethodBuilder, and a bytecode emitter.

%prep
%setup -q -n %{name}-%{commit}
%if %{remove_tests}
find | grep "\\.class$"
#find | grep "\\.jar$"
rm -rvf Procyon.CompilerTools/src/test/
find | grep "\\.class$" && exit 1
find | grep "\\.jar$"   && exit 1
%endif
#to allow smooth patching
dos2unix Procyon.Decompiler/build.gradle
dos2unix build.gradle
dos2unix README.md
dos2unix Procyon.CompilerTools/src/main/java/com/strobel/assembler/metadata/MethodBinder.java
%patch -P3 -p1

%build
mkdir -p build/Procyon.CompilerTools/{libs,classes}
mkdir -p build/Procyon.Core/{libs,classes}
mkdir -p build/Procyon.Decompiler/{libs,classes}
mkdir -p build/Procyon.Expressions/{libs,classes}
mkdir -p build/Procyon.Reflection/{libs,classes}

javac -d build/Procyon.Core/classes/ ` find Procyon.Core/src/main/java -type f | grep  "\.java"`
javac -d build/Procyon.Reflection/classes/    -cp build/Procyon.Core/classes/ ` find Procyon.Reflection/src/main/java -type f | grep  "\.java"`
javac -d build/Procyon.Expressions/classes/   -cp build/Procyon.Core/classes/:build/Procyon.Reflection/classes/ ` find Procyon.Expressions/src/main/java -type f | grep  "\.java"`
javac -d build/Procyon.CompilerTools/classes/ -cp build/Procyon.Core/classes/ ` find Procyon.CompilerTools/src/main/java -type f | grep  "\.java"`

# pack the jars
for x in Procyon.CompilerTools Procyon.Core Procyon.Reflection Procyon.Expressions ; do
  pushd build/$x/classes/
    project=`echo $x | sed -e "s/Procyon.//"  | sed -e 's/\(.*\)/\L\1/'`
    jar -cf ../../../build/$x/libs/%{name}-$project-%{version}.jar com
  popd
done

# create just launcher jar to be used in fedora
mkdir build/launcher-minimal
mkdir build/launcher-minimal/classes
javac -source 8 -target 8 -cp  build/Procyon.Core/classes/:build/Procyon.CompilerTools/classes/:%{_javadir}/beust-jcommander.jar  -d build/launcher-minimal/classes ` find Procyon.Decompiler/src/main/java -type f | grep  "\.java"`
# pack the minimal jar
pushd build/launcher-minimal/classes/
jar -cf ../../../build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}.jar com
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE1}  $RPM_BUILD_ROOT/%{_bindir}/ # cusotm launcher for main method in main jar
mkdir -p $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.CompilerTools/libs/%{name}-compilertools-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Core/libs/%{name}-core-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Expressions/libs/%{name}-expressions-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Reflection/libs/%{name}-reflection-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/

pushd   $RPM_BUILD_ROOT/%{_javadir}/%{name}/
ln -s %{name}-compilertools-%{version}.jar %{name}-compilertools.jar
ln -s %{name}-core-%{version}.jar %{name}-core.jar
ln -s %{name}-decompiler-%{version}.jar %{name}-decompiler.jar
ln -s %{name}-expressions-%{version}.jar %{name}-expressions.jar
ln -s %{name}-reflection-%{version}.jar %{name}-reflection.jar
popd

%files
%license License.txt
%doc README.md

%files compilertools
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-compilertools-%{version}.jar
%{_javadir}/%{name}/%{name}-compilertools.jar
%license License.txt
%doc README.md

%files core
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-core-%{version}.jar
%{_javadir}/%{name}/%{name}-core.jar
%license License.txt
%doc README.md

%files expressions
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-expressions-%{version}.jar
%{_javadir}/%{name}/%{name}-expressions.jar
%license License.txt
%doc README.md

%files decompiler
%dir %{_javadir}/%{name}
%{_bindir}/%{name}-decompiler
%{_javadir}/%{name}/%{name}-decompiler-%{version}.jar
%{_javadir}/%{name}/%{name}-decompiler.jar
%license License.txt
%doc README.md

%files reflection
%dir %{_javadir}/%{name}/
%{_javadir}/%{name}/%{name}-reflection-%{version}.jar
%{_javadir}/%{name}/%{name}-reflection.jar
%license License.txt
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.8.20220221.git88a95fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0-0.7.20220221.git88a95fa
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.6.20220221.git88a95fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.5.20220221.git88a95fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.4.20220221.git88a95fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.3.20220221.git88a95fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.2.20220221.git88a95fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.1.20220221.git88a95fa
- bumped to 0.6.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.36-0.11.20210619.git92ba3f4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.5.36-0.10.20210619.git92ba3f4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.5.36-0.9.20210619.git92ba3f4
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.36-0.8.20210619.git92ba3f4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.36-0.7.20210619.git92ba3f4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Jiri Vanek <jvanek@redhat.com> - 0.5.36-0.6-92ba3f4
- moved to commit versioning

* Thu Jun 03 2021 Marian Koncek <mkoncek@redhat.com> - 1.0~SNAPSHOT-1
- Update to upstream version 1.0~SNAPSHOT

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.36-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.5.36-0.4
- set source/target of 8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.36-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.5.36-0.2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Feb 18 2020  Jiri Vanek <jvanek@redhat.com> - 0.5.36-0.1
- bumped to latest tagged forest 0.5.36
- fixed bug in usage of newer jcommander

* Tue Feb 18 2020  Jiri Vanek <jvanek@redhat.com> - 0.5.33-0.5.pre02
- removed fat jar, as gradle is gone
- removed javadoc and srcs artifacts. will eb building by javac
- buit by javac instead of gradle

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.33-0.3.pre02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.33-0.2.pre02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Jiri Vanek <jvanek@redhat.com> 0.5.33-0.1.pre02
- created special package for assembled fat jar
- adapted rest of package to include and cooperate with minimal decompiler frontend

* Fri Dec 21 2018 Jiri Vanek <jvanek@redhat.com> 0.5.33-0.1.pre01
- inital load
