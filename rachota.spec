%global checkout 602hg
Name:           rachota
Version:        2.4
Release:        2.%{checkout}%{?dist}
Summary:        Straightforward timetracking

License:        CDDL-1.0
URL:            http://rachota.sourceforge.net/en/index.html
## Upstream does not provide any source tarball.
## We have to check them out via mercurial.
# hg clone http://hg.code.sf.net/p/rachota/code rachota
# cd rachota
# hg update -c 602
# cd ..
# tar caf rachota.tar.gz rachota
Source0:        %{name}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  jpackage-utils

BuildRequires:  junit

BuildRequires:  maven-local

BuildRequires:  desktop-file-utils

Requires:       jpackage-utils

Requires:       java

%description
Rachota is a portable application for timetracking different projects. It runs
everywhere. It displays time data in diagram form, creates customized reports
and invoices or analyses measured data and suggests hints to improve user's
time usage. The totally portable yet personal timetracker. 

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%build
%mvn_build

%install
%mvn_install

%jpackage_script org.cesilko.rachota.gui.MainWindow "" "" %{name} %{name} true

install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}



%files -f .mfiles
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files javadoc -f .mfiles-javadoc


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2.602hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 20 2022 Willmann Sébastien <sebastien.willmann@gmail.com> - 2.4-1.602hg
- Fix build by updating to latest version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-26.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.3-25.20130104cvs
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3-24.20130104cvs
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-23.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-22.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-21.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-20.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.3-19.20130104cvs
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-18.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-17.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-16.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-15.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-14.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-13.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-12.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-11.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 2.3-10.20130104cvs
- Fixed build failure due to doclint

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-9.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-8.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-6.20130104cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 05 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 2.3-5.20130104cvs
- Update to last cvs version

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4.20120110cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 2.3-3.20120110cvs
- Rachota now creates configuration in home: patch not needed anymore

* Sun Jan 08 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 2.3-2.20111231cvs
- Replaced cp by install
- Removed .jar and .class cleanup, since there is nothing to cleanup
- Changed patch: now storing configuration in $HOME/.config/rachota

* Sun Jan 01 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 2.3-1.20111231cvs
- Spec file creation

