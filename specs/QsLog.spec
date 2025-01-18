%global commit 2959cec27825e53d1554a32668f1f7892ca351c7
%global medcommit %(c=%{commit}; echo ${c:0:12})
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           QsLog
Version:        0
Release:        30.%{shortcommit}git%{?dist}
Summary:        An easy to use logger that is based on Qt's QDebug class
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://bitbucket.org/razvanpetru/qslog

Source0:        https://bitbucket.org/razvanpetru/qslog/get/%{shortcommit}.tar.gz

# Don't install docs
Patch0:         QsLog-nodoc.patch
# Install libraries in correct directory
Patch1:         QsLog-libdir.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel

%description
QsLog is an easy to use logger that is based on Qt's QDebug class.
Features:
* Six logging levels (from trace to fatal)
* Logging level threshold configurable at runtime.
* Minimum overhead when logging is turned off.
* Supports multiple destinations, comes with file and debug destinations.
* Thread-safe
* Supports logging of common Qt types out of the box.
 
%package devel
Summary:         Development headers and library for QsLog
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and libraries necessary
for compiling against QsLog.

%prep
%setup -q -n razvanpetru-qslog-%{medcommit}
%patch -P0 -p1 -b .nodoc
%patch -P1 -p1 -b .libdir
# Prepare LICENSE
head -n 25 QsLog.cpp | sed "s|// ||g" > LICENSE
touch -r QsLog.cpp LICENSE

# Fix EOL encoding
for f in QsLog.h QsLogDestConsole.h QsLogLevel.h QsLogDest.h LICENSE; do
    sed 's|\r||g' $f > $f.new && \
    touch -r $f $f.new && \
    mv $f.new $f
done

%build
%qmake_qt4 QsLogSharedLibrary.pro
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%doc LICENSE QsLogReadme.txt
%{_libdir}/libQsLog.so.*

%files devel
%{_includedir}/QsLog/
%{_libdir}/libQsLog.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-30.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0-29.2959cecgit
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-28.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-21.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-14.2959cecgit
- Added gcc-c++ buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0-9.2959cecgit
- use %%qmake_qt4 macro to ensure proper build flags

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-8.2959cecgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-7.2959cecgit
- Rebuilt for GCC 5 C++11 ABI change

* Wed Aug 20 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-6.2959cecgit
- Update to newest snapshot.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-6.54hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.54hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Dan Horák <dan[at]danny.cz> - 0-4.54hg
- Bump rev and rebuild, fixes build on secondary arches

* Thu Jan 02 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-3.54hg
- Review fixes.

* Thu Jan 02 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-2.54hg
- Generate LICENSE from source.

* Wed Dec 18 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-1.54hg
- First release.
