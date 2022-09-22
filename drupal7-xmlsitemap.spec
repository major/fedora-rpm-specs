%{?drupal7_find_provides_and_requires}

%global module xmlsitemap

Name:          drupal7-%{module}
Version:       2.6
Release:       9%{?dist}
Summary:       Creates an XML sitemap conforming to the sitemaps.org protocol

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 2.6)
Requires:      php-date
Requires:      php-pcre
Requires:      php-xmlwriter

%description
The XML sitemap module creates a sitemap that conforms to the sitemaps.org
specification [1]. This helps search engines to more intelligently crawl a
website and keep their results up to date. The sitemap created by the module
can be automatically submitted to Ask, Google, Bing (formerly Windows Live
Search), and Yahoo! search engines. The module also comes with several
submodules that can add sitemap links for content, menu items, taxonomy
terms, and user profiles.

Please read the included README.txt [2], the handbook documentation [3],
and the current list of known issues [4]for more information before using
the module.

This package provides the following Drupal modules:
* %{module}
* %{module}_custom
* %{module}_engines
* %{module}_i18n
* %{module}_menu
* %{module}_node
* %{module}_taxonomy
* %{module}_user

[1] http://sitemaps.org/
[2] https://cgit.drupalcode.org/xmlsitemap/tree/README.txt
[3] https://www.drupal.org/handbook/modules/xmlsitemap
[4] https://www.drupal.org/node/482550


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6-1
- Update to 2.6 (RHBZ #1602973 / SA-CONTRIB-2018-053)
- https://www.drupal.org/sa-contrib-2018-053
- Spec and repo cleanup

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 23 2015 Peter Borsa <peter.borsa@gmail.com> 2.2-1
- Update to 2.2
- Upstream release notes can be found at https://www.drupal.org/node/2417069

* Sun May 25 2014 Peter Borsa <peter.borsa@gmail.com> 2.0-1
- Initial package
