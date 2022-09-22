%{?drupal7_find_provides_and_requires}

%global module jquery_update
%global pre_release alpha5

Name:          drupal7-%{module}
Version:       3.0
Release:       0.14%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Upgrades the version of jQuery in Drupal core to a newer version of jQuery

# License breakdown:
# - GPLv2+
#     - jquery_update Drupal module
# - (MIT and BSD and GPLv2) and (MIT and BSD and GPLv1):
#     - replace/jquery/1.5
#     - replace/jquery/1.6
#     - replace/jquery/1.7
# - MIT:
#     - replace/jquery/1.8
#     - replace/jquery/1.9
#     - replace/jquery/1.10
#     - replace/jquery/1.11
#     - replace/jquery/1.12
#     - replace/jquery/2.1
#     - replace/jquery/2.2
#     - replace/jquery/3.1
#     - replace/jquery-migrate/1
#     - replace/jquery-migrate/3
#     - replace/ui
# - MIT and GPLv1:
#     - replace/jquery.form/2
#     - replace/jquery.form/3
# - MIT and LGPLv3:
#     - replace/jquery.form/4
License:       GPLv2+ and (MIT and BSD and GPLv2) and (MIT and BSD and GPLv1) and MIT and (MIT and GPLv1) and (MIT and LGPLv3)
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 3.0-alpha5)
# <none>

# Bundled
## replace/jquery/1.5/
Provides:      bundled(js-jquery) = 1.5.1
## replace/jquery/1.6/
Provides:      bundled(js-jquery) = 1.6.4
## replace/jquery/1.7/
Provides:      bundled(js-jquery) = 1.7.2
## replace/jquery/1.8/
Provides:      bundled(js-jquery) = 1.8.3
## replace/jquery/1.9/
Provides:      bundled(js-jquery) = 1.9.1
## replace/jquery/1.10/
Provides:      bundled(js-jquery) = 1.10.2
## replace/jquery/1.11/
Provides:      bundled(js-jquery) = 1.11.2
## replace/jquery/1.12/
Provides:      bundled(js-jquery) = 1.12.4
## replace/jquery/2.1/
Provides:      bundled(js-jquery) = 2.1.4
## replace/jquery/2.2/
Provides:      bundled(js-jquery) = 2.2.4
## replace/jquery/3.1/
Provides:      bundled(js-jquery) = 3.1.1
## replace/jquery-migrate/1/
Provides:      bundled(js-jquery-migrate) = 1.4.1
## replace/jquery-migrate/3/
Provides:      bundled(js-jquery-migrate) = 3.0.0
## replace/jquery.form/2/
Provides:      bundled(js-jquery-form) = 2.69
## replace/jquery.form/3/
Provides:      bundled(js-jquery-form) = 3.51.0
## replace/jquery.form/4/
Provides:      bundled(js-jquery-form) = 4.0.1
## replace/ui/
Provides:      bundled(js-jquery-ui) = 1.10.2

%description
Upgrades the version of jQuery in Drupal core to a newer version of jQuery.

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.md .rpm/docs/
mkdir -p .rpm/docs/replace/ui
mv replace/ui/*.txt .rpm/docs/replace/ui/

: Remove unneeded file
rm -f replace/ui/ui/.jshintrc


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.14.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.13.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.12.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.11.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.10.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.9.alpha5
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.8.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.7.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.6.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.5.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.4.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.3.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.2.alpha5
- Updated to 3.0-alpha5 (RHBZ #1437265)

* Fri Mar 10 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.1.alpha4
- Updated to 3.0-alpha4 (RHBZ #1430714)
- Added license breakdown
- Updated license to include bundled licenses

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7-1
- Updated to 2.7 (RHBZ #1273670)
- SA-CONTRIB-2015-158: https://www.drupal.org/node/2598426
- Modified bundled(*) provides

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6-1
- Updated to 2.6 (RHBZ #1222725)
- SA-CONTRIB-2015-123: https://www.drupal.org/node/2507729
- Added bundled(*) provides
- Spec cleanup

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Peter Borsa <peter.borsa@gmail.com> - 2.5-1
- Update to 2.5 (BZ 1186191)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Peter Borsa <peter.borsa@gmail.com> - 2.4-1
- Update to upstream 2.4 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2231919

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Peter Borsa <peter.borsa@gmail.com> - 2.3-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 4 2011 Scott Dodson <sdodson@sdodson.com> - 2.2-1
- Initial Drupal 7 Package
