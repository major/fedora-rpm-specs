%global realname hamcrest
%global upstream hyperthunk
%global git_tag 0766ea004f7dd900c36b06aff14dbbac1d03b425


Name:		erlang-%{realname}
Version:	0.1.0
Release:	22%{?dist}
BuildArch:	noarch
Summary:	A framework for writing matcher objects using declarative rules
License:	MIT and BSD
URL:		https://github.com/%{upstream}/%{realname}-erlang
VCS:		scm:git:https://github.com/%{upstream}/%{realname}-erlang.git
#Source0:	https://github.com/%{upstream}/%{realname}-erlang/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}-erlang/archive/%{git_tag}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-proper
BuildRequires:	erlang-rebar


%description
Hamcrest is a framework for writing matcher objects allowing 'match' rules to
be defined declaratively. There are a number of situations where matchers are
invaluable, such as UI validation, or data filtering, but it is in the area of
writing flexible tests that matchers are most commonly used.


%prep
#%setup -q -n %{realname}-erlang-%{version}
%autosetup -p1 -n %{realname}-erlang-%{git_tag}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{rebar_ct -C test.config}


%files
%license LICENCE
%doc NOTES README.markdown
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.1.0-13
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.1.0-11
- Update to the latest master
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Merlin Mathesius <mmathesi@redhat.com> - 0.1.0-4
- Import upstream patch to support OTP 19 (BZ#1404854).

* Thu Jun  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1.0-3
- Spec-file cleanup

* Sun Feb 14 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1.0-2
- Fixed FTBFS in Rawhide

* Sun Feb 14 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1.0-1
- Initial package
