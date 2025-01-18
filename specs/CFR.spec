Name:           CFR
Version:        0.151
Release:        17%{?dist}
Summary:        CFR - Another Java Decompiler

License:        MIT
URL:            https://github.com/leibnitz27/cfr
Source0:        https://github.com/leibnitz27/cfr/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin

Requires:       java-headless
Requires:       javapackages-tools

Provides:       cfr
Provides:       Cfr

%global lowercase_name cfr
%global build_folder %{lowercase_name}-%{version}

%description
CFR will decompile modern Java features - including much of Java 9, 12 & 14,
but is written entirely in Java 6, so will work anywhere!
It'll even make a decent go of turning class files from other JVM languages back into java!

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%autosetup -n %{build_folder}
%pom_remove_plugin :git-commit-id-plugin
%pom_remove_plugin :templating-maven-plugin
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin
sed "s;<javaVersion>1.6</javaVersion>;<javaVersion>1.8</javaVersion>;" -i pom.xml

# workaround for template-maven-plugin
sed -i 's/${project.version}/%{version}/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
sed -i 's/${git.commit.id.abbrev}/%{version}/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
sed -i 's/${git.dirty}/false/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
cp %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java %{_builddir}/%{build_folder}/src/org/benf/cfr/reader/util/CfrVersionInfo.java


%build
%mvn_build


%install
rm -rf $RPM_BUILD_ROOT
%mvn_install
%jpackage_script org.benf.cfr.reader.Main "" "" %{name}/%{name} %{lowercase_name}


%files -f .mfiles
%license LICENSE
%doc README.md
%{_bindir}/%{lowercase_name}


%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.151-15
- Rebuilt for java-21-openjdk as system jdk

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.151-14
- Rebuilt for java-21-openjdk as system jdk

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.151-8
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.151-7
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 ohrdlick <ohrdlick@redhat.com> - 0.151-5
- bumped javaVersion from 1.6 to 1.8 to make jdk17 happy

* Fri Aug 06 2021 ohrdlick <ohrdlick@redhat.com> - 0.151-4
- Added Provides attributes serving as package aliases

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.151-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 ohrdlicka <ohrdlick@redhat.com> - 0.151-1
- Initial 0.151 release
