# https://gcc.gnu.org/gcc-10/porting_to.html#common
%define _legacy_common_support 1

Name:		twlog
Version:	3.4
Release:	13%{?dist}
Summary:	Records basic ham radio log information
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later

URL:		http://wa0eir.bcts.info/twlog.html

Source0:	http://wa0eir.bcts.info/src/%{name}-%{version}.src.tar.gz
# Wrapper script to install user defaults
Source1:	%{name}.sh.in

# .desktop patch
Patch0:		%{name}-%{version}.desktop.patch
Patch1:		twlog-configure-c99.patch

BuildRequires:	desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:	xbae-devel

%description
Twlog records basic Ham log information. It was written
for day to day logging, not contesting. There are no dupe
checks or contest related features.


%prep
%autosetup -p1

# Set perms on source file
chmod 644 ./src/adif.c

%build
%configure
%make_build


%install
%make_install

# Install provided icon
mkdir -p %{buildroot}/%{_datadir}/pixmaps/
install -p -D -m 0644 ./src/icons/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications/	\
	%{buildroot}/%{_datadir}/applications/%{name}.desktop

# Move original binary to libexecdir
mkdir -p %{buildroot}/%{_libexecdir}/
mv %{buildroot}/%{_bindir}/%{name} %{buildroot}/%{_libexecdir}/%{name}-bin

# Install wrapper script installs needed files in users home directory.
install -p -D -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}

# Twlog default settings
mkdir -p %{buildroot}/%{_datadir}/X11/app-defaults/
install -p -D -m 0644 ./src/Twlog %{buildroot}/%{_datadir}/X11/app-defaults/Twlog


%files
%doc AUTHORS NEWS README TODO ChangeLog THANKS
%license COPYING
%{_bindir}/%{name}
%{_libexecdir}/%{name}-bin
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/X11/app-defaults/Twlog
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Peter Fordham <peter.fordham@gmail.com> - 3.4-7
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Richard Shaw <hobbes1069@gmail.com> - 3.4-1
- Update to 3.4.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Kalev Lember <klember@redhat.com> - 2.7-12
- Rebuilt for libXm soname bump

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraprojecct.org> - 2.7-3
- Rebuild for F14/Rawhide

* Mon Jul 19 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraprojecct.org> - 2.7-2
- Apply configure patch to search proper library directories on x86_64

* Sat Jul 17 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraprojecct.org> - 2.7-1
- New upstream release
- Edit spec per review
- Added desktop-file-install to verify .desktop file

* Thu Jul 15 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraprojecct.org> - 2.6-3
- Tweek install wrapper
- Twlog already checks for log directory. Creates it if not exists.
- Commented routine from wrapper.

* Mon Jul 12 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraprojecct.org> - 2.6-2
- Tweek install wrapper

* Mon Jul 12 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraprojecct.org> - 2.6-1
- Initial spec build
