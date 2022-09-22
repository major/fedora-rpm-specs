%{?drupal7_find_provides_and_requires}

%global module feeds
%global pre_release beta4

Name:          drupal7-%{module}
Version:       2.0
Release:       0.30%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Aggregates RSS/Atom/RDF feeds, imports CSV files and more

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# feeds.info
Requires:      drupal7(ctools)
Requires:      drupal7(job_scheduler)
# phpcompatinfo (computed from version 2.0-beta4)
Requires:      php-curl
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-libxml
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xml


%description
Import or aggregate data as nodes, users, taxonomy terms or simple database
records.

This package provides the following Drupal modules:
* %{module}
* %{module}_import
* %{module}_news (requires drupal7-features and drupal7-views)
* %{module}_ui

%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.30.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.29.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.28.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.27.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.26.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.25.beta4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.24.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.23.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.22.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.21.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.20.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.19.beta4
- Update to 2.0-beta4 (RHBZ #1495024)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.18.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.17.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.16.beta3
- Update to 2.0-beta3 (RHBZ #1398472)

* Mon Aug 01 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.15.beta2
- Update to 2.0-beta2 (RHBZ #1310474)
- Removed %%defattr

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.14.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.13.beta1
- Update to 2.0-beta1 (RHBZ #1242139)

* Wed Jul 01 2015 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.12.alpha9
- Update to 2.0-alpha9
- Release notes can be found at https://www.drupal.org/node/2507273

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.11.alpha8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.10.alpha8
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.9.alpha8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.8.alpha8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.7.alpha8
- Fix versioning to be newer than alpha7 release

* Tue Apr 23 2013 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.1.alpha8
- Update to upstream alpha8 bug fix release
- Upstream changelog for the bug fixes in this release is at http://drupal.org/node/1977140

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.7.alpha7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.5.alpha7
- Bug fix update for Drupal issue #1807920: Imported nodes have NULL format.

* Wed Oct 10 2012 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.5.alpha6
- Security fix

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.4.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 02 2012 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.3.alpha5
- New upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.2.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 23 2011 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.1.alpha4
- Initial packaging
