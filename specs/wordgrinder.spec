Name:           wordgrinder
Version:        0.8
Release:        11%{?dist}
Summary:        A command line word processor

License:        MIT
URL:            http://cowlark.com/wordgrinder
%global pkgid   %{name}-%{version}
Source:         https://github.com/davidgiven/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc make ncurses-devel ninja-build
BuildRequires:  lua-devel lua-libs lua lua-filesystem
BuildRequires:  zlib-devel libXft-devel
BuildRequires:  minizip-devel
Requires:       ncurses-libs lua-filesystem

%description
WordGrinder is a Unicode-aware character cell word processor that runs in a
terminal (or a Windows console). It is designed to get the hell out of your way
and let you get some work done.

WordGrinder is a word processor for processing words. It is not WYSIWYG. It is
not point and click. It is not a desktop publisher. It is not a text editor. It
does not do fonts and it barely does styles. What it does do is words. It's
designed for writing text. It gets out of your way and lets you type

%package x11
Summary: X11 version of WordGrinder
Requires: %name = %version-%release
Requires: libX11
%description x11
An X11 version of the WordGrinder word processor.

%prep

%setup -q -n %{name}-%{version}

###############################################################################
%build

PREFIX=$RPM_BUILD_ROOT/%{_prefix} OBJDIR=$RPM_BUILD_ROOT/tmp WANT_STRIPPED_BINARIES=no make %{?_smp_mflags}

###############################################################################
%install

make install PREFIX=$RPM_BUILD_ROOT/%{_prefix}
install -D -m 0644 %{_builddir}/%{name}-%{version}/extras/wordgrinder.desktop %{buildroot}%{_datadir}/applications/wordgrinder.desktop

###############################################################################
%post x11
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun x11
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans x11
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


###############################################################################
%files
%license licenses/COPYING.WordGrinder
%_bindir/wordgrinder
%_docdir/wordgrinder/README.wg
%_mandir/man1/wordgrinder.1*

%files x11
%license licenses/COPYING.WordGrinder
%_bindir/xwordgrinder
%_mandir/man1/xwordgrinder.1*
%{_datadir}/applications/wordgrinder.desktop
%{_datadir}/pixmaps/wordgrinder.png
%{_datadir}/mime-info/wordgrinder.mime

###############################################################################
%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Ben Cotton <bcotton@fedoraproject.org> - 0.8-5
- Stop overwriting CFLAGS, which also fixes a FTBFS

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.8-1
- Update to version 0.8
- Make wordgrinder-x11 package standalone

* Tue Sep 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.7.2-6
- Change ncurses dependency to be more specific

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Ben Cotton <bcotton@fedoraproject.org> - 0.7.2-1
- Update to latest upstream release
- Remove unnecessary patch to build scripts

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 05 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.7.1-1
- Update to latest upstream release
- Remove unneeded dependences, which allows us more build arches
- Split the X11 version into an optional subpackage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-4
- Fix debuginfo issues

* Thu Jul 06 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-3
- Update the patch to build on Fedora 26

* Sun Jul 02 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-2
- Change lua to a version supported by upstream (5.1)

* Wed Jun 07 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-1
- Initial RPM release
