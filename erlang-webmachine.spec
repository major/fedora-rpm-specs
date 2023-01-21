%global realname webmachine
%global upstream webmachine


Name:		erlang-%{realname}
Version:	1.11.1
Release:	11%{?dist}
BuildArch:	noarch
Summary:	A REST-based system for building web applications
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-webmachine-0001-Disable-faulty-test.patch
Patch2:		erlang-webmachine-0002-Enable-verbose-output-during-testing.patch
BuildRequires:	erlang-ibrowse
BuildRequires:	erlang-meck
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar


%description
A REST-based system for building web applications.


%prep
%autosetup -p1 -n %{realname}-%{version}
chmod 644 src/wmtrace_resource.erl
chmod -x priv/trace/wmtrace.css
chmod -x priv/trace/wmtrace.js


%build
%{erlang_compile}


%install
%{erlang_install}
# Additional resources
cp -arv priv %{buildroot}%{erlang_appdir}/


%check
# FIXME requires rebar3
#%%{erlang_test}


%files
%license LICENSE
%doc docs/http-headers-status-v3.png README.md THANKS
%{erlang_appdir}/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.11.1-4
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.11.1-1
- Ver. 1.11.1
- Switch to noarch

* Fri Aug 31 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.10.9-1
- Ver. 1.10.9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.10.8-11
- Fix FTBFS

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 27 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.10.8-9
- Spec-file cleanups

* Fri Mar  4 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.10.8-1
- Ver. 1.10.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.10.1-3
- Don't treat warnings as errors (fixes FTBFS with Erlang R16B)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.10.1-1
- Ver. 1.10.1

* Fri Mar 22 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.10.0-1
- Ver. 1.10.0

* Sun Mar 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.9.3-1
- Ver. 1.9.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.9.2-1
- Ver. 1.9.2
- Add _isa to the Requires
- Drop defattr directive

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.9.1-1
- Ver. 1.9.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.8.0-2
- Cosmetic

* Mon Jan 10 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.8.0-1
- Ver. 1.8.0

* Sat Oct 30 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.7.3-1
- Initial build

