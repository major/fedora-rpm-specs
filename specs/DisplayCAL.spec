# Use define instead of global to ensure it's evaluated when used
%define lc_name %(echo "%{name}" | tr '[:upper:]' '[:lower:]')

Name:		DisplayCAL
Version:	3.9.14
Release:	3%{?dist}
Summary:	Display calibration and profiling tool focusing on accuracy and versatility
License:	GPL-3.0-or-later
URL:		https://github.com/eoyilmaz/displaycal-py3
Source0:	%{pypi_source}
Patch0:		displaycal-3.9.3-udev-dir.patch
Patch1:		displaycal-skip-update-check.patch
Patch2:		displaycal-3.9.14-fix-autostart-location.patch
Patch3:		displaycal-3.9.12-delete-pyvercheck.patch

BuildRequires:	gcc
BuildRequires:	git-core
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pyproject-rpm-macros
BuildRequires:	xdg-user-dirs

Requires:	argyllcms
Requires:	hicolor-icon-theme
# workaround for crash with pyglet as sound backend
Requires:	SDL2_mixer

Provides:	%{lc_name} = %{version}-%{release}
Provides:	dispcalGUI = %{version}-%{release}

%description
This utility calibrates and characterizes display devices using one
of many supported measurement instruments, with support for
multi-display setups and a variety of available options for advanced
users, such as verification and reporting functionality to evaluate
ICC profiles and display devices, creating video 3D LUTs, as well as
optional CIECAM02 gamut mapping to take into account varying viewing
conditions.

%prep
%autosetup -S git -n %{lc_name}-%{version}

# Delete git data to prevent broken versioning
rm -rf .git

# Delete existing egg
rm -rf DisplayCAL.egg-info
# Delete PKG-INFO that causes inadvertent Python version restrictions
rm PKG-INFO

# hack to force creating dist/net.displaycal... (missed due pyproject)
sed -i -e 's|create_appdata = |create_appdata = True or |' setup.py

# drop prebuilt modules
find . -name '*.so' -print -delete

# fix paths
%ifarch %{arm32} %{ix86}
ln -s ./lib64 DisplayCAL/lib32
sed -i -e 's/DisplayCAL\.lib64/DisplayCAL\.lib32/g' DisplayCAL/RealDisplaySizeMM.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
export CFLAGS="%{build_cflags} -Wno-incompatible-pointer-types"
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
mv %{buildroot}%{_datadir}/DisplayCAL/z-displaycal-apply-profiles.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/

%files
%docdir %{_docdir}/%{name}-%{version}/
%doc %{_docdir}/%{name}-%{version}/*
%license LICENSE.txt
%{_sysconfdir}/xdg/autostart/z-displaycal-apply-profiles.desktop
%{_bindir}/%{lc_name}*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{lc_name}*.png
%{_datadir}/applications/%{lc_name}*.desktop
%{_metainfodir}/net.displaycal.%{name}.appdata.xml
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}.dist-info/
%{_mandir}/man1/%{lc_name}*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.9.14-2
- Rebuild for fixed package metadata

* Thu Oct 31 2024 Josh Stone <jistone@redhat.com> - 3.9.14-1
- Update to DisplayCAL 3.9.14

* Mon Aug 19 2024 Neal Gompa <ngompa@fedoraproject.org> - 3.9.12-5
- Add patch to support Python 3.12 and Python 3.13

* Sun Aug 18 2024 Neal Gompa <ngompa@fedoraproject.org> - 3.9.12-4
- Add patch to remove overly strict Python runtime check

* Sat Jul 27 2024 Neal Gompa <ngompa@fedoraproject.org> - 3.9.12-3
- Drop unneeded egg data

* Sat Jul 13 2024 Neal Gompa <ngompa@fedoraproject.org> - 3.9.12-2
- Adapt for Fedora

* Thu Apr 04 2024 David GEIGER <daviddavid@mageia.org> 3.9.12-1.mga10
+ Revision: 2054356
- new version: 3.9.12

* Tue Jan 16 2024 papoteur <papoteur@mageia.org> 3.9.11-3.mga10
+ Revision: 2031653
- workaround for crash with pyglet as sound backend, pulling sdl2_mixer which has precedence (mga#32697)

* Sun Dec 31 2023 David GEIGER <daviddavid@mageia.org> 3.9.11-2.mga10
+ Revision: 2024873
- add py3.12 support

* Tue Dec 19 2023 David GEIGER <daviddavid@mageia.org> 3.9.11-1.mga10
+ Revision: 2019816
- new version: 3.9.11

* Tue Dec 19 2023 papoteur <papoteur@mageia.org> 3.9.10-3.mga10
+ Revision: 2019485
- Mass Rebuild - Python 3.12
+ David GEIGER <daviddavid@mageia.org>
- rebuild for py3.12

* Thu Dec 01 2022 David GEIGER <daviddavid@mageia.org> 3.9.10-1.mga9
+ Revision: 1913674
- new version: 3.9.10
- rediff skip-update-check patch

* Fri Sep 30 2022 papoteur <papoteur@mageia.org> 3.9.8-1.mga9
+ Revision: 1893487
- fix installation location of autostart file
- new version: 3.9.8

* Sun May 15 2022 papoteur <papoteur@mageia.org> 3.9.3-1.mga9
+ Revision: 1858237
- new 3.9.3
- restore displaycal now ported to Python 3
+ Sysadmin Bot <umeabot@mageia.org>
- Mageia 8 Mass Rebuild

* Mon Aug 19 2019 David GEIGER <daviddavid@mageia.org> 3.8.5.0-1.mga8
+ Revision: 1429917
- new version: 3.8.5.0

* Mon Jul 08 2019 David GEIGER <daviddavid@mageia.org> 3.8.3.0-1.mga8
+ Revision: 1419467
- new version: 3.8.3.0

* Fri Apr 05 2019 David GEIGER <daviddavid@mageia.org> 3.7.2.0-1.mga7
+ Revision: 1385912
- new version: 3.7.2.0

* Mon Jan 28 2019 David GEIGER <daviddavid@mageia.org> 3.7.1.4-1.mga7
+ Revision: 1361558
- new version: 3.7.1.4

* Tue Dec 25 2018 David GEIGER <daviddavid@mageia.org> 3.7.1.3-1.mga7
+ Revision: 1344960
- new version: 3.7.1.3

* Fri Nov 30 2018 David GEIGER <daviddavid@mageia.org> 3.7.1.2-1.mga7
+ Revision: 1336811
- new version: 3.7.1.2

* Sun Nov 18 2018 David GEIGER <daviddavid@mageia.org> 3.7.1.1-1.mga7
+ Revision: 1330755
- new version: 3.7.1.1

* Sun Oct 21 2018 David GEIGER <daviddavid@mageia.org> 3.7.0.0-1.mga7
+ Revision: 1323222
- new version: 3.7.0.0
- switch to 55-Argyll.rules to support new udev (mga#23733)

* Fri Sep 21 2018 David GEIGER <daviddavid@mageia.org> 3.6.2.0-1.mga7
+ Revision: 1295897
- new version: 3.6.2.0

* Sat Aug 18 2018 David GEIGER <daviddavid@mageia.org> 3.6.1.1-1.mga7
+ Revision: 1252514
- new version: 3.6.1.1

* Mon Apr 30 2018 David GEIGER <daviddavid@mageia.org> 3.5.3.0-1.mga7
+ Revision: 1223902
- new version: 3.5.3.0

* Sat Apr 07 2018 David GEIGER <daviddavid@mageia.org> 3.5.2.0-1.mga7
+ Revision: 1215879
- new version: 3.5.2.0

* Fri Mar 23 2018 David GEIGER <daviddavid@mageia.org> 3.5.1.0-1.mga7
+ Revision: 1211431
- new version: 3.5.1.0
- rename and rediff udev-dir patch

* Mon Feb 26 2018 David GEIGER <daviddavid@mageia.org> 3.5.0.0-1.mga7
+ Revision: 1205245
- new version: 3.5.0.0

* Thu Jan 04 2018 David GEIGER <daviddavid@mageia.org> 3.4.0.0-1.mga7
+ Revision: 1190081
- new version: 3.4.0.0

* Thu Nov 09 2017 David GEIGER <daviddavid@mageia.org> 3.3.5.0-1.mga7
+ Revision: 1176692
- new version: 3.3.5.0

* Sat Sep 23 2017 David GEIGER <daviddavid@mageia.org> 3.3.4.1-1.mga7
+ Revision: 1157787
- new version: 3.3.4.1

* Sat Sep 02 2017 David GEIGER <daviddavid@mageia.org> 3.3.3.0-1.mga7
+ Revision: 1150723
- new version: 3.3.3.0

* Sun Jul 02 2017 David GEIGER <daviddavid@mageia.org> 3.3.2.0-1.mga6
+ Revision: 1108913
- new version: 3.3.2.0

* Sun Jan 15 2017 David GEIGER <daviddavid@mageia.org> 3.2.3.0-1.mga6
+ Revision: 1081884
- new version: 3.2.3.0

* Sun Dec 11 2016 David GEIGER <daviddavid@mageia.org> 3.2.1.0-1.mga6
+ Revision: 1074203
- new version: 3.2.1.0

* Sun Oct 30 2016 David GEIGER <daviddavid@mageia.org> 3.1.7.3-1.mga6
+ Revision: 1064156
- new version: 3.1.7.3

* Fri Oct 14 2016 David GEIGER <daviddavid@mageia.org> 3.1.7.0-1.mga6
+ Revision: 1060737
- new version: 3.1.7.0

* Sun Aug 28 2016 David GEIGER <daviddavid@mageia.org> 3.1.6.0-1.mga6
+ Revision: 1049349
- new version: 3.1.6.0

* Sat Aug 20 2016 David GEIGER <daviddavid@mageia.org> 3.1.5.0-1.mga6
+ Revision: 1047143
- new version: 3.1.5.0

* Sun Jul 24 2016 David GEIGER <daviddavid@mageia.org> 3.1.4.0-1.mga6
+ Revision: 1043512
- new version: 3.1.4.0

* Tue May 10 2016 David GEIGER <daviddavid@mageia.org> 3.1.3.1-1.mga6
+ Revision: 1012317
- new version: 3.1.3.1

* Mon Feb 22 2016 David GEIGER <daviddavid@mageia.org> 3.1.0.0-1.mga6
+ Revision: 976005
- new version: 3.1.0.0 (fixes mga#17803)
- new upstream URL and Source URL
- rename and rediff udev-dir patch
- use new python macros
- requires python-numpy
- obsoletes/provides old upstream name on dispcalGUI
- update files list
- move to new upstream name on displaycal

* Fri Feb 05 2016 Sysadmin Bot <umeabot@mageia.org> 1.2.7.0-9.mga6
+ Revision: 938821
- Mageia 6 Mass Rebuild

* Wed Oct 15 2014 Sysadmin Bot <umeabot@mageia.org> 1.2.7.0-8.mga5
+ Revision: 744682
- Second Mageia 5 Mass Rebuild

* Sat Sep 27 2014 Thierry Vignaud <tv@mageia.org> 1.2.7.0-7.mga5
+ Revision: 726130
- rebuild for missing pythoneggs deps

* Tue Sep 16 2014 Sysadmin Bot <umeabot@mageia.org> 1.2.7.0-6.mga5
+ Revision: 678756
- Mageia 5 Mass Rebuild
+ Olav Vitters <ovitters@mageia.org>
- add gobject-introspection BR for typelib auto BR

* Sat May 31 2014 Pascal Terjan <pterjan@mageia.org> 1.2.7.0-5.mga5
+ Revision: 628160
- Rebuild for new Python

* Sat Nov 02 2013 Funda Wang <fwang@mageia.org> 1.2.7.0-4.mga4
+ Revision: 548862
- add requires on python-gi

* Tue Oct 22 2013 Sysadmin Bot <umeabot@mageia.org> 1.2.7.0-3.mga4
+ Revision: 542551
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 Pascal Terjan <pterjan@mageia.org> 1.2.7.0-2.mga4
+ Revision: 497727
- Rebuild to add different pythonegg provides for python 2 and 3

* Wed Jul 31 2013 Funda Wang <fwang@mageia.org> 1.2.7.0-1.mga4
+ Revision: 461407
- update file list
- new version 1.2.7.0

* Sun Feb 10 2013 Nicolas Lécureuil <neoclust@mageia.org> 0.8.9.3-1.mga3
+ Revision: 397779
- imported package dispcalGUI
