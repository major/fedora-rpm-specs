%{?drupal7_find_provides_and_requires}

%global module i18n

Name:          drupal7-%{module}
Version:       1.26
Release:       9%{?dist}
Summary:       Enables multilingual content

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# i18n.info
Requires:      drupal7(locale)
Requires:      drupal7(variable)
# phpcompatinfo (computed from version 1.26)
Requires:      php-pcre

%description
This is a collection of modules to extend Drupal core multilingual capabilities
and be able to build real life multilingual sites. Some features:

* Taxonomy translation (both, per language terms and translatable terms)
* Multilingual variables
* Multilingual blocks (control visibility per language and translate title and
  content)
* Language selection (when you switch the site language you'll see only the
  content for that language)

Read a complete feature overview in the Internationalization handbook: Building
multilingual sites [1].

This package provides the following Drupal modules:
* %{module}
* %{module}_block
* %{module}_contact
* %{module}_field
* %{module}_forum
* %{module}_menu
* %{module}_node
* %{module}_path
* %{module}_redirect
* %{module}_select
* %{module}_string
* %{module}_sync
* %{module}_taxonomy
* %{module}_translation
* %{module}_user
* %{module}_variable

[1] https://www.drupal.org/node/133977


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/
for SUB_MODULE in block contact field forum menu node path redirect select string sync taxonomy translation user variable
do
    SUB_MODULE=i18n_${SUB_MODULE}
    mkdir .rpm/docs/${SUB_MODULE}
    mv ${SUB_MODULE}/*.txt .rpm/docs/${SUB_MODULE}/
done


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.26-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.26-1
- Updated to 1.26 (RHBZ #1569976)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.18-1
- Updated to 1.18 (RHBZ #1462473)

* Sat Apr 29 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.17-1
- Updated to 1.17 (RHBZ #1443260)

* Sun Feb 26 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.15-1
- Updated to 1.15 (RHBZ #1417909)
- Add additional README.txt files to %%doc

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.14-1
- Updated to 1.14 (RHBZ #1387880)

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.13-3
- Minor spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.13-1
- Updated to 1.13 (BZ #1219472)
- Keep documentation where end-users expect it

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.12-1
- Updated to 1.12 (BZ #1186193)
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Peter Borsa <peter.borsa@gmail.com> - 1.11-1
- Update to upstream 1.11 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2242497

* Thu Aug 22 2013 Peter Borsa <peter.borsa@gmail.com> - 1.10-1
- Update to upstream 1.10 release for security and bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2070589

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Peter Borsa <peter.borsa@gmail.com> - 1.9-1
- Update to 1.9

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Feb 10 2013 Scott Dodson <sdodson@redhat.com> 1.8-0
- Update to 1.8
- Make sure drupal7-variable > 2.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Peter Borsa <peter.borsa@gmail.com> - 1.7-1
- Update to 1.7

* Wed Jun 27 2012 Scott Dodson <sdodson@redhat.com> - 1.6-0
- Update to 1.6 BZ834182

* Wed Apr 25 2012 Scott Dodson <sdodson@redhat.com> - 1.5-0
- Update to 1.5 BZ814917

* Mon Feb 06 2012 Scott Dodson <sdodson@redhat.com> - 1.4-0
- Update to 1.4 BZ781352

* Tue Jan 17 2012 Scott Dodson <sdodson@redhat.com> - 1.3-0
- Update to 1.3 Bug 781352

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 7 2011 Scott Dodson <sdodson@redhat.com - 1.2-0
- Update to 1.2 BZ757677

* Sun Nov 6 2011 Scott Dodson <sdodson@redhat.com> - 1.1-1
- Update to 1.1

* Wed Aug 31 2011 Scott Dodson <sdodson@redhat.com> - 1.0-1
- Initial Packaging
