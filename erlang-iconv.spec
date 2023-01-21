%global srcname iconv

%global p1_utils_ver 1.0.19

Name:       erlang-%{srcname}
Version:    1.0.13
Release:    2%{?dist}
Summary:    Fast encoding conversion library for Erlang / Elixir
License:    ASL 2.0
URL:        https://github.com/processone/iconv/
Source0:    https://github.com/processone/iconv/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:     erlang-iconv-0001-Disable-port-compiler-until-we-package-it.patch
Provides:   erlang-p1_iconv = %{version}-%{release}
Obsoletes:  erlang-p1_iconv <= 1.0.0-2
BuildRequires: gcc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
Erlang bindings for libiconv. This is used by ejabberd.


%prep
%autosetup -n iconv-%{version}


%build
%configure --enable-nif
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc c_src/iconv.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/iconv.o
gcc c_src/iconv.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -o priv/lib/iconv.so


%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/iconv.so $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/


%check
%{erlang3_test}


%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.0.13-1
- Update to 1.0.13

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11 (#1858904).
- Fix FTBFS (#1863504).
- https://github.com/processone/iconv/blob/1.0.11/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-5
- Rebuild for Erlang 22 (#1775733).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.10-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
