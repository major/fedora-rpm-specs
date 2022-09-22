%{?drupal7_find_provides_and_requires}

%global module ctools

Name:          drupal7-%{module}
Version:       1.15
Release:       9%{?dist}
Summary:       Primarily a set of APIs and tools to improve the developer experience

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 1.15)
Requires:      php-date
Requires:      php-gd
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-session
Requires:      php-spl

%description
This suite is primarily a set of APIs and tools to improve the developer
experience. It also contains a module called the Page Manager whose job
is to manage pages. In particular it manages panel pages, but as it grows
it will be able to manage far more than just Panels.

For the moment, it includes the following tools:
* Plugins -- tools to make it easy for modules to let other modules implement
      plugins from .inc files.
* Exportables -- tools to make it easier for modules to have objects that live
      in database or live in code, such as 'default views'.
* AJAX responder -- tools to make it easier for the server to handle AJAX
      requests and tell the client what to do with them.
* Form tools -- tools to make it easier for forms to deal with AJAX.
* Object caching -- tool to make it easier to edit an object across multiple
      page requests and cache the editing work.
* Contexts -- the notion of wrapping objects in a unified wrapper and providing
      an API to create and accept these contexts as input.
* Modal dialog -- tool to make it simple to put a form in a modal dialog.
* Dependent -- a simple form widget to make form items appear and disappear
      based upon the selections in another item.
* Content -- pluggable content types used as panes in Panels and other modules
      like Dashboard.
* Form wizard -- an API to make multi-step forms much easier.
* CSS tools -- tools to cache and sanitize CSS easily to make user-input CSS
      safe.

This package provides the following Drupal modules:
* bulk_export
* %{module}
* %{module}_access_ruleset
* %{module}_ajax_sample
* %{module}_custom_content
* %{module}_plugin_example
* page_manager
* stylizer
* term_depth
* views_content


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.15-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.15-1
- Updated to 1.15 (RHBZ #1541732)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.12-1
- Updated to 1.12 (RHBZ #1397368)

* Thu Nov 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.11-1
- Updated to 1.11 (RHBZ #1385608)

* Sun Sep 11 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.10-1
- Updated to 1.10 (RHBZ #1370660)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jared Smith <jsmith@fedoraproject.org> - 1.9-2
- Remove call to %%defattr macro, as it is no longer needed

* Tue Aug 25 2015 Jared Smith <jsmith@fedoraproject.org> - 1.9-1
- Update to upstream 1.9 release, including new features (1.9)
- This update includes security updates from the 1.8 release as well
- Upstream changelog at https://www.drupal.org/node/2554183

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Jared Smith <jsmith@fedoraproject.org> - 1.7-1
- Update to upstream 1.7 release for security fixes
- SA-CONTRIB-2015-079 details at https://www.drupal.org/node/2454909
- Full upstream changelog at https://www.drupal.org/node/2454883

* Sat Feb 07 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6-1
- Updated to 1.6 (BZ #1187880)

* Sat Dec 13 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5-1
- Updated to 1.5 (BZ #1166343)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Peter Borsa <peter.borsa@gmail.com> - 1.4-1
- Update to upstream 1.4 release for bug and security fixes
- Upstream changelog for this release is available at https://drupal.org/node/2194551

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 4 2013 Peter Borsa <peter.borsa@gmail.com> - 1.3-1
- Upstream 1.3 release
- SA-CONTRIB-2013-041

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Peter Borsa <peter.borsa@gmail.com> - 1.2-1
- Update to upstream 1.2 release

* Thu Aug 09 2012 Peter Borsa <peter.borsa@gmail.com> - 1.1-1
- Update to upstream 1.1 release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Jared Smith <jsmith@fedoraproject.org> - 1.0-1
- Update to upstream 1.0 release

* Wed Mar 28 2012 Jared Smith <jsmith@fedoraproject.org> - 1.0-0.2.rc2
- Update to upstream rc2 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 11 2011 Jared Smith <jsmith@fedoraproject.org> - 1.0-0.1.rc1
- Initial version for Drupal 7

* Sat Aug 06 2011 Jared Smith <jsmith@fedoraproject.org> - 1.0-rc1
- Initial version for Drupal 7
