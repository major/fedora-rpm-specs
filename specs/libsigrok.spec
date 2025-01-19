Name:           libsigrok
Version:        0.5.2
Release:        15%{?dist}
Summary:        Basic hardware access drivers for logic analyzers
# Combined GPLv3+ and GPLv2+ and BSD
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org/
Source0:        http://sigrok.org/download/source/libsigrok/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1877485
# https://sigrok.org/gitweb/?p=libsigrok.git;a=commit;h=3decd3b1f0cbb3a035f72e9eade42279d0507b89
Patch0:         libsigrok-0.5.2-lto.patch

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  glibmm24-devel
BuildRequires:  libzip-devel
BuildRequires:  zlib-devel
BuildRequires:  libieee1284-devel
BuildRequires:  libusb1-devel
BuildRequires:  libftdi-devel
BuildRequires:  libserialport-devel     >= 0.1.1
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libtirpc-devel
BuildRequires: make

%description
%{name} is a shared library written in C which provides the basic API
for talking to hardware and reading/writing the acquired data into various
input/output file formats.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        cxx
Summary:        C++ bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    cxx
The %{name}-cxx package contains C++ libraries for %{name}.

%package        cxx-devel
Summary:        Development files for  %{name} C++ bindings
Requires:       %{name}-cxx%{?_isa} = %{version}-%{release}

%description    cxx-devel
The %{name}-cxx-devel package contains libraries and header files for
developing applications that use %{name} C++ bindings.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for developing software
with %{name}.


%prep
%autosetup -p1
# Upstream thinks it's a good idea to have two udev files. We disagree.
sed -e 's/ENV{ID_SIGROK}="1"/TAG+="uaccess"/g' contrib/60-libsigrok.rules -i


%build
# --disable-gpib: Fedora doesn't ship libgpib
# --disable-python: We don't package python bindings because they are a PITA
#                   for maintainers and are pretty horrible and useless anyway
# --disable-java: Be explicit rather than rely on missing java-devel
# --disable-ruby: Be explicit rather than rely on missing ruby-devel
%configure --disable-static --disable-python --disable-gpib --disable-java --disable-ruby CPPFLAGS=-I/usr/include/tirpc LDFLAGS=-ltirpc
make %{?_smp_mflags} V=1

# Doxygen produces different output based on the build arch. This will make
# our builds fail since -doc is a noarch package.
echo "Documentation not packaged in this version" > README.fedora


%install
%make_install
# Install udev rules
install -D -p -m 0644 contrib/60-libsigrok.rules %{buildroot}%{_udevrulesdir}/60-libsigrok.rules

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README README.devices NEWS COPYING
%{_libdir}/libsigrok.so.4*
%{_udevrulesdir}/60-libsigrok.rules

# TODO: What are we supposed to do with these icons and MIME types?
%exclude %{_datadir}/icons/hicolor/48x48/mimetypes/libsigrok.png
%exclude %{_datadir}/icons/hicolor/scalable/mimetypes/libsigrok.svg
%exclude %{_datadir}/mime/packages/vnd.sigrok.session.xml

%files devel
%{_includedir}/libsigrok/
%{_libdir}/libsigrok.so
%{_libdir}/pkgconfig/libsigrok.pc

%files cxx
%{_libdir}/libsigrokcxx.so.4*

%files cxx-devel
%{_includedir}/libsigrokcxx/
%{_libdir}/libsigrokcxx.so
%{_libdir}/pkgconfig/libsigrokcxx.pc

%files doc
%doc README.fedora


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.2-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Dan Horák <dan[at]danny.cz> - 0.5.2-4
- fix build with LTO (#1877485)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Dan Horák <dan[at]danny.cz> - 0.5.2-1
- update to libsigrok 0.5.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Dan Horák <dan[at]danny.cz> - 0.5.1-3
- build with libtirpc to enable VXI (#1724865)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 mrnuke <mr.nuke.me@gmail.com> - 0.5.1-1
- New and excitinf libsigrok-0.5.1 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Alexandru Gagniu <mr.nuke.me@gmail.com> - 0.5.0-1
- Update to libsigrok 0.5.0

* Tue Feb 28 2017 Remi Collet <remi@fedoraproject.org> - 0.4.0-3
- rebuild for new libzip

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.4.0-1
- "cxx-devel" subpackage "Requires" libsigrok-cxx, not libsigrok
- Add "post" and "postun" steps for "cxx" subpackage

* Sat Feb 06 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.4.0-0
- Update to libsigrok 0.4.0
- Convert GROUP="plugdev" udev rules to TAG+="uaccess" using sed
- Add "cxx" and "cxx-devel" packages for C++ bindings.
- Add minimum version (0.1.1) for libserialport-devel package
- Add libieee1284-devel dependency for "hung-chang-dso-2100" driver
- Remove autoreconf step, as it is no longer needed

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.3.0-4
- Fix used rules to use "uaccess" tag instead of "plugdev" group

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 0.3.0-2
- rebuild for new libzip

* Sat Sep 20 2014 Dan Horák <dan[at]danny.cz> - 0.3.0-1
- update to libsigrok 0.3.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Dan Horák <dan[at]danny.cz> - 0.2.2-3
- rebuilt for libftdi1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 04 2013 Dan Horák <dan[at]danny.cz> - 0.2.2-1
- update to libsigrok 0.2.2

* Mon Nov 04 2013 Dan Horák <dan[at]danny.cz> - 0.2.1-4
- udev rules should react also on the usbmisc subsystem

* Sun Nov 03 2013 Dan Horák <dan[at]danny.cz> - 0.2.1-3
- scan /sys/class/usbmisc
- add support for Rigol DS1152 scopes with upgraded bandwidth
- resolves: #1025968

* Wed Aug 21 2013 Remi Collet <rcollet@redhat.com> - 0.2.1-2
- rebuild for new libzip

* Fri Aug 09 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.2.1-1
- Update to libsigrok 0.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 04 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.2.0-1
- Update to libsigrok 0.2.0 (inlcudes soname version bump)
- All working drivers are enabled by default. Don't manually enable them.
- Package provided udev rules
- Remove unneeded 'rm -rf buildroot'
- Remove unneeded 'defattr'
- Remove ChangeLog from documentation (only contains a git log)

* Wed Mar 13 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.1-3
- Drop dependency of -doc subpackage
- Use explicit soversion in files section

* Sat Dec 01 2012 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.1-2
- Add comment explaining chioce of license
- Removed  _missing_build_ids_terminate_build undef
- Add comment explaining doxygen warnings

* Wed Oct 10 2012 Alexandru Gagniuc mr.nuke.me[at]gmail[dot]com - 0.1.1-1
- Initial RPM release
