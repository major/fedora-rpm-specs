%global srcname fast_yaml

%global p1_utils_ver 1.0.20

Name: erlang-%{srcname}
Version: 1.0.33
Release: 2%{?dist}

License: ASL 2.0
Summary: An Erlang wrapper for libyaml "C" library
URL:     https://github.com/processone/fast_yaml/
Source0: https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:  erlang-fast_yaml-0001-Disable-port-compiler-until-we-package-it.patch
Provides:  erlang-p1_yaml = %{version}-%{release}
Obsoletes: erlang-p1_yaml < 1.0.2

BuildRequires: gcc
BuildRequires: erlang-rebar3
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: libyaml-devel

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
P1 YAML is an Erlang wrapper for libyaml "C" library.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc c_src/fast_yaml.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fast_yaml.o
gcc c_src/fast_yaml.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -lyaml -o priv/lib/fast_yaml.so


%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib


%check
%{erlang3_test}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.0.33-1
- Update to 1.0.33

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.27-1
- Update to 1.0.27 (#1807286).
- https://github.com/processone/fast_yaml/blob/1.0.27/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.22-1
- Update to 1.0.22 (#1789167).
- https://github.com/processone/fast_yaml/blob/1.0.22/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.21-2
- Bring fast_yaml back to s390x (#1772969).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.21-1
- Update to 1.0.21 (1742455).
- https://github.com/processone/fast_yaml/blob/1.0.20/CHANGELOG.md
- https://github.com/processone/fast_yaml/blob/1.0.21/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.19-1
- Update to 1.0.19 (#1713301).
- https://github.com/processone/fast_yaml/blob/1.0.19/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18 (#1683116).
- https://github.com/processone/fast_yaml/blob/1.0.18/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.17-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
