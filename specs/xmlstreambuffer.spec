Name:           xmlstreambuffer
Version:        2.1.0
Release:        8%{?dist}
Summary:        Stream Based Representation for XML Infoset
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/eclipse-ee4j/metro-xmlstreambuffer
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/metro-xmlstreambuffer-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(junit:junit)

%description
Stream based representation for XML infoset.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n metro-xmlstreambuffer-%{version}

pushd streambuffer

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_dep :woodstox-core
popd

%build
pushd streambuffer
%mvn_build
popd

%install
pushd streambuffer
%mvn_install
popd

%files -f streambuffer/.mfiles
%license LICENSE.md NOTICE.md
%doc CONTRIBUTING.md README.md

%files javadoc -f streambuffer/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.1.0-5
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Marian Koncek <mkoncek@redhat.com> - 2.1.0-1
- Update to upstream version 2.1.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.10-6
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.10-5
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.5.10-3
- Remove workaround for SUREFIRE-1897

* Fri Oct 29 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.5.10-2
- Remove javadoc package

* Sat Oct 23 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.5.10-1
- Update to version 1.5.10
- Add javadoc package
- Enable test
- Simplified module-info.class build

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Dogtag PKI Team <pki-devel@redhat.com> - 1.5.9-4
- Drop test dependencies

* Fri Jun 04 2021 Dogtag PKI Team <pki-devel@redhat.com> - 1.5.9-3
- Disable tests

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5.9-1
- Update to version 1.5.9.

* Fri Aug 07 2020 Mat Booth <mat.booth@redhat.com> - 1.5.4-15
- Allow building on JDK 11 and correct license tag

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.5.4-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 gil cattaneo <puntogil@libero.it> 1.5.4-4
- add missing build requires: maven-plugin-bundle

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 gil cattaneo <puntogil@libero.it> 1.5.4-1
- update to 1.5.4
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.5.1-4
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 gil cattaneo <puntogil@libero.it> 1.5.1-2
- switch to XMvn, minor changes to adapt to current guideline

* Tue Oct 30 2012 gil cattaneo <puntogil@libero.it> 1.5.1-1
- update to 1.5.1

* Wed Oct 03 2012 gil cattaneo <puntogil@libero.it> 1.5-1
- update to 1.5

* Sat Mar 31 2012 gil cattaneo <puntogil@libero.it> 1.4-1
- initial rpm
