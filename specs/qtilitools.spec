Name:		qtilitools
Version:	0.1.2
Release:	2%{?dist}
License:	BSD-3-Clause
URL:		https://github.com/qtilities/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Scripts/commands used with qtilities apps
BuildArch:      noarch

# Fix to no longer need gcc-c++ as this project doesn't compile
# anything
Patch0:         language-fix.patch

BuildRequires:  cmake

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/qtls-translate
%{_datadir}/cmake/qtilitools

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 30 2024 Steve Cossette <farchord@gmail.com> - 0.1.2-1
- 0.1.2
