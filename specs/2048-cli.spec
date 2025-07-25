Name:           2048-cli
Version:        0.9.1
Release:        24%{?gitrel}%{?dist}
Summary:        The game 2048 for your Linux terminal

License:        MIT
URL:            https://github.com/Tiehuis/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0000:      %{name}-%{version}-include-string-h.patch
Patch0001:      %{name}-%{version}-fix-Wformat.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
A cli version of the game 2048 for your Linux terminal.


%package nocurses
Summary:        The game 2048 for your Linux terminal (non-ncurses)

%description nocurses
A non-ncurses cli version of the game 2048 for your Linux terminal.


%package sdl
Summary:        The game 2048 for your Linux terminal (SDL)

BuildRequires:  SDL2_ttf-devel
BuildRequires:  liberation-mono-fonts

Requires:       liberation-mono-fonts

%description sdl
A SDL version of the game 2048 for your Linux terminal.


%prep
%autosetup -p 1


%build
export TTF_FONT_PATH="%{_datadir}/fonts/liberation/LiberationMono-Regular.ttf"
%make_build terminal
mv 2048 2048nc
%make_build sdl
mv 2048 2048sdl
%make_build curses


%install
# There is no install-target in Makefile.
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1,%{_pkgdocdir}}
install -pm 0755 2048 2048nc 2048sdl %{buildroot}%{_bindir}
install -pm 0644 man/2048.1 %{buildroot}%{_mandir}/man1/2048.1
install -pm 0644 man/2048.1 %{buildroot}%{_mandir}/man1/2048nc.1
install -pm 0644 man/2048.1 %{buildroot}%{_mandir}/man1/2048sdl.1


%files
%license LICENSE
%doc README.md
%{_bindir}/2048
%{_mandir}/man1/2048.1*

%files nocurses
%license %{_datadir}/licenses/%{name}*
%doc %{_pkgdocdir}
%{_bindir}/2048nc
%{_mandir}/man1/2048nc.1*

%files sdl
%license %{_datadir}/licenses/%{name}*
%doc %{_pkgdocdir}
%{_bindir}/2048sdl
%{_mandir}/man1/2048sdl.1*


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Björn Esser <besser82@fedoraproject.org> - 0.9.1-23
- Add patch to properly #include<string.h> where needed
- Add patch to fix -Wformat
- Drop old cruft from spec file

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 0.9.1-1
- new upstream release 0.9.1

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 0.9.1-0.2.git20151229.4520781
- properly apply CFLAGS, without clobbering the Makefile-preset

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 0.9.1-0.1.git20151229.4520781
- update to new snapshot git20151229.4520781
- handle %%license and %%doc properly

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7.git20150225.dc9adea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Björn Esser <bjoern.esser@gmail.com> - 0.9-6.git20150225.dc9adea
- update to new snapshot git20150225.dc9adea

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5.git20141214.723738c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 14 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-4.git20141214.723738c
- update to new snapshot git20141214.723738c, obsoletes Patch0

* Sat Dec 13 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-3
- updated Patch0

* Sat Dec 13 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-2
- added Patch0 to fix malformated manpages

* Fri Dec 05 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-1
- new upstream release v0.9
- obsoleted Patch0

* Fri Dec 05 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8-3.git20141205.a9505d9
- updated to new snapshot git20141205.a9505d9
- added Patch0 to have manpages

* Thu Dec 04 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8-2
- dropped Patch0 (#1170231)
- some minor readability clean-up

* Wed Dec 03 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8-1
- initial rpm-release (#1170231)
