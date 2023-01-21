%global srcname xmpp

%global ezlib_ver 1.0.8
%global fast_tls_ver 1.1.8
%global fast_xml_ver 1.1.43
%global idna_ver 6.0.0
%global p1_utils_ver 1.0.20
%global stringprep_ver 1.0.22

Name:       erlang-%{srcname}
Version:    1.4.9
Release:    6%{?dist}
Summary:    Erlang/Elixir XMPP parsing and serialization library

License:    ASL 2.0
URL:        https://github.com/processone/xmpp/
Source0:    https://github.com/processone/xmpp/archive/%{version}/xmpp-%{version}.tar.gz
# https://github.com/processone/xmpp/pull/3
Patch0:     0001-Allow-fxml.hrl-to-be-found-from-system-libs.patch

BuildRequires: gcc
BuildRequires: erlang-ezlib >= %{ezlib_ver}
BuildRequires: erlang-fast_tls >= %{fast_tls_ver}
BuildRequires: erlang-fast_xml >= %{fast_xml_ver}
BuildRequires: erlang-idna >= %{idna_ver}
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar
BuildRequires: erlang-stringprep >= %{stringprep_ver}

Requires: erlang-ezlib >= %{ezlib_ver}
Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-fast_xml >= %{fast_xml_ver}
Requires: erlang-idna >= %{idna_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}
Requires: erlang-stringprep >= %{stringprep_ver}


%description
XMPP is an Erlang XMPP parsing and serialization library, built on top of Fast
XML.


%prep
%setup -q -n %{srcname}-%{version}

%patch0 -p0


%build
%{rebar_compile}


%install
%{erlang_install}

install -p -D -m 755 priv/lib/* --target-directory=%{buildroot}%{erlang_appdir}/priv/lib/


%check
%{rebar_eunit}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc doc
%doc README.md
%{erlang_appdir}


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4.9-1
- Update to 1.4.9 (#1807248).
- https://github.com/processone/xmpp/blob/1.4.9/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4 (#1789112).
- https://github.com/processone/xmpp/blob/1.4.4/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4.2-2
- Bring xmpp back to s390x (#1775737).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2 (#1742454).
- https://github.com/processone/xmpp/blob/1.4.2/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4 (#1706342).
- https://github.com/processone/xmpp/blob/1.3.4/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2 (#1667604).
- https://github.com/processone/xmpp/blob/1.3.2/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.2.8-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8.
- https://github.com/processone/xmpp/blob/1.2.8/CHANGELOG.md
