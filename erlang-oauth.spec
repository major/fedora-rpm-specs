%global realname oauth
%global upstream tim


Name:		erlang-%{realname}
Version:	2.1.0
Release:	6%{?dist}
BuildArch:	noarch
Summary:	An Erlang OAuth 1.0 implementation
License:	MIT
URL:		http://github.com/%{upstream}/%{name}
VCS:		scm:git:https://github.com/%{upstream}/%{name}.git
Source0:	https://github.com/%{upstream}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	erlang-rebar3


%description
An Erlang OAuth 1.0 implementation. Includes functions for generating
signatures (client side), verifying signatures (server side), and some
convenience functions for making OAuth HTTP requests (client side).


%prep
%setup -q


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%doc CHANGELOG.md README.md THANKS.txt
%license LICENSE.txt
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr  7 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-2
- Switch to rebar3

* Thu Jan 27 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-1
- Ver. 2.1.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr  3 2021 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-1
- Ver. 2.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-8
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Ver. 1.6.0
- Drop upstreamed patches

* Fri Sep  9 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-4
- Spec-file cleanups according to Fedora Erlang Packaging Guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-1
- Ver. 1.5.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.4.0-1
- Ver. 1.4.0 (API incompatible update)
- Removed compatibility with Fedora < 12, RHEL < 6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-1
- Ver. 1.1.1 (Incompatible with Erlang/OTP < R14B)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-1
- First stable release (this is the same as git7d85d3e with the patch no. 1)

* Wed Sep 22 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.git7d85d3e
- Narrowed BuildRequires
- New git snapshot

* Mon Jul 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.5.gite8aecf0
- Rebuild with new Erlang R14A
- Simplified spec-file
- Added missing requirement - erlang-kernel

* Fri May 28 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.4.gite8aecf0
- Fixed CouchDB failure (see rhbz #597093)
- Fixed reqirements for F-11

* Thu May 27 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.gite8aecf0
- Fixed explicit requires on EL-[45]

* Thu May 13 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.2.gite8aecf0
- Narrowed explicit requires

* Wed Apr  7 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.gite8aecf0
- initial package

