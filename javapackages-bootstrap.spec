# Exclude automatically generated requires on java interpreter which is not
# owned by any package
%global         __requires_exclude ^%{_jvmdir}/java

# Don't run OSGi dependency generators on private (bundled) JARs
%global         __requires_exclude_from \\.jar$
%global         __provides_exclude_from \\.jar$

# Generated list of bundled packages
%global         __local_generator_provides cat %{_builddir}/%{buildsubdir}/bundled-provides.txt
%global         __local_generator_path ^%{metadataPath}/.*$

%global         debug_package %{nil}

%global javaHomePath %{_jvmdir}/java-17-openjdk
%global mavenHomePath %{_datadir}/%{name}
%global metadataPath %{mavenHomePath}/maven-metadata
%global artifactsPath %{_jnidir}
%global launchersPath %{_libexecdir}/%{name}

#global git_hash ...
#global git_short_hash %(echo %{git_hash} | cut -b -7)

Name:           javapackages-bootstrap
Version:        1.15.0
Release:        1%{?dist}
Summary:        A means of bootstrapping Java Packages Tools
# For detailed info see the file javapackages-bootstrap-PACKAGE-LICENSING
License:        Apache-1.1 AND Apache-2.0 AND (Apache-2.0 OR EPL-2.0) AND (Apache-2.0 OR LGPL-2.0-or-later) AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-2.5 AND CC0-1.0 AND CPL-1.0 AND EPL-1.0 AND EPL-2.0 AND (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0) AND LicenseRef-Fedora-Public-Domain AND MIT AND Plexus AND SMLNJ AND Saxpath AND xpp
URL:            https://github.com/fedora-java/javapackages-bootstrap
ExclusiveArch:  %{java_arches}

Source0:        https://github.com/fedora-java/javapackages-bootstrap/releases/download/%{version}/javapackages-bootstrap-%{version}.tar.xz
#Source0:        https://github.com/fedora-java/javapackages-bootstrap/archive/%{git_short_hash}.tar.gz

# License breakdown
Source1:        javapackages-bootstrap-PACKAGE-LICENSING
Source2:        generate-bundled-provides.sh

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
Source1024:     disruptor.tar.xz
Source1025:     easymock.tar.xz
Source1026:     extra-enforcer-rules.tar.xz
Source1027:     felix-parent-pom.tar.xz
Source1028:     felix-utils.tar.xz
Source1029:     fusesource-pom.tar.xz
Source1030:     guava.tar.xz
Source1031:     guice.tar.xz
Source1032:     hamcrest.tar.xz
Source1033:     httpcomponents-client.tar.xz
Source1034:     httpcomponents-core.tar.xz
Source1035:     httpcomponents-parent-pom.tar.xz
Source1036:     injection-api.tar.xz
Source1037:     jaf-api.tar.xz
Source1038:     jansi.tar.xz
Source1039:     javacc-maven-plugin.tar.xz
Source1040:     javacc.tar.xz
Source1041:     javaparser.tar.xz
Source1042:     jcommander.tar.xz
Source1043:     jctools.tar.xz
Source1044:     jdom.tar.xz
Source1045:     jdom2.tar.xz
Source1046:     jflex.tar.xz
Source1047:     jsoup.tar.xz
Source1048:     jsr-305.tar.xz
Source1049:     junit4.tar.xz
Source1050:     junit5.tar.xz
Source1051:     log4j.tar.xz
Source1052:     mail-api.tar.xz
Source1053:     maven-antrun-plugin.tar.xz
Source1054:     maven-apache-resources.tar.xz
Source1055:     maven-archiver.tar.xz
Source1056:     maven-artifact-transfer.tar.xz
Source1057:     maven-assembly-plugin.tar.xz
Source1058:     maven-bundle-plugin.tar.xz
Source1059:     maven-common-artifact-filters.tar.xz
Source1060:     maven-compiler-plugin.tar.xz
Source1061:     maven-dependency-analyzer.tar.xz
Source1062:     maven-dependency-plugin.tar.xz
Source1063:     maven-dependency-tree.tar.xz
Source1064:     maven-enforcer.tar.xz
Source1065:     maven-file-management.tar.xz
Source1066:     maven-filtering.tar.xz
Source1067:     maven-jar-plugin.tar.xz
Source1068:     maven-parent-pom.tar.xz
Source1069:     maven-plugin-testing.tar.xz
Source1070:     maven-plugin-tools.tar.xz
Source1071:     maven-remote-resources-plugin.tar.xz
Source1072:     maven-resolver.tar.xz
Source1073:     maven-resources-plugin.tar.xz
Source1074:     maven-shared-incremental.tar.xz
Source1075:     maven-shared-io.tar.xz
Source1076:     maven-shared-utils.tar.xz
Source1077:     maven-source-plugin.tar.xz
Source1078:     maven-surefire.tar.xz
Source1079:     maven-verifier.tar.xz
Source1080:     maven-wagon.tar.xz
Source1081:     maven.tar.xz
Source1082:     mockito.tar.xz
Source1083:     modello.tar.xz
Source1084:     moditect.tar.xz
Source1085:     modulemaker-maven-plugin.tar.xz
Source1086:     mojo-parent-pom.tar.xz
Source1087:     objenesis.tar.xz
Source1088:     opentest4j.tar.xz
Source1089:     osgi-annotation.tar.xz
Source1090:     osgi-cmpn.tar.xz
Source1091:     osgi-core.tar.xz
Source1092:     plexus-archiver.tar.xz
Source1093:     plexus-build-api.tar.xz
Source1094:     plexus-cipher.tar.xz
Source1095:     plexus-classworlds.tar.xz
Source1096:     plexus-compiler.tar.xz
Source1097:     plexus-components-pom.tar.xz
Source1098:     plexus-containers.tar.xz
Source1099:     plexus-interpolation.tar.xz
Source1100:     plexus-io.tar.xz
Source1101:     plexus-languages.tar.xz
Source1102:     plexus-pom.tar.xz
Source1103:     plexus-resources.tar.xz
Source1104:     plexus-sec-dispatcher.tar.xz
Source1105:     plexus-testing.tar.xz
Source1106:     plexus-utils.tar.xz
Source1107:     plexus-xml.tar.xz
Source1108:     qdox.tar.xz
Source1109:     servlet-api.tar.xz
Source1110:     sisu-inject.tar.xz
Source1111:     sisu-mojos.tar.xz
Source1112:     sisu-plexus.tar.xz
Source1113:     slf4j.tar.xz
Source1114:     testng.tar.xz
Source1115:     univocity-parsers.tar.xz
Source1116:     velocity-engine.tar.xz
Source1117:     xmlunit.tar.xz
Source1118:     xmvn-generator.tar.xz
Source1119:     xmvn.tar.xz
Source1120:     xz-java.tar.xz

BuildRequires:  byaccj
BuildRequires:  gcc
BuildRequires:  java-17-openjdk-devel
BuildRequires:  jurand
BuildRequires:  rpm-devel
BuildRequires:  rpm-local-generator-support

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

%prep
%setup -q
# Dynamically generate bundled Provides
%{SOURCE2} >bundled-provides.txt

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
%{metadataPath}/*
%{artifactsPath}/*
%{launchersPath}/*
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*

%license %{_licensedir}/%{name}
%doc README.md
%doc AUTHORS

%changelog
* Wed Feb 07 2024 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.15.0-1
- Update to upstream version 1.15.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.14.0-1
- Update to upstream version 1.14.0

* Wed Oct 25 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.13.0-3
- Dynamically generate bundled Provides

* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.13.0-2
- Convert License tag to SPDX format

* Fri Aug 25 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.13.0-1
- Update to upstream version 1.13.0

* Mon Aug 21 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.12.0-1
- Update to upstream version 1.12.0

* Thu Aug 17 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11.0-2
- Update to upstream version 1.11.0

* Thu Aug 10 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10.0-1
- Update to upstream version 1.10.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
