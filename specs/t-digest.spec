%global url     https://github.com/tdunning/%{name}

Name:           t-digest
Version:        3.2
Release:        11%{?dist}
Summary:        A new data structure for on-line accumulation of statistics
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{url}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
#grep -ir -e "<p/>"
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TreeDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/ArrayDigest.java
Patch0:         jdk8-javadoc.patch
Patch1:         sourceTarget.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local

Requires:       java

%description
A new data structure for accurate on-line accumulation of rank-based statistics
eg. quantiles and trimmed means. The t-digest algorithm is also very parallel
friendly making it useful in map-reduce and parallel streaming applications.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep 
%setup -q -n %{name}-%{name}-%{version}
#%%patch0
%patch -P1
# Useless tasks, pom_remove_plugin is in maven-local pkg
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin com.carrotsearch.randomizedtesting

%build
#skipping tests, they requires currently unpacked depndences
%mvn_build --force

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICES

%files javadoc  -f .mfiles-javadoc
%license LICENSE NOTICES

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.2-8
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.2-3
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.2-2
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-1
- updated to 3.2
- uapplied patch0         jdk8-javadoc.patch
- added and applied  patch1         sourceTarget.patch

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Fabio Valentini <decathorpe@gmail.com> - 3.0-14
- Package javadocs again since they're built anyway.
- Fixes building the package with Java 11.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-13
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon May 04 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12
- dropping javadoc to build with jdk11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 gil cattaneo <puntogil@libero.it> 3.0-4
- remove useless plugin
- remove duplicate files
- introduce license macro

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Jiri Vanek <jvanek@redhat.com> - 3.0-2
- added  patch0, jdk8-javadoc.patch (will be upstreamed)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jul 20 2014 Jiri Vanek <jvanek@redhat.com> - 3.0-1
- Initial packaging
