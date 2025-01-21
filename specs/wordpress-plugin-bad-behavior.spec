%global plugin_name bad-behavior
%global plugin_human_name Bad Behavior


Name:		wordpress-plugin-%{plugin_name}
Version:	2.2.13
Release:	23%{?dist}
Summary:	%{plugin_human_name} plugin for WordPress

# According to http://plugins.trac.wordpress.org/ all plugins are licensed
# under the GPL unless otherwise stated in the plugin source.
# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:	LGPL-3.0-or-later
URL:		http://www.bad-behavior.ioerror.us/
Source0:	http://downloads.wordpress.org/plugin/%{plugin_name}.%{version}.zip
Requires:	wordpress
BuildArch:	noarch

%description
Bad Behavior is a PHP-based solution for blocking link spam and the robots
which deliver it.

Bad Behavior complements other link spam solutions by acting as a gatekeeper,
preventing spammers from ever delivering their junk, and in many cases, from
ever reading your site in the first place. This keeps your site's load down,
makes your site logs cleaner, and can help prevent denial of service conditions
caused by spammers.

Bad Behavior also transcends other link spam solutions by working in a
completely different, unique way. Instead of merely looking at the content of
potential spam, Bad Behavior analyzes the delivery method as well as the
software the spammer is using. In this way, Bad Behavior can stop spam attacks
even when nobody has ever seen the particular spam before.

Bad Behavior is designed to work alongside existing spam prevention services to
increase their effectiveness and efficiency. Whenever possible, you should run
it in combination with a more traditional spam prevention service.

This package is built for use with WordPress (wordpress), not WordPress MU.


%prep
%setup -q -c
echo 'To enable "%{plugin_human_name}", go to the administrative section
of your blog, "Plugins", and enable the plugin there.' > README.fedora

%build

%install
rm -rf %{buildroot}
# Pull doc files up so they aren't duplicated
mv %{plugin_name}/{lgpl-3.0.txt,README.txt} .
# Trim some non-WordPress files we don't need
rm -f %{plugin_name}/bad-behavior-{lifetype,mediawiki}.php
mkdir -p %{buildroot}%{_datadir}/wordpress/wp-content/plugins/
cp -a %{plugin_name} %{buildroot}%{_datadir}/wordpress/wp-content/plugins/
# Note, no %find_lang since there are no language files



%files
%doc lgpl-3.0.txt README.txt README.fedora
%{_datadir}/wordpress/wp-content/plugins/%{plugin_name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.13-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Nick Bebout <nb@fedoraproject.org> - 2.2.13-1
- Upgrade to 2.2.13

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Feb 26 2011 Nick Bebout <nb@fedoraproject.org> 2.0.42-1
- Remove -mu subpackage, bump to 2.0.42

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 18 2010 Nick Bebout <nb@fedoraproject.org> 2.0.38-1
- Update to 2.0.38

* Fri May 28 2010 Nick Bebout <nb@fedoraproject.org> 2.0.36-1
- Update to 2.0.36

* Tue Nov 10 2009 Nick Bebout <nb@fedoraproject.org> 2.0.32-2
- Remove non-applicable comment about language files

* Mon Nov 9 2009 Nick Bebout <nb@fedoraproject.org> 2.0.32-1
- Fix packaging issues

* Wed Jul 15 2009 Michael Hampton <error@ioerror.us> 2.0.28
- Initial package build
