Name:       spectre-meltdown-checker
Version:    0.46
Release:    6%{?dist}

Summary:    Spectre & Meltdown vulnerability/mitigation checker for Linux
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
URL:        https://github.com/speed47/spectre-meltdown-checker
Source0:    https://github.com/speed47/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:     pr495-Fix-Retpoline-detection-for-Linux-6.9+-issue-490.patch

BuildArch:  noarch

Requires:   /bin/sh
Requires:   binutils
Requires:   bzip2
Requires:   coreutils
Requires:   findutils
Requires:   gawk
Requires:   grep
Requires:   kmod
Requires:   sed
Requires:   util-linux

%if !0%{?rhel} == 7
Requires:   zstd
Suggests:   iucode-tool
Suggests:   procps-ng
Suggests:   sqlite
Suggests:   unzip
Suggests:   wget
%endif

BuildRequires: help2man

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} -n "Spectre and Meltdown mitigation detection tool" \
    --no-info --output=%{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README.md
%{_bindir}/*
%{_mandir}/man1/%{name}*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Charles R. Anderson <cra@alum.wpi.edu> - 0.46-5
- Fix Retpoline detection for Linux 6.9+ (issue #490) PR#495

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.46-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 12 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.46-1
- Update to 0.46

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 02 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.45-1
- Update to 0.45

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.44-1
- Update to 0.44

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.43-1
- Update to 0.43

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.42-1
- Update to 0.42

* Wed May 15 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.41-1
- Update to 0.41

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.40-1
- Update to 0.40

* Mon Aug 13 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.39-1
- Update to 0.39

* Tue Aug 07 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.38-1
- Update to 0.38

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.37-1
- Update to 0.37

* Tue Apr 03 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.36-1
- Update to 0.36

* Sun Feb 18 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.35-1
- Update to 0.35

* Tue Feb 13 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.34-1
- Update to 0.34

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.33-1
- Initial package
