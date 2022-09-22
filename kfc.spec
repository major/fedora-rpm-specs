Name:           kfc
Version:        0.1.3
Release:        4%{?dist}
Summary:        Terminal-emulator color palette setter written in POSIX C99

License:        MIT
URL:            https://github.com/mcpcpc/kfc
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libX11-devel

%description
kfc ("KISS for colors") is a terminal-emulator color palette setter written in
POSIX C99. This allows one to achieve consistent colors across all terminal
utilities and applications.

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
%doc README docs
%{_bindir}/kfc
%{_datadir}/kfc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1.3-1
- Initial package
