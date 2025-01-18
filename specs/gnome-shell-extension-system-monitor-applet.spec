%global extuuid    system-monitor-next@paradoxxx.zero.gmail.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    gnome-shell-system-monitor-applet
%global giturl     https://github.com/mgalgs/%{gitname}

%{!?git_post_release_enabled: %global git_post_release_enabled 1}

%if 0%{?git_post_release_enabled}
  # Git commit is needed for post-release version.
  %global gitcommit 94916490f8ed1f47902af46cbde182013cd3f0b7
  %global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
  %global gitsnapinfo .20240904git%{gitshortcommit}
%endif

Name:           gnome-shell-extension-system-monitor-applet
Epoch:          1
Version:        38
Release:        34%{?gitsnapinfo}%{?dist}
Summary:        A Gnome shell system monitor extension

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://extensions.gnome.org/extension/3010/system-monitor-next/
Source0:        %{giturl}/archive/%{?gitcommit}%{!?gitcommit:v%{version}}/%{name}-%{version}%{?gitshortcommit:-%{gitshortcommit}}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  %{_bindir}/glib-compile-schemas
BuildRequires:  make

Requires:       gnome-shell-extension-common

# CentOS 7 build environment doesn't support Suggests tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       gnome-tweaks
%endif


%description
Display system information in gnome shell status bar, such as memory usage,
CPU usage, and network rate...


%prep
%autosetup -n %{gitname}-%{?gitcommit}%{!?gitcommit:%{version}} -p 1


%build
%make_build BUILD_FOR_RPM=1


%install
%make_install VERSION=%{version} DESTDIR=%{buildroot} BUILD_FOR_RPM=1

# Cleanup unused files.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Install schema.
%{__mkdir} -p %{buildroot}%{gschemadir}
%{__cp} -pr %{extuuid}/schemas/*gschema.xml %{buildroot}%{gschemadir}

# Install i18n.
%{_bindir}/find %{extuuid} -name '*.po' -print -delete
%{__cp} -pr %{extuuid}/locale %{buildroot}%{_datadir}

# Create manifest for i18n.
%find_lang %{name} --all-name


# CentOS 7 doesn't compile gschemas automatically, Fedora does.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%doc README.md
%license COPYING
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-34.20240904git9491649
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-33.20240904git9491649
- Updated to last upstream commits
- Drop unused compat.js
- Use Cogl.Color instead of Clutter.Color
- Add 47 to supported shell versions
- Drop debug log

* Tue Aug 20 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-32.20240820git81f07ce
- Updated to last upstream commits
- Focus fan graph on reported range
- Add option to rotate chart labels
- Adjust URL accordingly to the switch to the forked github sources repository

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-31.20240717git4bd03a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-30.20240717git4bd03a2
- Updated to last upstream commits
- Fix sensors labels determinism - RHBZ#2186601
  Thanks to Dominik Mierzejewski
- Change message shown when no fan/temperature sensor files are found - prefs.js
- Use template literals in common.js
- GPU: Un-hardcode /bin/bash location
- Fix common.js missing from build
- Update compiled Portuguese locales to resolve permadiff

* Thu May 02 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-29.20240502git4a1cfff
- Updated to last upstream commits
- Fix tooltip text being garbled/blurry

* Tue Mar 26 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-28.20240326git002f432
- Add compatibility with gnome-shell 46 - RHBZ#2268402

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-27.20231104git0f042e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-26.20231104git0f042e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 04 2023 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-25.20231104git0f042e8
- Upgrade from forked github repository for gnome-shell >= 45 - RHBZ#2240571
  https://github.com/mgalgs/gnome-shell-extension-system-monitor-applet
  More information in:
  https://github.com/paradoxxxzero/gnome-shell-system-monitor-applet/issues/795

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-24.20230420git21d7b4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-23.20230420git21d7b4e
- Migrated to SPDX license
- Add patch for gnome-shell < 3.34 (rhel 8) - RHBZ#2184351
- Add patch for compatibility with gnome-shell 44 - RHBZ#2188339

* Sun Mar 26 2023 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-22.20230326git21d7b4e
- Updated to last upstream commits
- Remove patch for gnome 43 - applied upstream
- Disable Python output buffering
- Add setting for tooltip delay
- Added the possibility to rearrange the graphs
- Remove "nvidia gpu only" message
- gpu_usage.sh: Replace cut and gawk with shell internals
- Wrap into register class
- Fix a small typo in extension.js
- Add space before 'R' in disk usage string
- Gnome-Shell 43 compatibility update
- Continue running when screen is locked and optionally show on lockscreen,
  using session modes

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-21.20220527gitb359d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-20.20220527gitb359d88
- Added support for gnome 43

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-19.20220527gitb359d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-18.20220527gitb359d88
- Added built for RHEL9
- Updated to last upstream commits
- Updated Brazilian Portuguese and Portuguese translations
- Updated README.md file

* Tue Mar 01 2022 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-17.20220301git2c6eb0a
- Updated to last upstream commits
- Added support for gnome 42
- Fixes SPEC file for rpmlint error rpm-buildroot-usage

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-16.20211103git11d43a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-15.20211103git11d43a8
- Updated to last upstream commits
- Updated and cleaned-up PO template files
- Updated some translations
- Added support for gnome 41

* Thu Jul 22 2021 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-14.20210722git9a96c54
- Updated to last upstream commits
- Added GPU stats for AMDGPU
- Added support for displaying GPU memory in the chart
- Add support for display scale factor
- Small fixes to thermal monitoring
- Added support for gnome-shell 40 - Removed Fedora patches (applied upstream)
- Remove clutter dependency on GNOME 40
- Improve graph settings and rendering

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-13.20210507gitbc38ccf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-12.20210507gitbc38ccf
- Updated to last upstream commits
- Added and updated translations
- Add units for network speeds over one gigabit
- Don't use version but check for function
- Fixed thermal sensor dropdown label rendering
- Prevent refreshes while the Shell is busy
- gpu_usage.sh improvements
- prefs: Remove unused Clutter reference
- Update prefs to support gnome 40 - RHBZ#1956148, RHBZ#1957479

* Sat Mar 20 2021 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-11.20210320git0b42126
- Updated to last upstream commits
- Fix gnome-shell and information spelling
- Fix for top left corner info
- Use utilities-system-monitor icon
- Numerous fixes for translations and locales handling
- Fix GPU not translated

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-10.20200503git7f8f0a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-9.20200503git7f8f0a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-8.20200503git7f8f0a7
- Updated to last upstream commits
- Fix string warning: Use ByteArray
- Fixed malformed nl translation. Updated makefile to put builds in ./dist
- Cleaned and switched Recommends tag for gnome-tweaks to Suggests tag as dnf
  treats it as Requires tag - RHBZ#1830474

* Thu Apr 16 2020 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-7.20200416git32cc79e
- Updated to last upstream commits
- Support for gnome-shell 3.36 added, and keep legacy usage
- Be able to show preferences from menu
- Make compact work even on resize
- Use UPower directly to remove warning
- Dropped patches (applied upstream)

* Wed Mar 25 2020 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-6.20200325gitcd2704c
- Updated to last upstream commits
- Translate to Turkish language
- Add patch to fix typo nvidia-settings in gpu_usage.sh - RHBZ#1794158
- Add patch to improve fetching values for NVidia GPU usage

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-5.20191019gitf00e248
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-4.20191019gitf00e248
- Updated to last upstream commits
- Use Gio.Subprocess for cleaner child process handling
- Updated Italian Translation
- Updated Slovak translation
- Edited gpu_usage.sh to work with glxinfo
- Included GS 3.34. Fixed formatting
- Removed duplicate css class
- Added Dutch (Netherlands) translation
- Use enums (instead of magic numbers) with GLib.file_test()

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-3.20190515gitfc83a73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-2.20190515gitfc83a73
- Updated to last upstream commits
- Fix #504  (array.to string() warnings)
- Remove obsolete compatibility code
- Scale width of elements if compact display is on
- Updated translation files
- Reverted ByteArray usage breaking display of thermal and fan speed
- Fixed frequency display showing blank due to ByteArray.tostring

* Mon Apr 29 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-1
- New upstream release (Fedora patches applied - RHBZ#1703693)
- Dropped previous Fedora patches

* Sat Apr 27 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:36-5.20190427gitc08bfd7
- Updated to last upstream commits
- Reworked Makefile
- Support for gnome-shell 3.32 added
- Added patches to support Fedora RPM package build

* Sun Feb 24 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:36-4.20190224git2583911
- Updated to last upstream commits
- Get rid of synchronous IO (read)
- Add Japanese translation
- Fix translation for 'GiB' in German
- Add a Makefile target to reload the extension

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:36-3.20190116gitd341bf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:36-2.20190116gitd341bf6
- Updated to last upstream commits
- Updating battery, check prefs
- Bugfix/fix net mount related login hangs after suspend
- Make the log messages more easy to filter from journalctl

* Wed Sep 19 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 1:36-1.20180919git21ae32a
- Updated to last upstream commits
- Support for gnome-shell 3.30 added
- Close unwanted _stdin_ and _stderr_ file descriptors

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:35-3.20180629gitd0b3a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 1:35-2.20180629gitd0b3a3a
- Updated to last upstream commits
- Improve post-release versions management

* Tue Apr 10 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 1:35-1.20180410git751d557
- Updated to last upstream commits
- Added the ability to manage post-release versions (git commit hash) and
  try not to mess up the version schema
- Added VERSION variable to install section to avoid git fatal message

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Björn Esser <besser82@fedoraproject.org> - 1:33-1
- New upstream release
- Follow upstream versioning
- Bump Epoch since previous people messed up the versioning scheme
- Simplify packaging

* Tue Oct 24 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.3.20171005git61b0a60
- Add support for EPEL 7.
- Revert upstream requires - Works with fresh vanilla Fedora with gnome-shell.

* Tue Oct 24 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.2.20171005git61b0a60
- Requires libgtop2 and NetworkManager-glib
- Fix NVidia GPU support
- Spec file rework

* Sat Oct 07 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.1.20171005git61b0a60
- Spec file cleanup

* Thu Oct 05 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20171005git61b0a60
- Updated to new upstream release
- Fixed battery module error and crash

* Sat Sep 30 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170930gitf24f167
- Updated to new upstream release
- Added support for Gnome 3.26
- Added GPU usage (NVidia)
- Updated translations

* Thu Sep 28 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170928git0a9f7a0
- Updated to new upstream release

* Thu Aug 17 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170817git746f33d
- Updated to new upstream release

* Mon May 01 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170501git59f443e
- Updated to new upstream release

* Tue Apr 11 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170411git0948ded
- Updated to new upstream release

* Thu Dec 22 2016 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20161222git3967cdd
- Updated to new upstream release

* Tue Apr 05 2016 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20160405git8b31f07
- Updated to new upstream release

* Wed Sep 30 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150930git81d1c08
- spec file cleanup
- Updated to new upstream release

* Wed Apr 15 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150415git44abf9a
- Updated to new upstream release

* Wed Feb 04 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150204gitd04c136
- Updated to new upstream release
- Added correct %%license tag to license files

* Wed Jan 28 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150129git6b9973e
- Updated to new upstream release

* Wed Jan 28 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150128gitccafeef
- Updated to new upstream release

* Fri Oct 10 2014 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.git59767af
- Updated to new upstream release

* Wed May 07 2014 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.git1b632f9
- Updated to new upstream release

* Wed Mar 06 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.gitfcecbaa
- Updated to new upstream release

* Sun Jan 13 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.git3f2c93e
- Updated to new upstream release

* Sun Oct 21 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.gitec4b4b7
- Updated to new upstream release v24

* Fri Aug 31 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v18-0.1.git96a05d5
- Updated to new upstream release v18

* Sun Aug 19 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 2.0b1-0.1.git74500bd
- Updated to new upstream release 2.0b1
- Completed spec file to install translations

* Sun Jun 26 2011 Fabian Affolter <fabian@bernewireless.net> - 1.92-1
- Updated to new upstream release 1.92

* Sat Jun 18 2011 Fabian Affolter <fabian@bernewireless.net> - 1.90-1
- Updated to new upstream release 1.90

* Wed Jun 08 2011 Fabian Affolter <fabian@bernewireless.net> - 0.99-1
- Updated to new upstream release 0.99

* Sat Jun 04 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-2
- Scriplet updated
- Version condition removed

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-1
- Initial package for Fedora
