%global commit 6f66135104dc50425c904898822d49c50e130751
%global date 20221228
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: CVT (Coordinated Video Timings) modeline calculator with CVT v1.2 timings
Name: cvt12
Version: 0^%{date}git%{shortcommit}
Release: 4%{?dist}
URL: https://github.com/kevinlekiller/cvt_modeline_calculator_12
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License: BSD-3-Clause
BuildRequires: gcc
BuildRequires: make

%description
CVT (Coordinated Video Timings) modeline calculator with CVT v1.2
timings.

This is a modified CVT modeline calculator based on cvt by
erich@uruk.org, which is based on GTF modeline calculator by Andy
Ritger.

This modified version adds support for CVT v1.2 (VESA-2013-3 v1.2).

%prep
%autosetup -n cvt_modeline_calculator_12-%{commit} -p1

%build
gcc $CFLAGS $LDFLAGS cvt12.c -o cvt12 -lm

%install
install -D -pm0755 -t %{buildroot}%{_bindir} cvt12

%files
%doc README.md
%{_bindir}/cvt12

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20221228git6f66135-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20221228git6f66135-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 01 2024 Dominik Mierzejewski <dominik@greysector.net> 0^20221228git6f66135-2
- ensure Fedora LDFLAGS are also used during build

* Tue Oct 10 2023 Dominik Mierzejewski <dominik@greysector.net> 0^20221228git6f66135-1
- change versioning scheme to caret notation
- drop redundant set_build_flags macro call

* Fri Sep 22 2023 Dominik Mierzejewski <dominik@greysector.net> 0-0.1.20221228git6f66135
- initial build
