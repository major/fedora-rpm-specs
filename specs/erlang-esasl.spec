%global realname esasl
%global upstream mikma


Name:		erlang-%{realname}
Version:	0.1
Release:	42.20120116git665cc80%{?dist}
Summary:	Simple Authentication and Security Layer (SASL) support for Erlang
# erlang sources are under BSD, C sources - under LGPLv2+
# Automatically converted from old format: BSD and LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/esasl-%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-esasl-0001-Adjust-app-file-template.patch
Patch2:		erlang-esasl-0002-Add-rebar.config.patch
BuildRequires:	erlang-rebar
BuildRequires:	gcc
BuildRequires:	libgsasl-devel
Provides:	%{realname} = %{version}-%{release}
%{?__erlang_drv_version:Requires: %{__erlang_drv_version}}


%description
Simple Authentication and Security Layer (SASL) support for Erlang.


%prep
%setup -q -n %{realname}-esasl-%{version}
rm -rf INSTALL Makefile.am NEWS bootstrap configure.ac esasl/Makefile.am esasl/priv/Makefile.am esasl/src/Makefile.am m4/ rules/
mv esasl/c_src/ c_src/
mv esasl/src/ src/
mv src/esasl.app-in src/esasl.app.src
mkdir -p example/
mv eldap_gsasl.diff src/eldap_expr.erl example/
%patch -P1 -p1
%patch -P2 -p1

%build
%{erlang_compile}


%install
%{erlang_install}
install -D -p -m 0755 priv/gsasl_drv $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/priv/gsasl_drv


%check
%{erlang_test}


%files
%license COPYING COPYING.LIB
%doc AUTHORS README
%{erlang_appdir}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-42.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-41.20120116git665cc80
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-40.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-39.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-38.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-37.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-36.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-35.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-34.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-33.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-31.20120116git665cc80
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-30.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-28.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-26.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1-21.20120116git665cc80
- Drop unneeded macro

* Sat Apr  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1-20.20120116git665cc80
- Rebuild with Erlang 18.3
- Use rebar for building

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-18.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-17.20120116git665cc80
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-16.20120116git665cc80
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1-13.20120116git665cc80
- Rebuild with new __erlang_drv_version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12.20120116git665cc80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1-11.20120116git665cc80
- Update to the latest git snapshot

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 28 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-7
- Narrow BuildRequires

* Mon Jul 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-6
- Rebuild with new Erlang/OTP R14A

* Fri May 28 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-5
- Narrow explicit requires

* Tue Feb 16 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-4
- Added two accidentally missing libraries
- Removed unneeded file ( eldap_expr.beam )

* Mon Feb 15 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-3
- Fixed issues, found during review.

* Wed Feb  3 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-2
- Fix for EPEL

* Sat Jan 16 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1-1
- Initial package for Fedora
