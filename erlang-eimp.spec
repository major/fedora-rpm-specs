%global srcname eimp

%global p1_utils_ver 1.0.20


Name:    erlang-eimp
Version: 1.0.17
Release: 7%{?dist}

License: ASL 2.0
Summary: Erlang Image Manipulation Process
URL:     https://github.com/processone/eimp/
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gd-devel
BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
eimp is an Erlang/Elixir application for manipulating graphic images
using external C libraries. It supports WebP, JPEG, PNG and GIF.


%prep
%autosetup -n %{srcname}-%{version}
rm configure


%build
autoreconf -ivf
%configure
%{rebar_compile}


%install
%{erlang_install}

install -p -D -m 755 priv/bin/* --target-directory=%{buildroot}%{erlang_appdir}/priv/bin/


%check
# The unit tests do not pass: https://github.com/processone/eimp/issues/5
echo "Skipping tests."


%files
%license LICENSE.txt
%doc README.md
%{_erllibdir}/%{srcname}-%{version}


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17 (#1807270).
- https://github.com/processone/eimp/blob/1.0.17/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.13-1
- Update to 1.0.13 (#1789164).
- https://github.com/processone/eimp/blob/1.0.13/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.12-2
- Bring eimp back to s390x (#1772963).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12 (#1742460).
- https://github.com/processone/eimp/blob/1.0.12/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11 (#1713302).
- https://github.com/processone/eimp/blob/1.0.11/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10 (#1683121).
- https://github.com/processone/eimp/blob/1.0.10/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9.
- https://github.com/processone/eimp/blob/1.0.9/CHANGELOG.md
