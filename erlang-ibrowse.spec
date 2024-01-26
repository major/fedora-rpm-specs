%global realname ibrowse
%global upstream cmullaparthi


Name:		erlang-%{realname}
Version:	4.4.2
Release:	10%{?dist}
BuildArch:	noarch
Summary:	Erlang HTTP client
License:	BSD or LGPLv2+
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-ibrowse-0001-use-is_ipv6_host-1-function-from-httpc.patch
Patch2:		erlang-ibrowse-0002-use-ssl-handshake-2-function-for-erlang-otp-21.patch
BuildRequires:	erlang-rebar3


%description
%{summary}.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}
install -D -p -m 0644 priv/%{realname}.conf %{buildroot}%{erlang_appdir}/priv/%{realname}.conf


%check
%{erlang3_test}


%files
%license BSD_LICENSE LICENSE
%doc CHANGELOG CONTRIBUTORS README.md doc/
%{erlang_appdir}/


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr  7 2022 Peter Lemenkov <lemenkov@gmail.com> - 4.4.2-5
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 4.4.2-1
- Ver. 4.4.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 4.4.1-3
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 4.4.1-1
- Ver. 4.4.1
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 4.4-1
- Ver. 4.4

* Wed Jun  8 2016 Peter Lemenkov <lemenkov@gmail.com> - 4.3-1
- Ver. 4.3

* Wed Apr 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 4.2.4-2
- Fix improper use of lager

* Wed Apr 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 4.2.4-1
- Ver. 4.2.4

* Thu Mar  3 2016 Peter Lemenkov <lemenkov@gmail.com> - 4.2.2-1
- Ver. 4.2.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Peter Lemenkov <lemenkov@gmail.com> - 4.0.1-1
- Ver. 4.0.1
- Support only Fedora 18+, EL6+
- Added patch for CouchDB 1.6.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 02 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.2.0-4
- Removed mentioning about test file from *.app

* Tue Jul 12 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.2.0-3
- Fix building on EL-5

* Sun May 15 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.2.0-2
- Added missing build requirements

* Sun May 15 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.2.0-1
- Ver. 2.2.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.3-1
- Ver. 2.1.3

* Wed Nov 10 2010 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-1
- Ver. 2.1.0

* Tue Sep 28 2010 Peter Lemenkov <lemenkov@gmail.com> - 2.0.1-1
- Ver. 2.0.1
- Narrowed BuildRequires

* Sun Jul 11 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-0.4.20100601git07153bc
- Add missing runtime requirement - erlang-sasl
- Rebuild with Erlang/OTP R14A

* Tue Jun  8 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-0.3.20100601git07153bc
- Also install header file

* Tue Jun  1 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-0.2.20100601git07153bc
- New git snapshot (with clarified licensing terms)

* Thu May 27 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-0.1.gita114ed3b
- Ver 1.6.0 from git with one patch ahead.

* Thu May 13 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.5.6-2
- Narrowed explicit requires

* Wed Apr  7 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.5.6-1
- initial package

