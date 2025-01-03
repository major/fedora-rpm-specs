Name:           Mars
Version:        4.5
Release:        29%{?dist}
Summary:        An interactive development environment for programming in MIPS assembly language

License:        MIT
URL:            http://courses.missouristate.edu/KenVollmar/MARS/
Source0:        https://github.com/dpetersanderson/MARS/releases/download/v.4.5.1/Mars4_5.jar
Source1:        Mars
Source2:        Mars.desktop
Source3:        build.xml
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  desktop-file-utils

Requires:       java

%description
MARS is a lightweight interactive development environment (IDE) for
programming in MIPS assembly language, intended for educational-level
use with Patterson and Hennessy's Computer Organization and Design.

%prep
%setup -q -c %{name}-%{version}

find . -name '*.jar'   -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

%build
sed -i 's/\r//' MARSlicense.txt

cp -p %{SOURCE3} build.xml
ant

%install
install -Dpm 644 %{name}.jar ${RPM_BUILD_ROOT}%{_javadir}/%{name}.jar
install -Dpm 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
desktop-file-install                                \
    --add-category="Development"                    \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE2}

%files
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_datadir}/applications/Mars.desktop
%doc MARSlicense.txt

%changelog
* Wed Jan 01 2025 W. Michael Petullo <mike@flyn.org> - 4.5-29
- Adjust to Mars moving to GitHub

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Marian Koncek <mkoncek@redhat.com> - 4.5-27
- Use system Java version

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 4.5-26
- Rebuilt for java-21-openjdk as system jdk

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 W. Michael Petullo <mike@flyn.org> - 4.5-22
- Remove jpackage-utils requirement; it is retired and not needed

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 W. Michael PEtullo <mike@flyn.org> - 4.5-20
- Build using Java 17

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 4.5-18
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.5-17
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 4.5-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 W. Michael Petullo <mike[@]flyn.org> - 4.5-8
- Fix BZ #1634466 by requiring java-1.8.0-openjdk

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Scott Tsai <scottt.tw@gmail.com> - 4.5-1
- Upstream 4.5

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Mat Booth <fedora@matbooth.co.uk> - 4.3-1
- Fix class not found exceptions at startup, rhbz#828973
- Also update to latest upstream
- Write a real build script to create the jar

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 06 2011 W. Michael Petullo <mike[@]flyn.org> - 4.1-3
- Ensure proper end of line encoding in MARSlicense.txt
- Add rm -rf $RPM_BUILD_ROOT

* Wed Feb 16 2011 W. Michael Petullo <mike[@]flyn.org> - 4.1-2
- Build 4.1 source

* Tue Jan 25 2011 W. Michael Petullo <mike[@]flyn.org> - 4.1-1
- New upstream version
- Replace tab with spaces
- Make setup quiet
- Add .desktop description
- Use noarch

* Thu Dec 23 2010 W. Michael Petullo <mike[@]flyn.org> - 4.0.1-1
- New upstream version
- Remove clean section
- Use SOURCE1 to install
- Add MARSlicense.txt
- Remove classpath definition from MANIFEST.MF

* Wed Nov 24 2010 W. Michael Petullo <mike[@]flyn.org> - 4.0-2
- Requires: jpackage-util to Requires: jpackage-utils

* Mon Aug 30 2010 W. Michael Petullo <mike[@]flyn.org> - 4.0-1
- Initial Fedora package
