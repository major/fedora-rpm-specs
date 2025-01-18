Name:           FlightCrew
Version:        0.9.1
Release:        41%{?dist}
Summary:        EPUB validator
License:        LGPL-3.0-or-later
URL:            https://sigil-ebook.com/
Source0:        https://github.com/Sigil-Ebook/flightcrew/releases/download/%{version}/FlightCrew-%{version}-Code.zip
Source1:        flightcrew-sigil-plugin.metainfo.xml
Patch1:         0001-use-system-zlib-if-available.patch
Patch2:         0002-use-system-boost-libraries-if-available.patch
Patch3:         0003-use-system-xerces-c-if-available.patch
Patch4:         0004-don-t-build-googlemock-when-NO_TEST_EXE-is-specified.patch
Patch5:         0005-move-zipextraction-under-FlightCrew.patch
Patch6:         0006-use-system-zipios-library-if-available.patch
Patch7:         0007-FlightCrew-plugin-Make-FlightCrew-plugin-work-on-uni.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1450956
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=861987
Patch8:         use_random_unique_tmp_path.patch
Patch9:         boost_176_scoped_ptr.patch
BuildRequires:  cmake
BuildRequires:  libappstream-glib
BuildRequires:  zlib-devel
BuildRequires:  boost-devel
BuildRequires:  xerces-c-devel >= 3.1
BuildRequires:  zipios++-devel
BuildRequires:  python3-devel
BuildRequires:  gcc-c++

%description
FlightCrew is a C++ epub validator.


%package        sigil-plugin
Summary:        Sigil FlightCrew epub validator plugin
Requires:       sigil
# Older versions of FlightCrew were directly linked into sigil, we
# hacked up the FlightCrew build to produce a dynamic-lib to make this
# work, but upstream never intended FlightCrew to be used this way and
# with the plugin this is no longer necessary
Obsoletes:      %{name} <= 0.8
Obsoletes:      %{name}-devel <= 0.8

%description    sigil-plugin
Sigil FlightCrew epub validator plugin.


%package        cli
Summary:        FlightCrew cli epub validator

%description    cli
FlightCrew cli epub validator.


%prep
%autosetup -c -p1

# Fix EOL encoding for %%doc
for i in COPYING*.txt ChangeLog.txt README.txt; do
    sed -i.old 's/\r//' "$i"
    touch -r "$i.old" "$i"
done

# remove unbundled stuff
rm -rf src/BoostParts src/zlib src/Xerces src/zipios
# remove test framework
rm -rf src/googlemock

# fix permissions
chmod a-x src/utf8-cpp/utf8/*.h

# Fix python shebang
sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' src/FlightCrew-plugin/plugin.py

%build
%{cmake} -DBUILD_SHARED_LIBS:BOOL=OFF -DSKIP_FC_GUI=1 -DNO_TEST_EXE=1
%{cmake_build}


%install
%{cmake_install}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/sigil/plugins/%{name}
install -p -m 755 src/FlightCrew-plugin/plugin.py \
  $RPM_BUILD_ROOT%{_datadir}/sigil/plugins/%{name}
install -p -m 644 src/FlightCrew-plugin/plugin.xml \
  $RPM_BUILD_ROOT%{_datadir}/sigil/plugins/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/flightcrew-sigil-plugin.metainfo.xml


%files sigil-plugin
%doc ChangeLog.txt README.txt
%license COPYING*.txt
%{_bindir}/flightcrew-plugin
%{_datadir}/appdata/flightcrew-sigil-plugin.metainfo.xml
%{_datadir}/sigil/plugins/%{name}

%files cli
%doc ChangeLog.txt README.txt
%license COPYING*.txt
%{_bindir}/flightcrew-cli


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Pete Walter <pwalter@fedoraproject.org> - 0.9.1-40
- Rebuild for xerces-c 3.3

* Fri Oct 18 2024 Pete Walter <pwalter@fedoraproject.org> - 0.9.1-39
- Rebuild for xerces-c 3.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-37
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-33
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-31
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.9.1-28
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-26
- Rebuilt for Boost 1.76.0 (using the right side tag)

* Mon Aug 09 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-25
- Patched and rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-22
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-19
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-15
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-13
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-11
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-8
- Rebuilt for Boost 1.64

* Mon May 15 2017 Dan Horák <dan[at]danny.cz> - 0.9.1-7
- fix temp dir handling (#1450956)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-5
- Rebuilt for Boost 1.63

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4
- Rebuild for Python 3.6

* Tue Aug 09 2016 Lumir Balhar <lbalhar@redhat.com> - 0.9.1-3
- Added `sed` to specfile to change shebang to python3

* Mon May 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-2
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 25 2016 Hans de Goede <hdegoede@redhat.com> - 0.9.1-1
- Update to 0.9.1
- No longer build as a library for use in sigil, instead
  provide a -sigil-plugin sub-package for sigil
- Make -sigil-plugin obsolete the old main (lib) and devel package
- Add -cli sub-package with the cli version of FlightCrew

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.2-20
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.7.2-19
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.7.2-17
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-15
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.7.2-14
- Rebuild for boost 1.57.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.7.2-11
- Rebuild for boost 1.55.0

* Wed Mar 19 2014 Dan Horák <dan[at]danny.cz> - 0.7.2-10
- Build with system zipios++ library (#1077716)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.7.2-8
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.2-7
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.2-6
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.2-5
- Rebuild for new boost

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 0.7.2-2
- Make -devel package Requires on main package include isa
- Drop buildroot and defattr boilerplate (no longer needed with recent rpm)
- Split the use-system-libs patch into its sub patches
- Add a FindFlightCrew cmake module
- Build XercesExtensions as a shared lib (including a Find... cmake module)

* Sat Dec 24 2011 Dan Horák <dan[at]danny.cz> - 0.7.2-1
- initial Fedora version
