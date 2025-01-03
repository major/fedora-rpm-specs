Name:           pocketsphinx
Epoch:          2
Version:        5.0.3
Release:        6%{?dist}
Summary:        Real-time speech recognition

License:        BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://cmusphinx.github.io/
Source0:        https://github.com/cmusphinx/pocketsphinx/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-scikit-build

Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-models

%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%package devel
Summary:        Header files for developing with pocketsphinx
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(jquery)

%description devel
Header files for developing with pocketsphinx.

%package libs
Summary:        Shared libraries for pocketsphinx executables

%description libs
Shared libraries for pocketsphinx executables.

%package models
Summary:        Voice and language models for pocketsphinx
BuildArch:      noarch

%description models
Voice and language models for pocketsphinx.

%package plugin
Summary:        Pocketsphinx gstreamer plugin
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gstreamer1-plugins-base%{?_isa}

%description plugin
A gstreamer plugin for pocketsphinx.

%package -n python3-pocketsphinx
%{?python_provide:%python_provide python3-pocketsphinx}
Summary:        Python interface to pocketsphinx
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-pocketsphinx
Python interface to pocketsphinx.

%prep
%autosetup -p1

%build
# Build twice for Python and C (also below in install section).
# See https://github.com/cmusphinx/pocketsphinx/issues/342.
# CMAKE_MODULE_PATH is to find FindPythonExtensions.cmake from python3-scikit-build.
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_MODULE_PATH="%{python3_sitelib}/skbuild/resources/cmake" \
	-DSKBUILD="on" \
%cmake_build
mv redhat-linux-build redhat-linux-build-python
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DBUILD_GSTREAMER="on"
%cmake_build

%install
# Install twice for Python and C.
# See https://github.com/cmusphinx/pocketsphinx/issues/342.
%cmake_install
rm -rf redhat-linux-build
mv redhat-linux-build-python redhat-linux-build
%cmake_install

# See https://github.com/cmusphinx/pocketsphinx/issues/341
mkdir -p $RPM_BUILD_ROOT%{python3_sitearch}
mv $RPM_BUILD_ROOT/%{_prefix}/%{name}/* $RPM_BUILD_ROOT%{python3_sitearch}

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%doc AUTHORS NEWS README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files models
%{_datadir}/%{name}/

%files plugin
%{_libdir}/gstreamer-1.0/*

%files -n python3-pocketsphinx
%{python3_sitearch}/*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2:5.0.3-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:5.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2:5.0.3-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon May 15 2023 W. Michael Petullo <mike@flyn.org> - 5.0.3-1
- Update to 5.0.3
- Drop upstreamed patch

* Mon May 15 2023 W. Michael Petullo <mike@flyn.org> - 5.0.0-3
- Backport upstream s390x patch

* Mon May 15 2023 W. Michael Petullo <mike@flyn.org> - 5.0.0-3
- Replace use of patches after talking to upstream

* Mon May 15 2023 W. Michael Petullo <mike@flyn.org> - 5.0.0-2
- Exclude s390x
- Add commentary for patches

* Mon May 15 2023 W. Michael Petullo <mike@flyn.org> - 5.0.0-1
- Update to 5.0.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.13.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.12.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:5-0.11.prealpha
- Rebuilt for Python 3.11

* Fri Feb 11 2022 W. Michael Petullo <mike@flyn.org> - 1:5-0.10.prealpha
- Patch to remove stdbool.h conflict (BZ #2049655)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.9.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.8.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:5-0.7.prealpha
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.6.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.5.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:5-0.4.prealpha
- Rebuilt for Python 3.9

* Wed May 13 2020 W. Michael Petullo <mike@flyn.org> - 1:5-0.3.prealpha
- Fix incorrect version after incrementing the wrong number

* Wed May 13 2020 W. Michael Petullo <mike@flyn.org> - 1:6-0.2.prealpha
- Fix GStreamer dependency for plugin package

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.2.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 W. Michael Petullo <mike@flyn.org> - 1:5-0.1.prealpha
- More work to switch to Python 3
- Adjust version convention to match un-retired sphinxbase

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5prealpha-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5prealpha-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5prealpha-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Miro Hrončok <mhroncok@redhat.com> - 5prealpha-2
- Switch to Python 3

* Sun Jul 22 2018 W. Michael Petullo <mike@flyn.org> - 5prealpha-1
- New upstream release

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-21
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-18
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-17
- Python 2 binary package renamed to python2-pocketsphinx
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Jerry James <loganjerry@gmail.com> - 0.8-12
- Support long utterances (bz 1356809)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Jerry James <loganjerry@gmail.com> - 0.8-9
- Rebuild for sphinxbase linked with atlas
- Add Provides: bundled(jquery)
- Minor spec file cleanups

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep  5 2013 Jerry James <loganjerry@gmail.com> - 0.8-6
- Split the voice and language models into a noarch subpackage due to size

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Jerry James <loganjerry@gmail.com> - 0.8-4
- Different approach to the -largefile patch to fix problems with the original
- Drop -aarch64 patch since we now run autoreconf
- Add -doxygen patch to fix broken doxygen comments

* Thu Mar 28 2013 Jerry James <loganjerry@gmail.com> - 0.8-3
- Add -largefile patch for large file support
- Add -aarch64 patch (bz 926360)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jerry James <loganjerry@gmail.com> - 0.8-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 0.7-4
- Rebuild for bz 772699
- New project URL

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.7-3
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Fri Jul 15 2011 Jerry James <loganjerry@gmail.com> - 0.7-2
- Use RPM 4.9's new filter scheme to remove bogus provides
- Minor spec file cleanups

* Tue Apr 19 2011 Jerry James <loganjerry@gmail.com> - 0.7-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- New upstream release
- All sources are now BSD

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Nov 20 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-4
- Update python BRs for Rawhide

* Fri Aug 21 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-3
- More review issues:
- Fix license (gstreamer plugin is LGPLv2+)
- Remove unnecessary zero-byte turtle dictionary file

* Fri Aug 21 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-2
- Fix issues raised in review by Andrew Colin Kissa, namely:
- Improve description and summary
- Change the group to Applications/Multimedia

* Tue Mar 24 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Jul 10 2008 Jerry James <loganjerry@gmail.com> - 0.5-1
- Update to 0.5

* Wed Mar  5 2008 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- Initial RPM
