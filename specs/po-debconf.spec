
# Handle Debian +nmu<n> version suffixes
# As they are non-numeric we move them to the release part
# Per Fedora policy:
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/#_release_and_post_release_versions
%global	posttag	nmu1
%global	release_posttag %{?posttag:.%{posttag}}
%global	tarball_posttag %{?posttag:+%{posttag}}
%global	debian_fqn %{name}_%{version}%{tarball_posttag}

# Some self tests are failing. For now make it optional.
# To try it, simply run: mock --with=check
%bcond_with check

Name:		po-debconf
Version:	1.0.21
Release:	17%{release_posttag}%{?dist}
Summary:	Tool for managing templates file translations with gettext

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://tracker.debian.org/pkg/po-debconf
Source0:	https://ftp.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}%{tarball_posttag}.tar.xz

BuildArch:	noarch

BuildRequires:  make
BuildRequires:	po4a
BuildRequires:	dpkg-dev
BuildRequires:	/usr/bin/pod2html

# Needed for check
%if %{with check}
BuildRequires: perl-generators
BuildRequires: perl(Test)
BuildRequires: perl(Test::Harness)
BuildRequires: debconf
BuildRequires: intltool
%endif

Requires:	perl-interpreter
Requires:	intltool
Requires:	gettext

# Debian optional run-time features
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:	perl(Compress::Zlib)
Requires:	perl(Mail::Sendmail)
Requires:	perl(Mail::Box::Manager)
%else
Recommends:	perl(Compress::Zlib)
Recommends:	perl(Mail::Sendmail)
Recommends:	perl(Mail::Box::Manager)
%endif


%description
This package is an alternative to debconf-utils, and provides
tools for managing translated debconf templates files with
common gettext utilities.

%prep
%setup -q -n %{name}-%{version}%{tarball_posttag}

# Fix upstream
chmod -x COPYING


%build
%make_build


%install
mkdir -p \
	%{buildroot}/%{_bindir} \
	%{buildroot}/%{_datadir}/%{name}/

for prog in debconf-gettextize debconf-updatepo po2debconf podebconf-display-po podebconf-report-po; do
	install -pm 755 $prog %{buildroot}/%{_bindir}
done

# I don't know what to do with these
rm -rf doc/vi

for lang_man in `find doc/ -name "*.1" -exec dirname {} \; | sort -u`; do
	lang_id=$(basename $lang_man | sed -e 's/en//g')
	mkdir -p %{buildroot}/%{_mandir}/man1/
	mkdir -p "%{buildroot}/%{_mandir}/$lang_id/man1"
	for man in $lang_man/*.1; do
		dest_name=$(basename $man | sed -e "s/\.$lang_id\././")
		install -pm 644 "$man" "%{buildroot}/%{_mandir}/$lang_id/man1/$dest_name"
	done
done

install -pm 644 encodings %{buildroot}%{_datadir}/%{name}/
install -pm 644 pot-header %{buildroot}%{_datadir}/%{name}/
cp -a podebconf-report-po_templates/ %{buildroot}%{_datadir}/%{name}/templates
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1345764
# https://bugzilla.redhat.com/show_bug.cgi?id=591389#c18
ln -s ../bin %{buildroot}%{_datadir}/intltool-debian

%find_lang po-debconf --without-mo --with-man --all-name

%if %{with check}
%check
( cd ./tests && PODEBCONF_LIB=/usr/bin ./run.pl )
%endif

%files -f po-debconf.lang
%doc README README-trans
%license COPYING
%{_mandir}/man1/*.1*
%{_bindir}/debconf-gettextize
%{_bindir}/debconf-updatepo
%{_bindir}/po2debconf
%{_bindir}/podebconf-display-po
%{_bindir}/podebconf-report-po
%{_datadir}/%{name}
%{_datadir}/intltool-debian

%changelog
* Thu Dec 26 2024 Sérgio Basto <sergio@serjux.com> - 1.0.21-17.nmu1
- Revert BR to dpkg-dev, to avoid circular dependencies

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.21-16.nmu1
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-15.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-14.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-13.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-12.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-11.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-10.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Sérgio Basto <sergio@serjux.com> - 1.0.21-9.nmu1
- Mail::Box::Manager, Mail::Sendmail and Compress::Zlib is only needed for
  podebconf-report, if program needs the perl module and it is not installed,
  it will send a warning, so these perl modules are optional.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-8.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-7.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 16 2021 Sérgio Basto <sergio@serjux.com> - 1.0.21-6.nmu1
- Update to 1.0.21+nmu1 (#1911559)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Sérgio Basto <sergio@serjux.com> - 1.0.21-2
- html2text is not needed

* Wed Oct 09 2019 Sérgio Basto <sergio@serjux.com> - 1.0.21-1
- Update to 1.0.21

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Sérgio Basto <sergio@serjux.com> - 1.0.20-5
- Add symlink to /usr/share/intltool-debian (#1345764)
- Add License macro

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.0.20-2
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Tue Feb 14 2017 Sérgio Basto <sergio@serjux.com> - 1.0.20-1
- Update po-debconf to 1.0.20 (#1296739)
- po-debconf-1.0.16-fix-prefix.patch is upstreamed.

* Tue Feb 14 2017 Sérgio Basto <sergio@serjux.com> - 1.0.16-9.nmu3
- Bump version

* Thu Jan 26 2017 Sérgio Basto <sergio@serjux.com> - 1.0.16-8.nmu3
- Update to 1.0.16+nmu3 (same version currently in Debian/stable)

* Mon Feb 15 2016 Oron Peled <oron@actcom.co.il> - 1.0.16-7.nmu2
- Fix FTBFS in rawhide - bug #1307868
- Fixed build dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-6.nmu2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-5.nmu2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-4.nmu2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Oron Peled <oron@actcom.co.il> - 1.0.16-3.nmu2
- Fixed build dependency
- Fix FTBFS in rawhide - bug #992741

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.16-2.nmu2
- Perl 5.18 rebuild

* Thu May  9 2013 Oron Peled <oron@actcom.co.il> - 1.0.16-1.nmu2
- Use same upstream version as Debian/wheezy
- Remove patch1 (no-utf8)
- Added more build-requires to enable features detected at build-time
- Preserve timestamps during installation (install -p)
- Prepare for 'check' -- some self-tests still fail

* Mon May 14 2012 Oron Peled <oron@actcom.co.il> - 1.0.16+nmu1-1
- Now debconf is in Fedora (#5913320). It provides the perl classes missing
  to install po-debconf.
- Installed translated man pages to correct names (without $LANG in the
  man-page name, only in the prefixing directory)
- Use find_lang for translated man-pages
- Don't specify exact compression scheme for (non-tranlated) man-pages
- Removed Build-Root (not needed for modern Fedora)

* Tue May 11 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.16-3
- Add requirement for html2text
- Add build requirement for debhelper
- First package
