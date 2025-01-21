Name:           src
Version:        1.38
Release:        3%{?dist}
Summary:        Simple Revision Control

License:        BSD-2-Clause
URL:            https://gitlab.com/esr/src
Source0:        https://gitlab.com/esr/src/-/archive/%{version}/%{name}-%{version}.tar.bz2
    
BuildRequires:  rubygem-asciidoctor
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  rcs

Requires:       rcs
Requires:       python3
Recommends:     git-core

BuildArch:      noarch

%description
Simple Revision Control is RCS reloaded with a modern UI, designed to
manage single-file solo projects kept more than one to a directory.
Has a modern, svn/hg/git-like UI

%prep
%autosetup
%py3_shebang_fix src

%build
%make_build all FAQ.html

%install
%make_install prefix=%{_prefix}

%files
%license COPYING
%doc FAQ.html
%{_bindir}/src
%{_mandir}/man1/src.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 Bob Hepple <bob.hepple@gmail.com> - 1.38-1
- new version

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 13 2023 Bob Hepple <bob.hepple@gmail.com> - 1.32-1
- new version
- SPDX license

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Bob Hepple <bob.hepple@gmail.com> - 1.29-1
- new version
- remove Patch0:src-1.28-backport-1bbebb4a.patch 

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Bob Hepple <bob.hepple@gmail.com> - 1.28-2
- rebuilt

* Thu Apr 22 2021 Bob Hepple <bob.hepple@gmail.com> - 1.28-1
- rebuilt

