Name:           dmtx-utils
Version:        0.7.6
Release:        11%{?dist}.1
Summary:        Tools for working with Data Matrix 2D bar-codes

License:        LGPLv2+
# http://www.libdmtx.org/ doesn't work any more
# outdated info is still at http://libdmtx.sourceforge.net/
URL:            https://github.com/dmtx
Source0:        https://github.com/dmtx/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(Wand)
BuildRequires: make

Provides:       libdmtx-utils = %{version}-%{release}
Obsoletes:      libdmtx-utils < 0.7.4


%description
libdmtx is open source software for reading and writing Data Matrix 2D
bar-codes on Linux, Unix, OS X, Windows, and mobile devices. At its core
libdmtx is a shared library, allowing C/C++ programs to use its capabilities
without restrictions or overhead.

The included utility programs, dmtxread and dmtxwrite, provide the official
interface to libdmtx from the command line, and also serve as a good reference
for programmers who wish to write their own programs that interact with
libdmtx.


%prep
%autosetup -p1

./autogen.sh


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING COPYING.LESSER
%doc AUTHORS ChangeLog KNOWNBUG README README.linux TODO
%{_bindir}/dmtx*
%{_mandir}/man1/dmtx*.1*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.6-9.1
- rebuild for new ImageMagick

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 0.7.6-3
- Rebuild for new ImageMagick 6.9.10

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Dan Horák <dan@danny.cz> - 0.7.6-1
- updated to 0.7.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Michael Cronenworth <mike@cchtml.com> - 0.7.4-8
- Rebuild for new ImageMagick

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 0.7.4-7
- Rebuild for ImageMagick 6 reversion, drop ImageMagick 7 patch

* Fri Aug 25 2017 Michael Cronenworth <mike@cchtml.com> - 0.7.4-6
- Rebuild for new ImageMagick

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Kevin Fenzi <kevin@scrye.com> - 0.7.4-4
- Rebuild for new ImageMagick

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar  6 2017 Dan Horák <dan@danny.cz> - 0.7.4-2
- add BR: gcc

* Fri Mar  3 2017 Dan Horák <dan@danny.cz> - 0.7.4-1
- initial Fedora version
