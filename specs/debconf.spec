%if 0%{?rhel} >= 10
    %bcond_with gnome
%else
    %bcond_without gnome
%endif


Name:           debconf
Version:        1.5.87
Release:        3%{?dist}
Summary:        Debian configuration management system

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://tracker.debian.org/pkg/debconf
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch

#Build-Depends: debhelper-compat (= 12), dh-exec, dh-python, po-debconf, po4a (>= 0.23)
#Build-Depends-Indep: perl (>= 5.10.0-16), python3 (>= 3.1.2-8), gettext (>= 0.13), libintl-perl
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  po4a >= 0.23
BuildRequires:  gettext >= 0.13
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

# Required in Debconf/Encoding.pm
# to test frontends : dpkg-reconfigure --frontend=kde tzdata
Requires:       perl(Text::Iconv)
Requires:       perl(Text::WrapI18N)
Requires:       perl(Text::CharWidth)
# Required in Debconf/Gettext.pm
Requires:       perl(Locale::gettext)

Obsoletes:      debconf-kde < 1.5.69-5

%description
Debconf is a configuration management system for Debian
packages. Packages use Debconf to ask questions when
they are installed.

%package gnome
Summary:       GNOME frontend for debconf
Requires:      %{name} = %{version}-%{release}

%description gnome
This package contains the GNOME frontend for debconf.

%package LDAP
Summary:       Experimental LDAP driver for debconf
Requires:      %{name} = %{version}-%{release}

%description LDAP
This package contains an experimental database driver to provide LDAP support
for debconf

%package doc
Summary:        Debconf documentation
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains lots of additional documentation for Debconf,
including the debconf user's guide, documentation about using
different backend databases via the /etc/debconf.conf file, and a
developer's guide to debconf.

%package i18n
Summary:        Full internationalization support for debconf
Requires:       %{name} = %{version}-%{release}

%description i18n
This package provides full internationalization for debconf,
including translations into all available languages, support
for using translated debconf templates, and support for
proper display of multibyte character sets.

%package utils
Summary:        This package contains some small utilities for debconf developers
Requires:       %{name} = %{version}-%{release}

%description utils
This package contains some small utilities for debconf developers.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python3 for debconf
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
This package contains the python3 for debconf.


%prep
%setup -q -n work


%build
%make_build


%install
make install-utils prefix=%{buildroot}
make install-i18n prefix=%{buildroot}
#make install-python3 prefix=%{buildroot}
install -d %{buildroot}%{python3_sitelib}
install -m 0644 debconf.py  %{buildroot}%{python3_sitelib}

make install-rest prefix=%{buildroot}

# Add /var/cache/debconf and initial contents
mkdir -p %{buildroot}/%{_var}/cache/%{name}
touch %{buildroot}/%{_var}/cache/%{name}/config.dat
touch %{buildroot}/%{_var}/cache/%{name}/passwords.dat
touch %{buildroot}/%{_var}/cache/%{name}/templates.dat

mkdir -p \
        %{buildroot}/%{perl_vendorlib} \
        %{buildroot}/%{_mandir}/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/de/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/fr/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/ru/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/pt_BR/man{1,3,8}

chmod 755 %{buildroot}/%{_datadir}/%{name}/confmodule*

# Base and i18n man pages
for man in \
        "debconf-apt-progress" \
        "debconf-communicate" \
        "debconf-copydb" \
        "debconf-escape" \
        "debconf-set-selections" \
        "debconf-show" \
        "debconf" \
        "dpkg-preconfigure" \
        "dpkg-reconfigure"; do

    for level in 1 8; do
        for lang in de fr pt_BR ru; do
            if test -f doc/man/gen/$man.$lang.$level; then
                short_lang=`echo "$lang" | sed 's/_.*//'`
                install -m 644 doc/man/gen/$man.$lang.$level %{buildroot}/%{_mandir}/$lang/man$level/$man.$level
                echo "%lang($short_lang) %{_mandir}/$lang/man$level/$man.$level*" >> "man-i18n.lang"
            fi
        done
        test -f doc/man/gen/$man.$level && \
            install -m 644 doc/man/gen/$man.$level %{buildroot}/%{_mandir}/man$level/$man.$level
    done
done

# Doc foo
for man in \
        "Debconf::Client::ConfModule" \
        "confmodule" \
        "debconf.conf" \
        "debconf-devel" \
        "debconf"; do

    for level in 3 5 7; do
        for lang in de fr pt_BR ru; do
            if test -f doc/man/$man.$lang.$level*; then
                short_lang=`echo "$lang" | sed 's/_.*//'`
                install -m 644 doc/man/$man.$lang.$level* %{buildroot}/%{_mandir}/$lang/man$level/$man.$level
                echo "%lang($short_lang) %{_mandir}/$lang/man$level/$man.$level*" >> "man-doc.lang"
            fi
        done
        test -f doc/man/$man.$level && \
            install -m 644 doc/man/$man.$level %{buildroot}/%{_mandir}/man$level/$man.$level
    done
done

# Utils man pages
for man in get-selections \
            getlang \
            loadtemplate \
            mergetemplate; do
    for lang in de fr pt_BR ru; do
        short_lang=`echo "$lang" | sed 's/_.*//'`
        if test -f doc/man/gen/debconf-$man.$lang.1; then
            install -m 644 doc/man/gen/debconf-$man.$lang.1 %{buildroot}/%{_mandir}/$lang/man1/debconf-$man.1
            echo "%lang($short_lang) %{_mandir}/$lang/man1/debconf-$man.1*" >> "man-utils.lang"
        fi
    done
    test -f doc/man/gen/debconf-$man.1 && \
        install -m 644 doc/man/gen/debconf-$man.1 %{buildroot}/%{_mandir}/man1/debconf-$man.1
done

%find_lang debconf

%files
%doc doc/README doc/EXAMPLES doc/CREDITS doc/README.translators doc/README.LDAP doc/TODO
%doc debian/changelog debian/README.Debian
%license debian/copyright
%config(noreplace) %{_sysconfdir}/debconf.conf
%{_bindir}/debconf
%{_bindir}/debconf-apt-progress
%{_bindir}/debconf-communicate
%{_bindir}/debconf-copydb
%{_bindir}/debconf-escape
%{_bindir}/debconf-set-selections
%{_bindir}/debconf-show
%{_sbindir}/dpkg-preconfigure
%{_sbindir}/dpkg-reconfigure
%{perl_vendorlib}/Debconf
%{perl_vendorlib}/Debian
%{_datadir}/%{name}
%{_mandir}/man1/debconf-apt-progress.1*
%{_mandir}/man1/debconf-communicate.1*
%{_mandir}/man1/debconf-copydb.1*
%{_mandir}/man1/debconf-escape.1*
%{_mandir}/man1/debconf-set-selections.1*
%{_mandir}/man1/debconf-show.1*
%{_mandir}/man1/debconf.1*
%{_mandir}/man8/dpkg-preconfigure.8*
%{_mandir}/man8/dpkg-reconfigure.8*
%{_datadir}/pixmaps/debian-logo.png
%{_var}/cache/%{name}
%exclude %{perl_vendorlib}/Debconf/Element/Gnome*
%exclude %{perl_vendorlib}/Debconf/FrontEnd/Gnome*
%exclude %{perl_vendorlib}/Debconf/DbDriver/LDAP.pm


%files LDAP
%doc doc/README.LDAP
%{perl_vendorlib}/Debconf/DbDriver/LDAP.pm


%if %{with gnome}
%files gnome
%{perl_vendorlib}/Debconf/Element/Gnome*
%{perl_vendorlib}/Debconf/FrontEnd/Gnome*
%endif


%files doc -f man-doc.lang
%doc samples/
%license debian/copyright
%doc doc/debconf.schema
%doc doc/hierarchy.txt
%doc doc/namespace.txt
%doc doc/passthrough.txt
%{_mandir}/man3/confmodule.3*
%{_mandir}/man5/debconf.conf.5*
%{_mandir}/man7/debconf-devel.7*
%{_mandir}/man7/debconf.7*


%files i18n -f man-i18n.lang -f debconf.lang
%doc debian/changelog debian/copyright debian/README.Debian


%files utils -f man-utils.lang
%doc debian/changelog debian/copyright debian/README.Debian
%{_bindir}/debconf-get-selections
%{_bindir}/debconf-getlang
%{_bindir}/debconf-loadtemplate
%{_bindir}/debconf-mergetemplate
%{_mandir}/man1/debconf-get-selections.1*
%{_mandir}/man1/debconf-getlang.1*
%{_mandir}/man1/debconf-loadtemplate.1*
%{_mandir}/man1/debconf-mergetemplate.1*

%files -n python%{python3_pkgversion}-%{name}
%{python3_sitelib}/debconf.py
%{python3_sitelib}/__pycache__/debconf.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Sérgio Basto <sergio@serjux.com> - 1.5.87-2
- Drop debconf-gnome on epel 10 because we don't have perl-GTK3 package
  and I don't know if we'll ever have or want have it (perl-GTK3 on epel 10)

* Sat Sep 07 2024 Packit <hello@packit.dev> - 1.5.87-1
- Update to version 1.5.87
- Resolves: rhbz#2296312

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.86-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.86-2
- Rebuilt for Python 3.13

* Mon May 06 2024 Packit <hello@packit.dev> - 1.5.86-1
- Update to version 1.5.86
- Resolves: rhbz#2255752

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.82-2
- Rebuilt for Python 3.12

* Mon Mar 27 2023 Sérgio Basto <sergio@serjux.com> - 1.5.82-1
- Update debconf to 1.5.82 (#2148805)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.79-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.79-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.79-4
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.79-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Sérgio Basto <sergio@serjux.com> - 1.5.79-1
- Update debconf to 1.5.79 (#2016839)

* Fri Aug 13 2021 Sérgio Basto <sergio@serjux.com> - 1.5.77-1
- Update debconf to 1.5.77 (#1970631)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.76-3
- Rebuilt for Python 3.10

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.76-2
- Perl 5.34 rebuild

* Sat Mar 20 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.5.76-1
- Update to 1.5.76 (#1941164)

* Sun Mar 07 2021 Sérgio Basto <sergio@serjux.com> - 1.5.75-1
- Update to 1.5.75 (#1933511)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.74-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.74-5
- Perl 5.32 rebuild

* Sat Jun 06 2020 Sérgio Basto <sergio@serjux.com> - 1.5.74-4
- Add sub-package LDAP driver to avoid the big number of dependencies of
  perl-LDAP
- Drop BRs perl-libintl-perl, debhelper and po-debconf

* Wed Jun 03 2020 Sérgio Basto <sergio@serjux.com> - 1.5.74-3
- Re-add sub-package gnome to avoid the big number of dependencies of perl-GTK3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.74-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Sérgio Basto <sergio@serjux.com> - 1.5.74-1
- Update to 1.5.74

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Sérgio Basto <sergio@serjux.com> - 1.5.73-2
- Fix typo on commit 77cbe078

* Tue Oct 08 2019 Sérgio Basto <sergio@serjux.com> - 1.5.73-1
- Update to 1.5.73

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.69-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.69-7
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.69-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.69-5
- Perl 5.30 rebuild

* Tue May 28 2019 Sérgio Basto <sergio@serjux.com>
- Obsoletes debconf-kde and debconf-gnome sub-packages

* Mon May 27 2019 Petr Pisar <ppisar@redhat.com> - 1.5.69-4
- Remove an unused build dependency on perl-Qt-devel (bug #1676813)
- Require Perl ABI by all packages that install module into standard paths

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com>
- Rebuilt to change main python from 3.4 to 3.6

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.69-2
- Subpackage python2-debconf has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Sep 17 2018 Sérgio Basto <sergio@serjux.com> - 1.5.69-1
- Update to 1.5.69 (#1504325)
- Provide Python2 and Python3 sub packages (#1531598)
- Fix FTBFS (#1603758)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.63-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Sérgio Basto <sergio@serjux.com> - 1.5.63-1
- Update to 1.5.63 (#1453021)

* Wed Aug 16 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.60-5
- Add a build-time dependency on python2-devel

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.60-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Sérgio Basto <sergio@serjux.com> - 1.5.60-1
- Update debconf to 1.5.60

* Thu Jan 26 2017 Sérgio Basto <sergio@serjux.com> - 1.5.59-1
- Update debconf to 1.5.59

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.56-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.56-5
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.56-2
- Perl 5.22 rebuild

* Fri May 01 2015 Sérgio Basto <sergio@serjux.com> - 1.5.56-1
- Update to 1.5.56 , version of Debian 8 stable .

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.53-2
- Perl 5.20 rebuild

* Mon Jul 28 2014 Sérgio Basto <sergio@serjux.com> - 1.5.53-1
- Update to 1.5.53 (same version currently in Debian/testing)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Oron Peled <oron@actcom.co.il> - 1.5.52-1
- Update to 1.5.52 (same version currently in Debian/testing)

* Thu Oct 10 2013 Sandro Mani <manisandro@gmail.com> - 1.5.51-1
- Update to 1.5.51
- Drop upstreamed patches
- Split off gnome and kde frontends to subpackages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.5.49-4
- Perl 5.18 rebuild

* Sun Jun 09 2013 Oron Peled <oron@actcom.co.il> - 1.5.49-3
- Added missing /var/cache/debconf and initial contents

* Mon Jun 03 2013 Sérgio Basto <sergio@serjux.com> - 1.5.49-2
- Source rpms will have last 2 commits, which document better our patches.

* Wed Apr  3 2013 Oron Peled <oron@actcom.co.il> - 1.5.49-1
- Bump to version used by Debian/wheezy
- Fix 'find ... -perm' in Makefile to modern format. The deprecated
  format (+100) caused problems with find version >= 4.5.11
- Split 'make install' as is done in debian/rules for consistency

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.5.42-6
- Perl 5.16 rebuild

* Sun May 13 2012 Oron Peled <oron@actcom.co.il> - 1.5.42-5
- Bump release to match f17, f16 builds

* Sat May 12 2012 Oron Peled <oron@actcom.co.il> - 1.5.42-4
- Fix find_lang for man-pages. It is not smart enough to do
  it all in one swoop. So we generate the expected results
  manually (during installation)
- Fix exclude of python3 (picked wrong directory on x86-64

* Tue May  1 2012 Oron Peled <oron@actcom.co.il> - 1.5.42-3
- Added --with-man and --all-name to find_lang
- Use wild-cards for language directories of man-pages 

* Thu Apr 12 2012 Oron Peled <oron@actcom.co.il> - 1.5.42-2
- Added find_lang stuff
- Don't specify man-pages compression
- Added BR python
- Added BR perl-Qt (for KDE frontend)

* Mon Mar 26 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.5.42-1
- New upstream version

* Tue Sep  7 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.5.32-4
- Fix available python interpreters (4)
- Fix %%install (4)
- Fix build requirements (3)
- Include doc, i18n and utils packages (2)
- First package (1)
