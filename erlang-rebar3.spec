%global realname rebar3
%global otp_app_name rebar

# Bootstrapping
%global bootstrap 1

Name:     erlang-%{realname}
Version:  3.22.0
Release:  2%{?dist}
Summary:  Tool for working with Erlang projects
License:  ASL 2.0 and MIT
URL:      https://github.com/erlang/%{realname}
Source0:  %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:  rebar3.escript
Patch1:   erlang-rebar3-0001-Skip-deps.patch
Patch2:   erlang-rebar3-0002-Unbundle-hex_core-ver.-0.7.1.patch
Patch3:   erlang-rebar3-0003-WIP-ignore-deps-on-demand.patch
Patch4:   erlang-rebar3-0004-WIP-prefer-locally-installed-plugins.patch
%if 0%{?bootstrap}
# noop
%else
BuildRequires:  erlang-rebar3
%endif

BuildArch: noarch
BuildRequires:  erlang-bbmustache
BuildRequires:  erlang-certifi
BuildRequires:  erlang-cf
BuildRequires:  erlang-cth_readable
BuildRequires:  erlang-dialyzer
BuildRequires:  erlang-edoc
BuildRequires:  erlang-erl_interface
BuildRequires:  erlang-erlware_commons
BuildRequires:  erlang-erts
BuildRequires:  erlang-eunit_formatters
BuildRequires:  erlang-getopt
BuildRequires:  erlang-hex_core
BuildRequires:  erlang-parsetools
BuildRequires:  erlang-providers
BuildRequires:  erlang-relx
BuildRequires:  erlang-rpm-macros
BuildRequires:  erlang-ssl_verify_fun
BuildRequires:  perl-interpreter

# FIXME wip
#Requires:	erlang-abnfc
#Requires:	erlang-gpb

# This one cannot be picked up automatically
Requires:	erlang-cth_readable
# This one cannot be picked up automatically
# See https://bugzilla.redhat.com/960079
Requires:	erlang-common_test
# Requires for port compiling - no direct references in Rebar's src/*.erl files
Requires:	erlang-erl_interface
# This one cannot be picked up automatically
Requires:	erlang-eunit_formatters
# This one cannot be picked up automatically
# See https://bugzilla.redhat.com/960079
Requires:	erlang-parsetools

Requires:	erlang-rpm-macros >= 0.3.6

%description
Rebar3 is an Erlang tool that makes it easy to create, develop, and release
Erlang libraries, applications, and systems in a repeatable manner.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
ebin_paths=$(perl -e 'print join(":", grep { !/rebar/} (glob("%{_libdir}/erlang/lib/*/ebin"), glob("%{_datadir}/erlang/lib/*/ebin")))')

%if 0%{?bootstrap}
DIAGNOSTIC=1 ./bootstrap bare compile --paths $ebin_paths --separator :
%else
DEBUG=1 %{realname} bare compile --paths $ebin_paths --separator :
%endif

%install
# Install rebar script itself
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/rebar3

mkdir -p %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 _build/bootstrap/lib/rebar/ebin/*.beam %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 _build/bootstrap/lib/rebar/ebin/%{otp_app_name}.app %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/

# Copy the contents of priv folder
cp -a apps/rebar/priv %{buildroot}%{_erllibdir}/%{realname}-%{version}/

mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m644 manpages/%{realname}.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md rebar.config.sample THANKS
%{_bindir}/%{realname}
%{_datadir}/erlang/lib/%{realname}-%{version}
%{_mandir}/man1/%{realname}.1*

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul  6 2023 Peter Lemenkov <lemenkov@gmail.com> - 3.22.0-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr  7 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.18.0-5
- One more missing dep

* Thu Feb 17 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.18.0-4
- One more missing dep

* Thu Feb 17 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.18.0-3
- Missing deps

* Fri Feb  4 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.18.0-2
- Install templates
- Drop bundled hex_core

* Wed Feb  2 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.18.0-1
- New upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.14.3-1
- New upstream release

* Tue Dec  1 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.14.1-1
- New upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Timothée Floure <fnux@fedoraproject.org> - 3.13.1-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Timothée Floure <fnux@fedoraproject.org> - 3.11.1-1
- New upstream release

* Fri May 31 2019 Timothée Floure <fnux@fedoraproject.org> - 3.10.1-1
- Rebase on latest upstream release

* Thu May 30 2019 Timothée Floure <fnux@fedoraproject.org> - 3.8.0-4
- Rebootstrap from upstream rebar 3.8.0 binary (see packaging-comittee/#889 on pagure)

* Fri Mar 08 2019 Timothée Floure <fnux@fedoraproject.org> - 3.8.0-3
- Add dependency on erlang-hex_core
- Load noarch erlang dependencies during compilation

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Timothée Floure <fnux@fedoraproject.org> - 3.8.0-1
- New upstream release

* Tue Dec 18 2018 Timothée Floure <fnux@fedoraproject.org> - 3.6.2-3
- Switch to noarch in accord with 'Changes/TrueNoarchErlangPackages'

* Wed Dec 12 2018 Timothée Floure <fnux@fedoraproject.org> - 3.6.2-2
- Disable bootstaping following initial build in rawhide

* Fri Oct 12 2018 Timothée Floure <fnux@fedoraproject.org> - 3.6.2-1
- Let there be package
