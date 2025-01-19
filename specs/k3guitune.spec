Name:           k3guitune
Version:        1.01
Release:        38%{?dist}
Summary:        Musical instrument tuner

# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            http://home.planet.nl/~lamer024/k3guitune.html
Source0:        http://home.planet.nl/~lamer024/files/k3guitune-%{version}.tar.gz
# guitune author made guitune_logo.xpm available in gtkguitune, available in
#     http://www.geocities.com/harpin_floh/mysoft/gtkguitune-0.7.tar.gz
Source1:        %{name}.xpm
# patch by dtimms to fix the parameters supplied in some calling functions,
#     without this compile dies:
Patch0:         %{name}-1.01-fix-multiple-parameters-bug.patch

Patch1:         %{name}-desktop-file.patch
# from http://www.kde-apps.org/content/show.php/K3Guitune?content=15358
#     fix fftw library usage bugs: 
Patch2:         %{name}-1.01-fftw.patch

BuildRequires: gcc
BuildRequires: kdelibs3-devel
BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: bio2jack-devel
BuildRequires: make


%description
K3Guitune is a guitar-and-other-instruments tuner. It takes a signal from the 
microphone, calculates its frequency, and displays it on a note scale 
graphic and an oscilloscope. It supports normal, Wien, and physical tuning.


%prep
%setup -q
%patch -P0 -p1 -b .fix-multiple-parameters-bug
%patch -P1 -p1 -b .desktop-file
%patch -P2 -p1 -b .fftw
%{__rm} -rf po/*.gmo

# fix UTF-8 encodings
for nonutffile in ChangeLog AUTHORS; do
  iconv -f iso8859-1 -t utf-8 $nonutffile > $nonutffile.conv 
  touch -r $nonutffile $nonutffile.conv
  %{__mv} -f $nonutffile.conv $nonutffile
done

# adjustment to allow input via bio2jack
sed -i 's|JACKSoundInput::JACKSoundInput|JACKSoundInput|' k3guitune/soundinput.h


%build
%configure --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__install} -p -m 644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

desktop-file-install                           \
    --add-category="AudioVideo"                \
    --add-category="Audio"                     \
    --delete-original                          \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applnk/Multimedia/%{name}.desktop

# remove symlinks with absolute paths, and recreate with relative paths
%{__rm} %{buildroot}/%{_docdir}/HTML/*/%{name}/common
cd %{buildroot}/%{_docdir}/HTML/
for lang in *; do
  ln -sf ../common $lang/%{name}/
done


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/%{name}/
%{_docdir}/HTML/*/%{name}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.01-37
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 David Timms <iinet.net.au@dtimms> - 1.01-29
- remove broken RPATH of /usr/lib64 using sed/libtool method

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.01-20
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.01-14
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 David Timms <iinet.net.au@dtimms> - 1.01-6
- add sed to enable input from jack server
- add BuildRequires: bio2jack

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 11 2009 David Timms <iinet.net.au@dtimms> - 1.01-4
- fix command order for nonutffile timestamping

* Tue Mar 10 2009 David Timms <iinet.net.au@dtimms> - 1.01-3
- mod icon cache update to use newly ratified scriptlets
- enable jack audio support via BR: bio2jack
- mod symlink fix to be more flexible in the future
- remove install of INSTALL
- mod to use more macro style invocations, except url and source
- del Requires: hicolor-icon-them since it wil be detected via kdelibs3
- clarify License tag since some source files are licensed GPLv2 only.
- fix previous changelog date

* Sun Mar  8 2009 David Timms <iinet.net.au@dtimms> - 1.01-2
- add missing BR: alsa-lib-devel
- add patch for fftw library usage bug
- fix absolute symlink to be a relative symlink

* Fri Jan 30 2009 David Timms <iinet.net.au@dtimms> - 1.01-1
- Initial spec for Fedora based on Dries Verachtert's package
- Updated to release 1.01, the final release.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Updated to release 0.5.2.
