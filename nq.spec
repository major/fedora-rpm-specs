Name:           nq
Version:        0.5
Release:        7%{?dist}
Summary:        Unix command line queue utility

License:        CC0-1.0
URL:            https://github.com/leahneukirchen/nq
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl(Test::Harness)

Recommends:     (tmux or screen)

%description
The nq utility provides a very lightweight queuing system without requiring 
setup, maintenance, supervision or any long-running processes.

%prep
%autosetup

%build
%make_build CFLAGS='%{build_cflags}'

%check
%make_build check

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md NEWS.md
%{_bindir}/%{name}
%{_bindir}/fq
%{_bindir}/tq
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/fq.1*
%{_mandir}/man1/tq.1*

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Gustavo Costa <xfgusta@gmail.com> - 0.5-4
- Use SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 26 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.5-1
- Remove patch
- Update to 0.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 0.4-1
- Initial package
