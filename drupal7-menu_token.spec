%{?drupal7_find_provides_and_requires}

%global module menu_token
%global pre_release beta7

Name:          drupal7-%{module}
Version:       1.0
Release:       0.22%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Provides tokens in menu items (links)

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# menu_token.info
Requires:      drupal7(ctools)
Requires:      drupal7(entity)
Requires:      drupal7(menu)
Requires:      drupal7(token)
Requires:      drupal7(uuid)
# phpcompatinfo (computed from version 1.0-beta7)
#     <none>


%description
Menu Token module provides tokens, that could be used in title or in
path of menu items (links). For example, if you create a menu item with
path:"user/[current-user:uid]", the url will be changed "on fly" to:
"user/1" (assuming you are user 1).

Tokens are provided by Token [1] module. Menu Token allows to use both
global tokens and entity ones: node, user, term, etc. Entity tokens have
several methods of substitution: from context, random and user defined.

This package provides the following Drupal 7 module:
* %{module}

[1] https://www.drupal.org/project/token


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
#mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
#%%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.19.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.17.beta7
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.9.beta7
- Updated to 1.0-beta7 (RHBZ #1287336)
- Spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.8.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.4.beta5
- Update to upstream 1.0-beta5 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2019931

* Sun Feb 10 2013 Scott Dodson <sdodson@redhat.com> - 1.0-0.3.beta4
- Update to 1.0-beta4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 24 2012 Scott Dodson <sdodson@redhat.com - 1.0-0.2.beta1
- Upstream update to beta1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 4 2011 Scott Dodson <sdodson@redhat.com> - 1.0-0.1.alpha3
- Initial Drupal 7 Package
