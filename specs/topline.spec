Name:		topline
Version:	0.6
Release:	4%{?dist}
Summary:	Per-core/NUMA CPU and disk utilization plain-text grapher
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/kilobyte/topline
Source0:	https://github.com/kilobyte/topline/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc

%description
This is a top-of-the-line logger of CPU usage patterns, designed for
machines with ca. 50-300 total hardware threads (fewer works but results
in a narrow graph, more requires a very wide terminal).  Every per-tick
sample is shown abusing Unicode characters to fit within a single line.

Disk usage is also shown in a similarly terse per-device way, as %%
utilization for reads and writes.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$CFLAGS" CPPFLAGS="$CPPFLAGS" LDFLAGS="$LDFLAGS"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install topline %{buildroot}%{_bindir}
cp -p topline.1* %{buildroot}%{_mandir}/man1

%files
%{_bindir}/topline
%{_mandir}/man1/topline.1*
%license LICENSE
%doc README.md

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 dam Borowski <kilobyte@angband.pl> 0.6-1
- New upstream release.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Adam Borowski <kilobyte@angband.pl> 0.5-3
- Pass CXXFLAGS.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep  6 2021 Adam Borowski <kilobyte@angband.pl> 0.5-1
- New upstream release.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr  1 2021 Adam Borowski <kilobyte@angband.pl> 0.4-1
- Latest upstream, fixing issues with glibc 33, and on 64 big-endian.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Adam Borowski <kilobyte@angband.pl> 0.3-1
- Latest upstream.
- Review issues (capitalize short desc, license name, man page perms).

* Mon Jan 27 2020 Adam Borowski <kilobyte@angband.pl> 0.2-1
- Initial packaging.
