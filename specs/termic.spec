Name: termic
Version: 1.3
Release: 4%{?dist}
BuildArch: noarch
Summary: GCC powered interactive C/C++ terminal created with BASH

License: GPL-3.0-only
URL: https://github.com/hanoglu/termic
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires: bash gcc gcc-c++

%description
TermiC is an interactive C/C++ terminal powered by GCC and written in BASH.
It provides a convenient way to experiment with C/C++ code snippets.

%prep
%autosetup -n TermiC-%{version}

%install
install -D -p -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -p -m 644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%check

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%license LICENSE.txt
%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%autochangelog
