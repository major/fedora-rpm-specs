%global realname jsx
%global upstream talentdeficit


Name:		erlang-%{realname}
Version:	3.1.0
Release:	7%{?dist}
BuildArch:	noarch
Summary:	A streaming, evented json parsing toolkit
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-jsx-0001-Adapt-to-OTP-24.patch
BuildRequires:	erlang-rebar3


%description
An Erlang application for consuming, producing and manipulating json. inspired
by yajl.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%license LICENSE
%doc CHANGES.md README.md
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr  6 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.1.0-3
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug  9 2021 Peter Lemenkov <lemenkov@gmail.com> - 3.1.0-1
- Ver. 3.1.0
- Fix FTBFS with Erlang 24

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.9.0-1
- Ver. 2.9.0
- Switch to noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.8.0-2
- Spec-file cleanups

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.8.0-1
- Ver. 2.8.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 01 2013 gil cattaneo <puntogil@libero.it> 1.4.2-2
- add debug_package nil
- fix requires list
- drop erlang-eunit

* Fri Jul 12 2013 gil cattaneo <puntogil@libero.it> 1.4.2-1
- initial rpm
