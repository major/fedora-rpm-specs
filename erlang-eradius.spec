%global realname eradius
%global upstream travelping


Name:		erlang-%{realname}
Version:	2.3.1
Release:	3%{?dist}
BuildArch:	noarch
Summary:	Erlang RADIUS server framework
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-eradius-0001-Ignore-plugins.patch
Patch2:		erlang-eradius-0002-Disable-prometheus-support.patch
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar3


%description
Erlang RADIUS server framework.


%prep
%autosetup -p 1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%license LICENSE
%doc METRICS.md README.md sample/
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.3.1-1
- Ver. 2.3.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.2.4-1
- Ver. 2.2.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.9.2-1
- Ver. 0.9.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.8.9-3
- Convert into a noarch package.
- Rebuild against the noarch lager (#1589611).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.8.9-1
- Ver. 0.8.9

* Tue Nov 14 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.8.8-1
- Switch upstream to Travelping
- Spec-file cleanup

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.7-4
- Added missing build-requires on python

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.8.7-1
- Ver.0.8.7 (API compatible)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 31 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.8.5-1
- Ver. 0.8.5 (bugfix release)

* Mon Oct 03 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-1
- Ver. 0.8.4

* Thu Sep 15 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.8.3-1
- Ver. 0.8.3

* Wed Sep 14 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2

* Tue Sep 13 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.8.1-1
- Ver. 0.8.1

* Tue Sep 13 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.8.0-1
- Ver. 0.8.0

* Fri Sep 09 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-2
- Added missing BuildRequires

* Fri Sep 09 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-1
- Ver. 0.7.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20070627cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.7.20070627cvs
- Narrow list of BuildRequires

* Mon Jul 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.20070627cvs
- Narrow list of runtime requirements
- Rebuild for new Erlang/OTP R14A

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20070627cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Peter Lemenkov <lemenkov@gmail.com> - 0-0.4.20070627cvs
- Changed naming scheme

* Mon Jul  6 2009 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.cvs20070627
- Proper versioning scheme
- Added two missing header-files
- Fixed permissions for MIT_LICENSE and eradius_server.erl

* Tue Apr 21 2009 Peter Lemenkov <lemenkov@gmail.com> - 0-0.2
- Get rid of unnecessary source files

* Wed Mar 25 2009 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1
- initial build

