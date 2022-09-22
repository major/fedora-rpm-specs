%{?drupal7_find_provides_and_requires}

%global module crumbs

Name:          drupal7-%{module}
Version:       2.7
Release:       9%{?dist}
Summary:       The ultimate breadcrumbs module

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 2.7)
Requires:      php-date
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

%description
Crumbs is a powerful breadcrumb-building machine, generating high-quality
breadcrumbs for most every page on your site, with minimal configuration.

The Crumbs engine takes advantage of the hierarchical nature inherent to
breadcrumbs: It calculates the parent of the current page, the parent of
the parent, etc, until it has the complete breadcrumb trail.

Crumbs uses plugins with fine-grained user-defined priorities, for each
step in this process. Plugins for most of your favorite modules are already
built-in, and you can add more.

A lot of stuff that would require laborious configuration with other
breadcrumb-building modules, does work out of the box with Crumbs. And if it
doesn't, there are powerful and ways to configure, customize and extend.

Where in other breadcrumb-customizing modules you need to define complete
breadcrumbs for various pages and their all their children, in Crumbs you
mostly just say "A is the parent of B", and it can solve all the rest of
the puzzle by itself.

This package provides the following Drupal modules:
* %{module}
* %{module}_example (requires manual install of xautoload)
* %{module}_labs


%prep
%setup -qn %{module}

: Remove executable bits
find . -type f -perm /+x -print0 | xargs -0 chmod -x

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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7-1
- Update to 2.7 (RHBZ #1583178)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6-1
- Updated to 2.6 (RHBZ #1497438)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 31 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5-1
- Updated to 2.5 (RHBZ #1322633)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3-1
- Updated to 2.3 (SA-CONTRIB-2015-082 / BZ #1205941)

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2-1
- Updated to 2.2 (BZ #1150460)
- Removed RPM README b/c it only explained common Drupal workflow

* Wed Sep 24 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1-1
- Updated to 2.1 (BZ #1140107)
- %%license usage

* Thu Aug 07 2014 Peter Borsa <peter.borsa@gmail.com> 2.0-0.8.beta19
- Update to upstream 2.0-beta19 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2315031

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.7.beta13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Peter Borsa <peter.borsa@gmail.com> 2.0-0.6.beta13
- Update to upstream 2.0-beta13 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2167279

* Wed Sep 11 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.5.beta9
- Update to upstream 2.0-beta9 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2073701

* Sat Aug 17 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.4.beta7
- Update to upstream 2.0-beta7 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2067691

* Fri Aug 16 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.3.beta5
- Update to upstream 2.0-beta5 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2064257

* Tue Aug 13 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.2.beta4
- Update to upstream 2.0-beta4 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2063791

* Thu Aug 08 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.1.beta1
- Update to upstream 2.0-beta1 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2060015

* Wed Aug 07 2013 Peter Borsa <peter.borsa@gmail.com> - 1.10-1
- Update to upstream 1.10 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2051987

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.9-2
- Updated for drupal7-rpmbuild 7.22-5

* Sat May 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.9-1
- Initial package
