%global real_name gnome-colors

Name: gnome-colors-icon-theme
Summary: GNOME-Colors icon theme
Version: 5.5.1
Release: 24%{?dist}
Url: http://code.google.com/p/gnome-colors
Source0: http://%{real_name}.googlecode.com/files/%{real_name}-src-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Requires: gnome-icon-theme

# https://bugzilla.redhat.com/show_bug.cgi?id=1645368#c19
Patch1: remove-undefined-filter.patch

# the build is segfaulting due to
# https://bugzilla.redhat.com/show_bug.cgi?id=1556793
# so we use prebuilt pngs and svgs instead
# this is content, so strictly speaking this is not forbidden
%bcond_with prebuilt

# `mockbuild -N --without prebuilt` this on Fedora 22
# cd /var/lib/mock/fedora-22-x86_64/root/builddir/build/BUILD/gnome-colors-icon-theme-5.5.1/
# tar -cvzf gnome-colors-built-5.5.1.tar.gz gnome-colors-*
Source1: %{real_name}-built-%{version}.tar.gz

BuildRequires: icon-naming-utils >= 0.8.7
BuildRequires: ImageMagick

%if %{without prebuilt}
BuildRequires: inkscape
%endif
BuildRequires: make

%description
The GNOME-Colors is a project that aims to make the GNOME desktop as 
elegant, consistent and colorful as possible.

The current goal is to allow full color customization of themes, icons, 
GDM logins and splash screens. There are already seven full color-schemes 
available; Brave (Blue), Human (Orange), Wine (Red), Noble (Purple), Wise 
(Green), Dust (Chocolate) and Illustrious (Pink). An unlimited amount of 
color variations can be rebuilt and recolored from source, so users need 
not stick to the officially supported color palettes.

GNOME-Colors is mostly inspired/based on Tango, GNOME, Elementary, 
Tango-Generator and many other open-source projects. More information 
can be found in the AUTHORS file.

%prep
%autosetup -p1 -c %{real_name}-icon-theme-%{version}
# Make it build with Inkscape 1.0rc1+
sed -i 's|inkscape --without-gui -f /dev/stdin -e|inkscape --pipe -o|' Makefile

# link the start-here icon to the Fedora icon
for dir in gnome-colors-common/*/places; do
  cd $dir
  ln -sf ../apps/fedora-logo-icon.* start-here.*
  cd -
done
# change name from GNOME -> GNOME-Colors
rename 'gnome' '%{real_name}' themes/*
sed -i -e 's/GNOME/GNOME-Colors/' themes/*

%if %{with prebuilt}
tar -xzf %{SOURCE1}
find gnome-colors-* -type f  -exec touch {} +
%endif

%build
%{make_build}

%install
%{make_install}

%global themes %{_datadir}/icons/gnome-colors-common %{_datadir}/icons/gnome-colors-brave %{_datadir}/icons/gnome-colors-carbonite %{_datadir}/icons/gnome-colors-dust %{_datadir}/icons/gnome-colors-human %{_datadir}/icons/gnome-colors-illustrious %{_datadir}/icons/gnome-colors-noble %{_datadir}/icons/gnome-colors-tribute %{_datadir}/icons/gnome-colors-wine %{_datadir}/icons/gnome-colors-wise

%transfiletriggerin -- %{_datadir}/icons/gnome-colors
for THEME in %themes; do gtk-update-icon-cache --force ${THEME} &>/dev/null || : ; done

%transfiletriggerpostun -- %{_datadir}/icons/gnome-colors
for THEME in %themes; do gtk-update-icon-cache --force ${THEME} &>/dev/null || : ; done

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_datadir}/icons/gnome-colors-common/
%ghost %{_datadir}/icons/gnome-colors-common/icon-theme.cache
%{_datadir}/icons/gnome-colors-brave/
%ghost %{_datadir}/icons/gnome-colors-brave/icon-theme.cache
%{_datadir}/icons/gnome-colors-carbonite/
%ghost %{_datadir}/icons/gnome-colors-carbonite/icon-theme.cache
%{_datadir}/icons/gnome-colors-dust/
%ghost %{_datadir}/icons/gnome-colors-dust/icon-theme.cache
%{_datadir}/icons/gnome-colors-human/
%ghost %{_datadir}/icons/gnome-colors-human/icon-theme.cache
%{_datadir}/icons/gnome-colors-illustrious/
%ghost %{_datadir}/icons/gnome-colors-illustrious/icon-theme.cache
%{_datadir}/icons/gnome-colors-noble/
%ghost %{_datadir}/icons/gnome-colors-noble/icon-theme.cache
%{_datadir}/icons/gnome-colors-tribute/
%ghost %{_datadir}/icons/gnome-colors-tribute/icon-theme.cache
%{_datadir}/icons/gnome-colors-wine/
%ghost %{_datadir}/icons/gnome-colors-wine/icon-theme.cache
%{_datadir}/icons/gnome-colors-wise/
%ghost %{_datadir}/icons/gnome-colors-wise/icon-theme.cache

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-18
- Fix empty trash bin icon on MATE desktop (#1645368)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-14
- Use prebuilt images
- Switch to triggers

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-6
- Use %%global instead of %%define
- Use %%{make_install}
- Use icon cache scriplets form wiki

* Sun Sep 01 2013 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-5
- Link the start-here icon to the Fedora icon

* Fri Aug 30 2013 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-4
- Removed BuildRoot definition and Group
- Removed %%clean section
- Removed rm -rf form %%install
- Removed %%defattr from %%files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 18 2009 Michal Nowak <mnowak@redhat.com> - 5.5.1-1
- 5.5.1

* Tue Aug  4 2009 Michal Nowak <mnowak@redhat.com> - 5.3-1
- 5.3
- Requires: gnome-icon-theme

* Mon Aug  3 2009 Michal Nowak <mnowak@redhat.com> - 5.2.2-1
- initial packaging

