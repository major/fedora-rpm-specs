%global realname stdlib2
%global upstream kivra


Name:		erlang-%{realname}
Version:	1.4.3
Release:	4%{?dist}
BuildArch:	noarch
Summary:	Erlang stdlib extensions
License:	BSD
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-folsom
BuildRequires:	erlang-rebar3


%description
Erlang stdlib extensions.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%doc README.md
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr  6 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.4.3-1
- Ver. 1.4.3
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug  9 2021 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.5.20180928git4cf3a70
- New git snapshot
- Convert to noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170810git5ccd9b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.20170810git5ccd9b2
- Rebuild for Erlang 20 (with proper builddeps)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170810git5ccd9b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20170810git5ccd9b2
- Initial build
