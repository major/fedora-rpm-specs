Name: writerperfect
Version: 0.9.6
Release: %autorelease
Summary: A collection of tools to transform various file formats into ODF

License: LGPL-2.1-or-later OR MPL-2.0
URL: http://sourceforge.net/p/libwpd/wiki/writerperfect/
Source: http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: pkgconfig(libabw-0.1)
BuildRequires: pkgconfig(libcdr-0.1)
BuildRequires: pkgconfig(libe-book-0.1)
BuildRequires: pkgconfig(libeot)
BuildRequires: pkgconfig(libepubgen-0.1)
BuildRequires: pkgconfig(libetonyek-0.1)
BuildRequires: pkgconfig(libfreehand-0.1)
BuildRequires: pkgconfig(libgsf-1)
BuildRequires: pkgconfig(libmspub-0.1)
BuildRequires: pkgconfig(libmwaw-0.3)
BuildRequires: pkgconfig(libodfgen-0.1)
BuildRequires: pkgconfig(libqxp-0.0)
BuildRequires: pkgconfig(libpagemaker-0.0)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librvngabw-0.0)
BuildRequires: pkgconfig(libstaroffice-0.0)
BuildRequires: pkgconfig(libvisio-0.1)
BuildRequires: pkgconfig(libwpd-0.10)
BuildRequires: pkgconfig(libwpg-0.3)
BuildRequires: pkgconfig(libwps-0.4)
BuildRequires: pkgconfig(libzmf-0.0)

Patch0: 0001-fix-build-with-libgsf.patch
Patch1: 0001-Fix-linking-with-newer-tools-by-getting-the-library-.patch

%description
%{name} is a collection of command-line tools to transform various document
formats into ODF. Among supported input formats are:
* AbiWord
* Adobe PageMaker
* Apple Keynote
* Corel WordPerfect
* CorelDRAW
* Microsoft Publisher
* Microsoft Visio
* Microsoft Works
* QuarkXPress

%package epub
Summary: A collection of tools to transform various file formats into EPUB

%description epub
%{name} is a collection of command-line tools to transform various document
formats into EPUB. Among supported input formats are:
* AbiWord
* Adobe PageMaker
* Apple Keynote
* Corel WordPerfect
* CorelDRAW
* Microsoft Publisher
* Microsoft Visio
* Microsoft Works

%package abw
Summary: A collection of tools to transform various file formats into AbiWord

%description abw
%{name} is a collection of command-line tools to transform various document
formats into AbiWord format. Among supported input formats are:
* Apple Pages
* Corel WordPerfect
* Microsoft Works

%prep
%autosetup -p1

%build
aclocal
automake
%configure \
    --disable-silent-rules \
    --disable-werror \
    --with-import-libs \
    --with-export-libs \
    --with-libeot \
    --with-libgsf

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in `ls %{buildroot}%{_bindir}`; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 *2abw.1 *2epub.1 *2od?.1 %{buildroot}/%{_mandir}/man1

%files
%doc NEWS README
%license COPYING.LGPL COPYING.MPL
%{_bindir}/abw2odt
%{_bindir}/cdr2odg
%{_bindir}/cmx2odg
%{_bindir}/ebook2odt
%{_bindir}/fh2odg
%{_bindir}/key2odp
%{_bindir}/mwaw2odf
%{_bindir}/numbers2ods
%{_bindir}/qxp2odg
%{_bindir}/pages2odt
%{_bindir}/pmd2odg
%{_bindir}/pub2odg
%{_bindir}/sd2odf
%{_bindir}/vsd2odg
%{_bindir}/vss2odg
%{_bindir}/wks2ods
%{_bindir}/wpd2odt
%{_bindir}/wpft2odf
%{_bindir}/wpg2odg
%{_bindir}/wps2odt
%{_bindir}/zmf2odg
%{_mandir}/man1/abw2odt.1*
%{_mandir}/man1/cdr2odg.1*
%{_mandir}/man1/cmx2odg.1*
%{_mandir}/man1/ebook2odt.1*
%{_mandir}/man1/fh2odg.1*
%{_mandir}/man1/key2odp.1*
%{_mandir}/man1/mwaw2odf.1*
%{_mandir}/man1/numbers2ods.1*
%{_mandir}/man1/pages2odt.1*
%{_mandir}/man1/pmd2odg.1*
%{_mandir}/man1/pub2odg.1*
%{_mandir}/man1/qxp2odg.1*
%{_mandir}/man1/sd2odf.1*
%{_mandir}/man1/vsd2odg.1*
%{_mandir}/man1/vss2odg.1*
%{_mandir}/man1/wks2ods.1*
%{_mandir}/man1/wpd2odt.1*
%{_mandir}/man1/wpft2odf.1*
%{_mandir}/man1/wpg2odg.1*
%{_mandir}/man1/wps2odt.1*
%{_mandir}/man1/zmf2odg.1*

%files epub
%doc NEWS README
%license COPYING.LGPL COPYING.MPL
%{_bindir}/abw2epub
%{_bindir}/cdr2epub
%{_bindir}/cmx2epub
%{_bindir}/ebook2epub
%{_bindir}/fh2epub
%{_bindir}/key2epub
%{_bindir}/mwaw2epub
%{_bindir}/pages2epub
%{_bindir}/pmd2epub
%{_bindir}/pub2epub
%{_bindir}/qxp2epub
%{_bindir}/sd2epub
%{_bindir}/vsd2epub
%{_bindir}/vss2epub
%{_bindir}/wpd2epub
%{_bindir}/wpft2epub
%{_bindir}/wpg2epub
%{_bindir}/wps2epub
%{_bindir}/zmf2epub
%{_mandir}/man1/abw2epub.1*
%{_mandir}/man1/cdr2epub.1*
%{_mandir}/man1/cmx2epub.1*
%{_mandir}/man1/ebook2epub.1*
%{_mandir}/man1/fh2epub.1*
%{_mandir}/man1/key2epub.1*
%{_mandir}/man1/mwaw2epub.1*
%{_mandir}/man1/pages2epub.1*
%{_mandir}/man1/pmd2epub.1*
%{_mandir}/man1/pub2epub.1*
%{_mandir}/man1/qxp2epub.1*
%{_mandir}/man1/sd2epub.1*
%{_mandir}/man1/vsd2epub.1*
%{_mandir}/man1/vss2epub.1*
%{_mandir}/man1/wpd2epub.1*
%{_mandir}/man1/wpft2epub.1*
%{_mandir}/man1/wpg2epub.1*
%{_mandir}/man1/wps2epub.1*
%{_mandir}/man1/zmf2epub.1*

%files abw
%doc NEWS README
%license COPYING.LGPL COPYING.MPL
%{_bindir}/abw2abw
%{_bindir}/ebook2abw
%{_bindir}/mwaw2abw
%{_bindir}/pages2abw
%{_bindir}/sd2abw
%{_bindir}/wpd2abw
%{_bindir}/wpft2abw
%{_bindir}/wps2abw
%{_mandir}/man1/abw2abw.1*
%{_mandir}/man1/ebook2abw.1*
%{_mandir}/man1/mwaw2abw.1*
%{_mandir}/man1/pages2abw.1*
%{_mandir}/man1/sd2abw.1*
%{_mandir}/man1/wpd2abw.1*
%{_mandir}/man1/wpft2abw.1*
%{_mandir}/man1/wps2abw.1*

%changelog
%autochangelog
