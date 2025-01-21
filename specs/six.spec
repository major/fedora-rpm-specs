Name:           six
Version:        0.5.3
Release:        46%{?dist}
Summary:        Hex playing program

License:        GPL-1.0-or-later
URL:            http://six.retes.hu/
Source0:        http://six.retes.hu/download/%{name}-%{version}.tar.gz
Patch0:         six-gcc43.patch
Patch50:	six-fix-DSO.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  kdelibs3-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Six is a Hex  playing program for Linux/Un*x systems running KDE. It has a
strong AI, an easy to use GUI and can import emails from Richard's PBEM server.

%prep
%setup -q
%patch -P0 -p0
%patch -P50 -p0
%{__sed} -i 's/DocPath\=six\/six\.html/Categories\=Game\;BoardGame\;/' six/six.desktop
%{__sed} -i 's/Terminal\=0/Terminal\=false/' six/six.desktop
echo "Encoding=UTF-8" >> six/six.desktop

%build
%configure --disable-dependency-tracking
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/six/common

%find_lang %{name}

desktop-file-install                                    \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --delete-original                               \
        $RPM_BUILD_ROOT%{_datadir}/applnk/Games/Board/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO VERSION
%{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/doc/HTML/en/%{name}
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/locolor
%{_datadir}/mimelnk/application/vnd.kde.six.desktop
%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/icons/locolor || :
%{_bindir}/gtk-update-icon-cache --quiet --ignore-theme-index %{_datadir}/icons/locolor || :

%postun
touch --no-create %{_datadir}/icons/locolor || :
%{_bindir}/gtk-update-icon-cache --quiet --ignore-theme-index %{_datadir}/icons/locolor || :

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-44
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-30
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.3-24
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> 0.5.3-20
- Remove vendor prefix from desktop file

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> 0.5.3-19
- Add qt-mt to the list of explicitly linked libraries

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-16
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.5.3-13
- FTBFS fix

* Thu Apr 29 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.5.3-12
- DSO fix #564751

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 09 2008 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-9
- gcc 4.3 rebuild
* Thu Jan 10 2008 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-8
- gcc 4.3 patch
* Tue Jan 08 2008 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-7
- fixed BR
* Sat Aug 25 2007 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-6
- BuildID rebuild
* Mon Aug 20 2007 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-5
- License tag update
* Fri Jan 12 2007 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-4
- added --ignore-theme-index to gtk-update-icon-cache for locolor icons
* Fri Jan 12 2007 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-3
- added locolor icons to gtk-update-icon-cache
* Fri Jan 12 2007 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-2
- added check, post & postun sections
- fixed .desktop file
* Mon Jan 08 2007 Rafał Psota <rafalzaq@gmail.com> - 0.5.3-1
- Initial release
