# fonts folder managed in xorg-x11-fonts but we don't want to enforce everything
%global _x11fontdir %{_datadir}/X11/fonts

%global aurgiturl    https://git.archlinux.org/svntogit/community.git

Name:           cmatrix
Version:        2.0
Release:        11%{?dist}
Summary:        A scrolling 'Matrix'-like screen

License:        GPL-2.0-or-later
URL:            https://github.com/abishekvashok/%{name}
Source0:        https://github.com/abishekvashok/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-tty
Patch0:         cmatrix-x11-font-path.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  help2man
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  console-setup
BuildRequires:  xorg-x11-fonts-misc


%description
Let's see the cool scrolling lines from the famous movie 'The Matrix'.


%package x11-fonts
Summary:            The font of 'Matrix' for X11

Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%if 0%{?fedora}
Suggests:           xorg-x11-fonts
%endif

%description x11-fonts
The font seen in the famous movie 'The Matrix' to be used in X11.


%prep
%autosetup
cp -p %{SOURCE1} .
# install fonts properly
sed -i -r 's: (%{_prefix}): \$(DESTDIR)\1:' Makefile.am


%build
autoreconf -ivf
%configure
%make_build
help2man -N -o %{name}.1 ./%{name}


%install
install -dm0755 %{buildroot}%{_exec_prefix}/lib/kbd/consolefonts
%make_install
install -Dpm0644 mtx.pcf %{buildroot}%{_x11fontdir}/misc/mtx.pcf
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%post x11-fonts
mkfontdir %{_x11fontdir}/misc

%postun x11-fonts
if [ "$1" = "0" -a -d %{_x11fontdir}/misc ]; then
  mkfontdir %{_x11fontdir}/misc
fi


%files
%license COPYING
%doc AUTHORS ChangeLog CODE_OF_CONDUCT.md CONTRIBUTING.md ISSUE_TEMPLATE.md NEWS README README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-tty
%{_exec_prefix}/lib/kbd/consolefonts/matrix.*
%{_mandir}/man1/%{name}.1*

%files x11-fonts
# we don't want to depend on other x11 fonts
%dir %{_x11fontdir}
%dir %{_x11fontdir}/misc
%{_x11fontdir}/misc/mtx.pcf
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 28 2023 Didier Fabert <didier.fabert@gmail.com> - 2.0-7
- migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Nov 25 2020 Didier Fabert <didier.fabert@gmail.com> - 2.0-1
- Update from new upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jun 17 2017 Raphael Groner <projects.rg@smart.ms> - 1.2a-1
- initial
