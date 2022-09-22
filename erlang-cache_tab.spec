%global srcname cache_tab

%global p1_utils_ver 1.0.20

Name: erlang-cache_tab
Version: 1.0.25
Release: 5%{?dist}

License: ASL 2.0
Summary: Erlang cache table application
URL: https://github.com/processone/cache_tab/
Source0: https://github.com/processone/cache_tab/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
This application is intended to proxy back-end operations for Key-Value insert,
lookup and delete and maintain a cache of those Key-Values in-memory, to save
back-end operations. Operations are intended to be atomic between back-end and
cache tables. The lifetime of the cache object and the max size of the cache
can be defined as table parameters to limit the size of the in-memory tables.


%prep
%autosetup -n cache_tab-%{version}


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
%doc README.md
%{_erllibdir}/%{srcname}-%{version}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.25-1
- Update to 1.0.25 (#1807250).
- https://github.com/processone/cache_tab/blob/1.0.25/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.21-1
- Update to 1.0.21 (#1789138).
- https://github.com/processone/cache_tab/blob/1.0.21/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.20-2
- Bring cache_tab back to s390x (#1772962).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.20-1
- Update to 1.0.20 (#1742463).
- https://github.com/processone/cache_tab/blob/1.0.20/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.19-1
- Update to 1.0.19 (#1713296).
- https://github.com/processone/cache_tab/blob/1.0.19/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18 (#1683120).
- https://github.com/processone/cache_tab/blob/1.0.18/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.17-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17.
- https://github.com/processone/cache_tab/blob/1.0.17/CHANGELOG.md
