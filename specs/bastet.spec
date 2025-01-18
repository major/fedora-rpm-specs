Name:		bastet
Version:	0.43.2
Release:	11%{?dist}
Summary:	An evil falling bricks game

License:	GPL-3.0-or-later
URL:		https://github.com/fph/bastet
Source0:	https://github.com/fph/bastet/archive/%{version}.zip
Source1:	%{name}.desktop
# self-made icon
Source2:	%{name}.png
Patch0:		bastet-tr1.patch
Patch1:         bastet-fmt-str.patch

BuildRequires:  gcc-c++
BuildRequires:	boost-devel ncurses-devel desktop-file-utils
BuildRequires: make


%description
Bastet is a simple ncurses-based falling bricks like game. Unlike 
normal, however, Bastet does not choose your next brick at random. 
Instead, it uses a special algorithm designed to choose the worst 
brick possible. As you can imagine, playing Bastet can be a very 
frustrating experience!


%prep
%setup -q

%patch -P0 -p1
%patch -P1 -p0

# remove reference to Tetris to match our guidelines
sed -e 's/Tetris(R)/any falling bricks game/g' -e 's/Tetris/falling bricks game/g' \
-e 's/tetris/falling bricks game/g' README > README.new
mv -f README.new README
# remove also any reference to Tetris in the bastet manpage
sed -e 's/Tetris(r)/any falling bricks game/g' -e 's/tetris/falling bricks game/g' \
bastet.6 > bastet.6.new
mv -f bastet.6.new bastet.6


%build

make %{?_smp_mflags} CXXFLAGS="%{optflags}"


%install
rm -rf %{buildroot}

# install the AppData file
%__mkdir_p %{buildroot}%{_datadir}/appdata
cp bastet.appdata.xml %{buildroot}%{_datadir}/appdata/

mkdir -p %{buildroot}%{_bindir}

install -p -m 755 bastet %{buildroot}%{_bindir}/bastet

# below the desktop file and icon stuff
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications	\
	%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2}				\
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# manpage
mkdir -p %{buildroot}%{_mandir}/man6/
      install -p -m 0644 %{name}.6 \
      %{buildroot}%{_mandir}/man6/%{name}.6


%files
%doc AUTHORS LICENSE NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.43.2-7
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.43.2-5
- migrated to SPDX license

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.43.2-4
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.43.2-1
- 0.43.2

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.43.1-36
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-34
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-31
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-29
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-25
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-22
- Rebuilt for Boost 1.66

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.43.1-21
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-18
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-17
- Rebuilt for Boost 1.64

* Thu Jun 01 2017 Richard Hughes <rhughes@redhat.com> - 0.43.1-16
- Fix AppData file to validate (also sent upstream).

* Wed Feb 22 2017 Jon Ciesla <limburgher@gmail.com> - 0.43.1-15
- Fix FTBFS.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-13
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-12
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-10
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.43.1-9
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.43.1-7
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.43.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.43.1-4
- Rebuild for boost 1.57.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Richard Hughes <richard@hughsie.com> - 0.43.1-1
- New upstream release

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.43-22
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.43-20
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.43-19
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.43-18
- Rebuild for Boost-1.53.0

* Thu Jul 26 2012 Jon Ciesla <limburgher@gmail.com> - 0.43-17
- Rebuild for boost 1.50.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-15
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Jon Ciesla <limb@jcomserv.net> - 0.43-13
- Rebuild for new boost.

* Thu Jul 21 2011 Jon Ciesla <limb@jcomserv.net> - 0.43-12
- Rebuild for new boost.

* Fri Apr 08 2011 Jon Ciesla <limb@jcomserv.net> - 0.43-11
- Rebuild for new boost.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.43-9
- rebuild for new boost

* Fri Jul 30 2010 Jon Ciesla <limb@jcomserv.net> - 0.43-8
- Rebuild for new boost.

* Thu Jan 21 2010 Jon Ciesla <limb@jcomserv.net> - 0.43-7
- Rebuild for new boost.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 06 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 0.43-5
- Changed CFLAGS to CXXFLAGS

* Fri Jun 05 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 0.43-4
- Added new icon cache scriptlets
- Added optflags
- Changed license to GPLv3+
- Removed manually gzip of manpage

* Thu Jun 04 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 0.43-3
- Add manpage
- Removed reference to Tetris in the bastet manpage

* Mon Jun 01 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 0.43-2
- Removed reference to Tetris to match our guidelines

* Mon Jun 01 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 0.43-1
- Initial SPEC file
