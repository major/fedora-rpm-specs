# wx-config
%global wxversion %(wx-config-3.2 --release)
%global wxincdir %{_includedir}/wx-%{wxversion}

Name:           wxsqlite3
Version:        4.10.2
Release:        1%{?dist}
Summary:        C++ wrapper around the SQLite 3.x database

License:        LGPL-3.0-or-later WITH WxWindows-exception-3.1
URL:            https://github.com/utelle/wxsqlite3
Source0:        https://github.com/utelle/wxsqlite3/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# don't %%build the included wxSQLite+ application
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  wxGTK-devel
BuildRequires:  sqlite-devel
BuildRequires:  doxygen
BuildRequires:  dos2unix
BuildRequires:  autoconf
BuildRequires:  automake


%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database and is
specifically designed for use in programs based on the wxWidgets library.
wxSQLite3 does not try to hide the underlying database, in contrary almost all
special features of the current SQLite3 version 3.6.22 are supported, like for
example the creation of user defined scalar or aggregate functions. Since
SQLite stores strings in UTF-8 encoding, the wxSQLite3 methods provide
automatic conversion between wxStrings and UTF-8 strings. This works best for
the Unicode builds of wxWidgets. In ANSI builds the current locale conversion
object (wxConvCurrent) is used for conversion to/from UTF-8. Special care has
to be taken if external administration tools are used to modify the database
contents, since not all of these tools operate in Unicode resp. UTF-8 mode.
wxSQLite3 includes an optional extension for SQLite supporting key based
database file encryption using 128 bit AES encryption. Starting with version
1.9.6 of wxSQLite3 the encryption extension is compatible with the SQLite
amalgamation source. Experimental support for 256 bit AES encryption has been
added in version 1.9.8.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       wxGTK-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation 
that use %{name}.


%prep
%autosetup -n %{name}-%{version}

# activate correct build folder
#mv build30 build

# delete bundled sqlite3 files
find -name sqlite3 -type d | xargs rm -rfv

# set correct permission
#chmod a+x configure

# fixex E: wrong-script-end-of-line-encoding
dos2unix readme.md 

# fixes W: spurious-executable-perm
find docs -type f -exec chmod a-x {} \;
chmod a-x include/wx/wxsqlite3.h src/wxsqlite3.cpp

# fixes E: script-without-shebang
chmod -x LICENCE.txt readme.md

%build
#autoreconf --install --force
autoreconf
%configure --enable-shared=yes --enable-static=no --enable-codec=chacha20 \
          --enable-codec=sqlcipher --enable-codec=rc4 --enable-codec=aes256 \
          --enable-codec=aes128
# use correct wx-config file
sed -i -e 's|WX_CONFIG_NAME=wx-config|WX_CONFIG_NAME=wx-config-3.2|g' configure

%make_build

# build docs
pushd docs
doxygen
popd

%install
%make_install INSTALL="install -p"

# move headers from /usr/include/wx to /usr/include/wx-?.?/wx
mkdir %{buildroot}%{wxincdir}
mv %{buildroot}%{_includedir}/wx %{buildroot}%{wxincdir}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# install pkgconfig file
### mkdir -p %{buildroot}%{_libdir}/pkgconfig
###mv %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc


%ldconfig_scriptlets


%files
%doc readme.md
%license LICENCE.txt
%{_libdir}/*.so.*

%files devel
%{wxincdir}/wx/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so

%files doc
%doc docs/html


%changelog
* Fri Jan 17 2025 Martin Gansser <martinkg@fedoraproject.org> 4.10.2-1
- Update to 4.10.2

* Tue Jan 07 2025 Martin Gansser <martinkg@fedoraproject.org> 4.10.1-1
- Update to 4.10.1

* Thu Jan 02 2025 Martin Gansser <martinkg@fedoraproject.org> 4.10.0-1
- Update to 4.10.0

* Wed Oct 23 2024 Martin Gansser <martinkg@fedoraproject.org> 4.9.12-1
- Update to 4.9.12

* Mon Sep 23 2024 Martin Gansser <martinkg@fedoraproject.org> - 4.9.11-3
- Migrate to SPDX license

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Martin Gansser <martinkg@fedoraproject.org> 4.9.11-1
- Update to 4.9.11

* Wed May 29 2024 Martin Gansser <martinkg@fedoraproject.org> 4.9.10-1
- Update to 4.9.10

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Martin Gansser <martinkg@fedoraproject.org> 4.8.2-6
- Update wxsqlite3.spec to enable encryption

* Fri Aug 12 2022 Martin Gansser <martinkg@fedoraproject.org> 4.8.2-5
- Use correct wx-config file in configure

* Wed Aug 10 2022 Martin Gansser <martinkg@fedoraproject.org> 4.8.2-4
- Set wxversion to 3.1 for fedora <= 36

* Mon Aug 08 2022 Martin Gansser <martinkg@fedoraproject.org> 4.8.2-3
- Set wxversion to 3.0 for fedora <= 36

* Sun Aug 07 2022 Martin Gansser <martinkg@fedoraproject.org> 4.8.2-2
- Set wxversion to 3.2 for fedora} >= 37

* Fri Aug 05 2022 Martin Gansser <martinkg@fedoraproject.org> 4.8.2-1
- Update to 4.8.2

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 4.5.1-7
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 Martin Gansser <martinkg@fedoraproject.org> 4.5.1-1
- Update to 4.5.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.10git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.9git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.8git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Martin Gansser <martinkg@fedoraproject.org> 3.4.1-0.7git91de286
- Fix FTBFS due missing BR gcc-c++ (RHBZ#1606715)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.6git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.5git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.4git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.3git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-0.2git91de286
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Martin Gansser <martinkg@fedoraproject.org> 3.4.1-0.1git91de286
- Update to 3.4.1-0.1git91de286

* Sun Aug 28 2016 Martin Gansser <martinkg@fedoraproject.org> 3.4.0-0.1git6feb9d1
- Update to 3.4.0-0.1git6feb9d1

* Sun Apr 24 2016 Martin Gansser <martinkg@fedoraproject.org> 3.3.2-0.1gitb05867d
- switched to github
- added BR doxygen
- spec file cleanup

* Sun Apr 10 2016 Martin Gansser <martinkg@fedoraproject.org> 3.3.1-1
- Update to 3.3.1
- Replaced BR wxGTK-devel by wxGTK3-devel

* Sat Feb 06 2016 Martin Gansser <martinkg@fedoraproject.org> 3.3.0-3
- Added BR dos2unix
- fixed rpmlint warnings

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Martin Gansser <martinkg@fedoraproject.org> 3.3.0-1
- Update to 3.3.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.2.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 05 2015 Martin Gansser <martinkg@fedoraproject.org> 3.2.1-1
- Update to 3.2.1

* Sun Jan 04 2015 Martin Gansser <martinkg@fedoraproject.org> 3.2.0-2
- fixed library path in pkgconfig file

* Sun Jan 04 2015 Martin Gansser <martinkg@fedoraproject.org> 3.2.0-1
- Update to 3.2.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Martin Gansser <martinkg@fedoraproject.org> 3.1.1-1
- update to 3.1.1

* Mon Jun 02 2014 Martin Gansser <martinkg@fedoraproject.org> 3.1.0-2
- dropped CXXFLAGS to avoid compiler warnings

* Wed May 28 2014 Martin Gansser <martinkg@fedoraproject.org> 3.1.0-1
- Update to 3.1.0
- added CXXFLAGS to avoid compiler warnings

* Mon Dec 9 2013 Martin Gansser <martinkg@fedoraproject.org> 3.0.6.1-1
- update to 3.0.6.1

* Mon Sep 9 2013 Martin Gansser <martinkg@fedoraproject.org> 3.0.5-1
- Update to 3.0.5

* Sun May 5 2013 Martin Gansser <martinkg@fedoraproject.org> 3.0.3-1
- Update to 3.0.3
- rebuild for new release
- Update wxsqlite3-3.0.1.pc.in to wxsqlite3-3.0.3.pc.in due lib name change

* Sat Feb 16 2013 Martin Gansser <martinkg@fedoraproject.org> 3.0.2-1
- Update to 3.0.2
- rebuild for new release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Martin Gansser <martinkg@fedoraproject.org> 3.0.1-4
- added own Debian-compatible pkgconfig file
- specfile cleanup

* Mon Dec 24 2012 Martin Gansser <martinkg@fedoraproject.org> 3.0.1-3
- added %%wx-config to determine wx version
- moved wx header files to corresponding wx-version
- removed requirement in doc section

* Sun Dec 23 2012 Martin Gansser <martinkg@fedoraproject.org> 3.0.1-2
- added wxsqlite3.pc patch for pkgconfig

* Sat Nov 24 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.1-1
- update to 3.0.1
- specfile cleanup

* Sat Oct 20 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.0.1-7
- added wxsqlite3.pc file

* Tue Oct 16 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.0.1-6
- added chmod a-x for all files 
- added chmod a+x for configure29 

* Sun Oct 14 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.0.1-5
- corrected wx include path in file section
- dropped unusual percentage symbol from doc subpackage
- deleted unecessary Requires from doc subpackage

* Sun Oct 14 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.0.1-4
- removed %%_isa requirement from doc subpackage
- added BuildArch noarch to doc subpackage
- dropped chmod for configure

* Sun Oct 14 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.0.1-3
- spec file cleanup
- dropped chmod for configure
- deleted bundled sqlite3 files
- removed %%defattr in file section becaus of no EPEL5 packaging
- corrected ownership of %%{_includedir}/wx in file section
- make install preserve timestamps
- added isa to requires tag
- improve executable flags for files in the doc folder
- separated  html files into doc subpackage

* Sun Sep 23 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.0.1-2
- removed unrecognized configure options

* Wed Sep 19 2012 Martin Gansser <linux4martin[at]gmx.de> 3.0.0.1-1
- rebuild for new release

* Tue Aug 30 2011 Dan Horák <dan[at]danny.cz> 2.1.3-1
- updated to 2.1.3

* Sat Apr 23 2011 Dan Horák <dan[at]danny.cz> 2.1.1-1
- updated to 2.1.1

* Thu Apr 14 2011 Dan Horák <dan[at]danny.cz> 2.1.0-1
- updated to 2.1.0

* Sun Dec 12 2010 Dan Horák <dan[at]danny.cz> 2.0.2-1
- updated to 2.0.2

* Mon Nov  1 2010 Dan Horák <dan[at]danny.cz> 2.0.1-1
- updated to 2.0.1

* Tue Aug 10 2010 Dan Horák <dan[at]danny.cz> 2.0.0.1-1
- updated to 2.0.0.1

* Sat Jul 24 2010 Dan Horák <dan[at]danny.cz> 2.0.0-1
- updated to 2.0.0

* Mon Mar 22 2010 Dan Horák <dan[at]danny.cz> 1.9.9-1
- updated to 1.9.9

* Sun Feb 14 2010 Dan Horák <dan[at]danny.cz> 1.9.8-1
- initial Fedora version
