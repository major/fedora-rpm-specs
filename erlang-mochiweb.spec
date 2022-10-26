%global realname mochiweb
%global upstream mochi


Name:		erlang-%{realname}
Version:	3.1.1
Release:	1%{?dist}
BuildArch:	noarch
Summary:	An Erlang library for building lightweight HTTP servers
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-xmerl
Provides:	%{realname} = %{version}-%{release}


%description
An Erlang library for building lightweight HTTP servers.


%prep
%autosetup -p1 -n %{realname}-%{version}
rm -f .gitignore ./examples/example_project/.gitignore



%build
%{erlang3_compile}


%install
%{erlang3_install}

# Additional skeleton files
cp -arv scripts %{buildroot}%{_erllibdir}/%{realname}-%{version}
cp -arv support %{buildroot}%{_erllibdir}/%{realname}-%{version}


%check
%{erlang3_test}


%files
%license LICENSE
%doc CHANGES.md README.md examples/
%{erlang_appdir}/


%changelog
* Mon Oct 24 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.1.1-1
- Ver. 3.1.1

* Thu Aug 18 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.1.0-1
- Ver. 3.1.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.0.0-1
- Ver. 3.0.0

* Sat Jan 29 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.22.0-1
- Ver. 2.22.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Peter Lemenkov <lemenkov@gmail.com> - 2.21.0-1
- Ver. 2.21.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb  6 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.20.1-1
- Ver. 2.20.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.20.0-1
- Ver. 2.20.0

* Mon Nov 11 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.19.0-3
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.19.0-1
- Ver. 2.19.0
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.18.0
- Ver. 2.18.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.17.0-1
- Ver. 2.17.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.16.0-1
- Ver. 2.16.0

* Mon Jun 27 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.15.1-1
- Ver. 2.15.1

* Wed May 11 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.15.0-1
- Ver. 2.15.0

* Mon Mar 14 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.13.1-1
- Ver. 2.13.1

* Thu Mar  3 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.13.0-2
- Don't ship .gitignore

* Thu Mar  3 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.13.0-1
- Ver. 2.13.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.4.2-2
- Fixed issue with R16B01

* Sat Mar 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.4.2-1
- Ver. 2.4.2

* Thu Jan 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.4.1-1
- Ver. 2.4.1

* Sat Jan 26 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.4.0-2
- Fixed regression (see https://github.com/mochi/mochiweb/issues/97 )

* Fri Jan 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.4.0-1
- Ver. 2.4.0 (fix for Erlang R16)
- Dropped patches for EL5 (Erlang R12B)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 06 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-5
- Don't remove test-file (rhbz #675699)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-3
- Added erlang-xmerl as BuildRequires

* Mon Nov 22 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-2
- Added accidentally removed dependency required for %%check

* Sat Nov 13 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-1
- Ver. 1.4.1

* Wed Oct 13 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.0-1
- Ver. 1.4.0

* Wed Sep 29 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.8.20100929git9687b40
- Narrowed BuildRequires
- Restricted explicit requirement for obsoleted fd_server module (rhbz #601152)
- Dropped upstreamed patch6

* Tue Aug 17 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.7.20100724git9a53dbd7
- Fix improper int to string conversion

* Wed Aug 11 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.6.20100724git9a53dbd7
- Fixed all tests on EL-5
- New git snapshot

* Tue Jul 13 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.5.20100507svn159
- Fixed several tests on EL-5 (enough to allow CouchDB to pass its own self-tests)

* Mon Jul 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.4.20100507svn159
- Rebuild with new Erlang
- Simplified spec-file

* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.3.20100507svn159
- Added %%check target and fixed mochiweb:test()
- Fix EL-5 build

* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.2.20100507svn159
- Removed accidentally added macro

* Mon May 31 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.3-0.1.20100507svn159
- New pre-release version (from VCS).

* Thu May 13 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.svn154
- Initial package
