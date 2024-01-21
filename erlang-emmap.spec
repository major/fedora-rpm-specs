%global realname emmap
%global upstream krestenkrab
%global git_tag 05ae1bb


Name:		erlang-%{realname}
Version:	0
Release:	0.39.git05ae1bb%{?dist}
Summary:	Erlang mmap interface
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
#Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{git_tag}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar
BuildRequires:	gcc
BuildRequires:	gcc-c++


%description
This Erlang library provides a wrapper that allows you to memory map files into
the Erlang memory space.


%prep
%autosetup -n %{realname}-05ae1bbc8b9b584473483023643fdc3f329a7698


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md doc/
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.39.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.38.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.37.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 0-0.35.git05ae1bb
- Rebuild for Erlang 25

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.34.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.33.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.git05ae1bb
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.28.git05ae1bb
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.26.git05ae1bb
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.23.git05ae1bb
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.22.git05ae1bb
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.17.git05ae1bb
- Rebuild for Erlang 19

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 0-0.16.git05ae1bb
- Drop unneeded macro

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 0-0.15.git05ae1bb
- Rebuild with Erlang 18.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.12.git05ae1bb
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 0-0.11.git05ae1bb
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 0-0.10.git05ae1bb
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 0-0.8.git05ae1bb
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.git05ae1bb
- Added missing build-dependency on erlang-edown

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 0-0.4.git05ae1bb
- Drop no longer needed patch
- Add dependency on NIF API version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git05ae1bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Peter Lemenkov <lemenkov@gmail.com> - 0-0.2.git05ae1bb
- Upstreamed patch, few fixes, and added emmap:read_line/1 function

* Tue Nov 13 2012 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.git8725d46
- Initial build
