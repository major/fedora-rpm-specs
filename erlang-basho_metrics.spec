%global realname basho_metrics
%global upstream basho


Name:		erlang-%{realname}
Version:	1.0.0
Release:	51%{?dist}
Summary:	Fast performance metrics for Erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-basho_metrics-0001-Use-C-11.patch
BuildRequires:	boost-devel
BuildRequires:	erlang-rebar
BuildRequires:	gcc-c++


%description
An open source Erlang library for efficient calculation of service performance
metrics.


%prep
%autosetup -p1 -n %{realname}-%{version}
rm -rf c_src/boost


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc README.org
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-47
- Rebuild for Erlang 25

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-43
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-40
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-38
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-35
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-34
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-30
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-27
- Rebuilt for Boost 1.63

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-26
- Rebuild for Erlang 19

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-25
- Drop unneeded macro

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-24
- Rebuild with Erlang 18.3

* Thu Mar  3 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-23
- Cleanup spec-file according to the Erlang Packaging Guidelines

* Fri Feb 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-22
- Fixed FTBFS in Rawhide

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-20
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-19
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.0-17
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-15
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.0.0-14
- Rebuild for boost 1.57.0

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-13
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-12
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  1 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-10
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.0.0-8
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.0.0-6
- Rebuild for boost 1.54.0

* Sun Mar 10 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-5
- Added new dependency

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-2
- Added comment regarding source tarball retrieval
- Filtered out *.so provides
- Removed bundled boost headers and build against boost-devel
- Dropped obsoleted defattr() directive

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-1
- Ver. 1.0.0
