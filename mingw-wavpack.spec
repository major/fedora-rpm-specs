%{?mingw_package_header}

Name:           mingw-wavpack
Version:        5.5.0
Release:        3%{?dist}
Summary:        Completely open audiocodec

License:        BSD
URL:            http://www.wavpack.com/
Source:         http://www.wavpack.com/wavpack-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.


%package -n mingw32-wavpack
Summary:        %{summary}

%description -n mingw32-wavpack
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack library for the Win32 target.


%package -n mingw32-wavpack-tools
Summary:        %{summary} tools
Requires:       mingw32-wavpack = %{version}-%{release}

%description -n mingw32-wavpack-tools
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack tools for the Win32 target.


%package -n mingw64-wavpack
Summary:        %{summary}

%description -n mingw64-wavpack
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack library for the Win64 target.


%package -n mingw64-wavpack-tools
Summary:        %{summary} tools
Requires:       mingw64-wavpack = %{version}-%{release}

%description -n mingw64-wavpack-tools
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack tools for the Win64 target.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n wavpack-%{version}


%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}
# remove libtool files
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
# remove documentation (it's in the native version)
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw64_mandir}

%files -n mingw32-wavpack
%doc AUTHORS
%license COPYING
%dir %{mingw32_includedir}/wavpack
%{mingw32_bindir}/libwavpack-1.dll
%{mingw32_includedir}/wavpack/*.h
%{mingw32_libdir}/pkgconfig/*
%{mingw32_libdir}/libwavpack.dll.a

%files -n mingw32-wavpack-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-wavpack
%doc AUTHORS
%license COPYING
%dir %{mingw64_includedir}/wavpack
%{mingw64_bindir}/libwavpack-1.dll
%{mingw64_includedir}/wavpack/*.h
%{mingw64_libdir}/pkgconfig/*
%{mingw64_libdir}/libwavpack.dll.a

%files -n mingw64-wavpack-tools
%{mingw64_bindir}/*.exe


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 František Dvořák <valtri@civ.zcu.cz> - 5.5.0-1
- Update to 5.5.0
- Security fix for CVE-2022-2476

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 František Dvořák <valtri@civ.zcu.cz> - 5.4.0-5
- Security fix for CVE-2021-44269

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 5.4.0-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 14 2021 František Dvořák <valtri@civ.zcu.cz> - 5.4.0-1
- Update to 5.4.0
- Security fix for CVE-2020-35738

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 František Dvořák <valtri@civ.zcu.cz> - 5.1.0-9
- Autosetup macro
- Security fix for CVE-2018-10536, CVE-2018-10537, CVE-2018-10538,
  CVE-2018-10539, CVE-2018-10540
- Security fix for CVE-2018-19840, CVE-2018-19841
- Security fix for CVE-2019-11498, CVE-2019-1010315
- Security fix for CVE-2019-1010319
- Security fix for CVE-2019-1010317

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.1.0-8
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 František Dvořák <valtri@civ.zcu.cz> - 5.1.0-4
- Security fix for CVE-2018-6767, CVE-2018-7253, and CVE-2018-7254

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 David King <amigadave@amigadave.com> - 5.1.0-1
- Update to 5.1.0 (#1420680)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.80.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 21 2016 David King <amigadave@amigadave.com> - 4.80.0-1
- Update to 4.80.0 (#1329173)
- Use license macro for COPYING

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.70.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 František Dvořák <valtri@civ.zcu.cz> - 4.70.0-1
- New release 4.70.0
- %%mingw_make_install macro deprecated

* Wed Feb 12 2014 František Dvořák <valtri@civ.zcu.cz> - 4.60.1-1
- Initial package
