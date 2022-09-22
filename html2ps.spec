# Enable ImageMagick for converting images other than EPS and XBM
%if 0%{?rhel}
%bcond_with html2ps_enables_ImageMagick
%else
%bcond_without html2ps_enables_ImageMagick
%endif
# Otherwise handle JPEG images with djpeg
%bcond_without html2ps_enables_djpeg
# Otherwise handle images with netpbm
%bcond_without html2ps_enables_netpbm

%define my_subversion b7
Name:           html2ps
Version:        1.0
Release:        0.44.%{my_subversion}%{?dist}
Summary:        HTML to PostScript converter
License:        GPLv2+
URL:            http://user.it.uu.se/~jan/%{name}.html
Source0:        http://user.it.uu.se/~jan/%{name}-1.0%{my_subversion}.tar.gz
Source1:        xhtml2ps.desktop
Patch0:         http://ftp.de.debian.org/debian/pool/main/h/%{name}/%{name}_1.0b5-5.diff.gz
# use xdg-open in xhtml2ps
Patch1:         %{name}-1.0b5-xdg-open.patch
# patch config file from debian to use dvips, avoid using weblint 
# don't set letter as default page type, paperconf will set the default
Patch2:         %{name}-1.0b5-config.patch
# Remove deprecated variable, bug #822117
Patch3:         %{name}-1.0b7-Remove-deprecated-variable.patch
# Fix Perl 5.22 warnings, bug #1404275
Patch4:         html2ps-1.0b7-Fix-perl-5.22-warnings.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
Requires:       ghostscript
# Depend on paperconf directly (instead of libpaper package) for rpmlint sake
Requires:       %{_bindir}/paperconf
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
Requires:       tex(dvips)
Requires:       tex(tex)

# Remove ImageMagick dependency if the feature is disabled
%if %{without html2ps_enables_ImageMagick}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Image::Magick\\)
%if %{with html2ps_enables_djpeg}
# libjpeg-turbo-utils for djpeg
Requires:       libjpeg-turbo-utils
%endif
%if %{with html2ps_enables_netpbm}
Requires:       netpbm-progs
%endif
%endif

%description
An HTML to PostScript converter written in Perl.
* Many possibilities to control the appearance. 
* Support for processing multiple documents.
* A table of contents can be generated.
* Configurable page headers/footers.
* Automatic hyphenation and text justification can be selected. 


%package -n xhtml2ps
Summary:     GUI front-end for html2ps
Requires:    html2ps = %{version}-%{release}
Requires:    xdg-utils

%description -n xhtml2ps
X-html2ps is freely-available GUI front-end for html2ps, a HTML-to-PostScript
converter.


%prep
%setup -q -n %{name}-1.0%{my_subversion}
%patch0 -p1
%patch1 -p1 -b .xdg-open
%patch2 -p1 -b .config
%patch3 -p1 -b .deprecated

# convert README to utf8
iconv -f latin1 -t utf8 < README > README.utf8
touch -c -r README README.utf8
mv README.utf8 README

patch -p1 < debian/patches/01_manpages.dpatch
# 03_html2ps.dpatch is against 1.0b5, adjust it to 1.0b6
< debian/patches/03_html2ps.dpatch sed -e 's|/opt/misc/|/it/sw/share/www/|' | \
    patch -p1

%patch4 -p1

%build
# Change default configuration
sed -i \
    -e 's/ImageMagick: [01]/ImageMagick: %{with html2ps_enables_ImageMagick}/' \
    -e 's/PerlMagick: [01]/PerlMagick: %{with html2ps_enables_ImageMagick}/' \
    debian/config/html2psrc
%if %{without html2ps_enables_ImageMagick}
sed -i \
    -e '/package {/ a \ \ \ \ djpeg: %{with html2ps_enables_djpeg};' \
    -e '/package {/ a \ \ \ \ netpbm: %{with html2ps_enables_netpbm};' \
    debian/config/html2psrc
%endif


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5}

sed -e 's;/etc/html2psrc;%{_sysconfdir}/html2psrc;' \
    -e 's;/usr/share/doc/html2ps;%{_pkgdocdir};' \
        html2ps > $RPM_BUILD_ROOT%{_bindir}/html2ps
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/html2ps
install -p -m0644 html2ps.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m0644 html2psrc.5 $RPM_BUILD_ROOT%{_mandir}/man5
sed -e 's;/usr/bin;%{_bindir};' \
    -e 's;/usr/share/texmf-texlive;%{_datadir}/texmf;' \
    debian/config/html2psrc > $RPM_BUILD_ROOT%{_sysconfdir}/html2psrc

install -m0755 -p contrib/xhtml2ps/xhtml2ps $RPM_BUILD_ROOT%{_bindir}
desktop-file-install \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE1}


%files
%license COPYING
%doc README sample html2ps.html
%config(noreplace) %{_sysconfdir}/html2psrc
%{_bindir}/html2ps
%{_mandir}/man1/html2ps.1*
%{_mandir}/man5/html2psrc.5*

%files -n xhtml2ps
%license contrib/xhtml2ps/LICENSE
%doc contrib/xhtml2ps/README
%{_bindir}/xhtml2ps
%{_datadir}/applications/*xhtml2ps.desktop

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.44.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.43.b7
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.42.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.41.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.40.b7
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.39.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.38.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.37.b7
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.36.b7
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.35.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.34.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.33.b7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.32.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.31.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.30.b7
- Perl 5.28 rebuild

* Tue Apr 10 2018 Petr Pisar <ppisar@redhat.com> - 1.0-0.29.b7
- Disable ImageMagick on RHEL (bug #1564998)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.28.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Petr Pisar <ppisar@redhat.com> - 1.0-0.27.b7
- Remove deprecated Encoding entry from xhtml2ps desktop file

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.26.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.25.b7
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.24.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Petr Pisar <ppisar@redhat.com> - 1.0-0.23.b7
- Fix Perl 5.22 warnings (bug #1404275)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.22.b7
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.20.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.19.b7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-0.18.b7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.17.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Petr Pisar <ppisar@redhat.com> - 1.0-0.16.b7
- Documentation directory is unversioned now (bug #993842)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0-0.14.b7
- Perl 5.18 rebuild

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 1.0-0.13.b7
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.12.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.0-0.10.b7
- Perl 5.16 rebuild

* Wed May 16 2012 Petr Pisar <ppisar@redhat.com> - 1.0-0.9.b7
- Remove deprecated variable (bug #822117)
- Clean spec file
- Insert dependency on perl

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May  7 2010 Petr Pisar <ppisar@redhat.com> - 1.0-0.6.b7
- 1.0b7 bump
- Increase revision to 0.6 to have NVR upper then F-13 package

* Thu Apr 29 2010 Petr Pisar <ppisar@redhat.com> - 1.0-0.1.b6
- 1.0b6 bump (CVE-2009-5067, bug #530403)
- Fix regression from upstream 1.0b5..1.0b6
- Fix spelling
- Default attributes for xhtml2ps %%files
- Replace libpaper dependency with paperconf binary to make rpmlint happy

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr 18 2008 Patrice Dumas <pertusus@free.fr> 1.0-0.1.b5
- initial release
