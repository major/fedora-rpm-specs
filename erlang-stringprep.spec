%global srcname stringprep

%global p1_utils_ver 1.0.20


Name: erlang-%{srcname}
Version: 1.0.22
Release: 6%{?dist}

License: ASL 2.0 and TCL
Summary: A framework for preparing Unicode strings to help input and comparison
URL: https://github.com/processone/stringprep/
Source0: https://github.com/processone/stringprep/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:  erlang-p1_stringprep = %{version}-%{release}
Obsoletes: erlang-p1_stringprep < 1.0.3

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
Stringprep is a framework for preparing Unicode test strings in order to
increase the likelihood that string input and string comparison work. The
principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast
and efficient processing.


%prep
%autosetup -n stringprep-%{version}


%build
%{rebar_compile}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%check
%{rebar_eunit}


%files
%license LICENSE.txt LICENSE.TCL LICENSE.ALL
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.22-1
- Update to 1.0.22 (#1807190).
- https://github.com/processone/stringprep/blob/1.0.22/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18 (#1789037).
- https://github.com/processone/stringprep/blob/1.0.18/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-2
- Bring stringprep back to s390x (#1772971).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17 (#1742461).
- https://github.com/processone/stringprep/blob/1.0.17/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.16-1
- Update to 1.0.16 (#1713323).
- https://github.com/processone/stringprep/blob/1.0.16/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.15-1
- Update to 1.0.15 (#1683159).
- https://github.com/processone/stringprep/blob/1.0.15/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.14-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
