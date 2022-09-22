%{?drupal7_find_provides_and_requires}

%global module ds

Name:          drupal7-%{module}
Version:       2.16
Release:       9%{?dist}
Summary:       Extend the display options for every entity type

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# ds.info
Requires:      drupal7(ctools)
# phpcompatinfo (computed from version 2.16)
Requires:      php-pcre

%description
Display Suite allows you to take full control over how your content is displayed
using a drag and drop interface. Arrange your nodes, views, comments, user data
etc. the way you want without having to work your way through dozens of template
files. A predefined list of layouts (D7 only) is available for even more drag
and drop fun!

By defining custom view modes (build modes in D6), you can define how one piece
of content should be displayed in different places such as teaser lists, search
results, the full node, views etc.

Watch a screen-cast (http://drupal.org/node/644706) to see it all in action!

This package provides the following Drupal modules:
* %{module}
* %{module}_devel (NOTE: Requires install of the devel module)
* %{module}_extras
* %{module}_format
* %{module}_forms
* %{module}_search
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.16-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.16-1
- Updated to 2.16 (RHBZ #1569266 / SA-CONTRIB-2018-019)
- https://www.drupal.org/sa-contrib-2018-019

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.14-1
- Updated to 2.14 (RHBZ #1299271)
- Removed %%defattr

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.11-1
- Updated to 2.11 (RHBZ #1246471)

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.10-1
- Updated to 2.10 (RHBZ #1223769)
- Keep documentation where end-users expect it

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Peter Borsa <peter.borsa@gmail.com> 2.8-1
- Updated to 2.8 (BZ #1212234)

* Sun Nov 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 2.7-1
- Updated to 2.7 (BZ #1159477)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 11 2013 Peter Borsa <peter.borsa@gmail.com> - 2.6-1
- Update to upstream 2.6 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2081631

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4-2
- Fixed dependency typo (drupal7-cools => drupal7-ctools)

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4-1
- Updated to 2.4
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.2-1
- Initial package
