%global realname kvc
%global upstream etrepum


Name:		erlang-%{realname}
Version:	1.7.0
Release:	19%{?dist}
BuildArch:	noarch
Summary:	Key Value Coding for Erlang data structures
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-kvc-0001-Pass-source-files-through-epp-before-edoc-gen.patch
Patch2:		erlang-kvc-0002-More-greedy-guard.patch
BuildRequires:	erlang-rebar3


%description
kvc supports Key Value Coding-like queries on common Erlang data structures. A
common use case for kvc is to quickly access one or more deep values in decoded
JSON, or some other nested data structure. It can also help with some aggregate
operations. It solves similar problems that you might want to use a tool like
XPath or jQuery for, but it is far simpler and strictly less powerful. It's
inspired by Apple's NSKeyValueCoding protocol from Objective-C.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%check
%{erlang3_test}


%install
%{erlang3_install}


%files
%license LICENSE
%doc CHANGES.md README.md
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.7.0-16
- Fix FTBFS with Erlang 25
- Switch to rebar3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.7.0-8
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.7.0-1
- Ver. 1.7.0

