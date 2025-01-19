Name:           latex2rtf
Version:        2.3.18
Release:        15%{?dist}
Summary:        LaTeX to RTF converter that handles equations, figures, and cross-references
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://latex2rtf.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}a.tar.gz
# Do not use (non-existent on EL7) a4wide paper style in tests
Patch1:         latex2rtf-a4wide.patch
BuildRequires:  make
BuildRequires:  gcc
# For running the tests
BuildRequires:  ImageMagick
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)
BuildRequires:  texlive-courier
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-psfrag
BuildRequires:  texlive-times
Requires:       gawk
Requires:       grep
# For converting images, /usr/bin/convert
Requires:       ImageMagick
Requires:       sed
# For latex2png, ghostscript
Requires:       /usr/bin/eps2eps
# Including netpbm, latex2html, some sty files might be missing from userland
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexrecommended
%if 0%{?fedora}
Requires:       texlive-collection-latexextra
%endif

%description
LaTeX2rtf is a translator program which is intended to translate a LaTeX
document (precisely: the text and a limited subset of LaTeX tags) into the RTF
format which can be imported by several text processors (including Microsoft
Word for Windows and Word for Macintosh). 

%prep
%setup -q
%patch -P1 -p1 -b .a4wide

# fix Makefile
sed -i -e '/^\.PHONY/d' Makefile

# Get rid of iffy permissions.
chmod a-x cfg/*.cfg

# Delete prebuilt objects in case of subtle failure.
find -name "*.o" -delete -print

# Fix permissions again for normal files.
find . -type f -exec chmod 644 {} \;
chmod 755 test/bracecheck
chmod 755 scripts/latex2png

# Change encoding of documentation.
for txtfile in ChangeLog Copyright; do
 iconv -f ASCII -t UTF-8 $txtfile >$txtfile.new && \
 touch -r $txtfile $txtfile.new && \
 mv $txtfile{.new,} 
done

%build
# Set the necessary config options, including location of config files
# -fsigned-char is useful for special arches, don't forget it.
%make_build %{name} CFLAGS="%{optflags} -DUNIX -fsigned-char" LDFLAGS="%{?__global_ldflags}" PREFIX=%{_prefix}

%install
%make_install -j1 install-info PREFIX=%{_prefix}
# Remove unnecessary file from infodir
rm -frv %{buildroot}%{_infodir}/dir

%check
RTFPATH=`pwd`/cfg \
%{__make} check

%files
%doc ChangeLog doc/latex2rtf.pdf doc/latex2rtf.html doc/credits
%license Copyright doc/copying.txt
%{_bindir}/latex2png
%{_bindir}/latex2rtf
%{_datadir}/latex2rtf/
%{_infodir}/latex2rtf.info.*
%{_mandir}/man1/latex2png.1.*
%{_mandir}/man1/latex2rtf.1.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.18-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.18-4
- Fix build failures (#1863959)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.18-1
- Update to 2.3.18 (#1842187)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.17-1
- Update to 2.3.17 (#1561807)

* Tue Mar 20 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.16-5
- Fix build with Perl 5.26 (#1556018)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.16-1
- Update to 2.3.16 (#1441438)

* Mon May 01 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.15-1
- Update to 2.3.15 (#1441438)

* Mon May 01 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.14-1
- Update to 2.3.14 (#1441438)

* Tue Mar 28 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.13-1
- Update to 2.3.13 (#1435033)

* Mon Feb 13 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.12-1
- Update to 2.3.12 (#1413326)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.11-1
- Update to 2.3.11 (#1346517)
- Tests restored to upstream tarball

* Thu Mar 31 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.10-1
- Update to 2.3.10 (#1289786)
- Includes upstream fix for CVE-2015-8106 (#1282492)
- Tests removed from upstream tarball

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Orion Poplawski <orion@cora.nwra.com> - 2.3.8-6
- Do not use (non-existent on EL7) a4wide paper style in tests (bug #1136065)
- Drop %%make_build for EL7 compatibility

* Thu Feb 19 2015 Christopher Meng <rpm@cicku.me> - 2.3.8-5
- Fix broken requires again.

* Tue Feb 17 2015 Christopher Meng <rpm@cicku.me> - 2.3.8-4
- Add missing requires again.

* Mon Feb 02 2015 Christopher Meng <rpm@cicku.me> - 2.3.8-3
- Add missing requires for latex2png

* Thu Aug 28 2014 Christopher Meng <rpm@cicku.me> - 2.3.8-2
- Fix FTBFS with texinfo 5.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Christopher Meng <rpm@cicku.me> - 2.3.8-1
- Update to 2.3.8

* Tue Jul 01 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.7a-1
- Update to 2.3.7a.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.6-1
- Update to 2.3.6.

* Mon Feb 17 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.5-1
- Update to 2.3.5.

* Sun Nov 17 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3.

* Wed Feb 27 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.2a-1
- Update to 2.3.2a.

* Fri Feb 15 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1.

* Tue Oct 16 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-2
- Fixed build in EPEL.

* Tue Oct 16 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0.

* Wed Sep 26 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.2.1c-1
- Update to 2.2.1c.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-2
- Fix configuration directory location.

* Mon Jun 04 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 05 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-8
- Added patch to fix image height on 64-bit architectures.
  https://bugzilla.redhat.com/show_bug.cgi?id=497752

* Wed Mar 25 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-7
- Retry EPEL fix: disable check phase which doesn't seem to work 
  for some reason on EPEL 5 ppc (segfault in list.tex).

* Sun Mar 22 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-6
- Fix EPEL build.

* Sat Mar 21 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-5
- Keep documentation time stamps when converting encoding.

* Fri Mar 13 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-4
- Added check phase.

* Thu Mar 12 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-3
- Review fixes.

* Sun Dec 21 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-2
- Fix perms on config files.

* Sun Nov 02 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.9.19-1
- First release.
