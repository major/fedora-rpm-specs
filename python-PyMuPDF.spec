%global pypi_name PyMuPDF
%global module_name fitz

Name:           python-%{pypi_name}
Version:        1.23.8
Release:        2%{?dist}
Summary:        Python binding for MuPDF - a lightweight PDF and XPS viewer

License:        AGPL-3.0-or-later
URL:            https://github.com/pymupdf/PyMuPDF
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-fix-test_-font.patch
Patch1:         0001-test_pixmap-adjust-to-turbojpeg.patch
Patch2:         0001-adjust-tesseract-tessdata-path-to-Fedora-default.patch

BuildRequires:  python3-devel
BuildRequires:  python3-fonttools
BuildRequires:  python3-pillow
BuildRequires:  python3-pip
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-furo
BuildRequires:  rst2pdf
BuildRequires:  gcc gcc-c++
BuildRequires:  swig
BuildRequires:  zlib-devel
BuildRequires:  mupdf-static
# Can be removed if mupdf provides a shared library
BuildRequires:  libjpeg-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  jbig2dec-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  gumbo-parser-devel
BuildRequires:  leptonica-devel
BuildRequires:  tesseract-devel

%global _description %{expand:
This is PyMuPDF, a Python binding for MuPDF - a lightweight PDF and XPS
viewer.  MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction
book formats, and it is known for its top performance and high rendering
quality.  With PyMuPDF you therefore can also access files with extensions
*.pdf, *.xps, *.oxps, *.epub, *.cbz or *.fb2 from your Python scripts.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
# provide the importable module:
%py_provides python3-%{module_name}

%description -n python3-%{pypi_name} %_description

%package        doc
Summary:        Documentation for python-%{pypi_name}
BuildArch:      noarch

%description    doc
python-%{pypi_name}-doc contains documentation and examples for PyMuPDF

%prep
%autosetup -n %{pypi_name}-%{version} -p 1

%build
# generate debug symbols
export PYMUPDF_SETUP_MUPDF_BUILD_TYPE='debug'
# build against system mupdf:
export PYMUPDF_SETUP_MUPDF_BUILD=''
# build original implementation only:
export PYMUPDF_SETUP_IMPLEMENTATIONS='a'
CFLAGS="$CFLAGS -I/usr/include -I/usr/include/freetype2 -I/usr/include/harbuzz -I/usr/include/mupdf"
LDFLAGS="$LDFLAGS -lfreetype -lgumbo -lharfbuzz -ljbig2dec -ljpeg -lleptonica -lmupdf -lmupdf-third -lopenjp2 -ltesseract"
%pyproject_wheel
sphinx-build docs docs_built

%install
%pyproject_install

%check
# FIXME: Crashes with Aborted, corrupted double-linked list
%ifarch s390 s390x
%pytest || :
%else
# test_fontarchives tries to download special module via pip
%pytest -k 'not test_fontarchive'
%endif

%files -n python3-%{pypi_name}
%license COPYING
%{python3_sitearch}/%{module_name}/
%{python3_sitearch}/PyMuPDF*

%files doc
%doc docs_built/* README.md

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.8-1
- Update to new upstream release 1.23.8 (rhbz#2252504)

* Sat Dec 02 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.7-1
- Update to new upstream release 1.23.7 (rhbz#2252504)

* Mon Nov 06 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.6-1
- Update to new upstream release 1.23.6 (rhbz#2244148)

* Mon Nov 06 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.5-1
- Update to new upstream release 1.23.5 (rhbz#2244148)

* Wed Oct 11 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.4-2
- Rebuild for mupdf 1.23.4

* Tue Oct 10 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.4-1
- Update to new upstream release 1.23.4 (rhbz#2241098)

* Tue Oct 10 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.3-3
- Adjust tesseract tessdata path to Fedora default

* Sat Oct 07 2023 Sandro Mani <manisandro@gmail.com> - 1.23.3-2
- Rebuild (tesseract)

* Mon Sep 04 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.23.3-1
- Update to new upstream release 1.23.3 (rhbz#2231206)
- Switch to new pyproject packaging macros

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Sandro Mani <manisandro@gmail.com> - 1.22.5-3
- Rebuild (tesseract)

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.22.5-2
- Rebuilt for Python 3.12

* Thu Jun 22 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.22.5-1
- Update to new upstream release 1.22.5 (rhbz#2216869)

* Thu May 11 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.22.3-2
- Reenable test suite where possible

* Thu May 11 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.22.3-1
- Update to new upstream release 1.22.3 (rhbz#2186919)

* Fri Apr 28 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.22.2-1
- Update to new upstream release 1.22.2 (rhbz#2186919)

* Mon Apr 24 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.22.1-1
- Update to new upstream release 1.22.1 (rhbz#2186919)
- Minor bug fixes

* Sat Apr 15 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.22.0-1
- Update to new upstream release 1.22.0 (rhbz#2186919)
- Text extraction now includes glyphs that overlap with clip rect, not just those contained entirely.
- Compatibility with mupdf 1.22.0, various bug fixes.

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 1.21.1-6
- Rebuild (tesseract)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Sandro Mani <manisandro@gmail.com> - 1.21.1-4
- Rebuild (tesseract)

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 1.21.1-3
- Rebuild (leptonica)

* Sat Dec 17 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.21.1-2
- SPDX migration

* Tue Dec 13 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.21.1-1
- Update to new upstream release 1.21.1 (rhbz#2152969)

* Tue Nov 08 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.21.0-1
- Update to new upstream release 1.21.0 (rhbz#2139246)

* Fri Aug 12 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.20.2-1
- Update to new upstream release 1.20.2 (#2118056)

* Thu Jul 28 2022 Scott Talbert <swt@techie.net> - 1.20.1-1
- Update to new upstream release 1.20.1 (#2101869)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-2
- Rebuild (tesseract)

* Fri Jun 17 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.20.0-1
- Update to new upstream release 1.20.0 (bz #2097589)

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.19.6-4
- Rebuilt for Python 3.11

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1.19.6-3
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 1.19.6-2
- Rebuild for tesseract 5.1.0

* Tue Mar 08 2022 Scott Talbert <swt@techie.net> - 1.19.6-1
- Update to new upstream release 1.19.6 (#2061128)

* Fri Feb 25 2022 Sandro Mani <manisandro@gmail.com> - 1.19.5-2
- Rebuild (leptonica)

* Fri Feb 18 2022 Scott Talbert <swt@techie.net> - 1.19.5-1
- Update to new upstream release 1.19.5 (#2050691)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Scott Talbert <swt@techie.net> - 1.19.4-1
- Update to new upstream release 1.19.4 (#2036460)

* Sun Dec 19 2021 Sandro Mani <manisandro@gmail.com> - 1.19.3-3
- Rebuild (tesseract)

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 1.19.3-2
- Rebuild (tesseract)

* Tue Dec 14 2021 Scott Talbert <swt@techie.net> - 1.19.3-1
- Update to new upstream release 1.19.3 (#2031602)

* Sun Nov 21 2021 Scott Talbert <swt@techie.net> - 1.19.2-1
- Update to new upstream release 1.19.2 (#2025180)

* Sun Oct 24 2021 Michael J Gruber <mjg@fedoraproject.org> - 1.19.1-1
- Update to new upstream release 1.19.1
- Enable OCR with the leptonica/tesseract engine

* Sun Oct 17 2021 Michael J Gruber <mjg@fedoraproject.org> - 1.19.0-1
- Update to new upstream release 1.19.0 (#2014860)

* Fri Sep 17 2021 Scott Talbert <swt@techie.net> - 1.18.19-1
- Update to new upstream release 1.18.19 (#2005248)

* Sun Sep 12 2021 Scott Talbert <swt@techie.net> - 1.18.17-1
- Update to new upstream release 1.18.17 (#1997388)

* Mon Aug 09 2021 Scott Talbert <swt@techie.net> - 1.18.16-1
- Update to new upstream release 1.18.16 (#1991265)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Scott Talbert <swt@techie.net> - 1.18.15-1
- Update to new upstream release 1.18.15 (#1981087)

* Tue Jun 15 2021 Scott Talbert <swt@techie.net> - 1.18.14-1
- Update to new upstream release 1.18.14 (#1967360)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.18.13-2
- Rebuilt for Python 3.10

* Thu May 06 2021 Scott Talbert <swt@techie.net> - 1.18.13-1
- Update to new upstream release 1.18.13 (#1957559)

* Sat Apr 17 2021 Scott Talbert <swt@techie.net> - 1.18.11-1
- Update to new upstream release 1.18.11 (#1948243)

* Thu Mar 25 2021 Scott Talbert <swt@techie.net> - 1.18.10-1
- Update to new upstream release 1.18.10 (#1933388)

* Wed Feb 24 2021 Michael J Gruber <mjg@fedoraproject.org> - 1.18.8-2
- rebuild for mupdf CVE-2021-3407

* Sat Feb 06 2021 Scott Talbert <swt@techie.net> - 1.18.8-1
- Update to new upstream release 1.18.8 (#1924379)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  9 2021 Scott Talbert <swt@techie.net> - 1.18.6-1
- Update to new upstream release 1.18.6 (#1913766)

* Sun Dec 20 14:22:47 EST 2020 Scott Talbert <swt@techie.net> - 1.18.5-1
- Update to new upstream release 1.18.5 (#1908813)

* Fri Nov 20 20:19:08 EST 2020 Scott Talbert <swt@techie.net> - 1.18.4-1
- Update to new upstream release 1.18.4 (#1900148)

* Mon Nov  9 19:43:10 EST 2020 Scott Talbert <swt@techie.net> - 1.18.3-1
- Update to new upstream release 1.18.3 (#1896141)

* Sun Nov  8 09:38:33 EST 2020 Scott Talbert <swt@techie.net> - 1.18.2-1
- Update to new upstream release 1.18.2 (#1892160)

* Mon Oct 26 2020 Scott Talbert <swt@techie.net> - 1.18.1-1
- Update to new upstream release 1.18.1 (#1889179)

* Thu Oct 08 2020 Michael J Gruber <mjg@fedoraproject.org> - 1.18.0-1
- Update to new upstream release 1.18.0

* Fri Sep 18 2020 Michael J Gruber <mjg@fedoraproject.org> - 1.17.4-2
- rebuild with jbig2dec 0.19

* Tue Jul 28 2020 Scott Talbert <swt@techie.net> - 1.17.4-1
- Update to new upstream release 1.17.4 (#1860498)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Scott Talbert <swt@techie.net> - 1.17.3-1
- Update to new upstream release 1.17.3 (#1854562)

* Fri Jun 26 2020 Scott Talbert <swt@techie.net> - 1.17.2-1
- Update to new upstream release 1.17.2 (#1850817)

* Thu Jun 18 2020 Scott Talbert <swt@techie.net> - 1.17.1-1
- Update to new upstream release 1.17.1 (#1848770)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Michael J Gruber <mjg@fedoraproject.org> - 1.17.0-1
- Update to new upstream release 1.17.0 (#1838287)

* Mon May 04 2020 Scott Talbert <swt@techie.net> - 1.16.18-1
- Update to new upstream release 1.16.18 (#1822800)

* Sun Mar 29 2020 Scott Talbert <swt@techie.net> - 1.16.16-1
- Update to new upstream release 1.16.16 (#1818610)

* Thu Mar 26 2020 Scott Talbert <swt@techie.net> - 1.16.14-1
- Update to new upstream release 1.16.14 (#1817211)

* Wed Mar 18 2020 Scott Talbert <swt@techie.net> - 1.16.13-1
- Update to new upstream release 1.16.13 (#1814049)

* Fri Mar 13 2020 Scott Talbert <swt@techie.net> - 1.16.12-1
- Update to new upstream release 1.16.12 (#1812963)

* Tue Feb 25 2020 Scott Talbert <swt@techie.net> - 1.16.11-1
- Update to new upstream release 1.16.11 (#1806372)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Scott Talbert <swt@techie.net> - 1.16.10-1
- Update to new upstream release 1.16.10 (#1785875)

* Thu Dec 12 2019 Scott Talbert <swt@techie.net> - 1.16.9-1
- Update to new upstream release 1.16.9 (#1773810)

* Tue Nov 12 2019 Scott Talbert <swt@techie.net> - 1.16.7-1
- Update to new upstream release 1.16.7 (#1771130)

* Thu Nov 07 2019 Scott Talbert <swt@techie.net> - 1.16.6-1
- Update to new upstream release 1.16.6 (#1768266)

* Tue Oct 15 2019 Scott Talbert <swt@techie.net> - 1.16.5-1
- Update to new upstream release 1.16.5 (#1761164)

* Sat Sep 14 2019 Scott Talbert <swt@techie.net> - 1.16.2-1
- Update to new upstream release 1.16.2 (#1751945)

* Wed Sep 04 2019 Scott Talbert <swt@techie.net> - 1.16.1-1
- Update to new upstream release 1.16.1 (#1747043)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.20-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Scott Talbert <swt@techie.net> - 1.14.20-1
- Update to new upstream release 1.14.20 (#1742123)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Scott Talbert <swt@techie.net> - 1.14.17-1
- Update to new upstream release 1.14.17 (#1727474)

* Thu Jun 13 2019 Scott Talbert <swt@techie.net> - 1.14.16-1
- Update to new upstream release 1.14.16 (#1713110)

* Wed Jun 12 2019 Scott Talbert <swt@techie.net> - 1.14.14-3
- Temporarily build our own copy of mupdf to fix FTBFS (#1716518)

* Tue May 07 2019 Scott Talbert <swt@techie.net> - 1.14.14-2
- Restore linking with harfbuzz (#1706753)

* Thu Apr 18 2019 Scott Talbert <swt@techie.net> - 1.14.14-1
- New upstream release 1.14.14

* Mon Apr 08 2019 Scott Talbert <swt@techie.net> - 1.14.13-1
- New upstream release 1.14.13

* Fri Mar 22 2019 Scott Talbert <swt@techie.net> - 1.14.12-1
- New upstream release 1.14.12

* Tue Mar 12 2019 Scott Talbert <swt@techie.net> - 1.14.10-1
- New upstream release 1.14.10

* Fri Mar 08 2019 Scott Talbert <swt@techie.net> - 1.14.9-1
- New upstream release 1.14.9

* Thu Jan 31 2019 Scott Talbert <swt@techie.net> - 1.14.8-1
- New upstream release 1.14.8

* Fri Jan 25 2019 Scott Talbert <swt@techie.net> - 1.14.7-1
- New upstream release 1.14.7

* Tue Nov 20 2018 Scott Talbert <swt@techie.net> - 1.14.1-1
- New upstream release 1.14.1

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.13.20-2
- Subpackage python2-PyMuPDF has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Sep 14 2018 Scott Talbert <swt@techie.net> - 1.13.20-1
- New upstream release 1.13.20

* Sat Aug 04 2018 Scott Talbert <swt@techie.net> - 1.13.16-1
- New upstream release 1.13.16

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.13.15-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Scott Talbert <swt@techie.net> - 1.13.15-1
- New upstream release 1.13.15

* Fri Jul 20 2018 Scott Talbert <swt@techie.net> - 1.13.14-1
- New upstream release 1.13.14

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Scott Talbert <swt@techie.net> - 1.13.13-1
- New upstream release 1.13.13

* Wed Jun 27 2018 Scott Talbert <swt@techie.net> - 1.13.12-1
- New upstream release 1.13.12

* Tue Jun 26 2018 Scott Talbert <swt@techie.net> - 1.13.11-1
- New upstream release 1.13.11

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.13.10-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Scott Talbert <swt@techie.net> - 1.13.10-1
- New upstream release 1.13.10

* Sun Jun 10 2018 Scott Talbert <swt@techie.net> - 1.13.9-1
- Initial package.
