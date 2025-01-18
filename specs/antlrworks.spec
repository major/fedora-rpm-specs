Name:           antlrworks
Version:        1.5.2
Release:        32%{?dist}
Summary:        Grammar development environment for ANTLR v3 grammars

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.antlr3.org/works
Source0:        https://github.com/antlr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
# Fix compilation with JGoodies Forms >= 1.7.1
Patch0:         %{name}-1.5.2-jgoodies-forms_1.7.1.patch
# Add xdg-open to the list of available browsers to open the help
Patch1:         %{name}-1.5.2-browsers.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-forms)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:stringtemplate)
Requires:       graphviz
# Owns /usr/share/icons/hicolor
Requires:       hicolor-icon-theme
# Antlrworks requires javac
Requires:       java-devel >= 1:1.6.0
# Explicit requires for javapackages-tools since antlrworks-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
ANTLRWorks is a novel grammar development environment for ANTLR v3 grammars
written by Jean Bovet (with suggested use cases from Terence Parr). It combines
an excellent grammar-aware editor with an interpreter for rapid prototyping and
a language-agnostic debugger for isolating grammar errors. ANTLRWorks helps
eliminate grammar nondeterminisms, one of the most difficult problems for
beginners and experts alike, by highlighting nondeterministic paths in the
syntax diagram associated with a grammar. ANTLRWorks' goal is to make grammars
more accessible to the average programmer, improve maintainability and
readability of grammars by providing excellent grammar navigation and
refactoring tools, and address the most common questions and problems
encountered by grammar developers.


%prep
%autosetup -p0

# Remove MacOSX-specific code
rm -r src/org/antlr/xjlib/appkit/app/MacOS/

# remove unnecessary dependency on deprecated parent pom
%pom_remove_parent

%pom_remove_dep com.apple:AppleJavaExtensions
%pom_change_dep com.jgoodies:forms com.jgoodies:jgoodies-forms

# remove maven-compiler-plugin configuration that's broken with Java 11
%pom_remove_plugin :maven-compiler-plugin


%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8


%install
%mvn_install

%jpackage_script org.antlr.works.IDE "-Xmx400m" "" antlrworks:antlr:antlr3:antlr3-runtime:jgoodies-common:jgoodies-forms:stringtemplate:stringtemplate4 %{name} false

desktop-file-install \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

install -Dpm 0644 resources/icons/app.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for i in 16 32 64; do
  install -Dpm 0644 resources/icons/app_${i}x$i.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x$i/apps/%{name}.png
done

install -Dpm 0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata/%{name}.appdata.xml


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files -f .mfiles
%doc History.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/appdata/*.appdata.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.2-31
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.5.2-29
- Rebuilt for java-21-openjdk as system jdk

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.2-23
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.2-22
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.5.2-17
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5.2-16
- Override javac source and target version to fix builds using Java 11.

* Sat Apr 25 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5.2-15
- Remove unnecessary dependency on deprecated parent pom.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1.5.2-11
- Add explicit requirement for javapackages-tools for antlrworks
  script which uses java-functions. See RHBZ#1600426.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.2-8
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.2-6
- Build antlrworks using Maven
- Spec cleanup
- Add AppData file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.2-3
- Fix build with latest versions of stringtemplate4

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jul 11 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-9
- Fix compilation with JGoodies Forms 1.7.1

* Tue Jan 29 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-8
- Fix compilation with JGoodies Forms 1.6.0 (thanks to Mary Ellen Foster)

* Mon Jan 28 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-7
- Add missing Requires on antlr-tool (RHBZ #904572), until RHBZ #904979 is fixed

* Sat Jul 21 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-6
- Add stringtemplate as BuildRequires

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-4
- Add missing jgoodies-common jar in wrapper script

* Tue Feb 07 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-3
- Add version condition on antlr3-tool
- Fix wrapper script generation

* Thu Feb 02 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-2
- Remove unintended line break

* Thu Feb 02 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4-6
- Add jgoodies-common jar in the launcher classpath
- Fix compilation with JGoodies Common 1.4.2
- Spec cleanup

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 12 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.4-4
- Bump release

* Fri Jun  4 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.4-3
- Remove manual installation of antlrworks.desktop (managed by
  desktop-file-install)

* Thu Jun  3 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.4-2
- Remove release.txt and readme.txt from sources
- Add hicolor-icon-theme as a Requires since it owns
  %%{_datadir}/icons/hicolor
- Add call to desktop-file-install

* Fri May 14 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.4-1
- Initial RPM release
