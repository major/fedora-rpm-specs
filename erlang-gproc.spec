%global realname gproc
%global upstream uwiger


Name:		erlang-%{realname}
Version:	0.9.0
Release:	7%{?dist}
BuildArch:	noarch
Summary:	Extended process registry for Erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-edown
BuildRequires:	erlang-gen_leader
BuildRequires:	erlang-rebar3


%description
Extended process registry for Erlang.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}
install -D -p -m 0644 priv/sys.config %{buildroot}%{erlang_appdir}/priv/sys.config
# Remove edoc config files (not needed for end-users)
rm -f doc/edoc-info
rm -f doc/overview.edoc
rm -f doc/README.md


%check
%{erlang3_test}


%files
%license LICENSE
%doc doc/* README.md
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr  7 2022 Peter Lemenkov <lemenkov@gmail.com> - 0.9.0-4
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr  3 2021 Peter Lemenkov <lemenkov@gmail.com> - 0.9.0-1
- Ver. 0.9.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.8.0-1
- Ver. 0.8.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-3
- Rebuild for Erlang 20 (with proper builddeps)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-1
- Ver. 0.7.0
- License changed from ERPL to Apache Software License 2.0

* Fri Oct 06 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-7
- Reenable timing-sensitive tests (and a fix for them)

* Thu Oct 05 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-6
- Fix FTBFS in Rawhide (2nd attempt)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-3
- Fix FTBFS in Rawhide

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep  5 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-1
- Ver. 0.6.1

* Wed Jun  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.6-2
- Spec-file cleanups

* Thu Mar  3 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.6-1
- Ver. 0.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.2.17-2
- Added missing gproc_dist:set_value_shared/2 - https://github.com/uwiger/gproc/issues/46

* Mon Aug 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.2.17-1
- Ver. 0.2.17

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.2.16-1
- Ver. 0.2.16
- Drop upstreamed patches

* Sun Mar 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.2.15-2
- Fix doc installation

* Sat Mar 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.2.15-1
- Ver. 0.2.15
- Drop R12B (EL5) compatibility patches

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2.14-1
- Ver. 0.2.14 (API/ABI compatible release)

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2.13.3-1
- Ver. 0.2.13.3

* Sun Jul 29 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2.13-1
- Ver. 0.2.13

* Sat Jul 28 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2.11-4
- Another bunch of fixes for R12B

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2.11-2
- Allow build on EL5

* Tue May 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2.11-1
- Ver. 0.2.11 (fixes rhbz #824342)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20100929gitf0807c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20100929gitf0807c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.20100929gitf0807c9
- Fixed License tag
- Removed uit-tests which requires proprietary testing software framework

* Wed Nov 10 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.2.20100929gitf0807c9
- Use system-wide rebar
- Don't run make eunit twice

* Wed Sep 29 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20100929gitf0807c9
- Initial build

