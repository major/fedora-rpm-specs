Name: unclutter-xfixes
Version: 1.6
Release: 7%{?dist}
Summary: Hides the cursor on inactivity (rewrite of unclutter)
License: MIT
URL: https://github.com/Airblader/unclutter-xfixes
Provides: unclutter = %{version}-%{release}
Source0: https://github.com/Airblader/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: asciidoc
BuildRequires: gcc
BuildRequires: git
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libev-devel
BuildRequires: make

%description
This is a rewrite of the popular tool unclutter, but using the
x11-xfixes extension. This means that this rewrite doesn't use fake windows or
pointer grabbing and hence causes less problems with window managers and/or
applications.

%prep
%autosetup -S git_am

%build
make %{?_smp_mflags} CFLAGS="%{optflags} %{build_ldflags}"

%install
%make_install
rm -r %{buildroot}%{_prefix}/share/licenses

%files
%license LICENSE
%{_bindir}/unclutter
%{_mandir}/man1/unclutter.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Robbie Harwood <rharwood@redhat.com> - 1.6-1
- Initial import (1.6)
