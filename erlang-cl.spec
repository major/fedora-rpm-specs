%global realname cl
%global upstream tonyrog


Name:		erlang-%{realname}
Version:	1.2.4
Release:	16%{?dist}
Summary:	OpenCL binding for Erlang
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/cl-%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-cl-0001-Remove-handmade-makefile.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar
BuildRequires:	gcc
BuildRequires:	ocl-icd-devel
BuildRequires:	opencl-headers


%description
OpenCL binding for Erlang.


%prep
%autosetup -p1 -n %{realname}-cl-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
# Can't pass autotests for now due to limited OpenCL support in Fedora (?)
#%%{erlang_test}


%files
%license COPYRIGHT
%doc README examples/
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.2.4-12
- Rebuild for Erlang 25

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.2.4-5
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.2.4-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.2.4-1
- Ver. 1.2.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.2.3-4
- Rebuild for Erlang 20 (with proper builddeps)

* Tue Mar 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.2.3-3
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.2.3-1
- Ver. 1.2.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.2.1-13
- Rebuild for OpenCL 2.1

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.2.1-12
- Rebuild for Erlang 19

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-11
- Drop unneeded macro

* Sat Apr  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-10
- Rebuild with Erlang 18.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-9
- Rebuild with Erlang 18.2.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-6
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-5
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.2.1-3
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Initial package
