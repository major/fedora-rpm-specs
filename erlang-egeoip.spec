%global realname egeoip
%global upstream mochi
%global git_tag 4efda2c2b5b0084d3e77b8f0bbdec78514706b34


Name:		erlang-%{realname}
Version:	1.1
Release:	19%{?dist}
BuildArch:	noarch
Summary:	Erlang IP Geolocation module
License:	MIT and BSD with advertising
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
#Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{git_tag}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar
BuildRequires:	GeoIP-GeoLite-data-extra
Requires:	GeoIP-GeoLite-data-extra


%description
Erlang IP Geolocation module, currently supporting the MaxMind GeoLite City
Database.


%prep
%setup -q -n %{realname}-%{git_tag}
mv priv/LICENSE.txt LICENSE.geolitecity


%build
%{erlang_compile}


%install
%{erlang_install}
mkdir -p %{buildroot}%{erlang_appdir}/priv/
ln -s %{_datadir}/GeoIP/GeoLiteCity.dat %{buildroot}%{erlang_appdir}/priv/
# This file is a symlink to %{_datadir}/GeoIP/GeoLiteCountry.dat
ln -s %{_datadir}/GeoIP/GeoIP.dat %{buildroot}%{erlang_appdir}/priv/
ln -s %{_datadir}/GeoIP/GeoIPCity.dat %{buildroot}%{erlang_appdir}/priv/


%check
%{erlang_test}


%files
%license LICENSE
%license LICENSE.geolitecity
%doc README
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.1-10
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun  9 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.1-3
- Spec-file cleanups

* Wed Mar  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.1-2
- Use system-wide GeoIP data

* Fri Feb 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.1-1
- Ver. 1.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20111025git45c32ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20111025git45c32ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20111025git45c32ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20111025git45c32ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20111025git45c32ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20111025git45c32ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20111025git45c32ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.20111025git45c32ad
- Added unit-tests
- Invoke rebar with more verbosity
- Removed no longer required defattr() line
- Added API docs (doc/ directory)
- Confirmed the legal status of the LICENSE.geolitecity

* Tue May 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 0-0.2.20111025git45c32ad
- Update to the latest git tag

* Sat Jan 22 2011 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20110122gitfac69bb
- Initial build

