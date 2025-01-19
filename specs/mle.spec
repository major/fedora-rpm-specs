Summary:         A small, flexible, terminal-based text editor
Name:            mle
Version:         1.7.2
Release:         7%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:         Apache-2.0
URL:             https://github.com/adsr/mle
Source:          https://github.com/adsr/mle/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:   gcc
BuildRequires:   pcre2-devel
BuildRequires:   uthash-devel
BuildRequires:   lua-devel
BuildRequires:   glibc-langpack-en

%description
mle is a small, flexible, terminal-based text editor written in C.
Notable features include: full Unicode support, syntax highlighting,
scriptable rc file, macros, search and replace (PCRE), window
splitting, multiple cursors, and integration with various shell
commands.

%prep
%setup -q
sed -i 's|-llua5.4|-llua|g' Makefile
sed -i 's|install -D |install -D -p |g' Makefile
sed -i 's|<lua5.4/lua.h>|<lua.h>|g' mle.h
sed -i 's|<lua5.4/lualib.h>|<lualib.h>|g' mle.h
sed -i 's|<lua5.4/lauxlib.h>|<lauxlib.h>|g' mle.h

%build
%make_build

%check
LC_ALL=en_US.UTF-8 make %{?_smp_mflags} test

%install
%make_install prefix=%{_prefix}
install -D -p -v -m 644 mle.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/mle.1

%files
%license LICENSE
%doc README.md
%{_bindir}/mle
%{_mandir}/man1/mle.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.2-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 24 2023 Adam Saponara <as@php.net> - 1.7.2-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 Adam Saponara <as@php.net> - 1.5.0-1
- initial spec
