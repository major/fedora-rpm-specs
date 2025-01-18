%define         datever 20061216

Name:           MyPasswordSafe
Version:        0.6.7
Release:        52.%{datever}%{?dist}
Summary:        A graphical password management tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.semanticgap.com/myps/
Source0:        http://www.semanticgap.com/myps/release/MyPasswordSafe-%{datever}.src.tgz
Source1:        MyPasswordSafe.desktop
Patch0:         MyPasswordSafe-20061216-use-system-uuid.patch
# Both patches have been sent to support [AT] semanticgap [DOT] com on 2009/04/25
Patch1:         MyPasswordSafe-20061216-gcc43.patch
Patch2:         MyPasswordSafe-20090425-gcc44.patch
Patch3:         MyPasswordSafe-20061216-fix-off-by-one.patch
Patch4:         MyPasswordSafe-20061216-stack-trash.patch
Patch5:         MyPasswordSafe-20061216-unsigned-convert.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  boost-devel, qt3-devel, uuid-devel, libXScrnSaver-devel
BuildRequires:  desktop-file-utils

%description
MyPasswordSafe is a straight-forward, easy-to-use password manager that
maintains compatibility with Password Safe files. MyPasswordSafe has the
following features:

* Safes are encrypted when they are stored to disk.
* Passwords never have to be seen, because they are copied to the clipboard
* Random passwords can be generated.
* Window size, position, and column widths are remembered.
* Passwords remain encrypted until they need to be decrypted at the dialog
  and file levels.
* A safe can be made active so it will always be opened when MyPasswordSafe
  starts.
* Supports Unicode in the safes
* Languages supported: English and French


%prep
%setup -q -n %{name}-%{datever}

# Use the system installed ossp-uuid lib
%patch -P0 -p1 -b .use-system-uuid.patch

# Fix regressions due to stricter GCC 4.3 checking
%patch -P1 -p1 -b .gcc43

# GCC 4.4 patch
%patch -P2 -b .gcc44

# Fix off-by-one in EncryptedString::get
%patch -P3 -p1 -b off-by-one

# Fix stack trashing due to wrong array size calculations
%patch -P4 -p1 -b stack-trash

# Fix compiler warnings for narrowing to char
%patch -P5 -p1 -b unsigned-convert

%build

unset QTDIR || : ; . /etc/profile.d/qt.sh

make %{?_smp_mflags} PREFIX=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# Remove the docs, they are in the wrong place.
rm -rf $RPM_BUILD_ROOT%{_prefix}/share/doc

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor="fedora"               \
%endif
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications    \
    %{SOURCE1}



%files
%doc ChangeLog CHANGES COPYING README doc/manual.html doc/sshots/*.jpg
%{_bindir}/MyPasswordSafe
%{_datadir}/MyPasswordSafe
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-MyPasswordSafe.desktop
%else
%{_datadir}/applications/MyPasswordSafe.desktop
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-52.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.7-51.20061216
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-50.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-49.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-48.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-47.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-46.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-45.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-44.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-43.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-42.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-41.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-40.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-39.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-38.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-37.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-36.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-35.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-34.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.7-33.20061216
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-32.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.7-31.20061216
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-30.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 0.6.7-29.20061216
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.7-28.20061216
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-27.20061216
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.6.7-26.20061216
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-25.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.7-24.20061216
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.6.7-23.20061216
- Rebuild for boost 1.57.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-22.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-21.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.6.7-20.20061216
- Rebuild for boost 1.55.0

* Sat Dec 21 2013 Ralf Ertzinger <ralf@skytale.net> - 0.6.7-19.20061216
- Fix stack trashing due to wrong size calculation, closes bz1042667
- Fix compiler warnings about narrowing longs into chars

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-18.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.6.7-17.20061216
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.7-16.20061216
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-15.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-14.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-13.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-12.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Ralf Ertzinger <ralf@skytale.net>
- Fix off-by-one in encryptstring.cpp, closes bz652928

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-9.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.6.7-8.20061216
- Fix FTBFS: added MyPasswordSafe-20090425-gcc44.patch

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-7.20061216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.6.7-6.20061216
- fix license tag

* Sat Apr 05 2008 Ralf Ertzinger <ralf@skytale.net> 0.6.7-5.20061216
- Change BuildRequires to qt3-devel

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.7-4.20061216
- Autorebuild for GCC 4.3

* Fri Jan 04 2008 Ralf Ertzinger <ralf@skytale.net> 0.6.7-3.20061216
- Add patch to enable compilation with GCC4.3

* Fri Jul 06 2007 Ralf Ertzinger <ralf@skytale.net> 0.6.7-1.20061216
- Initial build for Fedora
