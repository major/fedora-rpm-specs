%global srcname ezlib


Name:       erlang-%{srcname}
Version:    1.0.8
Release:    8%{?dist}

License:    ASL 2.0
Summary:    Native zlib driver for Erlang
URL:        https://github.com/processone/ezlib/
Source0:    https://github.com/processone/ezlib/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:   erlang-p1_zlib = %{version}-%{release}
Obsoletes:  erlang-p1_zlib <= 1.0.1-2

BuildRequires: gcc
BuildRequires: erlang-rebar
BuildRequires: zlib-devel


%description
A native zlib driver for Erlang / Elixir, used by ejabberd.


%prep
%autosetup -n ezlib-%{version}


%build
%configure --enable-nif
# There is a pull request upstream for this -lz https://github.com/processone/ezlib/pull/1
LDFLAGS="$LDFLAGS -lz" %{rebar_compile}


%check
%{rebar_eunit}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/ezlib_drv.so \
    $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8 (#1807016).
- https://github.com/processone/ezlib/blob/1.0.8/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6 (#1713426).
- https://github.com/processone/ezlib/blob/1.0.6/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 (#1683183).
- https://github.com/processone/ezlib/blob/1.0.5/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
