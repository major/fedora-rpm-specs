Summary: Application for extraction and decompilation of JVM byte code
Name: java-runtime-decompiler
Version: 9.1
Release: %autorelease
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: https://github.com/pmikova/java-runtime-decompiler
Source0: https://github.com/judovana/%{name}/archive/%{name}-%{version}.tar.gz
Source1: %{name}
Source3: jrd.desktop
Source4: jrd-hex.desktop
Patch1: systemFernflower.patch
Patch2: systemProcyon.patch
Patch21: systemProcyonAssembler.patch
Patch3: rsyntaxVersion.patch
Patch4: systemCfr.patch
Patch5: systemJasm.patch
Patch51: systemJasm7.patch
Patch52: systemJasmG.patch
Patch53: systemJasmG7.patch
Patch6: systemJcoder.patch
Patch61: systemJcoder7.patch
Patch62: systemJcoderG.patch
Patch63: systemJcoderG7.patch
Patch7: removeMultilineSpotbugs.patch

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires: maven-local-openjdk25
BuildRequires: byteman
BuildRequires: rsyntaxtextarea
BuildRequires: junit5
BuildRequires: ant-junit5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: java-diff-utils
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-clean-plugin
BuildRequires: java-25-devel
BuildRequires: google-gson
BuildRequires: desktop-file-utils
BuildRequires: classpathless-compiler
BuildRequires: jurand
Requires: google-gson
Requires: byteman
Requires: rsyntaxtextarea
Requires: javapackages-tools
Requires: classpathless-compiler
Requires: java-diff-utils
Recommends: java
Recommends: %{name}-fernflower-plugin
Recommends: %{name}-procyon-plugin
Recommends: %{name}-cfr-plugin
Recommends: %{name}-asmtools-plugin
Recommends: %{name}-asmtools7-plugin

%description
This application can access JVM at runtime,
extract byte code from the JVM and decompile it, modify the obtained code and compile it back.
It also works with local classpath and source path and provide standalone hex, with binary diff.

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.

%package fernflower-plugin
Requires: fernflower
Summary: fernflower decompiler plugin for %{name}
Requires: %{name} = %{version}-%{release}

%description fernflower-plugin
This package provides bindings and requirements to fernflower decompiler for %{name}.

%package procyon-plugin
Requires: procyon-decompiler >= 0.6
Summary: procyon decompiler plugin for %{name}
Requires: %{name} = %{version}-%{release}

%description procyon-plugin
This package provides bindings and requirements to procyon decompiler for %{name}.

%package cfr-plugin
Requires: CFR
Summary: CFR decompiler plugin for %{name}
Requires: %{name} = %{version}-%{release}

%description cfr-plugin
This package provides bindings and requirements to CFR decompiler for %{name}.

%package asmtools-plugin
Requires: openjdk-asmtools >= 8.0.b09
Summary: asmtools disassembler and assembler plugin for %{name}
Requires: %{name} = %{version}-%{release}

%description asmtools-plugin
This package provides bindings and requirements to asmtools disassembler and assembler for %{name}.

%package asmtools7-plugin
Requires: openjdk-asmtools7
Summary: asmtools7 disassembler and assembler plugin for %{name}
Requires: %{name} = %{version}-%{release}

%description asmtools7-plugin
This package provides bindings and requirements to asmtools7 disassembler and assembler for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch 1 -p0
%patch 2 -p0
%patch 21 -p0
%patch 3 -p0
%patch 4 -p0
%patch 5 -p0
%patch 51 -p0
%patch 52 -p0
%patch 53 -p0
%patch 6 -p0
%patch 61 -p0
%patch 62 -p0
%patch 63 -p0
%patch 7 -p1

%java_remove_annotations decompiler_agent runtime-decompiler -s -n SuppressFBWarnings

%build
pushd runtime-decompiler
%pom_remove_plugin :maven-jar-plugin
popd
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :formatter-maven-plugin
%pom_remove_dep :spotbugs-annotations
xmvn --version
#echo $JAVA_HOME
#export JAVA_HOME=/usr/lib/jvm/java-25-openjdk #why?
xmvn --version
%mvn_build -f --xmvn-javadoc -- -Plegacy
CPLC=/usr/share/java/classpathless-compiler
$JAVA_HOME/bin/java -cp $CPLC/classpathless-compiler.jar:$CPLC/classpathless-compiler-api.jar:$CPLC/classpathless-compiler-util.jar:runtime-decompiler/target/runtime-decompiler-%{version}.jar org.jrd.backend.data.cli.Help > %{name}.1

%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/
pushd $RPM_BUILD_ROOT%{_mandir}/man1/
  ln -s %{name}.1 jrd.1
  ln -s %{name}.1 %{name}-hex.1
  ln -s %{name}.1 jrd-hex.1
popd

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
pushd $RPM_BUILD_ROOT%{_bindir}
  cp %{name} %{name}-hex
  sed 's/^run .*/run -hex "$@"/' -i %{name}-hex
  ln -s %{name} jrd
  ln -s %{name}-hex jrd-hex
popd

cp -r %{_builddir}/%{name}-%{name}-%{version}/runtime-decompiler/src/plugins/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor="fedora" --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}
desktop-file-install --vendor="fedora" --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE4}

#jd is not yet packed and sucks anyway
rm $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/plugins/JdDecompilerWrapper.java
rm $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/plugins/JdDecompilerWrapper.json

%files -f .mfiles
%attr(755, root, -) %{_bindir}/java-runtime-decompiler
%attr(755, root, -) %{_bindir}/java-runtime-decompiler-hex
%{_bindir}/jrd
%{_bindir}/jrd-hex
%{_mandir}/man1/java-runtime-decompiler*.1*
%{_mandir}/man1/jrd*.1*
# wrappers for decompilers
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%dir %{_datadir}/applications
%{_datadir}/applications/fedora-jrd.desktop
%{_datadir}/applications/fedora-jrd-hex.desktop

%files fernflower-plugin
%config %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.json

%files procyon-plugin
%config %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/ProcyonAssemblerDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/ProcyonAssemblerDecompilerWrapper.json

%files cfr-plugin
%config %{_sysconfdir}/%{name}/plugins/CfrDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/CfrDecompilerWrapper.json

%files asmtools-plugin
%config %{_sysconfdir}/%{name}/plugins/JasmDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JasmDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/JasmGDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JasmGDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/JcoderDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JcoderDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/JcoderGDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JcoderGDecompilerWrapper.json

%files asmtools7-plugin
%config %{_sysconfdir}/%{name}/plugins/Jasm7DecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/Jasm7DecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/JasmG7DecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JasmG7DecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/Jcoder7DecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/Jcoder7DecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/JcoderG7DecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JcoderG7DecompilerWrapper.json
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
