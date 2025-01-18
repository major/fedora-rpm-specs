Summary: An high level argument parsing library for bash
Name: bash-argsparse
Version: 1.8
Release: 6%{?dist}
License: WTFPL
URL: https://github.com/Anvil/bash-argsparse
Source0: http://argsparse.livna.org/%{name}-%{version}.tar.gz
BuildArch: noarch
# Binaries are required for unittest to perform cleanly.
BuildRequires: doxygen
BuildRequires: glibc-common
BuildRequires: util-linux
BuildRequires: /usr/bin/host

Requires: bash >= 4.1
Requires: util-linux
Requires: glibc-common
Requires: /usr/bin/host

%description
An high level argument parsing library for bash.

The purpose is to replace the option-parsing and usage-describing
functions commonly rewritten in all scripts.

This library is implemented for bash version 4. Prior versions of bash
will fail at interpreting that code.


%prep
%autosetup -n %{name}-%{name}-%{version}


%build
# Nothing to build, except the documentation.
doxygen


%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 argsparse.sh %{buildroot}/%{_bindir}
ln -s argsparse.sh %{buildroot}/%{_bindir}/argsparse


%check
./unittest


%files
%doc tutorial README.md html COPYING
%{_bindir}/argsparse
%{_bindir}/argsparse.sh


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.8-1
- Update to 1.8 rhbz#1488681
- Preserve source modification timestamps

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 5 2015 Dams <bash-argsparse[AT]livna.org> - 1.7-1
- Version 1.7

* Wed Jan 28 2015 Dams <bash-argsparse[AT]livna.org> - 1.6.2-1
- Version 1.6.2
- Dropped fedora patch (included upstream)

* Fri Oct 24 2014 Dams <bash-argsparse[AT]livna.org> - 1.6.1-3
- Using package names instead of path for Requires/BuildRequires

* Wed Oct 15 2014 Dams <bash-argsparse[AT]livna.org> - 1.6.1-2
- Added patch to fix some unittest issues

* Thu Oct 9 2014 Dams <bash-argsparse[AT]livna.org> - 1.6.1-1
- Version 1.6.1
- Fixed changelog names

* Thu Oct 9 2014 Dams <bash-argsparse[AT]livna.org> - 1.6-4
- Update host path in *Requires tags.

* Wed Oct 8 2014 Dams <bash-argsparse[AT]livna.org> - 1.6-3
- Added more BuildRequires to allow unittest script to run correctly
  restricted small environments

* Mon Sep 15 2014 Dams <bash-argsparse[AT]livna.org> - 1.6-2
- Fixed date in changelog entry

* Tue Aug 12 2014 Dams <bash-argsparse[AT]livna.org> - 1.6-1
- License tag is now WTFPL
- Removed trailing dot at the end of Summary
- Removed BuildRoot tag
- Requiring commands instead of packages

* Mon Jan 13 2014 Dams <bash-argsparse[AT]livna.org> - 1.6-0
- Version 1.6
- Added doxygen documentation
- check section

* Thu Mar 21 2013 Dams <bash-argsparse[AT]livna.org> - 1.5-0
- Version 1.5
- Updated Requires
- Removed old/fedora-obsolete directives/noise

* Thu Mar 14 2013 Dams <bash-argsparse[AT]livna.org> - 1.4-0
- Initial build.

