%global realname getopt
%global upstream jcomellas


Name:		erlang-%{realname}
Version:	1.0.2
Release:	6%{?dist}
BuildArch:	noarch
Summary:	Erlang module to parse command line arguments using the GNU getopt syntax
License:	BSD
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar


%description
Command-line parsing module that uses a syntax similar to that of GNU getopt.


%prep
%autosetup -p 1 -n %{realname}-%{version}
chmod 0644 examples/*.escript


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE.txt
%doc README.md examples/
%{erlang_appdir}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-2
- Ver. 1.0.2

* Tue Oct 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-1
- Ver. 1.0.2
- Bootstrap w/o tests

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-7
- Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-5
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-1
- Ver. 1.0.1

* Tue Nov 14 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-0.1
- Ver. 1.0.1
- Bootstrap w/o tests

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-4
- Spec-file cleanups

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-0
- Bootstrap ver. 0.8.2 with disabled tests

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-1
- Ver. 0.7.0
- Removed EL5-related stuff

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.6.0-1
- Ver. 0.6.0

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.5.2-2
- Rebuild with tests
- Finally fixed tests on EL5

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.5.2-1
- Ver. 0.5.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.4.4-2
- Workaround for EL5's rebar

* Sat Jun 02 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.4.4-1
- Ver. 0.4.4

* Fri Jun 01 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.4.3-2
- Fix building on EPEL-5 (again)
- Enabled tests

* Tue May 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.4.3-1
- Ver. 0.4.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct  6 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.3-3
- Fix building on EPEL-5

* Tue Oct  5 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.3-2
- Fixed License tag
- Doc-files now have 644 mode

* Thu Sep 30 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.3-1
- Initial package
- Disabled %%check section until rebar will be available

