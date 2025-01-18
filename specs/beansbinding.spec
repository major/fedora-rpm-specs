Name:           beansbinding
Version:        1.2.1
Release:        39%{?dist}
Summary:        Beans Binding (JSR 295) reference implementation

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://beansbinding.dev.java.net/
Source0:        https://beansbinding.dev.java.net/files/documents/6779/73673/beansbinding-1.2.1-src.zip
Patch0:         disable-doclint.patch
Patch1:         new-source-target.patch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel

Requires:       java >= 1:1.6.0
Requires:       javapackages-tools

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
In essence, Beans Binding (JSR 295) is about keeping two properties 
(typically of two objects) in sync. An additional emphasis is placed 
on the ability to bind to Swing components, and easy integration with 
IDEs such as NetBeans. This project provides the reference implementation.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -n %{name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
# remove all binary libs
find . -type f \( -iname "*.jar" -o -iname "*.zip" \) -print0 | xargs -t -0 %{__rm} -f

%build
%{ant} dist

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc license.txt releaseNotes.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-38
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.2.1-36
- Rebuilt for java-21-openjdk as system jdk

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.1-30
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.1-29
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.1-24
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 08 2020 Omair Majid <omajid@redhat.com> - 1.2.1-23
- Fix building against OpenJDK 11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Omair Majid <omajid@redhat.com> - 1.2.1-16
- Add BuildRequires on java-devel
- Resolves RHBZ 1423272

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Omair Majid <omajid@redhat.com> - 1.2.1-14
- Update to comply with latest packaging guidelines
- Require javapackges-tools

* Mon Jun 22 2015 Omair Majid <omajid@redhat.com> - 1.2.1-13
- Disable doclint

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Omair Majid <omajid@redhat.com> - 1.2.1-11
- Update to work with latest guidelines
- Fix build dependencies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 20 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.1-3
- Canonical using of %%{__rm}
- The %%{ant} macro is used instead of the ant command
- Redundant export of the $JAVA_HOME environment variable is removed
  in the %%build script

* Wed Aug 14 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.1-2
- java-devel & jpackage-utils are added as the build requirements
- jpackage-utils is added as the run-time requirement
- Appropriate values of Group Tags are chosen from the official list
- Redundant run-time requirements for /bin/* utilities are removed
- A ghost symlink for javadoc package is removed
- Documentation added

* Tue Jul 08 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.1-1
- Changing for Fedora

* Thu Dec 13 2007 Jaroslav Tulach <jtulach@mandriva.org> 0:1.2.1-1mdv2008.1
+ Revision: 119152
- First package of beansbinding library
- create beansbinding
