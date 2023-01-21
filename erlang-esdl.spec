%global realname esdl
%global upstream dgud


Name:           erlang-%{realname}
Version:        1.3.1
Release:        27%{?dist}
Summary:        Erlang OpenGL/SDL API and utilities
License:        MIT
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/esdl-%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  SDL-devel
BuildRequires:	erlang-rebar
BuildRequires:	dos2unix
BuildRequires:	gcc
# Dynamically loads erl_gl.so from erlang-wx package in sdl_video:setVideoMode/4
Requires:	erlang-wx%{?_isa}
Provides:	esdl = %{version}-%{release}
Obsoletes:	%{name}-devel < 1.0.1-2
%{?__erlang_drv_version:Requires: %{__erlang_drv_version}}


%description
A library that gives you access to SDL and OpenGL functionality in
your Erlang program.


%prep
%setup -q -n %{realname}-esdl-%{version}
chmod 0644 Readme
find -type f -name '*.hrl' | xargs dos2unix
find -type f -name '*.[ch]' | xargs chmod 0644
sed -i -e "s,git,\"%{version}\",g" src/sdl.app.src


%build
%{rebar_compile}


%install
%{erlang_install}
mkdir -p %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/src
install -p -m 0644 src/*.hrl %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/src


%check
%{erlang_test}


%files
%license license.terms
%doc Readme
%{erlang_appdir}/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-12
- Drop unneeded macro

* Fri Apr  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-11
- Rebuild with Erlang 18.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-9
- Rebuild with Erlang 18.2.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-7
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-6
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.3.1-4
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-2
- Rebuild with new __erlang_drv_version

* Thu Sep 05 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-1
- Ver. 1.3.1 (bugfix release)
- Switch building to rebar

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3-2
- New Requires on Erlang's driver API version

* Sat Mar 09 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3-1
- Ver. 1.3 (API compatible)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2-1
- new release 1.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-4
- Rebuild with new Erlang/OTP R14A
- Small typo in %%changelog was fixed

* Thu Jun 24 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-3
- Fix building on x86_64

* Wed Jun 23 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-2
- Rebuild
- Narrowed explicit requires
- No longer mention exact erlang's version in (Build)Requires
- Drop *-devel subpackage (includes moved to main package)
- Use Fedora-specific CFLAGS
- Fixed DOS line endings and permissions

* Tue Aug 11 2009 Gerard Milmeister <gemi@bluewin.ch> - 1.0.1-1
- new release 1.0.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.0626-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.0626-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.96.0626-4
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.96.0626-3
- Autorebuild for GCC 4.3

* Mon Dec 10 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.96.0626-2
- rebuild for erlang R12B

* Sun Apr  8 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.96.0626-1
- new version 0.96.0626

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.95.0630-8
- Rebuild for FE6

* Wed Jun  7 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.95.0630-7
- revert to use erlang R10B

* Thu May 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.95.0630-6
- rebuilt for erlang R11B-0

* Tue Apr 25 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.95.0630-4
- removed c_src directory

* Mon Apr 24 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.95.0630-3
- renamed package to erlang-esdl

* Mon Apr 24 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.95.0630-2
- split off devel package

* Thu Sep  8 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.95.0630-1
- New Version 0.95.0630

* Sun Mar  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.94.1025-1
- New Version 0.94.1025

* Sat Jul 17 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.94.0615-0.fdr.1
- New Version 0.94.0615

* Sun Apr 11 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.94.0125-0.fdr.1
- First Fedora release
