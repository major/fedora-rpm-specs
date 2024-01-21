%global realname riaknostic
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.7
Release:	17%{?dist}
BuildArch:	noarch
Summary:	A diagnostic tool for Riak installations
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-lager
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar


%description
A set of tools that diagnoses common problems which could affect a Riak node or
cluster. When experiencing any problem with Riak, riaknostic should be the
first thing run during troubleshooting. The tool is a plugin for Riak which can
be used via the riak-admin script.


%prep
%setup -q -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
cp -arv priv/ %{buildroot}%{erlang_appdir}/


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md doc/erlang.png doc/*.html doc/stylesheet.css
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.7-5
- Convert to a noarch package.
- Rebuild against the noarch lager (#1589611).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-1
- Ver. 2.1.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.3-6
- Spec-file cleanups

* Sat Mar  5 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.3-1
- Ver. 2.1.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-1
- Initial build
