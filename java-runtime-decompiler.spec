Summary: Application for extraction and decompilation of JVM byte code
Name: java-runtime-decompiler
Version: 9.1
Release: 1%{?dist}
License: GPLv3
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
BuildRequires: maven-local
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
BuildRequires: java-devel
BuildRequires: google-gson
BuildRequires: desktop-file-utils
BuildRequires: classpathless-compiler
Requires: google-gson
Requires: byteman
Requires: rsyntaxtextarea
Requires: java-headless
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
%patch1 -p0
%patch2 -p0
%patch21 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch51 -p0
%patch52 -p0
%patch53 -p0
%patch6 -p0
%patch61 -p0
%patch62 -p0
%patch63 -p0
%patch7 -p1

%build
pushd runtime-decompiler
%pom_remove_plugin :maven-jar-plugin
popd
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :formatter-maven-plugin
%pom_remove_dep :spotbugs-annotations
a=`find | grep ".*\.java$"`
for x in $a ; do 
  #grep -e ".*SuppressFBWarnings.*" $x && echo "^ $x ^"
  sed "s/.*SuppressFBWarnings.*//g" $x -i
done
xmvn --version
echo $JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk #why?
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
* Wed Jan 03 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-1
- update dto 9.1
- https://github.com/judovana/java-runtime-decompiler/releases/tag/java-runtime-decompiler-9.1
- https://github.com/judovana/java-runtime-decompiler/releases/tag/java-runtime-decompiler-9.0

* Fri Oct 13 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-1
- update dto 8.0
- https://github.com/pmikova/java-runtime-decompiler/releases/tag/java-runtime-decompiler-8.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-2
- added 2b99a244b592445962cdd15ca33f80449f9aa2ea.patch to fix compiler issue in jrd window

* Fri Jun 30 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-1
- moved to 7.3
- https://github.com/pmikova/java-runtime-decompiler/releases/tag/java-runtime-decompiler-7.3
- https://github.com/pmikova/java-runtime-decompiler/releases/tag/java-runtime-decompiler-7.2

* Wed Mar 15 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-1
- https://github.com/pmikova/java-runtime-decompiler/releases/tag/java-runtime-decompiler-7.1
- moved to jrd 7.1
- added desp on java-diff and new cplc
- fixed(?) procyon wrapper
  - todo procyon crashes witout trace
- removed jd wrapper (was new in 7.1, maybe will be added)
- split plugins to subpkgs
- added jrd-hex launcher
- added hex launcher, added jrd symlinks

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 6.1-4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 6.1-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0.pre.3-1
- bumped sources to upstream rc candidate

* Sun Dec 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0.pre.2-1
- bumped sources to upstream pre release

* Thu Aug 12 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0.pre.1-1
- umped sources to upstream pre release
- adapted jcoder plugin
- todo, patch for removed plugins

* Thu Aug 12 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-1
- bumped to final sources

* Mon Aug 09 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.rc1-1
- adapted manpage

* Mon Aug 02 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.beta2-1
- updated to 5.0
- removed jdk8 subpkg due to compiler api
- added Cfr and asmtools plugins
- todo man page

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Jiri Vanek <jvanek@redhat.com> - 4.0-2
- Added subpackage built by jdk8 to allow looking into jdk8 apps
- for some reason, jdk8 vm can not look into jdk11 vm, even if agent is correctly jdk8 version
- the config is still share, which is stupid, but I doubt there is another target audeince then me

* Tue Dec 08 2020 Jiri Vanek <jvanek@redhat.com> - 4.0-1
- built by jdk11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Mar 17 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-7
- aligned rsyntaxtextarea version, fixed javadoc generation

* Tue Mar 17 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-6
- changed jdk8 requirement

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Jiri Vanek <jvanek@redhat.com> - 3.0-3
- all stdouts from customlauncher moved to stderr

* Mon Aug 26 2019 Jiri Vanek <jvanek@redhat.com> - 3.0-0
- moved to usptream version 3.0
- adjusted configs, removed lambda patch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-5
- improved Patch3, includeLambdas.patch to sort the lamdas t the bottom

* Thu Jan 17 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-4
- added depndence of procyon decompiler (currenlty under review
- added and applied Patch2, systemProcyon.patch to enable system procyon out of thebox
- added and applied Patch3, includeLambdas.patch to at least list lamdas untill fixed in upstream

* Thu Jan 10 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-3
- added depndence of fernflower decompiler
- added and applied Patch1, systemFernflower.patch to enable system fernflower

* Wed Nov 28 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 2.0-2
- fixed changelog

* Mon Nov 19 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 2.0-1
- fixed issues listed in review (rhbz#1636019)
- added installation of desktop file

* Wed Jun 06 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 1.1-1
- initial commit
