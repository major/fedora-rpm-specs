# This package only contains header files.
%global debug_package %{nil}
%bcond_without check

Name:          jpcre2
Version:       10.32.01
Release:       12%{?dist}

Summary:       C++ wrapper for PCRE2 library
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://docs.neurobin.org/jpcre2/%{version}/
Source0:       https://github.com/jpcre2/jpcre2/archive/%{version}/jpcre2-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: pcre2-devel
%if %{with check}
BuildRequires: valgrind
%endif
BuildRequires: make

%description
PCRE2 is the name used for a revised API for the PCRE library, which is a set of
functions, written in C, that implement regular expression pattern matching
using the same syntax and semantics as Perl, with just a few differences. Some
features that appeared in Python and the original PCRE before they appeared in
Perl are also available using the Python syntax.

This provides some C++ wrapper classes/functions to perform regex operations
such as regex match and regex replace.

This project currently only contains header files, which can be found in the
%{name}-devel package.

%package    devel
Summary:    %{summary}
BuildArch:  noarch
Provides:   %{name}-static = %{version}-%{release}
Requires:   pcre2-devel

%description devel
PCRE2 is the name used for a revised API for the PCRE library, which is a set of
functions, written in C, that implement regular expression pattern matching
using the same syntax and semantics as Perl, with just a few differences. Some
features that appeared in Python and the original PCRE before they appeared in
Perl are also available using the Python syntax.

This provides some C++ wrapper classes/functions to perform regex operations
such as regex match and regex replace.

%prep
%setup -q

%build
%configure \
    --enable-cpp11 \
    --enable-test \
%if %{with check}
    --enable-thread-check \
    --enable-valgrind \
%endif

%make_build

%install
%make_install
pushd %{buildroot}
mkdir -p ./%{_defaultlicensedir}/jpcre2
mv ./{%{_defaultdocdir},%{_defaultlicensedir}}/jpcre2/COPYING
rm ./%{_defaultdocdir}/jpcre2/NEWS
popd

%check
%make_build check

%files devel
%dir %{_defaultlicensedir}/jpcre2
%license %{_defaultlicensedir}/jpcre2/COPYING
%dir %{_defaultdocdir}/jpcre2
%doc %{_defaultdocdir}/jpcre2/AUTHORS
%doc %{_defaultdocdir}/jpcre2/ChangeLog
%doc %{_defaultdocdir}/jpcre2/README.md
%{_includedir}/jpcre2.hpp

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 10.32.01-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.32.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 10.32.01-1
- initial package
