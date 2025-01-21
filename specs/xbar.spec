Name:           xbar
Version:        0.0.1
Release:        9%{?dist}
Summary:        Tiny XCB information bar

License:        MIT
URL:            https://github.com/mcpcpc/xbar
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel

%description
xbar is a tiny XCB status bar. An incredibly lightweight information bar,
designed to print important real-time system metrics. Beyond foreground and
background colors, xbar offers limited customization for a distraction-free
user experience.

%prep
%autosetup

%build
%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README CHANGELOG
%{_bindir}/xbar

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.0.1-1
- Initial package
