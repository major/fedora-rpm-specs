%global realname meck
%global upstream eproxus


Name:		erlang-%{realname}
Version:	0.9.2
Release:	8%{?dist}
BuildArch:	noarch
Summary:	A mocking library for Erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-meck-0001-Disable-erlang-unite-test-output-highlighting.patch
BuildRequires:	erlang-hamcrest
BuildRequires:	erlang-rebar3
# FIXME - calls to unexported cover:compile_beam/2, cover:get_term/1,
# cover:write/2


%description
With meck you can easily mock modules in Erlang. Since meck is intended to be
used in testing, you can also perform some basic validations on the mocked
modules, such as making sure no function is called in a way it should not.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
#%%{erlang3_test}
DEBUG=1 rebar3 eunit


%files
%license LICENSE
%doc README.md NOTICE
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr  7 2022 Peter Lemenkov <lemenkov@gmail.com> - 0.9.2-4
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr  3 2021 Peter Lemenkov <lemenkov@gmail.com> - 0.9.2-1
- Ver. 0.9.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Peter Lemenkov <lemenkov@gmail.com> - 0.9.0-1
- Ver. 0.9.0
- Fix FTBFS with Erlang 23

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.8.13-4
- Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.8.13-2
- Rebuild for noarch hamcrest

* Fri Feb 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.8.13-1
- Ver. 0.8.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.8.12-2
- Switch to noarch

* Wed Aug 15 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.8.12-1
- Ver. 0.8.12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.8.8-4
- Rebuild for Erlang 20 (with proper builddeps)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.8.8-2
- Fix for secondary arches

* Thu Aug 31 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.8.8-1
- Ver. 0.8.8

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul  4 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.8.7-1
- Ver. 0.8.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 27 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-4
- Spec-file cleanups

* Mon Mar  7 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-3
- Small spec-file cleanups

* Wed Mar  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-2
- Adjust spec according to Erlang Packaging Guidelines

* Sat Feb 13 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-1
- Ver. 0.8.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.7.2-5
- Fix build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.7.2-3
- Remove tests parametrized modules - they are no longer supported
- Drop support for EL5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.2-1
- Ver. 0.7.2

* Wed Aug 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.1-4
- Fix for EL5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.1-2
- Pick up all missing requires

* Mon Feb 13 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.7.1-1
- Rebase
- Review fixes (Peter Lemenkov, #705773)

* Wed May 18 2011 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.5-1
- Initial packaging
