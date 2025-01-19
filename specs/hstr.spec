Name:           hstr
Version:        3.1
Release:        5%{?dist}
Summary:        Suggest box like shell history completion

License:        Apache-2.0
URL:            https://github.com/dvorka/hstr
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  make

%description
A command line utility that brings improved shell command completion
from the history. It aims to make completion easier and faster than Ctrl-r.


%prep
%autosetup
autoreconf -fiv

%build
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc Changelog README.md
%{_bindir}/hh
%{_bindir}/%{name}
%{_datadir}/bash-completion/
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Jonathan Wright <jonathan@almalinux.org> - 3.1-1
- Update to 3.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 16 2023 Jonathan Wright <jonathan@almalinux.org> - 3.0-1
- Update to 3.0
- update license to spdx

* Tue Jan 24 2023 Leigh Scott <leigh123linux@gmail.com> - 2.6-1
- Update to 2.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Leigh Scott <leigh123linux@gmail.com> - 2.5-1
- Update to 2.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Leigh Scott <leigh123linux@gmail.com> - 2.4-1
- Update to 2.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Leigh Scott <leigh123linux@gmail.com> - 2.3-1
- Update to 2.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Leigh Scott <leigh123linux@gmail.com> - 2.2-1
- Update to 2.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.22-8
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 1.22-1
- Update to 1.22
- Remove build requires on autoconf

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.21-4
- Rebuild for readline 7.x

* Sat Nov 12 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.21-3
- Remove requires on ncurses and readline

* Thu Oct 27 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.21-2
- Add build requires on autoconf

* Sat Oct 22 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.21-1
- Update to 1.21
- Change source URL to GitHub
- Add build requires on automake
- Use %%autosetup macro

* Fri Jan 22 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.19-1
- Initial RPM release
