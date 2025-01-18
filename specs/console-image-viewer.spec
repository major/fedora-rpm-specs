%global upstream ConsoleImageViewer
%global launcher consoleImageViewer

Name:    console-image-viewer

Version: 1.2
Release: 25%{?dist}
Summary: Terminal image viewer

License:  MIT
URL:      https://github.com/judovana/ConsoleImageViewer
Source0:  https://github.com/judovana/ConsoleImageViewer/archive/%{upstream}-%{version}.tar.gz
Source1:  %{launcher}.man

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires: java-devel
BuildRequires: ant

Requires: java
Requires: javapackages-tools

%description
Highly scale-able, high quality, image viewer for ANSI terminals.


%prep
%setup -q -n %{upstream}-%{upstream}-%{version}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
sed 's;<attribute name="Main-Class" value="${main.class}"/>;;' -i nbproject/build-impl.xml
sed "s;1.6;1.8;g" -i nbproject/project.properties

%build
ant


%install
mkdir -p $RPM_BUILD_ROOT/%{_javadir}
cp dist/%{upstream}.jar $RPM_BUILD_ROOT/%{_javadir}/%{upstream}.jar

mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cat <<EOF > $RPM_BUILD_ROOT/%{_bindir}/%{launcher}
#!/bin/bash
. /usr/share/java-utils/java-functions
MAIN_CLASS=org.judovana.linux.ConsoleImageViewer
set_classpath "%{upstream}-%{version}"
run \${@}
EOF

chmod 755 $RPM_BUILD_ROOT/%{_bindir}/%{launcher}

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
gzip -c %{SOURCE1}  > $RPM_BUILD_ROOT/%{_mandir}/man1/%{launcher}.1.gz

%files 
%{_javadir}/%{upstream}.jar
%{_bindir}/%{launcher}
%{_mandir}/man1/%{launcher}.1.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.2-23
- requiring full jre, instead of headless
- RHBZ#2123726

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.2-22
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.2-16
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2-15
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- bumed source/rarget reelase to 1.8

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Jiri Vanek <jvanek@redhat.com> - 1.2-1
- initial package
