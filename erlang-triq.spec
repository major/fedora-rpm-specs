%global realname triq
%global upstream triq

Name:		erlang-%{realname}
Version:	1.3.0
Release:	10%{?dist}
BuildArch:	noarch
Summary:	A property-based testing library for Erlang
License:	ASL 2.0
URL:		https://gitlab.com/%{upstream}/%{realname}
VCS:		scm:git:https://gitlab.com/%{upstream}/%{realname}.git
Source0:	https://gitlab.com/%{upstream}/%{realname}/-/archive/v%{version}/%{realname}-%{version}.tar.bz2
BuildRequires:	erlang-rebar3


%description
A property-based testing library for Erlang.


%prep
%setup -q -n %{realname}-v%{version}-e68b47fe7b9e963ec45edf3bf9d5a4cd81831e3c
# FIXME breaks for unknown reason
rm -f test/triq_attr_tests.erl


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%license LICENSE
%doc NOTICE README.org THANKS
%{erlang_appdir}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 29 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-9
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-3
- Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0
- Switch upstream to GitLab
- Switch arch to noarch
- Fix FTBFS with Erlang 20+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul  4 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.1-1
- Ver. 1.1

* Tue Mar 28 2017 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.git2c49739
- Fix FTBFS in Rawhide
- Switched upstream to triqng

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitc7306b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 14 2016 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.gitc7306b8
- Initial packaging
