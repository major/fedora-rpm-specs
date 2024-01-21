%global realname erlsyslog
%global upstream lemenkov


Name:		erlang-%{realname}
Version:	0.8.0
Release:	18%{?dist}
Summary:	Syslog facility for Erlang
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar
BuildRequires:	gcc


%description
Syslog facility for Erlang.


%prep
%setup -q -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%doc example
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.8.0-1
- Ver. 0.8.0

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-13
- Drop unneeded macro

* Sat Apr  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-12
- Rebuild with Erlang 18.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-10
- Rebuild with Erlang 18.2.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-8
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-7
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-4
- Actually allow building proper debuginfo

* Thu Oct 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-3
- Rebuild with new erlang_drv_version number
- Explicitly set up CFLAGS to avoid bogus debuginfo generation (rhbz #958965)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.6.2-1
- Performance optimizations

* Thu May 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-1
- Fix for dynamic verbosity change

* Thu May 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.6-1
- Ver. 0.6
- Fixed driver locking on Erlang R16B
- Allow dynamically change verbosity level (don't print info or warning messages)

* Fri Apr 26 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.5-1
- Ver. 0.5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.4-1
- Ver. 0.4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2-1
- Ver. 0.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-5
- Narrowed BuildRequires

* Sun Jul 11 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-4
- Rebuild for Erlang/OTP R14A
- Simplified spec-file a bit

* Fri May 28 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-3
- Narrowed explicit requires

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun  4 2009 Peter Lemenkov <lemenkov@gmail.com> - 0.1-1
- Ver. 0.1

* Mon May  4 2009 Peter Lemenkov <lemenkov@gmail.com> - 0.1-0.3.svn10
- Get rid of unnecessary source files

* Fri Feb 20 2009 Peter Lemenkov <lemenkov@gmail.com> - 0.1-0.2.svn10
- New snapshot

* Thu Dec 18 2008 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.svn8
- Initial package

