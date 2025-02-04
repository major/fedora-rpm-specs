# Issues filed:
# https://github.com/neuronsimulator/iv/issues/14: -Wstrict-aliasing
# https://github.com/neuronsimulator/iv/issues/15: -Wchar-subscript


%global commit 14890c412662cd7d0c4bce1d777473a904168647
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global checkout_date 20200818

Name:           iv
Version:        0.1
Release:        0.12.%{checkout_date}git%{shortcommit}%{?dist}
Summary:        InterViews graphical library

License:  MIT
URl:      https://github.com/neuronsimulator/%{name}
Source0:  https://github.com/neuronsimulator/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Mark libraries and let them be installed in the correct default folder
# https://github.com/neuronsimulator/iv/pull/34
Patch0:   0001-Set-soversion-for-shared-objects-on-Linux-builds.patch
Patch1:   0002-Use-LIB_INSTALL_DIR-instead-of-hardcoding-lib.patch
# Avoid function pointers of unspecified arguments
# https://github.com/neuronsimulator/iv/pull/53
#
# Fixes:
#
# iv: FTBFS in Fedora rawhide/f42
# https://bugzilla.redhat.com/show_bug.cgi?id=2300528
Patch2:   %{url}/pull/53.patch

BuildRequires:  cmake
BuildRequires:  /usr/bin/libtoolize
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  xorg-x11-server-devel
BuildRequires:  libXext-devel
BuildRequires:  libXcomposite-devel
# Is built against a bundled version, does not provide its libraries etc.
# https://github.com/neuronsimulator/iv/issues/3
Provides: bundled(libtiff) = 3.00

# for %%{_datadir}/X11/app-defaults
Requires: libXt

%description
The InterViews graphical library used by NEURON.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit} -S git

# Remove the rpath helper
sed -i '/RpathHelper/ d' CMakeLists.txt

# Remove spurious executable permission
chmod -x README Copyright

# remove scripts
find . -name "_gendefs" -delete


%build
%cmake \
-DIV_ENABLE_SHARED=ON

%cmake_build


%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -delete

# Don't install these, we don't want anyone using them
rm -vrf $RPM_BUILD_ROOT/%{_includedir}/TIFF

# Move file to right folder
install -pm 0755 -d $RPM_BUILD_ROOT/%{_datadir}/X11/
mv -v $RPM_BUILD_ROOT/%{_datadir}/app-defaults  $RPM_BUILD_ROOT/%{_datadir}/X11/

# remove stray makefile
rm -f $RPM_BUILD_ROOT/%{_includedir}/Makefile.in
rm -rf $RPM_BUILD_ROOT/%{_includedir}/IV-{Win,Mac}

# correctly set up shared dirs
pushd $RPM_BUILD_ROOT/%{_libdir}/
    ln -sv ./libinterviews.so.0.0.0 libinterviews.so.0
    ln -sv ./libunidraw.so.0.0.0 libunidraw.so.0
popd

%files
%license Copyright
%doc README
%{_libdir}/libinterviews.so.0.0.0
%{_libdir}/libinterviews.so.0
%{_libdir}/libunidraw.so.0.0.0
%{_libdir}/libunidraw.so.0
%{_datadir}/X11/app-defaults/
%{_bindir}/idemo
%{_bindir}/iclass
%{_bindir}/idraw

%files devel
%{_includedir}/Dispatch/
%{_includedir}/IV-2_6/
%{_includedir}/IV-X11/
%{_includedir}/IV-look/
%{_includedir}/InterViews/
%{_includedir}/OS/
%{_includedir}/Unidraw/
%{_includedir}/ivcarbon.h
%{_includedir}/ivmcw.h
%{_includedir}/ivstream.h
%{_includedir}/ivversion.h
%{_includedir}/macivdef.h
%{_libdir}/libinterviews.so
%{_libdir}/libunidraw.so
%{_libdir}/cmake/iv/

%changelog
* Sun Feb 02 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1-0.12.20200818git14890c4
- Updated C23 patch

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.11.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.8.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.7.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.5.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.3.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.20200818git14890c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1-0.1.20200818git14890c4
- Update to latest upstream snapshot
- move to cmake

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20191117git08c48bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191117git08c48bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.1.20191117git08c48bb
- Update as per review comments
- Update to latest upstream commit: fixes -Wsequence-point
- Update to latest upstream commit: fixes library dependencies
- Correct location of app-info file and add Requires
- Improve find command
- Remove license from devel
- File compilation warning issues and note them as comments

* Wed Nov 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.0.20191106git74f1207
- Initial rpm build
