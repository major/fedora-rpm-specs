Name:           mcrcon
Version:        0.7.2
Release:        9%{?dist}
Summary:        Console based rcon client for minecraft servers
License:        Zlib
URL:            https://github.com/Tiiffi/mcrcon/
Source0:        https://github.com/Tiiffi/mcrcon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
Mcrcon is powerful IPv6 compliant minecraft rcon client with bukkit coloring
support. It is well suited for remote administration and to be used as part of
automated server maintenance scripts. Does not cause "IO: Broken pipe" or
"IO: Connection reset" spam in server console.

Features:
- Interactive terminal mode - keeps the connection alive
- Send multiple commands in one command line
- Silent mode - does not print rcon output
- Support for bukkit coloring on Windows and Linux (sh compatible shells)
- Multiplatform code - compiles on many platforms with only minor changes

%prep
%setup -q

# Fix line endings
sed -i 's/\r$//' README.md

%build
%make_build CFLAGS="-std=gnu99" EXTRAFLAGS="%{?__global_cflags} %{?__global_ldflags}"

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/mcrcon
%{_mandir}/man1/mcrcon.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar  3 2023 Paul Howarth <paul@city-fan.org> - 0.7.2-4
- Use SPDX-format license tag

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Paul Howarth <paul@city-fan.org> - 0.7.2-1
- Update to 0.7.2
  - Set default address to localhost
  - Add -w option for rcon command throttling
  - Deprecate -i flag for invoking terminal mode
  - Add workaround to prevent server-side bug
    (https://bugs.mojang.com/browse/MC-154617)
  - Quit gracefully when Ctrl-D or Ctrl+C is pressed
  - Remove "exit" and "quit" as quitting commands (these are actual rcon
    commands on some servers)
  - Suppress compiler warning (strncpy)
  - Fix erroneous string length in packet building function
  - Fix typo in ANSI escape sequence for LCYAN
  - Make stdout and stderr unbuffered
- Switch upstream URL from sourceforge to GitHub
- Make sure distribution compiler/linker flags are used
- Package CHANGELOG.md

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.6.1-3
- Remove Group tag

* Fri May 03 2019  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.6.1-2
- Specify gnu99 standard, required for gcc 4.8

* Fri May 03 2019  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.6.1-1
- Update to 0.6.1
- Use Fedora build flags and enable debuginfo

* Tue Mar 14 2017  Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Escape macro references in changelog
- Fix bogus date in %%changelog: Sat Nov 13 2016

* Sun Nov 13 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-5
- Fix typo in man page paths

* Sun Nov 13 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-4
- Include a basic manual page

* Sat Nov 12 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-3
- Fix %%description lines used more then 79 chars
- Use GitHub instead of Sourceforge for sources
- Change compiler flags according to upstream recommendation
- Convert README.md to unix line endings
- Remove unnecessary "rm -rf %%{buildroot}"

* Mon Nov  7 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-2
- Cleanup

* Mon Nov  7 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-1
- Initial build
