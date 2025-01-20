Name:       pyzy
Version:    0.1.0
Release:    35%{?dist}
Summary:    The Chinese PinYin and Bopomofo conversion library
License:    LGPL-2.1-or-later
URL:        http://code.google.com/p/pyzy
Source0:    http://pyzy.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:    http://pyzy.googlecode.com/files/pyzy-database-1.0.0.tar.bz2
Patch0:     pyzy-0.1.0-fixes-compile.patch
Patch1:     pyzy-0.1.0-port-to-python3.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  python3

# both android db and open phrase db are data files for pyzy, either one can be installed to provide pyzy-db.
Requires:   pyzy-db = %{version}-%{release}
Obsoletes:  ibus-pinyin-db-android
Provides:   ibus-pinyin-db-android
Obsoletes:  ibus-pinyin-db-open-phrase
Provides:   ibus-pinyin-db-open-phrase

%description
The Chinese Pinyin and Bopomofo conversion library.

%package    devel
Summary:    Development tools for pyzy
Requires:   %{name} = %{version}-%{release}
Requires:   glib2-devel

%description devel
The pyzy-devel package contains the header files for pyzy.

%package    db-open-phrase
Summary:    The open phrase database for pyzy
BuildArch:  noarch
Provides:   pyzy-db

%description db-open-phrase
The phrase database for pyzy from open-phrase project.

%package    db-android
Summary:    The android phrase database for pyzy
BuildArch:  noarch
Provides:   pyzy-db

%description db-android
The phrase database for pyzy from android project.

%prep
%autosetup -p1
cp -p %{SOURCE1} data/db/open-phrase

%build
%configure --disable-static --enable-db-open-phrase
# make -C po update-gmo
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README
%{_libdir}/lib*.so.*
%{_datadir}/pyzy/phrases.txt
%{_datadir}/pyzy/db/create_index.sql
%dir %{_datadir}/pyzy
%dir %{_datadir}/pyzy/db

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files db-open-phrase
%{_datadir}/pyzy/db/open-phrase.db

%files db-android
%{_datadir}/pyzy/db/android.db

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May  8 2023 Peng Wu <pwu@redhat.com> - 0.1.0-30
- Migrate to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Peng Wu <pwu@redhat.com> - 0.1.0-24
- Use Python 3
- Add pyzy-0.1.0-port-to-python3.patch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Peng Wu <pwu@redhat.com> - 0.1.0-19
- Use python2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Peng Wu <pwu@redhat.com> - 0.1.0-14
- Add python2 BuildRequires

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Peng Wu <pwu@redhat.com> - 0.1.0-11
- Fixes compile

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Peng Wu <pwu@redhat.com> - 0.1.0-6
- Obsoletes ibus-pinyin-db

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Peng Wu <pwu@redhat.com> - 0.1.0-4
- Minor fixes.

* Thu Dec 13 2012 Peng Wu <pwu@redhat.com> - 0.1.0-3
- Improves spec file.

* Tue Dec 11 2012 Peng Wu <pwu@redhat.com> - 0.1.0-2
- Fixes spec file.

* Fri Aug 08 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.0-1
- The first version.
