Name:           apache-commons-pool
Version:        1.6
Release:        40%{?dist}
Summary:        Apache Commons Pool Package
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://commons.apache.org/pool/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://www.apache.org/dist/commons/pool/source/commons-pool-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

%description
The goal of Pool package is it to create and maintain an object (instance)
pooling package to be distributed under the ASF license. The package should
support a variety of pool implementations, but encourage support of an
interface that makes these implementations interchangeable.

%{?javadoc_package}

%prep
%autosetup -p1 -n commons-pool-%{version}-src

# Compatibility links
%mvn_alias : org.apache.commons:commons-pool
%mvn_file : commons-pool %{name}

%build
%mvn_build -- -Dcommons.packageId=pool

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.txt RELEASE-NOTES.txt

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6-39
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.6-37
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 31 2024 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-36
- Port to apache-commons-parent 65

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.6-30
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.6-29
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 8 2021 Christian Schuermann <spike@fedoraproject.org> 1.6-27
- Cleanup spec file
- Enable tests

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.6-23
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Mat Booth <mat.booth@redhat.com> - 1.6-21
- Set compiler source and target to fix FTBFS

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Mat Booth <mat.booth@redhat.com> - 1.6-19
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-13
- Regenerate build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-10
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-8
- Use Requires: java-headless rebuild (#1067528)

* Thu Aug  8 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-7
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Mat Booth <fedora@matbooth.co.uk> - 1.6-5
- Add missing BuildRequires maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-3
- Install NOTICE file with javadoc package

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Alexander Kurtakov <akurtako@redhat.com> 1.6-1
- Update to latest release - 1.6.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5.7-1
- Update to latest version (1.5.7).

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5.6-2
- Adapt to current guidelines.

* Fri Apr 15 2011 Chris Spike <spike@fedoraproject.org> 1.5.6-1
- Updated to 1.5.6
- Fixed build for maven 3

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-4
- Removed maven* BRs in favour of apache-commons-parent
- Added deprecated groupId to depmap for compatibility reasons

* Mon Oct 18 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-3
- Removed Epoch

* Tue Oct 5 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-2
- Consistently using 'buildroot' macro instead of 'RPM_BUILD_ROOT' now

* Fri Oct 1 2010 Chris Spike <spike@fedoraproject.org> 1.5.5-1
- Rename and rebase from jakarta-commons-pool
