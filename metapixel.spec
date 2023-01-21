Summary: Photomosaic Generator
Name: metapixel
Version: 1.0.2
Release: 19%{?dist}
License: GPLv2 and LGPLv2+
URL: http://www.complang.tuwien.ac.at/schani/metapixel/
Source: http://www.complang.tuwien.ac.at/schani/%{name}/files/%{name}-%{version}.tar.gz

Requires: perl-interpreter
BuildRequires:  gcc
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: giflib-devel
BuildRequires: make
BuildRequires: perl-generators

Patch0:	metapixel-build-fixes.patch
Patch1: metapixel-copyright.patch
Patch2: metapixel-install.patch
# giflib-5.x compatibility
Patch3: metapixel-giflib5.patch

%description
A program for generating photomosaics.  It can generate classical 
photomosaics, in which the source image is viewed as a matrix of equally sized 
rectangles for each of which a matching image is substituted, as well as 
collage-style photomosaics, in which rectangular parts of the source image 
at arbitrary positions (i.e. not aligned to a matrix) are substituted by 
matching images.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make PREFIX=$RPM_BUILD_ROOT/usr install

%files
%doc NEWS README
%license COPYING
%{_mandir}/man1/metapixel.1*
%{_bindir}/metapixel-prepare
%{_bindir}/metapixel
%{_bindir}/metapixel-imagesize
%{_bindir}/metapixel-sizesort

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.0.2-9
- Rebuild (giflib)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.0.2-5
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Neil Horman <nhorman@tuxdriver.com> - 1.0.2-2
- Various fixes for fedora review

* Wed Aug 26 2015 Neil Horman <nhorman@tuxdriver.com> - 1.0.2-1
- Initial import
 
