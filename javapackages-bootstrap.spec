# Exclude automatically generated requires on java interpreter which is not
# owned by any package
%global         __requires_exclude ^%{_jvmdir}/java

# Don't run OSGi dependency generators on private (bundled) JARs
%global         __requires_exclude_from \\.jar$
%global         __provides_exclude_from \\.jar$

%global         debug_package %{nil}

%global javaHomePath %{_jvmdir}/java-17-openjdk
%global mavenHomePath %{_datadir}/%{name}
%global metadataPath %{mavenHomePath}/maven-metadata
%global artifactsPath %{_jnidir}
%global launchersPath %{_libexecdir}/%{name}

#global git_hash ...
#global git_short_hash %(echo %{git_hash} | cut -b -7)

Name:           javapackages-bootstrap
Version:        1.9.0
Release:        2%{?dist}
Summary:        A means of bootstrapping Java Packages Tools
# For detailed info see the file javapackages-bootstrap-PACKAGE-LICENSING
License:        ASL 2.0 and ASL 1.1 and (ASL 2.0 or EPL-2.0) and (EPL-2.0 or GPLv2 with exceptions) and MIT and BSD with advertising and BSD and EPL-1.0 and EPL-2.0 and CDDL-1.0 and xpp and CC0 and Public Domain
URL:            https://github.com/fedora-java/javapackages-bootstrap
ExclusiveArch:  %{java_arches}

Source0:        https://github.com/fedora-java/javapackages-bootstrap/releases/download/%{version}/javapackages-bootstrap-%{version}.tar.xz
#Source0:        https://github.com/fedora-java/javapackages-bootstrap/archive/%{git_short_hash}.tar.gz

# License breakdown
Source1:        javapackages-bootstrap-PACKAGE-LICENSING

Source101:      toolchains-openjdk8.xml

# To obtain the following sources:
# tar -xf ${name}-${version}.tar.xz
# pushd ${name}-${version}
# ./downstream.sh clone
# ./downstream.sh prep
# ./downstream.sh archive
# The results are in the archive directory
Source1001:     ant.tar.xz
Source1002:     aopalliance.tar.xz
Source1003:     apache-pom.tar.xz
Source1004:     apiguardian.tar.xz
Source1005:     asm.tar.xz
Source1006:     assertj-core.tar.xz
Source1007:     bnd.tar.xz
Source1008:     build-helper-maven-plugin.tar.xz
Source1009:     byte-buddy.tar.xz
Source1010:     cdi.tar.xz
Source1011:     cglib.tar.xz
Source1012:     common-annotations-api.tar.xz
Source1013:     commons-beanutils.tar.xz
Source1014:     commons-cli.tar.xz
Source1015:     commons-codec.tar.xz
Source1016:     commons-collections.tar.xz
Source1017:     commons-compress.tar.xz
Source1018:     commons-io.tar.xz
Source1019:     commons-jxpath.tar.xz
Source1020:     commons-lang.tar.xz
Source1021:     commons-logging.tar.xz
Source1022:     commons-parent-pom.tar.xz
Source1023:     cup.tar.xz
Source1024:     easymock.tar.xz
Source1025:     extra-enforcer-rules.tar.xz
Source1026:     felix-parent-pom.tar.xz
Source1027:     felix-utils.tar.xz
Source1028:     fusesource-pom.tar.xz
Source1029:     guava.tar.xz
Source1030:     guice.tar.xz
Source1031:     hamcrest.tar.xz
Source1032:     httpcomponents-client.tar.xz
Source1033:     httpcomponents-core.tar.xz
Source1034:     httpcomponents-parent-pom.tar.xz
Source1035:     injection-api.tar.xz
Source1036:     jansi.tar.xz
Source1037:     jcommander.tar.xz
Source1038:     jdom.tar.xz
Source1039:     jdom2.tar.xz
Source1040:     jflex.tar.xz
Source1041:     jsr-305.tar.xz
Source1042:     junit4.tar.xz
Source1043:     junit5.tar.xz
Source1044:     maven-antrun-plugin.tar.xz
Source1045:     maven-archiver.tar.xz
Source1046:     maven-artifact-transfer.tar.xz
Source1047:     maven-assembly-plugin.tar.xz
Source1048:     maven-bundle-plugin.tar.xz
Source1049:     maven-common-artifact-filters.tar.xz
Source1050:     maven-compiler-plugin.tar.xz
Source1051:     maven-dependency-analyzer.tar.xz
Source1052:     maven-dependency-plugin.tar.xz
Source1053:     maven-dependency-tree.tar.xz
Source1054:     maven-enforcer.tar.xz
Source1055:     maven-file-management.tar.xz
Source1056:     maven-filtering.tar.xz
Source1057:     maven-jar-plugin.tar.xz
Source1058:     maven-parent-pom.tar.xz
Source1059:     maven-plugin-testing.tar.xz
Source1060:     maven-plugin-tools.tar.xz
Source1061:     maven-remote-resources-plugin.tar.xz
Source1062:     maven-resolver.tar.xz
Source1063:     maven-resources-plugin.tar.xz
Source1064:     maven-resources.tar.xz
Source1065:     maven-shared-incremental.tar.xz
Source1066:     maven-shared-io.tar.xz
Source1067:     maven-shared-utils.tar.xz
Source1068:     maven-source-plugin.tar.xz
Source1069:     maven-surefire.tar.xz
Source1070:     maven-verifier.tar.xz
Source1071:     maven-wagon.tar.xz
Source1072:     maven.tar.xz
Source1073:     mockito.tar.xz
Source1074:     modello.tar.xz
Source1075:     modulemaker-maven-plugin.tar.xz
Source1076:     mojo-parent-pom.tar.xz
Source1077:     objenesis.tar.xz
Source1078:     opentest4j.tar.xz
Source1079:     osgi-annotation.tar.xz
Source1080:     osgi-cmpn.tar.xz
Source1081:     osgi-core.tar.xz
Source1082:     oss-parent-pom.tar.xz
Source1083:     plexus-archiver.tar.xz
Source1084:     plexus-build-api.tar.xz
Source1085:     plexus-cipher.tar.xz
Source1086:     plexus-classworlds.tar.xz
Source1087:     plexus-compiler.tar.xz
Source1088:     plexus-components-pom.tar.xz
Source1089:     plexus-containers.tar.xz
Source1090:     plexus-interpolation.tar.xz
Source1091:     plexus-io.tar.xz
Source1092:     plexus-languages.tar.xz
Source1093:     plexus-pom.tar.xz
Source1094:     plexus-resources.tar.xz
Source1095:     plexus-sec-dispatcher.tar.xz
Source1096:     plexus-utils.tar.xz
Source1097:     qdox.tar.xz
Source1098:     servlet-api.tar.xz
Source1099:     sisu-inject.tar.xz
Source1100:     sisu-mojos.tar.xz
Source1101:     sisu-plexus.tar.xz
Source1102:     slf4j.tar.xz
Source1103:     testng.tar.xz
Source1104:     univocity-parsers.tar.xz
Source1105:     velocity-engine.tar.xz
Source1106:     xbean.tar.xz
Source1107:     xmlunit.tar.xz
Source1108:     xmvn-generator.tar.xz
Source1109:     xmvn.tar.xz
Source1110:     xz-java.tar.xz

Provides:       bundled(ant) = 1.10.12
Provides:       bundled(aopalliance) = 1.0
Provides:       bundled(apache-parent) = 26
Provides:       bundled(apiguardian) = 1.1.2
Provides:       bundled(objectweb-asm) = 9.4
Provides:       bundled(assertj-core) = 3.19.0
Provides:       bundled(aqute-bnd) = 5.2.0
Provides:       bundled(maven-plugin-build-helper) = 3.2.0
Provides:       bundled(byte-buddy) = 1.11.22
Provides:       bundled(cdi-api) = 2.0.2
Provides:       bundled(cglib) = 3.3.0
Provides:       bundled(jakarta-annotations) = 1.3.5
Provides:       bundled(apache-commons-beanutils) = 1.9.4
Provides:       bundled(apache-commons-cli) = 1.5.0
Provides:       bundled(apache-commons-codec) = 1.15
Provides:       bundled(apache-commons-collections) = 3.2.2
Provides:       bundled(apache-commons-compress) = 1.21
Provides:       bundled(apache-commons-io) = 2.11.0
Provides:       bundled(apache-commons-jxpath) = 1.3
Provides:       bundled(apache-commons-lang3) = 3.12.0
Provides:       bundled(apache-commons-logging) = 1.2
Provides:       bundled(apache-commons-parent) = 53
Provides:       bundled(java_cup) = 0.11b
Provides:       bundled(easymock) = 4.3
Provides:       bundled(extra-enforcer-rules) = 1.5.1
Provides:       bundled(felix-parent) = 7
Provides:       bundled(felix-utils) = 1.11.8
Provides:       bundled(fusesource-pom) = 1.12
Provides:       bundled(guava) = 31.1
Provides:       bundled(google-guice) = 5.1.0
Provides:       bundled(hamcrest) = 2.2
Provides:       bundled(httpcomponents-client) = 4.5.13
Provides:       bundled(httpcomponents-core) = 4.4.13
Provides:       bundled(httpcomponents-project) = 12
Provides:       bundled(atinject) = 1.0.5
Provides:       bundled(jansi) = 2.4.0
Provides:       bundled(beust-jcommander) = 1.81
Provides:       bundled(jdom) = 1.1.3
Provides:       bundled(jdom2) = 2.0.6
Provides:       bundled(jflex) = 1.7.0
Provides:       bundled(jsr-305) = 3.0.2
Provides:       bundled(junit) = 4.13.1
Provides:       bundled(junit5) = 5.8.1
Provides:       bundled(maven-antrun-plugin) = 3.0.0
Provides:       bundled(maven-archiver) = 3.5.1
Provides:       bundled(maven-artifact-transfer) = 0.13.1
Provides:       bundled(maven-assembly-plugin) = 3.3.0
Provides:       bundled(maven-plugin-bundle) = 5.1.1
Provides:       bundled(maven-common-artifact-filters) = 3.2.0
Provides:       bundled(maven-compiler-plugin) = 3.10.1
Provides:       bundled(maven-dependency-analyzer) = 1.12.0
Provides:       bundled(maven-dependency-plugin) = 3.3.0
Provides:       bundled(maven-dependency-tree) = 3.1.0
Provides:       bundled(maven-enforcer) = 3.0.0
Provides:       bundled(maven-file-management) = 3.0.0
Provides:       bundled(maven-filtering) = 3.2.0
Provides:       bundled(maven-jar-plugin) = 3.2.0
Provides:       bundled(maven-parent) = 39
Provides:       bundled(maven-plugin-testing) = 3.3.0
Provides:       bundled(maven-plugin-tools) = 3.6.4
Provides:       bundled(maven-remote-resources-plugin) = 1.7.0
Provides:       bundled(maven-resolver) = 1.9.7
Provides:       bundled(maven-resources-plugin) = 3.2.0
Provides:       bundled(maven-resources) = 1.4
Provides:       bundled(maven-shared-incremental) = 1.1
Provides:       bundled(maven-shared-io) = 3.0.0
Provides:       bundled(maven-shared-utils) = 3.3.4
Provides:       bundled(maven-source-plugin) = 3.2.1
Provides:       bundled(maven-surefire) = 3.0.0~M6
Provides:       bundled(maven-verifier) = 1.7.2
Provides:       bundled(maven-wagon) = 3.5.1
Provides:       bundled(maven) = 3.9.1
Provides:       bundled(mockito) = 3.7.13
Provides:       bundled(modello) = 2.0.0
Provides:       bundled(modulemaker-maven-plugin) = 1.9
Provides:       bundled(mojo-parent) = 67
Provides:       bundled(objenesis) = 3.1
Provides:       bundled(opentest4j) = 1.2.0
Provides:       bundled(osgi-annotation) = 8.0.1
Provides:       bundled(osgi-compendium) = 7.0.0
Provides:       bundled(osgi-core) = 8.0.0
Provides:       bundled(sonatype-oss-parent) = 7
Provides:       bundled(plexus-archiver) = 4.2.7
Provides:       bundled(plexus-build-api) = 0.0.7
Provides:       bundled(plexus-cipher) = 2.0
Provides:       bundled(plexus-classworlds) = 2.6.0
Provides:       bundled(plexus-compiler) = 2.11.1
Provides:       bundled(plexus-components-pom) = 6.6
Provides:       bundled(plexus-containers) = 2.1.1
Provides:       bundled(plexus-interpolation) = 1.26
Provides:       bundled(plexus-io) = 3.2.0
Provides:       bundled(plexus-languages) = 1.1.1
Provides:       bundled(plexus-pom) = 8
Provides:       bundled(plexus-resources) = 1.2.0
Provides:       bundled(plexus-sec-dispatcher) = 2.0
Provides:       bundled(plexus-utils) = 3.4.1
Provides:       bundled(qdox) = 2.0.0
Provides:       bundled(jakarta-servlet) = 4.0.3
Provides:       bundled(sisu) = 0.3.5
Provides:       bundled(sisu-mojos) = 0.3.5
Provides:       bundled(sisu-plexus) = 0.3.5
Provides:       bundled(slf4j) = 1.7.36
Provides:       bundled(testng) = 7.4.0
Provides:       bundled(univocity-parsers) = 2.9.1
Provides:       bundled(velocity) = 1.7
Provides:       bundled(xbean) = 4.18
Provides:       bundled(xmlunit) = 2.8.2
Provides:       bundled(xmvn-generator) = 1.2.1
Provides:       bundled(xmvn) = 4.2.0
Provides:       bundled(xz-java) = 1.9

BuildRequires:  byaccj
BuildRequires:  gcc
BuildRequires:  java-17-openjdk-devel
BuildRequires:  jurand
BuildRequires:  rpm-devel

Requires:       bash
Requires:       coreutils
Requires:       java-17-openjdk-devel
Requires:       procps-ng
Requires:       lujavrite%{?_isa}

Requires:       javapackages-common

%description
In a nutshell, Java Packages Bootstrap (JPB) is a standalone build of all Java
software packages that are required for Java Packages Tools (JPT) to work.

In order to achieve reliable and reproducible builds of Java packages while
meeting Fedora policy that requires everything to be built from source, without
using prebuilt binary artifacts, it is necessary to build the packages in a
well-defined, acyclic order. Dependency cycles between packages are the biggest
obstacle to achieving this goal and JPT is the biggest offender -- it requires
more than a hundred of Java packages, all of which in turn build-require JPT.

JPB comes with a solution to this problem -- it builds everything that JPT needs
to work, without reliance on any Java software other than OpenJDK. JPT can
depend on JPB for everything, without depending on any other Java packages. For
example, JPB contains embedded version of XMvn, removing dependency of JPT on
XMvn, allowing JPT to be used before one builds XMvn package.

%package openjdk8
Summary:        OpenJDK 8 toolchain for Java Packages Bootstrap
Requires:       %{name}
Requires:       java-1.8.0-openjdk-devel

%description openjdk8
OpenJDK 8 toolchain for Java Packages Bootstrap.

%prep
%setup -q

# leave out the first source as it has already been extracted
# leave out licensing breakdown file
other_sources=$(echo %{sources} | cut -d' ' -f4-)

for source in ${other_sources}; do
  tar -xf "${source}"
done

for patch_path in patches/*/*; do
  package_name="$(echo ${patch_path} | cut -f2 -d/)"
  patch_name="$(echo ${patch_path} | cut -f3 -d/)"
  
  pushd "downstream/${package_name}"
  # Unify line endings
  find . -name '*.java' -exec sed -i 's/\r//' {} +
  sed 's/\r//' "../../patches/${package_name}/${patch_name}" | patch -p1
  popd
done

%build
export LC_ALL=C.UTF-8
JAVA_HOME=%{javaHomePath} ./mbi.sh build -parallel

%install
JAVA_HOME=%{javaHomePath} ./mbi.sh dist \
  -javaCmdPath=%{javaHomePath}/bin/java \
  -basePackageName=%{name} \
  -installRoot=%{buildroot} \
  -mavenHomePath=%{mavenHomePath} \
  -metadataPath=%{metadataPath} \
  -artifactsPath=%{artifactsPath} \
  -launchersPath=%{launchersPath} \
  -licensesPath=%{_licensedir}/%{name} \

# Use custom toolchains.xml
cp -p %{SOURCE101} %{buildroot}%{mavenHomePath}/conf/toolchains.xml

install -D -p -m 644 downstream/xmvn-generator/src/main/lua/xmvn-generator.lua %{buildroot}%{_rpmluadir}/%{name}-generator.lua
install -D -p -m 644 downstream/xmvn-generator/src/main/rpm/macros.xmvngen %{buildroot}%{_rpmmacrodir}/macros.jpbgen
install -D -p -m 644 downstream/xmvn-generator/src/main/rpm/macros.xmvngenhook %{buildroot}%{_sysconfdir}/rpm/macros.jpbgenhook
install -D -p -m 644 downstream/xmvn-generator/src/main/rpm/xmvngen.attr %{buildroot}%{_fileattrsdir}/jpbgen.attr

echo '
%%__xmvngen_debug 1
%%__xmvngen_libjvm %{javaHomePath}/lib/server/libjvm.so
%%__xmvngen_classpath %{artifactsPath}/%{name}/xmvn-generator.jar:%{artifactsPath}/%{name}/asm.jar:%{artifactsPath}/%{name}/commons-compress.jar
%%__xmvngen_provides_generators org.fedoraproject.xmvn.generator.jpms.JPMSGeneratorFactory
%%__xmvngen_requires_generators %%{nil}
%%__xmvngen_post_install_hooks org.fedoraproject.xmvn.generator.transformer.TransformerHookFactory
%%jpb_env PATH=/usr/libexec/javapackages-bootstrap:$PATH
' >%{buildroot}%{_rpmmacrodir}/macros.jpbgen

sed -i s/xmvn-generator/%{name}-generator/ %{buildroot}%{_sysconfdir}/rpm/macros.jpbgenhook
sed -i s/xmvn-generator/%{name}-generator/ %{buildroot}%{_fileattrsdir}/jpbgen.attr
sed -i s/_xmvngen_/_jpbgen_/ %{buildroot}%{_fileattrsdir}/jpbgen.attr

%check
%{buildroot}%{launchersPath}/xmvn --version

%files
%{mavenHomePath}
%exclude %{mavenHomePath}/conf/toolchains.xml
%{metadataPath}/*
%{artifactsPath}/*
%{launchersPath}/*
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*

%files openjdk8
%{mavenHomePath}/conf/toolchains.xml

%license %{_licensedir}/%{name}
%doc README.md
%doc AUTHORS

%changelog
* Fri Mar 31 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.0-2
- Rebuild with no changes

* Mon Mar 27 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.0-1
- Update to upstream version 1.9.0

* Mon Mar 20 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-1
- Update to upstream version 1.8.1

* Fri Mar 17 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.0-1
- Update to upstream version 1.8.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Marian Koncek <mkoncek@redhat.com> - 1.7.2-1
- Update to upstream version 1.7.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.1-1
- Update to upstream version 1.7.1

* Tue Jun 14 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.0-3
- Add openjdk8 toolchain subpackage

* Mon Jun 06 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.0-2
- Drop build-requires on javapackages-generators

* Fri May 13 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.0-1
- Update to upstream version 1.7.0

* Thu May 05 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0^20220505.git4f9a68a-2
- Fix dangling toolchains.xml symlink

* Thu May 05 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0^20220505.git4f9a68a-1
- Update to latest upstream snapshot

* Fri Apr 29 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0^20220429.git1cfada9-1
- Update to latest upstream snapshot

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.0^20220105.git9f283b7-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0^20220105.git9f283b7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Marian Koncek <mkoncek@redhat.com> - 1.5.0^20220105.git9f283b7-1
- Update to latest upstream snapshot

* Wed Nov 03 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0^20211102.gitd76c032-2
- Build with OpenJDK 17

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0^20211102.gitd76c032-1
- Update to latest upstream snapshot

* Thu Oct 28 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0^20211028.git2daa95f-1
- Update to latest upstream snapshot

* Fri Oct 15 2021 Marian Koncek <mkoncek@redhat.com> - 1.5.0~20211015.1e296d5-1
- Update to upstream snapshot 1e296d550d91f89f383e42ceeb0856b97214b51a

* Mon Jul 26 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-1
- Update to upstream version 1.5.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-1
- Update to upstream version 1.4.0

* Mon Feb 08 2021 Marian Koncek <mkoncek@redhat.com> - 1.3.0-1
- Update to upstream version 1.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-1
- Update to upstream version 1.2.0

* Thu Dec  3 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0

* Wed Nov 25 2020 Marian Koncek <mkoncek@redhat.com> - 1.0.0-1
- Initial commit
