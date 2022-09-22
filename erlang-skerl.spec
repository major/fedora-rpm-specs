%global realname skerl
%global upstream basho


Name:		erlang-%{realname}
Version:	1.1.0
Release:	36%{?dist}
Summary:	Skein hash function for Erlang, via NIFs
# Original skein sources are in Public Domain
# c_src/brg_*.h files are licensed under BSD or GPL (w/o explicit GPL version)
# src/hex.erl and src/skerl.erl are licensed under MIT
License:	Public Domain and BSD and MIT or GPL+
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-skerl-0001-Rewrote-hex-routines-under-MIT-license.patch
Patch2:		erlang-skerl-0002-Rewrote-Erlang-NIF-API-routines-under-MIT-license.patch
BuildRequires:	erlang-rebar
BuildRequires:	gcc-c++


%description
Skein hash function for Erlang, via NIFs.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%{erlang_appdir}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-35
- Rebuild for Erlang 25

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-28
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-26
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-23
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-22
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-17
- Rebuild for Erlang 19

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-16
- Drop unneeded macro

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-15
- Rebuild with Erlang 18.3

* Wed Feb 10 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-14
- Rebuild with Erlang 18.2.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-11
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-10
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-9
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.1.0-7
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-4
- Add dependency on NIF API version
- Removed EL5 support from spec-file

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jun 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-2
- Rewrote problematic files and relicensed them under MIT

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-1
- Ver. 1.1.0

* Mon Jan 10 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-1
- Ver. 1.0.0 (the same as previous git snapshot 1f6f580)

* Fri Nov 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20101112git1f6f580
- Initial build

