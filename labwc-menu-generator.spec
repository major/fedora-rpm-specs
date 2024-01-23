%global commit d7c81071f8b121ef83da32ae3fa16155d1a2ced9
%global commitdate 20231031
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           labwc-menu-generator
Version:        0~git%{commitdate}.%{shortcommit}
Release:        2%{?dist}
Summary:        Menu generator for labwc

# Tests are GPL-2.0-or-later
SourceLicense:  GPL-2.0-only AND GPL-2.0-or-later
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc-menu-generator
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  /usr/bin/prove
Supplements:    labwc


%description
%{summary}.


%prep
%autosetup -n %{name}-%{commit}


%build
%make_build


%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}


%check
make check


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20231031.d7c8107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 23 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20231031.d7c8107-1
- Initial package
