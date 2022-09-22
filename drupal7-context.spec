%{?drupal7_find_provides_and_requires}

%global module context

Name:          drupal7-%{module}
Version:       3.10
Release:       9%{?dist}
Summary:       Allows contextual conditions and reactions management

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# context.info
Requires:      drupal7(ctools)
# phpcompatinfo (computed from version 3.10)
Requires:      php-json
Requires:      php-pcre

%description
Context allows you to manage contextual conditions and reactions for different
portions of your site. You can think of each context as representing a "section"
of your site. For each context, you can choose the conditions that trigger this
context to be active and choose different aspects of Drupal that should react to
this active context.

Think of conditions as a set of rules that are checked during page load to see
what context is active. Any reactions that are associated with active contexts
are then fired.

This package provides the following Drupal modules:
* %{module}
* %{module}_layouts
* %{module}_ui


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
# Docs used at runtime
#mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
# Docs used at runtime
#%%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.10-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.10-1
- Updated to 3.10 (RHBZ #1683780 / SA-CONTRIB-2019-028)
- https://www.drupal.org/sa-contrib-2019-028

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.7-1
- Updated to 3.7 (RHBZ #1337356)
- Minor spec cleanups

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 13 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.6-1
- Updated to 3.6 (DRUPAL-SA-CONTRIB-2015-004 / BZ #1180429)

* Sat Dec 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.5-1
- Updated to 3.5 (BZ #1175146)

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.3-2
- Don't exclude *.txt in module directory

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.3-1
- Updated to 3.3 (BZ #1148310)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2-1
- Updated to 3.2 (BZ #1059560; release notes https://drupal.org/node/2183729)
- Spec cleanup

* Fri Nov 08 2013 Peter Borsa <peter.borsa@gmail.com> - 3.1-1
- Update to upstream 3.1 release for bug fixes
- Upstream changelog for this release: https://drupal.org/node/2113785
- Fixes CVE-2013-4445, CVE-2013-4446 BZ 1020777, BZ 1020262, BZ 1020781, BZ 1020784

* Sat Sep 28 2013 Scott Dodson <sdodson@redhat.com> - 3.0-0.7.rc1
- Update to upstream 3.0-rc1
- Upstream changelog for this release is available at https://drupal.org/node/2098831

* Wed Aug 07 2013 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.6.beta7
- Update to upstream 3.0-beta7 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2052487

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.5.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.4.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 03 2013 Scott Dodson <sdodson@redhat.com> - 3.0.0.3.beta6
- Update to 3.0-beta6
- Fixes CVE-2012-5655 BZ891586, BZ891587

* Sun Dec 09 2012 Scott Dodson <sdodson@redhat.com> - 3.0-0.3.beta5
- Update to 3.0-beta5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.3.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Scott Dodson <sdodson@redhat.com> - 3.0-0.2.beta3
- Update to beta3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.2.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Scott Dodson <sdodson@redhat.com> - 3.0-0.1.beta2
- Update to beta2

* Wed Aug 31 2011 Scott Dodson <sdodson@redhat.com> - 3.0-0.1.beta1
- Initial Packaging
