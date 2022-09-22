%global realname mozjs
%global upstream erlang-mozjs


Name:		erlang-js
Version:	1.9.2
Release:	6%{?dist}
Summary:	A Friendly Erlang to Javascript Binding
License:	ASL 2.0
URL:		http://github.com/%{upstream}/erlang-%{realname}
VCS:		scm:git:https://github.com/%{upstream}/erlang-%{realname}.git
Source0:	https://github.com/%{upstream}/erlang-%{realname}/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar
BuildRequires:	gcc-c++
BuildRequires:	mozjs68-devel


%description
A Friendly Erlang to Javascript Binding.


%prep
%autosetup -p1 -n erlang-%{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
install -m 644 priv/json2.js $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/priv


%check
# FIXME FIXME FIXME
# Fails with "too much recursion" on s390x, and I don't have access to any s390x machines
# Tracking bug - https://github.com/erlang-mozjs/erlang-mozjs/issues/1
%ifnarch s390x
# FIXME FIXME FIXME strange issues on armv7hl, aarch64, ppc64le
#%%{erlang_test}
%endif


%files
%license LICENSE
%doc README.org
%{erlang_appdir}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.9.2-5
- Rebuild for Erlang 25

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.9.2-1
- Ver. 1.9.2
- Built against mozjs68

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.9.0-6
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.9.0-4
- Rebuild with noarch deps

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.9.0-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.9.0-1
- Ver. 1.9.0
- New upstream
- Built against mozjs52

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.4.0-2
- Switch to mozjs24

* Tue Jan 24 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.4.0-1
- Ver. 1.4.0
- Switch to mozjs17

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-7
- Drop unneeded macro

* Fri Apr  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-6
- Rebuild with Erlang 18.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-4
- Added few more interesting patches

* Wed Jan 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-3
- Rebuild with Erlang 18.2.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-8
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-7
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.2.2-5
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-3
- Rebuild with new __erlang_drv_version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-1
- Ver. 1.2.2
- Dropped upstreamed patches

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 23 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-2
- Fix failure during tests if built with js-1.7.0 (EL5 & EL6)

* Sat Sep 22 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1
- Drop upstreamed patches

* Wed Sep 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Fri Jul 20 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-4
- Fix building releases using rebar
- Fix dependencides (add _isa)
- Drop EL5-related stuff

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-2
- Enable back building with js-1.7.0 (EL6)

* Thu Jul 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-1
- Ver. 1.0.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 13 2011 Martin Stransky <stransky@redhat.com> - 0.5.0-3
- build fix for js 1.8.5

* Fri Jan 28 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.5.0-2
- Drop unneeded runtime dependency on eunit

* Wed Jan  5 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.5.0-1
- Ver. 0.5.0

* Fri Sep 10 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.4-1
- Initial build
