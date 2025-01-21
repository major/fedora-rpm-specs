%global rctag rc8

Name:		wsjtx
Version:	2.7.0
Release:	11%{?dist}
Summary:	Weak Signal communication by K1JT

License:	GPL-3.0-or-later

URL:		http://physics.princeton.edu/pulsar/k1jt/wsjtx.html
Source0:    https://sourceforge.net/projects/wsjt/files/%{name}-%{version}%{?rctag:-%{rctag}}/%{name}-%{version}%{?rctag:-%{rctag}}.tgz
Source100:	wsjtx.appdata.xml

ExcludeArch:    i686

BuildRequires:	cmake
BuildRequires:	dos2unix
BuildRequires:	tar
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran

BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	desktop-file-utils
BuildRequires:	hamlib-devel
BuildRequires:	fftw-devel
BuildRequires:	libusbx-devel
BuildRequires:	systemd-devel
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:	boost169-devel
%else
BuildRequires:	boost-devel
%endif
BuildRequires:	portaudio-devel
%if 0%{?fedora}
BuildRequires:	asciidoc
BuildRequires:	rubygem-asciidoctor
BuildRequires:	libappstream-glib
%endif

%description
WSJT-X is a computer program designed to facilitate basic amateur radio
communication using very weak signals. It implements communication protocols
or "modes" called JT4, JT9, JT65, QRA64, ISCAT, MSK144, and WSPR, as well as
one called Echo for detecting and measuring your own radio signals reflected
from the Moon.


%prep
%setup -n %{name}-%{version}
#{?rctag:-%{rctag}}

# Remove bundled hamlib
rm -f src/hamlib*.tgz* src/hamlib*.tar.gz*

# Extract wsjtx source and clean up
tar -xzf src/%{name}.tgz
rm -f src/wsjtx.tgz*
find ./ -type f -exec chmod -x {} \;

cd %{name}

%if ! 0%{?rhel} < 8
# remove bundled boost. EL 7 is not required version.
rm -rf boost
%endif

# convert CR + LF to LF
dos2unix *.ui *.iss *.txt


%build
# The fortran code in this package is not type safe and will thus not work
# with LTO.  Additionally there are numerous bogus strncat calls that also
# need to be fixed for this package to work with LTO
%define _lto_cflags %{nil}

# Workaround for build with gcc-10, problem reported upstream
export CFLAGS="%{optflags} -fcommon"
export LDFLAGS="%{?__global_ldflags}"
# workaround for hamlib check, i.e. for hamlib_LIBRARY_DIRS not to be empty
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1

cd %{name}
%cmake -Dhamlib_STATIC=FALSE \
       -DBoost_NO_SYSTEM_PATHS=FALSE \
%if 0%{?rhel}
       -DBOOST_INCLUDEDIR=%{_includedir}/boost169 \
       -DBOOST_LIBRARYDIR=%{_libdir}/boost169 \
       -DWSJT_GENERATE_DOCS=FALSE \
       -DWSJT_SKIP_MANPAGES=TRUE
%endif

%cmake_build


%install
cd %{name}
%cmake_install

dos2unix %{buildroot}%{_datadir}/applications/message_aggregator.desktop

# Make sure the right style is used.
desktop-file-edit --set-key=Exec --set-value="wsjtx --style=fusion" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
# desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/wsjtx.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/message_aggregator.desktop

%if 0%{?fedora}
# appdata file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE100} %{buildroot}%{_metainfodir}/
%endif

# fix docs
install -p -m 0644 -t %{buildroot}%{_datadir}/doc/%{name} GUIcontrols.txt jt9.txt \
  v1.7_Features.txt wsjtx_changelog.txt

# drop wsjtx hamlib bins
rm -f %{buildroot}%{_bindir}/rigctl*-wsjtx


%if 0%{?fedora}
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%endif


%files
%license COPYING
%doc %{_datadir}/doc/%{name}
%{_bindir}/cablog
%{_bindir}/echosim
%{_bindir}/fcal
%{_bindir}/fmeasure
%{_bindir}/fmtave
%{_bindir}/fst4sim
%{_bindir}/hash22calc
%{_bindir}/jt4code
%{_bindir}/jt65code
%{_bindir}/jt9
%{_bindir}/jt9code
%{_bindir}/ft8code
%{_bindir}/message_aggregator
%{_bindir}/msk144code
%{_bindir}/q65sim
%{_bindir}/q65code
%{_bindir}/udp_daemon
%{_bindir}/wsjtx
%{_bindir}/wsjtx_app_version
%{_bindir}/wsprd
%{?fedora:%{_mandir}/man1/*.1.gz}
%{?fedora:%{_metainfodir}/*.xml}
%{_datadir}/applications/wsjtx.desktop
%{_datadir}/applications/message_aggregator.desktop
%{_datadir}/pixmaps/wsjtx_icon.png
%{_datadir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Richard Shaw <hobbes1069@gmail.com> - 2.7.0-10
- Update to 2.7.0 RC8.

* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.0-9
- Rebuild for Hamlib 4.6.

* Tue Oct 01 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.0-8
- Update to 2.7.0 RC7.

* Sat Sep 14 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.0-7
- Remove superfox binaries and patch build system.

* Thu Aug  1 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.0-6
- Update to 2.7.0 RC6.

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.0-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.0-5
- Update to 2.7.0 RC5.

* Mon Jan 22 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.0-3
- Update to 2.7.0 RC3.

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 2.7.0-2
- Rebuilt for Boost 1.83

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.6.1-2
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Richard Shaw <hobbes1069@gmail.com> - 2.6.1-1
- Update to 2.6.0.

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 2.5.4-5
- Rebuild for updated hamlib 4.5.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.5.4-3
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Richard Shaw <hobbes1069@gmail.com> - 2.5.4-1
- Update to 2.5.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.3-2
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.3-1
- New version
  Resolves: rhbz#2034707

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-2
- 36-build-side-49086

* Mon Nov 29 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.2-1
- New version
  Resolves: rhbz#2020399

* Mon Oct 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.1-1
- New version
  Resolves: rhbz#2016506

* Wed Oct 13 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-1
- New version
  Resolves: rhbz#2008230

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 2.4.0-5
- Rebuild for hamlib 4.3.1.

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-4
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 2.4.0-2
- Rebuild for hamlib 4.2.

* Mon May 24 2021 Richard Shaw <hobbes1069@gmail.com> - 2.4.0-1
- Update to 2.4.0.

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.3.1-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Fri Mar 26 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.1-1
- Update to 2.3.1.

* Wed Feb 03 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.0-1
- Update to 2.3.0 final.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.2-8
- Rebuild for hamlib 4.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.2-6
- Rebuilt for hamlib 4.0 release.

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.2-5
- Fixed FTBFS
  Resolves: rhbz#1865629

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 2.2.2-2
- Disable LTO

* Mon Jun 22 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.2-1
- Update to 2.2.2.

* Sat Jun 06 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-1
- Update to 2.2.1.

* Tue Jun 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.2-4
- Rebuilt with hamlib 4.0.

* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-3
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1800262

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.2-1
- Update to 2.1.2.

* Tue Nov 26 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-1
- Upate to 2.2.1.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-1
- Update to 2.1.0.

* Mon Feb 25 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.1-1
- Update to 2.0.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Richard Shaw <hobbes1069@gmail.com> - 2.0.0-8
- Update to 2.0.0 GA.

* Fri Sep 28 2018 Richard Shaw <hobbes1069@gmail.com> - 1.9.1-2
- Rebuild for hamlib 3.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Richard Shaw <hobbes1069@gmail.com> - 1.9.1-1
- Update to 1.9.1.
- Update compile patch to deal with qt5_use_modules no longer being available in
  rawhide/f29.

* Tue May 29 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-1
- New version
- Dropped gcc-8.0.1-compile-fix patch (not needed)

* Wed May  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-0.3.rc4
- New version
- De-fuzzified patches

* Wed Mar 21 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-0.2.rc3
- New version
- Updated gcc-8.0.1-compile-fix patch

* Fri Mar 16 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-0.1.rc2
- New version
- Fixed compilation with gcc-8.0.1
  Resolves: rhbz#1556544
- De-fuzzified compile-fix patch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-3
- Rebuilt for new fortran

* Fri Jan 19 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-2
- Do not force non-executable stack
  Resolves: rhbz#1535987
  Resolves: rhbz#1523446

* Mon Jan 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-1
- New version
  Resolves: rhbz#1534099
- De-fuzzified compile-fix patch

* Fri Sep  8 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-0.3.rc2
- Dropped rigctl*-wsjtx (hamlib copy)

* Sun Sep  3 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-0.2.rc2
- New version

* Fri Sep  1 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-0.1.rc1
- Initial version
