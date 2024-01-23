Name: libmodsecurity
Version: 3.0.10
Release: 2%{?dist}
Summary: A library that loads/interprets rules written in the ModSecurity SecRules

License: Apache-2.0
URL: https://github.com/SpiderLabs/ModSecurity

Source0: https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz

BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: make
BuildRequires: pkgconfig(libcurl)
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: pkgconfig(libmaxminddb)
%else
BuildRequires: pkgconfig(geoip)
%endif
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(lmdb)
BuildRequires: pkgconfig(yajl)
BuildRequires: ssdeep-devel

# libinjection is supposed to be bundled (same as with mod_security 2.x)
# See: https://github.com/client9/libinjection#embedding
Provides: bundled(libinjection) = 3.9.2

%description
Libmodsecurity is one component of the ModSecurity v3 project.
The library codebase serves as an interface to ModSecurity Connectors
taking in web traffic and applying traditional ModSecurity processing.
In general, it provides the capability to load/interpret rules written
in the ModSecurity SecRules format and apply them to HTTP content provided
by your application via Connectors.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package static
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for developing
applications that use %{name}.



%prep
%autosetup -n modsecurity-v%{version} -S git


%build
%configure --libdir=%{_libdir} --with-lmdb --with-pcre2 --without-pcre
%make_build


%install
%make_install

# Clean out files that should not be part of the rpm.
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets


%files
%doc README.md AUTHORS
%{_libdir}/*.so.*
%{_bindir}/*
%license LICENSE

%files devel
%doc README.md AUTHORS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig
%license LICENSE

%files static
%{_libdir}/*.a


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.0.10-1
- Update to 3.0.10 rhbz#2225895

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.0.9-2
- Use geoip instead of libmaxminddb for EPEL 7 and 8 builds

* Sat Apr 15 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.0.9-1
- 2828.patch: drop, included in 3.0.9
- Remove deps required for autoreconf
- Minor cosmetic change for configure
- ModSecurity_cookie_parsing_fix_303.patch: remove as not required since 3.0.4
- 0001-Fix-build-on-non-x86-arch.patch: remove as not required since 3.0.4
- modsecurity.pc: drop as is being shipped since 3.0.3

* Mon Mar 27 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.0.8-3
- Use PCRE2 rhbz#2128321
- Use libmaxminddb instead of old GeoIP
- Migrate to SPDX identifier for License
- Change homepage
- Remove .la file for EPEL

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 15 2022 Othman Madjoudj <athmane@fedoraproject.org> - 3.0.8-1
- Update to maintenance release 3.0.8

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.4-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Othman Madjoudj <athmane@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4
- Drop the patch (included in this release)

* Sat Mar 21 2020 Othman Madjoudj <athmane@fedoraproject.org> - 3.0.3-6
- Fix DoS vulnerability (CVE-2019-19886, RHBZ #1801720 / #1801719)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 31 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3 (rhbz #1672678)
- Remove pkg-config bits since it's included in this release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 3.0.2-4
- Back-port of modsecurity.pc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.2-2
- Rebuild after PR#1

* Sat Apr 14 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2 (rhbz #1563219)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 final release
- Drop upstreamed patch
- Add some new BRs

* Sun Oct 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.2.rc1
- Add a patch to fix the build on non-x86 arch

* Fri Sep 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.1.rc1
- Fix release tag

* Wed Aug 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.rc1
- Update to RC1
- Fix some spec issues

* Mon Feb 22 2016 Athmane Madjoudj <athmane@fedoraproject.org> 3.0-0.git
- Initial release

