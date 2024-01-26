%global realname cowlib
%global upstream ninenines


Name:		erlang-%{realname}
Version:	2.11.0
Release:	8%{?dist}
BuildArch:	noarch
Summary:	Support library for manipulating Web protocols
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar


%description
Support library for manipulating Web protocols.


%prep
%autosetup -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
# FIXME doesn't work with ProPer atm
#%%{__rebar} qc -vv


%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Peter Lemenkov <lemenkov@gmail.com> - 2.11.0-1
- Ver. 2.11.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.10.1-1
- Ver. 2.10.1

* Tue Nov 17 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.10.0-1
- Ver. 2.10.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.9.1-1
- Ver. 2.9.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.8.0-1
- Ver. 2.8.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.7.2-1
- Ver. 2.7.2

* Tue Apr 02 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.7.1-1
- Ver. 2.7.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.5.1-1
- Ver. 2.5.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.2.0-2
- Rebuild for Erlang 20 (with proper builddeps)

* Tue Mar 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.2.0-1
- Ver. 2.2.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-1
- Ver. 2.1.0

* Tue Nov 28 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.1-1
- Ver. 2.0.1

* Fri Oct 06 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-1
- Ver. 2.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 14 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Initial packaging
