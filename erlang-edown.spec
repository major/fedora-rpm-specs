%global realname edown
%global upstream uwiger


Name:		erlang-%{realname}
Version:	0.8.4
Release:	6%{?dist}
BuildArch:	noarch
Summary:	EDoc extension for generating Github-flavored Markdown
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-edown-0001-Remove-pre-18.0-code.patch
Patch2:		erlang-edown-0002-Don-t-use-git-command-for-branch-retrieval.patch
BuildRequires:	erlang-edoc
BuildRequires:	erlang-rebar3


%description
EDoc extension for generating Github-flavored Markdown.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%doc NOTICE README.md doc/
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr  6 2022 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-3
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-1
- Ver. 0.8.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Peter Lemenkov <lemenkov@gmail.com> - 0.8.3-1
- Ver. 0.8.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.8.1-11
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.8.1-8
- Switch to noarch

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.8.1-3
- Don't die if no git is available

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 27 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.1-1
- Ver. 0.8.1

* Wed Jun  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8-3
- More spec-file cleanups

* Mon Mar  7 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8-2
- Spec-file cleanups

* Thu Mar  3 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8-1
- Ver. 0.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.4-1
- Ver. 0.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.3.1-1
- Ver. 0.3.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 01 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.3.0-1
- Ver. 0.3.0
- Fixed building on EL5

* Mon May 28 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.2.4-2
- Use system-wide rebar

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.2.4-1
- Ver. 0.2.4
