%bcond_with pylirc
%bcond_without pulse

Summary: Simple Video for Linux radio card programs
Name:    fmtools
Version: 2.0.8
Release: 3%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://benpfaff.org/fmtools

Source0: http://benpfaff.org/fmtools/%{name}-%{version}.tar.gz
Source1: fmcontrol.tar.gz
Source2: http://benpfaff.org/fmtools/tkradio
Source3: http://benpfaff.org/fmtools/tkradio-mute
Source4: fmtools.desktop
Source5: radio.png
Source8: radio.gif
Source6: tkradio.py
Source7: fmlircrc
Patch0: fmcontrol-py3.patch
BuildRequires: autoconf automake
BuildRequires: gcc
BuildRequires: python3-devel

%description
This is a pair of hopefully useful control programs for Video for Linux
(v4l2) radio card drivers.  The focus is on control, so you may find these
programs a bit unfriendly.  Users are encouraged to investigate the source
and create wrappers or new programs based on this design.

fm      - a simple tuner
fmscan  - a simple band scanner

%package tkradio
Summary:       Python/Tk wrapper for fmtools
BuildRequires: desktop-file-utils
BuildRequires: make
Requires:      %{name} = %{version}
Requires:      python3
%{?with_pylirc:Requires: python3-lirc}
Requires:      vorbis-tools, python3-tkinter, alsa-utils
%if %{with pulse}
Requires:      pulseaudio-utils
BuildArch:     noarch
%endif

%description tkradio
This package provides a GUI for %{name}, with lirc support.
The stations are read from the same files used by fmcontrol,
and the lirc configuration file is in $HOME/.fmlircrc

The script fmcontrol.py saves one from remembering frequencies
and volumes when using the "fm" program from %{name}.
All that it does is to tune into a station specified by name, at the
frequency and volume specified in $HOME/.fmrc or $HOME/.radiostations,
or the volume given on the command line.

%prep
%setup -q -a1
%patch -P0 -p1 -b .py3

%build
autoreconf -vif
%configure
%make_build

%install
%make_install
install -pm 0755 %{SOURCE2} %{buildroot}%{_bindir}/tkradio.tcl
install -pm 0755 %{SOURCE3} %{buildroot}%{_bindir}/tkradio-mute.tcl
install -pm 0755 %{SOURCE6} %{buildroot}%{_bindir}/tkradio.py
install -pm 0755 fmcontrol/fmcontrol %{buildroot}%{_bindir}/fmcontrol.py
install -pm 0644 fmcontrol/README README.fmcontrol

# menu entry
desktop-file-install                                    \
        --vendor ""                                     \
        --dir %{buildroot}%{_datadir}/applications      \
        %{SOURCE4}

install -Dpm 0644 %{SOURCE5} %{buildroot}%{_datadir}/pixmaps/radio.png
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_datadir}/%{name}/fmlircrc
install -Dpm 0644 %{SOURCE8} %{buildroot}%{_datadir}/%{name}/radio.gif

%files 
%doc README
%license COPYING
%{_bindir}/fm
%{_bindir}/fmscan
%{_mandir}/man1/fm*.gz

%files tkradio
%doc README.fmcontrol fmcontrol/dot.*
%{_bindir}/tkradio*
%{_bindir}/fmcontrol.py
%{_datadir}/applications/fmtools.desktop
%{_datadir}/pixmaps/radio.png
%{_datadir}/%{name}/fmlircrc
%{_datadir}/%{name}/radio.gif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.8-2
- convert license to SPDX

* Thu Jul 18 2024 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.8-1
- Update to 2.0.8

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.0.7-18
- Switch to python3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.7-16
- rebuilt to fix FTBFS on F29+ fixes rhbz #1512890 and rhbz #1674890

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.7-13
- added gcc as BR

* Sun Feb 18 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.7-12
- Fix FTBFS + spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.7-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.7-2
- Fix FTBFS
- Cleanup spec

* Mon Sep 30 2013 Paulo Roma <roma@lcg.ufrj.br> 2.0.7-1
- Updated to 2.0.7

* Sun Sep 15 2013 Paulo Roma <roma@lcg.ufrj.br> 2.0.6-1
- Updated to latest git.

* Sun Sep 08 2013 Paulo Roma <roma@lcg.ufrj.br> 2.0.2-1
- Updated to latest git.

* Wed Sep 04 2013 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-14
- Applied patch volume for working in kernels >= 3.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 27 2011 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-9
- Using signal module.

* Sun Mar 13 2011 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-8
- Using Master for controling the volume.

* Thu Mar 10 2011 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-7
- Restoring the saved state (persistency).

* Sat Feb 26 2011 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-6
- Ported to python3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-4
- Condionally build with python-lirc.

* Mon Dec 06 2010 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-3
- Using mtTkinter so pylirc works, since it handles
  tk objects outside the main thread.
- Fixed desktop entry.

* Sun Jan 24 2010 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-2
- Fixed exception handling.
- Using pacat and parec for recording with pulseaudio.
- Updated URL.

* Sat Jan 09 2010 Paulo Roma <roma@lcg.ufrj.br> 2.0.1-1
- Updated to 2.0.1
- Removed fmtools.patch
- Added man pages.

* Thu Jan 07 2010 Paulo Roma <roma@lcg.ufrj.br> 2.0-10
- Fixed grep expression in tkradio.py

* Sat Jan 02 2010 Paulo Roma <roma@lcg.ufrj.br> 2.0-9
- Added libnotify support.
- Addded compression using oggenc.
- Added window icon.

* Wed Dec 30 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0-8
- Added recording support.

* Sun Dec 27 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0-7
- Replaced fmcontrol for fmcontrol.py
- Moved fmcontrol to tkradio package.
- Added lirc support.

* Wed Dec 23 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0-5
- Replaced BR tk for tkinter.

* Wed Dec 23 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0-4
- Include tkradio.py
- Fixed fmtools.desktop

* Sun Dec 20 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0-3
- Packaging tkradio separately.

* Sun Dec 20 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0-2
- Patched to make it work.
- Added desktop entry.

* Sun Dec 13 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0-1
- Initial v4l2 support provided by version 2.0
- Included tkradio and fmcontrol.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 17 2008 kwizart < kwizart at gmail.com > - 1.0.2-4
- Rebuild for F-10

* Sat Feb 09 2008 kwizart < kwizart at gmail.com > - 1.0.2-3
- Rebuild for gcc43

* Fri Sep 21 2007 kwizart <kwizart at gmail.com > - 1.0.2-2
- Fix shebang
- Fix perm on source
- Fix mixed use of spaces and tabs
- Remove internal header to use it from kernel-headers

* Sun Aug 26 2007 kwizart <kwizart at gmail.com > - 1.0.2-1
- Update to 1.0.2

* Mon Sep 04 2006 TC Wan <tcwan@cs.usm.my>
- Built Version 1.0 for FC 5
