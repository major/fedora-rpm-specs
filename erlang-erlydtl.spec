%global realname erlydtl
%global upstream erlydtl


Name:		erlang-%{realname}
Version:        0.13.1
Release:        5%{?dist}
BuildArch:      noarch
Summary:        Erlang implementation of the Django Template Language
License:        MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-erlydtl-0001-Verbose-testing.patch
Patch2:		erlang-erlydtl-0002-No-such-function-exported-gettext_compile-write_pret.patch
Patch3:		erlang-erlydtl-0003-No-such-function-exported-gettext_compile-fmt_filein.patch
Patch4:		erlang-erlydtl-0004-No-such-fun-gettext_compile-open_po_file-3.patch
Patch5:		erlang-erlydtl-0005-No-such-fun-gettext_compile-close_file-0.patch
Patch6:		erlang-erlydtl-0006-Support-Erlang-OTP-22.0.patch
Provides:       ErlyDTL = %{version}-%{release}
BuildRequires:  erlang-rebar


%description
ErlyDTL is an Erlang implementation of the Django Template Language. The
erlydtl module compiles Django Template source code into Erlang bytecode. The
compiled template has a "render" function that takes a list of variables and
returns a fully rendered document.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
cp -arv priv %{buildroot}/%{erlang_appdir}/


%check
%{erlang_test -C rebar-tests.config}


%files
%license LICENSE
%doc CONTRIBUTING.md NEWS.md README.markdown README_I18N
%{erlang_appdir}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Peter Lemenkov <lemenkov@gmail.com> - 0.13.1-1
- Ver. 0.13.1
- Fix FTBFS with Erlang 23

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.12.1-4
- Fix FTBFS with Erlang 21

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.12.1-1
- Ver. 0.12.1
- Fix FTBFS with Erlang 20

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Merlin Mathesius <mmathesi@redhat.com> - 0.11.1-2
- Import upstream patch to support OTP 19 (BZ#1404851).

* Thu May 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.11.1-1
- Ver. 0.11.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7.20130214git6a9845f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6.20130214git6a9845f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5.20130214git6a9845f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4.20130214git6a9845f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-3.20130214git6a9845f
- Rebuilt (fix FTBFS, see rhbz #992220)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2.20130214git6a9845f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-1.20130214git6a9845f
- Latest snapshot
- Removed tests for parametrized modules support

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6.20110306git889155f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5.20110306git889155f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4.20110306git889155f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 06 2011 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.6.0-3.20110306git889155f
- Update to latest git snapshot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 1 2010 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.6.0-1
- Initial Package
