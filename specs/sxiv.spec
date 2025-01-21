Name:           sxiv
Version:        26
Release:        13%{?dist}
Summary:        Simple (or small or suckless) X Image Viewer
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/muennich/%{name}/
Source0:        https://github.com/muennich/%{name}/archive/v%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  imlib2-devel
BuildRequires:  libexif-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xorg-x11-proto-devel

%description
sxiv is an alternative to feh and qiv. Its only dependency besides xlib
is imlib2. The primary goal for writing sxiv is to create an image viewer,
which only has the most basic features required for fast image viewing (the
ones I want). It works nicely with tiling window managers and its code base
should be kept small and clean to make it easy for you to dig into it and
customize it for your needs.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}
cd icon && make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
cd icon && make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/sxiv
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 26-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 26-8
- Rebuild fo new imlib2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Petr Šabata <contyk@redhat.com> - 26-1
- v26 bump

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Petr Šabata <contyk@redhat.com> - 25-1
- v25 bump

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 24-3
- Rebuild (giflib)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 05 2017 Petr Šabata <contyk@redhat.com> - 24-1
- v24 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Petr Šabata <contyk@redhat.com> - 1.3.2-1
- 1.3.2 bump

* Mon Aug 03 2015 Petr Šabata <contyk@redhat.com> - 1.3.1-4
- Don't own the applications directory (#1249206)

* Fri Jun 26 2015 Petr Šabata <contyk@redhat.com> - 1.3.1-3
- Correct the dep list
- Modernize spec

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Petr Šabata <contyk@redhat.com> - 1.3.1-1
- 1.3.1 bugfix bump

* Wed Oct 29 2014 Petr Šabata <contyk@redhat.com> - 1.3-1
- 1.3 bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Petr Šabata <contyk@redhat.com> - 1.2-1
- 1.2 bump

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 08 2013 Petr Šabata <contyk@redhat.com> - 1.1.1-2
- Don't use versioned docdir paths in the manpage (#1027734)

* Mon Oct 14 2013 Petr Šabata <contyk@redhat.com> - 1.1.1-1
- 1.1.1 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 08 2013 Petr Šabata <contyk@redhat.com> - 1.1-1
- 1.1 bump

* Wed Jan 30 2013 Petr Šabata <contyk@redhat.com> - 1.0-4
- Enhance the desktop file -- allow sxiv to open more files at once and
  list the supported MIME types (#905678)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Petr Sabata <contyk@redhat.com> - 1.0-1
- 1.0 bump

* Wed Aug 17 2011 Petr Sabata <contyk@redhat.com> - 0.9-1
- 0.9 bump

* Mon Jul 11 2011 Petr Sabata <contyk@redhat.com> - 0.8.2-2
- Respect RPM_OPT_FLAGS again (#720162)

* Thu Jul 07 2011 Petr Sabata <contyk@redhat.com> - 0.8.2-1
- 0.8.2 bump

* Wed May 11 2011 Petr Sabata <psabata@redhat.com> - 0.8.1-2
- Correcting license to GPLv2+
- Using Github URL as Source
- Respecting optflags
- Adding a crude desktop file

* Tue May 10 2011 Petr Sabata <psabata@redhat.com> - 0.8.1-1
- Initial import
