# This package needs to be run as root and may
# run for a long time, thus we build with full
# hardening. This flags is enabled by default
# on recent Fedora releases, but we need to
# specify it for EPEL <= 7 explicitly.
%global _hardened_build 1


Name:           timeshift
Version:        22.06.5
Release:        2%{?dist}
Summary:        System restore tool for Linux

License:        GPLv3+ or LGPLv3+
URL:            https://github.com/linuxmint/timeshift
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  vala

Requires:       cronie
Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       psmisc
Requires:       rsync

# For btrfs systems
Recommends:     btrfs-progs

%description
Timeshift for Linux is an application that provides functionality similar to
the System Restore feature in Windows and the Time Machine tool in Mac OS.
Timeshift protects your system by taking incremental snapshots of the file
system at regular intervals. These snapshots can be restored at a later date
to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files
are shared between snapshots which saves disk space. Each snapshot is a full
system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS
filesystem. BTRFS snapshots are supported only on BTRFS systems having an
Ubuntu-type subvolume layout (with @ and @home subvolumes).


%prep
%autosetup -p1
sed -i -e 's@--thread @@g' src/makefile
sed -i -e 's@--Xcc="-O3" @@g' src/makefile
sed -i '/${app_name}-uninstall/d' src/makefile

%build
for flag in %{optflags} %{?__global_ldflags}; do
  VALAFLAGS="$VALAFLAGS -X $flag"
done

# Inject Fedora compiler flags and the debug option to valac.
# Just dump the c-sources.
sed -i "s|^[\t ]*valac|& --ccode --save-temps -g $VALAFLAGS|" src/makefile
%make_build

# Move generated c-sources into flat tree so it can be picked
# up for -debugsource.
for f in `find src/ -type f -name '*.c'`; do
  mv -f $f src/
done

# Inject Fedora compiler flags and the debug option to valac
# Build the binaries.
sed -i "s|valac --ccode|valac|" src/makefile
%make_build


%install
%make_install
# Remove duplicate
rm -rf %{buildroot}%{_datadir}/appdata

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop


%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif


%files -f %{name}.lang
%license COPYING LICENSE.md
%doc AUTHORS README.md
%{_bindir}/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/timeshift-boot
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/timeshift-hourly
%ghost %attr(664, root, root) %{_sysconfdir}/timeshift.json
%config %{_sysconfdir}/timeshift/default.json



%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.09.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 15 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 21.09.1-1
- Update to 21.09.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 15 2020 Samuel Rakitničan <samuel.rakitnican@gmail.com> 20.03-1
- Update to 20.03
- Rework the uninstall script removal

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.08.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Richard Shaw <hobbes1069@gmail.com> - 19.08.1-1
- Update to 19.08.1.
- Add patch to deal with abstract class compile error.

* Sat Mar 09 2019 Samuel Rakitničan <samuel.rakitnican@gmail.com> 19.01-1
- Update to 19.01
- Remove upstream gcc optimisation flag -O3 (Since timeshift 18.8)

* Sun Mar 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 18.6.1-4
- Fix build errors with newer vala, remove --threads from makefile

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com> 18.6.1-1
- Update to 18.6.1 with vte291 fixes for F28 and rawhide

* Sun Jun 24 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com> 18.4-1
- Update to 18.4
- Add runtime dependency on psmisc
- Update sed expression to avoid false matches

* Sun Feb 18 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Remove rpath workaround, fixed since 18.2

* Sun Feb 18 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com> 18.2-1
- Update to 18.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Björn Esser <besser82@fedoraproject.org> - 18.1.1-4
- Generate useful -debugsource package

* Sun Jan 28 2018 Björn Esser <besser82@fedoraproject.org> - 18.1.1-3
- Properly apply system LDFLAGS and thus enable full hardening

* Fri Jan 26 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com> 18.1.1-2
- Add scriptlets for icon cache to EPEL only

* Thu Jan 25 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Add patch that changes location of AppData file
- Validate AppData file
- Updated description

* Thu Jan 25 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com> 18.1.1-1
- Update to 18.1.1
- Remove brackets around make_build and make_install
- Use autosetup macro

* Mon Jan 15 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Add runtime dependencies for cron, icons and polkit
- Fix the license

* Mon Jan 15 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com> 18.1-1
- Update to 18.1
- Revert wrong permissions for a ghost file from previous update
- Correct the license

* Sun Jan 14 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com> 17.11-1
- Update to 17.11
- Change to polkit instead of gksu/sudo

* Fri Sep 08 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 17.2-2
- Debug build
- Added config files to %%files that are created on runtime

* Thu Sep 07 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 17.2-1
- Adjust according to Fedora Packaging Guidelines
- Update to 17.2
- Fix build error with newer Fedora releases that uses vala 0.36

* Sat Mar 08 2014 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 2.0.85-1
- update

* Sat Dec 28 2013 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.3.3-1
- Update

* Sun Oct 06 2013 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.0-1
- Initial build.
