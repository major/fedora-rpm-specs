Name:          serp
Version:       1.15.2
Release:       0.20.20150412cvs%{?dist}
Summary:       Byte-code manipulation framework
License:       BSD
Url:           http://serp.sourceforge.net/
# cvs -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp login
# cvs -z3 -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp  export -r HEAD serp
# tar cJf serp-1.15.2-20150412-cvs.tar.xz serp
Source0:       serp-1.15.2-20150412-cvs.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
The goal of the serp byte-code framework is to tap the full 
power of byte-code modification while lowering its associated
costs. The framework provides a set of high-level APIs for 
manipulating all aspects of byte-code, from large-scale 
structures like class member fields to the individual 
instructions that comprise the code of methods. While in 
order to perform any advanced manipulation, some understanding 
of the class file format and especially of the JVM instruction 
set is necessary, the framework makes it as easy as possible
to enter the world of byte-code development.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_remove_plugin :jxr-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :surefire-report-maven-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']"

%mvn_file :%{name} %{name}
%mvn_alias :%{name} %{name}:%{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.20.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.15.2-0.19.20150412cvs
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.15.2-0.18.20150412cvs
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.17.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.16.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.15.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.14.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.15.2-0.13.20150412cvs
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.12.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.11.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.10.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.9.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.8.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.7.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.6.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 gil cattaneo <puntogil@libero.it> 1.15.2-0.5.20150412cvs
- regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-0.4.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 gil cattaneo <puntogil@libero.it> 1.15.2-0.3.20150412cvs
- rebuilt

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.2-0.2.20150412cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 gil cattaneo <puntogil@libero.it> 1.15.2-0.1.20150412cvs
- update to 1.15.2

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.14.2-0.9.20120406cvs
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-0.8.20120406cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.14.2-0.7.20120406cvs
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-0.6.20120406cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 gil cattaneo <puntogil@libero.it> 1.14.2-0.5.20120406cvs
- build with XMvn
- minor changes to adapt to current guideline

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-0.4.20120406cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.14.2-0.3.20120406cvs
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-0.2.20120406cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 06 2012 gil cattaneo <puntogil@libero.it> 1.14.2-0.1.20120406cvs
- initial rpm
