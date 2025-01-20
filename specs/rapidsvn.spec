%global commit 3a564e071c3c792f5d733a9433b9765031f8eed0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rapidsvn
Version:        0.13.0
Release:        0.20220209git%{shortcommit}%{?dist}
Summary:        Graphical interface for the Subversion revision control system

License:        GPL-3.0-or-later
URL:            http://www.rapidsvn.org/

Source0:        https://github.com/RapidSVN/RapidSVN/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         wxwidgets3.2.patch

# Has to be a manual requirement, because the library version appears to not
# be being bumped upstream on API changes - well, at least RapidSVN 0.9.2
# has unresolved symbols if run against svncpp from the 0.9.1 distribution
Requires:       svncpp = %{version}

BuildRequires: make
BuildRequires:  apr-devel, apr-util-devel
BuildRequires:  libtool >= 1.4.2
BuildRequires:  openldap-devel

# For doc generation; rapidsvn needs the "dot" tool from graphviz
BuildRequires:  docbook-style-xsl >= 1.58.1, doxygen, libxslt >= 1.0.27
BuildRequires:  graphviz

BuildRequires:  wxGTK-devel
BuildRequires:  desktop-file-utils

%description
RapidSVN is a GUI front-end for the Subversion revision control system. It
allows access to most of the features of Subversion through a user-friendly
interface.

%package -n svncpp
Summary:        C++ bindings for the Subversion client library
License:        LGPL-3.0-or-later
BuildRequires:  gcc-c++
BuildRequires:  subversion-devel
# for test framework
BuildRequires:  cppunit-devel
BuildRequires:  gettext
Requires:       subversion

%description -n svncpp
svncpp is a C++ wrapper for the C Subversion client library which abstracts
many parts of the C API and provides an object-oriented programming interface.

%package -n svncpp-devel
Summary:        Development resources for the 'svncpp' library
License:        LGPL-3.0-or-later
Requires:       svncpp = %{version}-%{release}

%description -n svncpp-devel
Development resources for the 'svncpp' C++ client library for Subversion.
Install this package if you need to compile an application that requires the
'svncpp' library.

%prep
%autosetup -n RapidSVN-%{commit}

%{__cat} <<EOF >rapidsvn.desktop
[Desktop Entry]
Encoding=UTF-8
Name=RapidSVN
GenericName=Subversion client
Comment=Manage Subversion repositories
Exec=rapidsvn
Icon=rapidsvn
Terminal=false
Type=Application
Categories=Development;GNOME;GTK;RevisionControl;
Version=0.9.4
EOF

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"

# The upstream Makefile is currently set up for OS/X and tries to use an old
# version of Python-native msgfmt.py, which doesn't work with Python3. Instead,
# we switch back to using the gettext version of 'msgfmt'
sed -i s/\#MSGFMT=msgfmt/MSGFMT=msgfmt/ librapidsvn/src/locale/Makefile.am
sed -i '/MSGFMT=python/d' librapidsvn/src/locale/Makefile.am


./autogen.sh
%configure \
        --disable-static \
        --with-svn-lib=%{_libdir} \
        --with-apu-config=%{_bindir}/apu-1-config \
        --with-apr-config=%{_bindir}/apr-1-config \
        --with-docbook-xsl-manpages=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl \
        --includedir=%{_includedir}/svncpp

make %{?_smp_mflags} LIBTOOL=/usr/bin/libtool

pushd doc/manpage
make manpage
popd

%install
make install DESTDIR=%{buildroot} LIBTOOL=/usr/bin/libtool

# Install desktop file and icon
%{__install} -D -m 644 librapidsvn/src/res/bitmaps/rapidsvn_128x128.png %{buildroot}%{_datadir}/pixmaps/rapidsvn.png
%{__install} -d -m 755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        rapidsvn.desktop

# Install manpage
%{__install} -D -m 644 doc/manpage/rapidsvn.1 %{buildroot}%{_mandir}/man1/rapidsvn.1

# Remove libtool stuff
rm -f %{buildroot}%{_libdir}/librapidsvn.{a,la}
rm -f %{buildroot}%{_libdir}/libsvncpp.{a,la}

# Can't see any meaningful use for this
rm -f %{buildroot}%{_libdir}/librapidsvn.so

%find_lang %{name}

%check
# Tests seem to be incomplete/not readily executable at present
#pushd libsvncpp/tests/
#sed -i s~/home/brent/dev/rapidsvn/~%{buildroot}~
#make
#./svncpptest | grep OK		
#if [ $? != 0 ]; then	
#    echo "svncpp tests failed"
#    exit 5
#fi


%ldconfig_scriptlets -n svncpp

%files -f %{name}.lang
%doc AUTHORS CHANGES FDL.txt GPL.txt LICENSE.txt README
%{_bindir}/rapidsvn
%{_libdir}/librapidsvn.so.*
%{_datadir}/applications/*rapidsvn.desktop
%{_datadir}/pixmaps/rapidsvn.png
%{_mandir}/man1/*

%files -n svncpp
%doc LGPL.txt
%{_libdir}/libsvncpp.so.4*

%files -n svncpp-devel
%doc doc/svncpp/html
%{_includedir}/svncpp/
%{_libdir}/libsvncpp.so

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20220209git3a564e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20220208git3a564e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.13.0-1.20220207git3a564e0
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20220207git3a564e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20220206git3a564e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20220205git3a564e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20220204git3a564e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 0.13.0-0.20220203git3a564e0
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20220202git3a564e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Tim Jackson <rpm@timj.co.uk> - 0.13.0-0.20220201git3a564e0
- Bring in some minor upstream fixes
- Rebuild for OpenLDAP 2.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181134git1b6dfc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181133git1b6dfc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181132git1b6dfc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181131git1b6dfc1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181130git1b6dfc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.13.0-0.20181129git1b6dfc1
- Force C++14 as this code is not C++17 ready

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181128git1b6dfc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181127git1b6dfc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.20181126git1b6dfc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.13.0-0.20181125git1b6dfc1
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Nov 24 2018 Tim Jackson <rpm@timj.co.uk> - 0.13.0-0.20181124git1b6dfc1
- Update to latest upstream snapshot; fixes (amongst other things) FTBFS rhbz #1606076
- Now uses wxGTK3
- libsvncpp is now LGPLv3+
- Fix build for F-30 with python3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Tim Jackson <rpm@timj.co.uk> - 0.12.1-14
- Add missing BuildRequire on gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.12.1-12
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.12.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 0.12.1-2
- Drop desktop vendor tag.

* Mon Feb 18 2013 Tim Jackson <rpm@timj.co.uk>
- Update to 0.12.1. Fixes crashes.
- Remove BuildRoot

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.12.0-2
- rebuilt against wxGTK-2.8.11-2

* Sat Nov 28 2009 Tim Jackson <rpm@timj.co.uk> 0.12.0-1
- Update to v0.12.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Tim Jackson <rpm@timj.co.uk> 0.10.0-1
- Update to v0.10.0
- Set default attrs for subpackages

* Tue Apr 14 2009 Tim Jackson <rpm@timj.co.uk> 0.9.8-1
- Update to v0.9.8
- License is now GPLv3+
- Update .desktop file categories (#487867)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 07 2008 Tim Jackson <rpm@timj.co.uk> 0.9.6-3
- Add missing BR on openldap-devel

* Tue Jun 03 2008 Tim Jackson <rpm@timj.co.uk> 0.9.6-2
- Fix spec file to build using latest RPM version
- Remove filename suffix from icon in desktop file as per standards

* Tue Mar 11 2008 Tim Jackson <rpm@timj.co.uk> 0.9.6-1
- Update to upstream 0.9.6 (#436157)
- Fix build on gcc 4.3 (#434474)
- Update License tags

* Mon Sep  3 2007 Joe Orton <jorton@redhat.com> 0.9.4-6
- rebuild for fixed 32-bit APR

* Thu Aug 23 2007 Joe Orton <jorton@redhat.com> 0.9.4-5
- don't link against neon directly

* Sat Dec 30 2006 Tim Jackson <rpm@timj.co.uk> 0.9.4-3
- Apply patches to build against wxGTK 2.8

* Sat Dec 30 2006 Tim Jackson <rpm@timj.co.uk> 0.9.4-3
- Rebuild for new wxGTK

* Sat Dec 09 2006 Tim Jackson <rpm@timj.co.uk> 0.9.4-2
- Nasty dist tag conflict (fc6 in devel)

* Sat Dec 09 2006 Tim Jackson <rpm@timj.co.uk> 0.9.4-1
- Update to 0.9.4
- Use new RapidSVN desktop icon

* Sat Sep 09 2006 Tim Jackson <rpm@timj.co.uk> 0.9.3-2
- Rebuild for FE6

* Fri Jun 23 2006 Tim Jackson <rpm@timj.co.uk> 0.9.3-1
- Update to 0.9.3
- Remove gcc4 patch; now fixed upstream

* Tue May 30 2006 Tim Jackson <rpm@timj.co.uk> 0.9.2-1
- Update to 0.9.2
- Add explicit dep on svn-cpp = [rapidsvn ver]

* Wed May 03 2006 Tim Jackson <rpm@timj.co.uk> 0.9.1-3
- libtool hack to fix RPATH issue

* Sat Apr 29 2006 Tim Jackson <rpm@timj.co.uk> 0.9.1-2
- Update list of docs inc. add GPL, LGPL docs and LICENSE.txt
- Remove autoconf from BR
- Fix manpage generation and add manpage to package
- Add graphviz BR for correct doc generation
- Add --disable-no-exceptions per README
- Use --disable-static since we don't use the static libs
- Spin off svncpp and svncpp-devel subpackages
- svncpp has ldconfig in post/postun
- Add --with-svn-lib which should fix build on x86_64
- Add %%check section using package's inbuilt tests (requires cppunit)

* Thu Apr 27 2006 Tim Jackson <rpm@timj.co.uk> 0.9.1-1
- Initial package for Fedora Extras; based originally on an old DAG spec
