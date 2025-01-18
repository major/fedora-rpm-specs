Name:           frog-protocols
Version:        0.01
Release:        2%{?dist}
Summary:        Faster moving Wayland protocols

License:        MIT
URL:            https://github.com/misyltoad/frog-protocols
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson

# This is a development package so add it for convention
Provides:       %{name}-devel = %{version}-%{release}


%description
%{name} contains Wayland protocol definitions for protocols
being developed in a more agile fashion to enable shipping
functionality to users more quickly. It is intended to
accelerate development of formal Wayland protocols.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE.md
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.01-1
- Initial package
