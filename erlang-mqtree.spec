%global srcname mqtree

%global p1_utils_ver 1.0.20


Name:       erlang-%{srcname}
Version:    1.0.10
Release:    6%{?dist}

# c_src/uthash.h is unspecified BSD
License:    ASL 2.0 and BSD
Summary:    Index tree for MQTT topic filters
URL:        https://github.com/processone/mqtree/
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar
BuildRequires: gcc
BuildRequires: openssl-devel

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
mqtree is an Erlang NIF implementation of N-ary tree
to keep MQTT topic filters for efficient matching.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{rebar_compile}


%install
install -d %{buildroot}%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* %{buildroot}%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%check
%{rebar_eunit}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10 (#1807345).
- https://github.com/processone/mqtree/blob/1.0.10/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6 (#1788885).
- https://github.com/processone/mqtree/blob/1.0.6/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.5-2
- Bring mqtree back to s390x (#1772970).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 (#1742469)
- https://github.com/processone/mqtree/compare/1.0.3...1.0.5
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (#1713422).
- https://github.com/processone/mqtree/compare/1.0.2...1.0.3

* Sun Apr 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.2-2
- Correct license to ASL 2.0 and BSD because c_src/uthash.h is unspecified BSD.

* Sat Apr 13 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.2-1
- Initial release.
