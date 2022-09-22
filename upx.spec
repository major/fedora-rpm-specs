Name:           upx
Version:        3.96
Release:        12%{?dist}
Summary:        Ultimate Packer for eXecutables

License:        GPLv2+ and Public Domain
URL:            http://upx.sourceforge.net/
Source0:        http://upx.sourceforge.net/download/%{name}-%{version}-src.tar.xz
Source1:        https://github.com/upx/upx-lzma-sdk/archive/v%{version}/upx-lzma-sdk-%{version}.tar.gz
Patch0:		upx-whitespace.patch
Patch1:         upx-nohtml.patch
Patch2:         dadfd43ecb9909b0fab18e77753953a91322c628.patch
Patch3:         2fcaa16c13eda34307ccceea2263e474c54ee075.patch
Patch4:         3781df9da23840e596d5e9e8493f22666802fe6c.patch
Patch5:         87b73e5cfdc12da94c251b2cd83bb01c7d9f616c.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  ucl-devel >= 1.01
BuildRequires:  zlib-devel
BuildRequires:  perl-podlators

%description
UPX is a free, portable, extendable, high-performance executable
packer for several different executable formats. It achieves an
excellent compression ratio and offers very fast decompression. Your
executables suffer no memory overhead or other drawbacks.


%prep
%setup -qn %{name}-%{version}-src
sed -i -e 's/ -O2/ /' -e 's/ -Werror//' src/Makefile

tar xfz %{SOURCE1} --strip-components=1 -C src/lzma-sdk/

%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export CXX="g++"
export CXXFLAGS="$RPM_OPT_FLAGS" # export, not to make so it won't trump all
export UPX_LUADIR=/usr/include
export UPX_UCLDIR=/usr/include/ucl
make %{?_smp_mflags} -C src
make -C doc


%install
install -Dpm 644 doc/upx.1   $RPM_BUILD_ROOT%{_mandir}/man1/upx.1
install -Dpm 755 src/upx.out $RPM_BUILD_ROOT%{_bindir}/upx


%files
%license COPYING LICENSE
%doc BUGS NEWS PROJECTS README README.1ST THANKS
%{_bindir}/upx
%{_mandir}/man1/upx.1*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.96-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.96-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.96-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.96-9
- Patch for CVE-2020-24119

* Thu Mar 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.96-8
- Patch for CVE-2021-20285

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.96-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.96-6
- Make PE load config directory address dword aligned

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.96-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.96-4
- Patch for segfault using preserve-build-id.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.96-2
- EVR bump for koji issue.

* Fri Jan 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.96-1
- 3.96

* Fri Jan 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.95-5
- Upstream patch for CVE-2019-20021

* Thu Aug 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.95-4
- Upstream patches for CVE-2019-14295 and CVE-2019-14296.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Gwyn Ciesla <limburgher@gmail> - 3.95-1
- 3.95.
- Switch to upstream's lzma fork.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.94-1
- 3.94, plus patch for CVE-2017-15056.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.93-1
- Latest upstream, fix for BZ 1429197.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.91-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.91-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.91-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Oct 16 2014 Jon Ciesla <limburgher@gmail.com> - 3.91-4
- Fix FTBFS.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Jon Ciesla <limburgher@gmail.com> - 3.91-1
- New upstream, BZ 1023719.
- Fix bad changelog date.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Jon Ciesla <limburgher@gmail.com> - 3.09-1
- New upstream.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Jon Ciesla <limburgher@gmail.com> - 3.08-1
- New upstream.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Tom Callaway <spot@fedoraproject.org> - 3.07-3
- use lzma-sdk system library/headers

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Jon Ciesla <limb@jcomserv.net> - 3.07-1
- New upstream.

* Fri Jan 08 2010 Jon Ciesla <limb@jcomserv.net> - 3.04-2
- LZMA fixes by John Reiser (jreiser@bitwagon.com) BZ 501636.

* Mon Nov 16 2009 Jon Ciesla <limb@jcomserv.net> - 3.04-1
- 3.04.
- Stict prototype patch upstreamed.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Jon Ciesla <limb@jcomserv.net> - 3.03-3
- Patch for stricter glibc.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 08 2008 Jon Ciesla <limb@jcomserv.net> - 3.03-1
- 3.03.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 3.02-2
- GCC 4.3 rebuild.

* Mon Dec 31 2007 Jon Ciesla <limb@jcomserv.net> - 3.02-1
- 3.02.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 3.01-2
- License tag correction.

* Mon Aug 06 2007 Jon Ciesla <limb@jcomserv.net> - 3.01-1
- 3.01.

* Sun May 13 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.00-1
- 3.00.

* Wed Apr  4 2007 Ville Skyttä <ville.skytta at iki.fi> - 2.03-1
- 2.03.

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.02-1
- 2.02.

* Tue May 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.00-2
- BR: zlib-devel.

* Tue May 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.00-1
- 2.00.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.25-5
- Rebuild.

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.25-4
- Rebuild.

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.25-3
- rebuilt

* Fri Dec 17 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.25-2
- Let rpmbuild take care of stripping binaries.
- Honor build environment settings better.

* Thu Jul  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.25-0.fdr.1
- Update to 1.25.

* Mon May  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.24-0.fdr.3
- Add workaround for building with UCL 1.02, thanks to upstream.

* Sun Nov 16 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.24-0.fdr.2
- Spec cleanup.

* Sat Jul 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.24-0.fdr.1
- First build.
