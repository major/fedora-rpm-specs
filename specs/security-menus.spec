Name:           security-menus
Version:        38
Release:        6%{?dist}
Summary:        Menu Structure for the Fedora Security Lab

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://pagure.io/security-lab
Source0:        https://releases.pagure.org/security-lab/%{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  desktop-file-utils

Requires:       redhat-menus
Requires:       xfce4-terminal

%description
This Package adds a Security Lab sub-menu to the xdg menu structure for 
GNOME and other desktop enviroments.

%{name} is listed among Fedora Security Lab packages.

%prep
%setup -n security-menu
rm -rf security-{dc3dd,scanmem}*.desktop

%build
# nothing to build

%install
make install DESTDIR=%{buildroot}
for file in %{buildroot}/%{_datadir}/applications/*.desktop; do 
    desktop-file-validate $file
done

%files
%doc AUTHORS COPYING README
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/*.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/applications/*.desktop

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 38-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 18 2023 Fabian Affolter <mail@fabian-affolter.ch> - 38-1
- Update meta information (closes rhbz#2169874)
- Update to new upstream release 38

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to new upstream release 1.3.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update to new upstream release 1.2.1

* Sat Aug 03 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-2
- Add 'xfce4-terminal' as requirements

* Wed Jul 31 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Update to new upstream release 1.2.0 (fixes #981826)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-1
- Update to new upstream release 1.1.3

* Sun Nov 04 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.2-1
- to new upstream release 1.1.2

* Wed Oct 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- to new upstream release 1.1.1

* Sun Oct 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Update menu entries
- Update spec file
- Switch to Terminal instead of gnome-terminal

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 17 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.5-1
- Update menu entries

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Joerg Simon <jsimon@fedoraproject.org> - 1.0.4-1
- Change menu entries

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Joerg Simon <jsimon@fedoraproject.org> - 1.0.3-1
- Change to downsize the spin

* Fri Aug 27 2010 Joerg Simon <jsimon@fedoraproject.org> - 1.0.2-1
- Add new entries

* Sat Mar 13 2010 Joerg Simon <jsimon@fedoraproject.org> - 1.0.1-1
- Add ncrack to the menu

* Fri Jan 15 2010 Hiemanshu Sharma <hiemanshu [AT] fedoraproject DOT org> - 1.0-7
- Change packge name to security-menus

* Wed Jan 13 2010 Hiemanshu Sharma <hiemanshu [AT] fedoraproject DOT org> - 1.0-6
- Fix .menu file, thanks to Joerg for the patch

* Tue Jan 12 2010 Hiemanshu Sharma <hiemanshu [AT] fedoraproject DOT org> - 1.0-5
- Rename X-Security-Lab to X-SecurityLab for better fdo compliance. Whitespces
  are usually just left out. i Add subcategories X-Anonymity, X-CodeAnalysis,
  X-Forensics,  X-IntrusionDetection, X-Password-Tools, X-Reconnaissance and 
  X-Wireless
- Use TryExec to determine installed apps, see
  http://standards.freedesktop.org/desktop-entry-spec/latest/ar01s05.html
- Menu tweaks
- Enhance Makefile
- Added AUTHORS
- Added ChangeLog (for upstream changes, not packaging).
- Added desktop-file-validate
- Fixed requires

* Sat Dec 19 2009 Hiemanshu Sharma <hiemanshu [AT] fedoraproject DOT org> - 1.0-4
- Change Categories to X-Security-Lab
- Change Source file name to include version number

* Sat Dec 19 2009 Hiemanshu Sharma <hiemanshu [AT] fedoraproject DOT org> - 1.0-3
- Rename files to start with security- to avoid conflict

* Sat Dec 19 2009 Hiemanshu Sharma <hiemanshu [AT] fedoraproject DOT org> - 1.0-2
- Fix problems with Makefile
- Fix License

* Fri Dec 18 2009 Hiemanshu Sharma <hiemanshu [AT] fedoraproject DOT org> - 1.0-1
- Initial package for Fedora
