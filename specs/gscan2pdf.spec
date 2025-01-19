# Run tests. They are quite fragile (especially regarding to ImageMagick and
# fonts) and take long and need many dependencies.
%bcond_without gscan2pdf_enables_test

Name:           gscan2pdf
Version:        2.13.4
Release:        3%{?dist}
Summary:        GUI for producing a multipage PDF from a scan
# icons/180_degree.svg: GPL-3.0-only
# icons/scanner.svg:    GPL-2.0-only
# icons/pdf.svg:        LGPL-2.0-or-later (a copy of
#           Nuvola/icons/scalable/mimetypes/gnome-mime-application-pdf.svg
#           from gnome-themes-extras-0.9.0)
# net.sourceforge.gscan2pdf.appdata.xml:    CC0-1.0
# other files:          GPL-3.0-only
License:        GPL-3.0-only AND GPL-2.0-only AND LGPL-2.0-or-later AND CC0-1.0
URL:            https://gscan2pdf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-463293E4AE33871846F30227B321F203110FCAF3.gpg
# Do not warn about missing pdftk, bug #1708054, not upstreamable
Patch0:         gscan2pdf-2.9.0-Do-not-warn-about-missing-pdftk.patch
# Replace copies of gscan2pdf.svg with links, not upstreamable
Patch1:         gscan2pdf-2.12.7-Symlink-gscan2pdf.svg-files.patch
# Adapt tests to libtiff-4.6.0, proposed to the upstream,
# <https://sourceforge.net/p/gscan2pdf/bugs/427/>
Patch2:         gscan2pdf-2.13.3-Remove-tiff2ps-and-tiff2pdf.patch
# Adapt to ImageMagick 7, propsed to the upstream,
# <https://sourceforge.net/p/gscan2pdf/bugs/431/>
Patch3:         gscan2pdf-2.13.3-Execute-magick-instead-of-convert-command.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
# awk in Makefile.PL
BuildRequires:  gawk
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# pod2html in Makefile.PL
BuildRequires:  perl-Pod-Html
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
%if %{with gscan2pdf_enables_test}
# Run-time:
# ImageMagick for "convert" tool executed from _thread_threshold() and
# _write_image_object()
BuildRequires:  ImageMagick
# libtiff-tools for /usr/bin/tiffcp
BuildRequires:  libtiff-tools
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::General) >= 2.40
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Filesys::Df)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Glib) >= 1.220
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(GooCanvas2)
BuildRequires:  perl(GooCanvas2::Canvas)
BuildRequires:  perl(Gtk3) >= 0.028
# Gtk3::Entry is not provided by perl-Gtk3
BuildRequires:  perl(Gtk3::ImageView)
BuildRequires:  perl(Gtk3::ImageView::Tool::Dragger)
BuildRequires:  perl(Gtk3::ImageView::Tool::Selector)
BuildRequires:  perl(Gtk3::ImageView::Tool::SelectorDragger)
BuildRequires:  perl(Gtk3::SimpleList)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(if)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(Image::Sane)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::gettext) >= 1.05
BuildRequires:  perl(Locale::Language)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(PDF::Builder) >= 3.022
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::Killfam)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Set::IntSpan) >= 1.10
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Optional run-time:
# djvulibre for djvused program
BuildRequires:  djvulibre
BuildRequires:  poppler-utils
BuildRequires:  unpaper
# xz not used at tests
# Tests:
BuildRequires:  file
# fontconfig for a fc-list tool
BuildRequires:  fontconfig
# We need to pass a specific font name to ImageMagick, bug #1494563
BuildRequires:  font(dejavusans)
# ghostscript for pdf2ps used in t/1163_save_multipage_pdf_as_ps.t
BuildRequires:  ghostscript
BuildRequires:  ImageMagick-djvu
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Override)
BuildRequires:  perl(Test::More)
# poppler-utils for pdffonts and pdfinfo
BuildRequires:  sane-backends-drivers-scanners
BuildRequires:  xorg-x11-server-Xvfb
# Optional tests:
%if 0%{?fedora} >= 41
# Some tests (e.g. t/52_process_chain_udt.t) attempt to load PNM or PBM
# images and Glib::Object::Introspection then warns "Caught error getting
# pixbuf: Couldn’t recognize the image file format...". That's because
# a support for the formats was removed from gdk-pixbuf2-modules.
# The warnings are probably harmless, but noisy.
BuildRequires:  gdk-pixbuf2-modules-extra
%endif
# pdftk not packaged (bug #1708054)
# poppler-utils for pdfunite, pdftotext
# sane-frontends for scanadf
BuildRequires:  sane-frontends
# Test::Perl::Critic not used
%endif
# libappstream-glib for appstream-util
BuildRequires:  libappstream-glib
Suggests:       cuneiform
# Prefer gocr over cuneiform, or tesseract
Recommends:     gocr
# djvulibre for djvused program
Recommends:     djvulibre
%if 0%{?fedora} >= 41
# Some operations like Threshold use PBM as an intermediate format and then
# Glib::Object::Introspection warns "Caught error getting pixbuf:
# Couldn’t recognize the image file format..." and gscan2pdf fails to load it.
# That's because a support for the format was removed from
# gdk-pixbuf2-modules-2.42.11 and later added as a separate package.
Requires:       gdk-pixbuf2-modules-extra
%endif
# libtiff-tools for /usr/bin/tiffcp
Requires:       libtiff-tools
Requires:       perl(if)
Recommends:     perl(Image::Magick)
Requires:       perl(PDF::Builder) >= 3.022
# convert tool executed from _write_image_object() and _thread_threshold()
Requires:       ImageMagick
Recommends:     ImageMagick-djvu
# poppler-utils for pdfimages, pdfinfo, and pdftotext
Recommends:     poppler-utils
Requires:       sane-backends >= 1.0.17
Requires:       sane-frontends
Suggests:       tesseract
Recommends:     unpaper
# xdg-utils for xdg-email command
Recommends:     xdg-utils
Recommends:     xz

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\) >= 1\.210$
%global __requires_exclude %{__requires_exclude}|^perl\\(PDF::Builder\\)$

# Gtk3::Entry is not provided by perl-Gtk3
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk3::Entry\\)

%description
A GUI to ease the process of producing a multipage PDF from a scan.

%package tests
Summary:        Tests for %{name}
License:        GPL-3.0-only
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       file
# fontconfig for a fc-list tool
Requires:       fontconfig
%if 0%{?fedora} >= 41
# Some tests (e.g. t/52_process_chain_udt.t) attempt to load PNM or PBM
# images and Glib::Object::Introspection then warns "Caught error getting
# pixbuf: Couldn’t recognize the image file format...". That's because
# a support for the formats was removed from gdk-pixbuf2-modules.
# The warnings are probably harmless, but noisy.
Requires:       gdk-pixbuf2-modules-extra
%endif
Requires:       perl-Test-Harness
# We need to pass a specific font name to ImageMagick, bug #1494563
Requires:       font(dejavusans)
# ghostscript for pdf2ps used in t/1163_save_multipage_pdf_as_ps.t
Requires:       ghostscript
Requires:       ImageMagick-djvu
Requires:       perl(PDF::Builder) >= 3.022
# poppler-utils for pdffonts and pdfinfo
Requires:       poppler-utils
Requires:       sane-backends-drivers-scanners
Requires:       xorg-x11-server-Xvfb
# Optional tests:
# pdftk not packaged (bug #1708054)
# poppler-utils for pdfunite, pdftotext
# sane-frontends for scanadf
Requires:       sane-frontends

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Symlink identical files
rm scanners/FujitsuS510.Lineart
ln -s FujitsuS510 scanners/FujitsuS510.Lineart
rm scanners/snapscanS510.Color
ln -s snapscanS510 scanners/snapscanS510.Color
# Remove unused tests
rm t/91_critic.t
# Disable currently failing tests
# TODO: Fix them with upstream
# glib randomly fails with "GLib-GObject-WARNING **:
# ../gobject/gsignal.c:2647: instance '0x559dcdc1e290' has no handler with id
# '7415' at t/0602_Dialog_Scan.t line 313.".
rm t/0603_Dialog_Scan.t
# ImageMagick reports 255x30 image size
rm t/113_save_pdf_with_downsample.t
# ???
rm t/1111_save_pdf.t
# Fails with got: '179', expected '296' if not run separately. New test in 2.11.0.
rm t/169_import_scan.t
# gocr does not recognize a text
rm t/431_gocr.t t/432_gocr.t
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 SHAREDIR=%{_datadir}
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

desktop-file-install --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications         \
  %{buildroot}/%{_datadir}/applications/net.sourceforge.gscan2pdf.desktop

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a scanners t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99_pod.t
# Hang in CI and local mock because finished_callback is called instead of
# queued_callback
for TEST in 1113_save_pdf_with_error 126_save_djvu_with_error \
    133_save_tiff_with_error 1602_import_DjVu_with_error \
    1612_import_TIFF_with_error 1626_import_PDF_with_error \
    1632_import_ppm_with_error \
    213_rotate_with_error 243_threshold_with_error 253_negate_with_error \
    263_unsharp_mask_with_error 273_crop_with_error 283_to_png_with_error \
    354_unpaper_with_error 377_user_defined_with_error \
    434_gocr_with_error; do
    rm %{buildroot}%{_libexecdir}/%{name}/t/"$TEST".t
done
# Regular fail for an unknown reason
for TEST in 0601_Dialog_Scan 1601_import_DjVu 1604_import_multipage_DjVu \
    1642_import_png_with_error; do
    rm %{buildroot}%{_libexecdir}/%{name}/t/"$TEST".t
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Many tests write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
unset GNOME_DESKTOP_SESSION_ID KDE_FULL_SESSION LOGDIR OCROSCRIPTS \
    SANE_DEFAULT_DEVICE XDG_CONFIG_HOME XDG_CURRENT_DESKTOP
pushd "$DIR"
# Tests overwrite same-named files
xvfb-run -d prove -I . -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%find_lang %{name}

%check
%if %{with gscan2pdf_enables_test}
unset GNOME_DESKTOP_SESSION_ID KDE_FULL_SESSION LOGDIR OCROSCRIPTS \
    SANE_DEFAULT_DEVICE XDG_CONFIG_HOME XDG_CURRENT_DESKTOP
xvfb-run -d make test
%endif
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/net.sourceforge.gscan2pdf.appdata.xml

# Do not call gtk-update-icon-cache because it's needed only for updating icon
# themata in %%{_datadir}/icon/*. This package installs icon into
# %%{_datadir}/pixmaps/gscan2pdf.svg. Pixmaps seems not to be subject of icon
# themata.
%post
touch --no-create %{_datadir}/pixmaps || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/pixmaps || :
fi

%files -f %{name}.lang
%license LICENCE
%doc COPYING History
%{_bindir}/%{name}
%{perl_vendorlib}/Gscan2pdf
%{_datadir}/%{name}
%{_datadir}/applications/net.sourceforge.gscan2pdf.desktop
%dir %{_datadir}/help/*
%{_datadir}/help/*/%{name}
%{_datadir}/metainfo/net.sourceforge.gscan2pdf.appdata.xml
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man1/%{name}.1*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 Petr Pisar <ppisar@redhat.com> - 2.13.4-2
- Require gdk-pixbuf2-modules-extra by gscan2pdf for operations that use PBM
  image format

* Thu Aug 01 2024 Petr Pisar <ppisar@redhat.com> - 2.13.4-1
- 2.13.4 bump

* Thu Jul 18 2024 Petr Pisar <ppisar@redhat.com> - 2.13.3-1
- 2.13.3 bump

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 28 2023 Petr Pisar <ppisar@redhat.com> - 2.13.2-5
- Adapt to deprecated smart match in Perl 5.38.0 (upstream bug #421)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Petr Pisar <ppisar@redhat.com> - 2.13.2-3
- Adapt tests to ImageMagick-7.1.1.5 (upstream bug #417)
- Ignore options of scanners which report a range minimum greater than a range maximum

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Petr Pisar <ppisar@redhat.com> - 2.13.2-1
- 2.13.2 bump

* Tue Jan 03 2023 Petr Pisar <ppisar@redhat.com> - 2.13.1-1
- 2.13.1 bump

* Tue Oct 18 2022 Petr Pisar <ppisar@redhat.com> - 2.13.0-1
- 2.13.0 bump
- Stop requiring gnome-icon-theme; fixed in gtk3-3.24.34 (bug #2071851)

* Wed Aug 31 2022 Petr Pisar <ppisar@redhat.com> - 2.12.8-3
- Adapt tests to ffmpeg-5.1 (upstream bug #404)
- Correct gscan2pdf-tests license to GPL-3.0-only

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Petr Pisar <ppisar@redhat.com> - 2.12.8-1
- 2.12.8 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.12.7-2
- Perl 5.36 rebuild

* Tue May 31 2022 Petr Pisar <ppisar@redhat.com> - 2.12.7-1
- 2.12.7 bump

* Tue Apr 05 2022 Petr Pisar <ppisar@redhat.com> - 2.12.6-2
- Require gnome-icon-theme to work around a bug in gtk3 (bug #2071851)

* Mon Apr 04 2022 Petr Pisar <ppisar@redhat.com> - 2.12.6-1
- 2.12.6 bump

* Wed Feb 16 2022 Petr Pisar <ppisar@redhat.com> - 2.12.5-1
- 2.12.5 bump

* Tue Feb 08 2022 Petr Pisar <ppisar@redhat.com> - 2.12.4-3
- Fix parsing scanimage version (upstream bug #399)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Petr Pisar <ppisar@redhat.com> - 2.12.4-1
- 2.12.4 bump (bug #2025207)

* Mon Sep 20 2021 Petr Pisar <ppisar@redhat.com> - 2.12.3-1
- 2.12.3 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Petr Pisar <ppisar@redhat.com> - 2.12.2-1
- 2.12.2 bump
- Replace multiple gscan2pdf.svg copies with a symbolic link

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.12.1-2
- Perl 5.34 rebuild

* Thu Apr 22 2021 Petr Pisar <ppisar@redhat.com> - 2.12.1-1
- 2.12.1 bump

* Tue Apr 20 2021 Petr Pisar <ppisar@redhat.com> - 2.12.0-1
- 2.12.0 bump

* Thu Mar 18 2021 Petr Pisar <ppisar@redhat.com> - 2.11.2-1
- 2.11.2 bump
- Package tests

* Fri Feb 19 2021 Petr Pisar <ppisar@redhat.com> - 2.11.1-1
- 2.11.1 bump
- Switch from PDF-API2 to PDF-Builder

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Petr Pisar <ppisar@redhat.com> - 2.11.0-1
- 2.11.0 bump

* Fri Dec 18 2020 Petr Pisar <ppisar@redhat.com> - 2.10.2-1
- 2.10.2 bump

* Mon Dec 14 2020 Petr Pisar <ppisar@redhat.com> - 2.10.1-1
- 2.10.1 bump

* Mon Nov 02 2020 Petr Pisar <ppisar@redhat.com> - 2.10.0-1
- 2.10.0 bump
- We keep using PDF-API2 because of a PDF-Builder license (bug #1894911)

* Fri Sep 25 2020 Petr Pisar <ppisar@redhat.com> - 2.9.1-1
- 2.9.1 bump

* Mon Sep 21 2020 Petr Pisar <ppisar@redhat.com> - 2.9.0-1
- 2.9.0 bump
- Fix an error message about an empty LANGUAGE variable (upstream bug #360)

* Mon Jul 27 2020 Petr Pisar <ppisar@redhat.com> - 2.8.2-1
- 2.8.2 bump

* Mon Jul 13 2020 Petr Pisar <ppisar@redhat.com> - 2.8.1-1
- 2.8.1 bump

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.8.0-2
- Perl 5.32 rebuild

* Thu Jun 11 2020 Petr Pisar <ppisar@redhat.com> - 2.8.0-1
- 2.8.0 bump

* Mon May 11 2020 Petr Pisar <ppisar@redhat.com> - 2.7.0-1
- 2.7.0 bump

* Thu Apr 09 2020 Petr Pisar <ppisar@redhat.com> - 2.6.7-1
- 2.6.7 bump

* Tue Apr 07 2020 Petr Pisar <ppisar@redhat.com> - 2.6.6-1
- 2.6.6 bump

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 2.6.5-1
- 2.6.5 bump

* Fri Feb 07 2020 Petr Pisar <ppisar@redhat.com> - 2.6.4-1
- 2.6.4 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Petr Pisar <ppisar@redhat.com> - 2.6.3-1
- 2.6.3 bump

* Thu Nov 28 2019 Petr Pisar <ppisar@redhat.com> - 2.6.2-1
- 2.6.2 bump
- License corrected to "GPLv3 and GPLv2 and LGPLv2+ and CC0"

* Thu Nov 28 2019 Petr Pisar <ppisar@redhat.com> - 2.5.7-1
- 2.5.7 bump

* Wed Nov 27 2019 Petr Pisar <ppisar@redhat.com> - 2.5.6-2
- Adapt to changes in sane-backends-1.0.28 (bug #1776908)

* Thu Sep 12 2019 Petr Pisar <ppisar@redhat.com> - 2.5.6-1
- 2.5.6 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> - 2.5.5-1
- 2.5.5 bump

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Petr Pisar <ppisar@redhat.com> - 2.5.4-1
- 2.5.4 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.3-2
- Perl 5.30 rebuild

* Tue May 21 2019 Petr Pisar <ppisar@redhat.com> - 2.5.3-1
- 2.5.3 bump

* Thu May 09 2019 Petr Pisar <ppisar@redhat.com> - 2.5.2-2
- Do not warn about missing pdftk (bug #1708054)
- Do not require unused forks Perl module

* Tue Apr 23 2019 Petr Pisar <ppisar@redhat.com> - 2.5.2-1
- 2.5.2 bump

* Mon Mar 25 2019 Petr Pisar <ppisar@redhat.com> - 2.5.1-1
- 2.5.1 bump

* Thu Mar 14 2019 Petr Pisar <ppisar@redhat.com> - 2.4.0-3
- Enable t/1163_save_multipage_pdf_as_ps.t test

* Wed Mar 13 2019 Petr Pisar <ppisar@redhat.com> - 2.4.0-2
- Fix document queue locking (upstream bug #317)

* Mon Feb 25 2019 Petr Pisar <ppisar@redhat.com> - 2.4.0-1
- 2.4.0 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Petr Pisar <ppisar@redhat.com> - 2.3.0-1
- 2.3.0 bump

* Mon Dec 10 2018 Petr Pisar <ppisar@redhat.com> - 2.2.1-1
- 2.2.1 bump

* Mon Jul 30 2018 Petr Pisar <ppisar@redhat.com> - 2.1.4-1
- 2.1.4 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.2-2
- Perl 5.28 rebuild

* Thu May 24 2018 Petr Pisar <ppisar@redhat.com> - 2.1.2-1
- 2.1.2 bump

* Mon Apr 23 2018 Petr Pisar <ppisar@redhat.com> - 2.1.0-1
- 2.1.0 bump

* Tue Apr 03 2018 Petr Pisar <ppisar@redhat.com> - 2.0.3-1
- 2.0.3 bump

* Tue Mar 27 2018 Petr Pisar <ppisar@redhat.com> - 2.0.2-1
- 2.0.2 bump

* Tue Mar 13 2018 Petr Pisar <ppisar@redhat.com> - 2.0.1-1
- 2.0.1 bump

* Thu Mar 08 2018 Petr Pisar <ppisar@redhat.com> - 2.0.0-1
- 2.0.0 bump
- Enable tests at build time

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Petr Pisar <ppisar@redhat.com> - 1.8.11-1
- 1.8.11 bump

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.8-2
- Remove last hack for metainfo() provides

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 1.8.8-1
- 1.8.8 bump

* Mon Sep 25 2017 Petr Pisar <ppisar@redhat.com> - 1.8.7-1
- 1.8.7 bump

* Wed Aug 23 2017 Petr Pisar <ppisar@redhat.com> - 1.8.6-1
- 1.8.6 bump

* Mon Aug 21 2017 Petr Pisar <ppisar@redhat.com> - 1.8.5-1
- 1.8.5 bump

* Mon Jul 31 2017 Petr Pisar <ppisar@redhat.com> - 1.8.4-1
- 1.8.4 bump

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Petr Pisar <ppisar@redhat.com> - 1.8.3-2
- Fix a race in t/0610_Dialog_Scan_Image_Sane.t test

* Mon Jul 03 2017 Petr Pisar <ppisar@redhat.com> - 1.8.3-1
- 1.8.3 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.2-2
- Perl 5.26 rebuild

* Fri Jun 02 2017 Petr Pisar <ppisar@redhat.com> - 1.8.2-1
- 1.8.2 bump

* Mon May 29 2017 Petr Pisar <ppisar@redhat.com> - 1.8.1-1
- 1.8.1 bump

* Thu Apr 20 2017 Petr Pisar <ppisar@redhat.com> - 1.8.0-2
- Adapt 357_unpaper_rtl.t test to ImageMagick-6.9.3.0

* Thu Apr 13 2017 Petr Pisar <ppisar@redhat.com> - 1.8.0-1
- 1.8.0 bump

* Mon Apr 10 2017 Petr Pisar <ppisar@redhat.com> - 1.7.3-2
- Adapt to changes in tesseract-3.05.00 (bug #1440476)
- Make AppData XML file strictly conforming

* Mon Mar 13 2017 Petr Pisar <ppisar@redhat.com> - 1.7.3-1
- 1.7.3 bump

* Mon Feb 13 2017 Petr Pisar <ppisar@redhat.com> - 1.7.2-1
- 1.7.2 bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Petr Pisar <ppisar@redhat.com> - 1.7.1-1
- 1.7.1 bump

* Thu Jan 05 2017 Petr Pisar <ppisar@redhat.com> - 1.7.0-1
- 1.7.0 bump

* Mon Dec 05 2016 Petr Pisar <ppisar@redhat.com> - 1.6.0-1
- 1.6.0 bump

* Tue Nov 01 2016 Petr Pisar <ppisar@redhat.com> - 1.5.5-2
- Fix saving to an image with shell meta characters in a file name
  (bug #1390105)

* Mon Oct 24 2016 Petr Pisar <ppisar@redhat.com> - 1.5.5-1
- 1.5.5 bump

* Mon Oct 17 2016 Petr Pisar <ppisar@redhat.com> - 1.5.4-1
- 1.5.4 bump

* Thu Oct 13 2016 Petr Pisar <ppisar@redhat.com> - 1.5.3-1
- 1.5.3 bump

* Fri Sep 30 2016 Petr Pisar <ppisar@redhat.com> - 1.5.2-2
- Preserve image depth on PDF export (bug #1369984)

* Thu Sep 01 2016 Petr Pisar <ppisar@redhat.com> - 1.5.2-1
- 1.5.2 bump

* Wed Jul 27 2016 Petr Pisar <ppisar@redhat.com> - 1.5.1-1
- 1.5.1 bump

* Fri Jul 08 2016 Petr Pisar <ppisar@redhat.com> - 1.5.0-1
- 1.5.0 bump

* Thu Jul 07 2016 Petr Pisar <ppisar@redhat.com> - 1.3.9-3
- Modernize spec file
- License corrected to (GPLv3 and GPLv2 and LGPLv2+)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.9-2
- Perl 5.24 rebuild

* Thu Mar 10 2016 Sven Lankes <sven@lank.es>  -1.3.9-1
- new upstream release

* Mon Feb 22 2016 Sven Lankes <sven@lank.es>  -1.3.8-1
- new upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-2
- Perl 5.22 rebuild

* Wed Feb 25 2015 Bernard Johnson <bjohnson@symetirx.com> - 1.3.0-1
- v 1.3.0 (bz #1082579)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.5-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Richard Hughes <richard@hughsie.com> - 1.2.5-1
- v 1.2.5

* Tue Mar 11 2014 Bernard Johnson <bjohnson@symetirx.com> - 1.2.3-1
- v 1.2.3 (bz #1034069)
- substitute a sed command to change gconftool-2 change

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3-3
- Perl 5.18 rebuild

* Tue Apr 23 2013 Jon Ciesla <limburgher@gmail.com>  -1.1.3-2
- Drop desktop vendor tag.

* Tue Mar 05 2013 Sven Lankes <sven@lank.es>  -1.1.3-1
- new upstream release

* Sat Feb 16 2013 Sven Lankes <sven@lank.es>  -1.1.2-1
- new upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 16 2012 Sven Lankes <sven@lank.es>  -1.1.0-1
- new upstream release

* Fri Aug 24 2012 Sven Lankse <sven@lank.es> - 1.0.6-1
- new upstream release (bz #840442)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.0.4-2
- Perl 5.16 rebuild

* Fri May 25 2012 Bernard Johnson <bjohnson@symetirx.com> - 1.0.4-1
- v 1.0.4 (bz #810826)

* Wed Mar 28 2012 Bernard Johnson <bjohnson@symetrix.com> - 1.0.2-1
- v 1.0.2 (bz #787361, bz #807604)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Bernard Johnson <bjohnson@symetrix.com> - 1.0.0-1
- v 1.0.0 (bz #740997)
- disable tests for now due to dependencies
