Summary: SQL / SQLI tokenizer parser analyzer library
Name: libinjection
Version: 3.10.0
Release: 13%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://github.com/libinjection/libinjection
Source0: https://github.com/libinjection/libinjection/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: Makefile-libinjection
Patch0: libinjection-3.10.0-use_correct_version.patch
Patch1: 0001-Cosmetics-addresses-some-issues-reported-by-cppcheck.patch
Patch2: 0002-Specify-Python-version-explicitly-in-shebangs.patch
Patch3: 0003-Adds-usage-info-libinjection_xss.patch
Patch4: 0004-Fix-cppcheck-errors.patch
Patch5: 0005-Pass-the-correct-pointer-to-memmem.patch
Patch6: 0006-feat-py3-update-build-syntax-to-py3.patch
Buildrequires: gcc make libtool python3

%description
SQL / SQLI tokenizer parser analyzer library

%package tests
Summary: Various tools for testing %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains various tools for testing.

Use it like:
reader -m 21 %{_datadir}/%{name}/false_*.txt

%package devel
Summary: Development files for %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%autosetup -p1
cp %{SOURCE1} src/Makefile

%build
%{__make} \
    CFLAGS="%{build_cflags}" \
    LDFLAGS="%{build_ldflags}" \
    -C src

%install
%makeinstall -C src

install -d %{buildroot}%{_datadir}/%{name}/
install -m0644 data/* %{buildroot}%{_datadir}/%{name}/

install -d %{buildroot}%{_libdir}/pkgconfig

cat > %{buildroot}%{_libdir}/pkgconfig/libinjection.pc << EOF
# libinjection pkg-config file

prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libinjection
Description: SQL / SQLI tokenizer parser analyzer library
URL: https://github.com/libinjection/libinjection
Version: %{version}
Requires:
Conflicts:
Libs: -L\${libdir} -linjection
Cflags: -I\${includedir}
EOF

# cleanup
rm -f %{buildroot}%{_libdir}/libinjection.*a

# For EPEL7 compatibility
%ldconfig_scriptlets

%files
%license COPYING
%doc README*
%{_bindir}/fptool
%{_bindir}/html5
%{_bindir}/sqli
%{_libdir}/*.so.*

%files tests
%{_bindir}/reader
%{_bindir}/testdriver
%{_bindir}/testspeedsqli
%{_bindir}/testspeedxss
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.10.0-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Neal Gompa <ngompa@fedoraproject.org> - 3.10.0-4
- Add ldconfig_scriptlets macro for EPEL 7

* Sun Dec 12 2021 Oden Eriksson <oe@nux.se> 3.10.0-3
- use the correct rpm macros for CFLAGS and LDFLAGS
- P1: use correct version
- P2-P6: add upstream fixes

* Fri Dec 10 2021 Oden Eriksson <oe@nux.se> 3.10.0-2
- S1: build it a bit nicer (libool, make)
- provide the test suite as well

* Fri Dec 10 2021 Oden Eriksson <oe@nux.se> 3.10.0-1
- fixed according to #2029308

* Mon Dec 06 2021 Oden Eriksson <oe@nux.se> 3.10.0-0
- initial RPM package
