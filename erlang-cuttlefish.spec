%global realname cuttlefish
%global upstream basho


Name:		erlang-%{realname}
Version:        2.1.1
Release:        3%{?dist}
BuildArch:      noarch
Summary:        A library for dealing with sysctl-like configuration syntax
License:        ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	%{realname}.escript
Patch1:		erlang-cuttlefish-0001-Disable-escript-generation.patch
Patch2:		erlang-cuttlefish-0002-No-rebar_mustache-available.patch
Patch3:		erlang-cuttlefish-0003-Add-recent-otp-versions-to-rebar.config.patch
Patch4:		erlang-cuttlefish-0004-erlang-get_stacktrace-0-deprecated.patch
BuildRequires:  erlang-bbmustache
BuildRequires:  erlang-getopt
BuildRequires:  erlang-lager
BuildRequires:  erlang-rebar3


%description
Cuttlefish is a library for Erlang applications that wish to walk the fine line
between Erlang app.configs and a sysctl-like syntax. The name is a pun on the
pronunciation of 'sysctl' and jokes are better explained.


%prep
%autosetup -p1 -n %{realname}-%{version}
# Temporarily remove rebar plugin until we start packaging rebar plugins
rm -f src/cuttlefish_rebar_plugin.erl


%build
%{erlang3_compile}


%install
%{erlang3_install}
# Install cuttlefish script itself
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{realname}


%check
%{erlang3_test}


%files
%doc README.md
%{_bindir}/%{realname}
%{erlang_appdir}/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 29 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.1.1-1
- Ver. 2.1.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-1
- Ver. 2.1.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.0.11-9
- Fix deprecation warning

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.11-1
- Ver. 2.0.11

* Tue Nov 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.10-1
- Ver. 2.0.10

* Tue Mar 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.6-1
- Initial packaging
