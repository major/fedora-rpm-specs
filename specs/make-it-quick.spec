Name:           make-it-quick
Version:        0.3.2
Release:        9%{?dist}
Summary:        A make-only build system for C/C++ programs
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/tao-3D/%{name}
Source:         https://github.com/tao-3D/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  make >= 3.82
BuildRequires:  gcc >= 4.8
BuildRequires:  gcc-c++ >= 4.8
Requires:       sed
Requires:       make >= 3.82
BuildArch:      noarch

%description
A simple make-only build system with basic auto-configuration that
can be used to rapidly build C and C++ programs.

%package devel
Summary:        Development files for make-it-quick
%description devel
Development files for make-it-quick

%prep
%autosetup

%build
%configure
%make_build COLORIZE= TARGET=release DESTDIR=%{buildroot}

%check
%make_build COLORIZE= TARGET=release check DESTDIR=%{buildroot}

%install
%make_install COLORIZE= TARGET=release PREFIX.license=/usr/share/licenses/ DESTDIR=%{buildroot}

%files
%doc README.md
%doc AUTHORS
%doc NEWS
%license COPYING

%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.mk

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/config
%{_datadir}/%{name}/config/*.c

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.2-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 1 2022 Christophe de Dinechin <dinechin@redhat.com> - 0.3.2-2
- Fix license install path to *not* use LICENSEDIR, not available at that step

* Mon Aug 1 2022 Christophe de Dinechin <dinechin@redhat.com> - 0.3.2-1
- Fix license install path to use LICENSEDIR
- Update to 0.3.2 to get fix for config.system-setup.mk

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Christophe de Dinechin <dinechin@redhat.com> - 0.3.1-2
- Rebuild including a missing commit
- Remove stray -I experiment

* Fri Nov 26 2021 Christophe de Dinechin <dinechin@redhat.com> - 0.3.1-1
- New upstream minor release
- Change in URL format for GitHub
- Adjustments of the spec file to pass DESTDIR explicitly
- Other minor adjustments due to variable changes in make-it-quick

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 9 2021 Christophe de Dinechin <dinechin@redhat.com> - 0.2.7-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 6 2020 Christophe de Dinechin <dinechin@redhat.com> - 0.2.6-1
- Minor fixes and typos

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Christophe de Dinechin <dinechin@redhat.com> - 0.2.5-1
- New upstream release
* Tue Mar 19 2019 Christophe de Dinechin <dinechin@redhat.com> - 0.2.4-1
- Address review comments (see comment #11 of BZ#1689277)
- Integrate fixes found while building SPICE
* Fri Mar 15 2019 Christophe de Dinechin <dinechin@redhat.com> - 0.2.3-1
- Address review comments (see comment #7 of BZ#1689277)
* Thu Mar 14 2019 Christophe de Dinechin <dinechin@redhat.com> - 0.2.2-1
- Change the way the config.system-setup.mk file is generated
- Address issues reported by rpmlint
* Tue Mar 12 2019 Christophe de Dinechin <dinechin@redhat.com> - 0.2.1-1
- Add support for man pages and improve handling ofr subdirectories
* Thu Mar  7 2019 Christophe de Dinechin <dinechin@redhat.com> - 0.2
- Finish packaging work
* Thu Sep 20 2018 Christophe de Dinechin <dinechin@redhat.com> - 0.1
- Initial version of the package
