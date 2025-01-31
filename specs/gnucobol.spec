%define _lto_cflags %{nil}
%undefine _package_note_file

Name:           gnucobol
Version:        3.2
Release:        7%{?dist}
Summary:        COBOL compiler

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GFDL-1.3-only AND FSFAP AND GPL-2.0-or-later AND LGPL-3.0-or-later

URL:            https://www.gnu.org/software/gnucobol/
Source0:        https://ftp.gnu.org/gnu/gnucobol/gnucobol-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gnucobol/gnucobol-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source3:        https://www.itl.nist.gov/div897/ctg/suites/newcob.val.Z
Source4:        http://downloads.sourceforge.net/%{name}/contrib/esql/%{name}-sql-3.0.tar.gz

# https://sourceforge.net/p/gnucobol/bugs/941/
Patch0:         xml-parser.patch

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  readline-devel
BuildRequires:  libdb-devel
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  perl-interpreter
BuildRequires:  libxml2-devel
BuildRequires:  json-c-devel
BuildRequires: make
# esql
BuildRequires: unixODBC-devel
BuildRequires: gcc-c++

Requires:       gcc
Requires:       glibc-devel
Requires:       gmp-devel
Requires:       redhat-rpm-config
Requires:       libcob = %{version}

%description
COBOL compiler, which translates COBOL
programs to C code and compiles them using GCC.

%package -n libcob
Summary:        GnuCOBOL runtime library
License:        LGPL-3.0-or-later

%description -n libcob
%{summary}.
Runtime libraries for GnuCOBOL

%package esql
Summary:        ESQL for GnuCOBOL
License:        LGPL-3.0-or-later

%description esql
%{summary}.
ESQL for GnuCOBOL

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0
cp %{SOURCE3} tests/cobol85/

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure --enable-hardening --with-db --with-xml2 --with-curses=ncursesw --with-json=json-c

%make_build

iconv -c --to-code=UTF-8 ChangeLog > ChangeLog.new
mv ChangeLog.new ChangeLog

tar -xzf %{SOURCE4}
pushd gnucobol-sql-3.0/
%configure --enable-static=no
%make_build
popd

%install
%make_install
find %{buildroot}/%{_libdir} -type f -name "*.*a" -exec rm -f {} ';'
rm -rf %{buildroot}/%{_infodir}/dir

pushd gnucobol-sql-3.0/
%make_install
popd

%find_lang %{name}

%check
(make check CFLAGS="%optflags -O" || make check TESTSUITEFLAGS="--recheck --verbose" || echo "Warning, unexpected results")
make test CFLAGS="%optflags -O"

%files -f %%{name}.lang
%license COPYING.DOC COPYING
%doc AUTHORS ChangeLog
%doc NEWS README THANKS
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
%{_includedir}/*
%{_libdir}/%{name}
%{_libdir}/libcob.so
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info.*
%{_mandir}/man1/cobc.1.*
%{_mandir}/man1/cobcrun.1.*
%{_mandir}/man1/cob-config.1.*


%files -n libcob
%license COPYING.LESSER
%{_libdir}/libcob.so.4*
%{_libdir}/gnucobol/CBL_OC_DUMP.so

%files esql
%{_bindir}/esqlOC
%{_libdir}/libocsql.so*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.2-5
- Patch for implicit function declaration

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.2-2
- Include esql 3.0

* Fri Jul 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.2-1
- 3.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-10
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-8
- Rebuild for link issue, disable package note.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-6
- Rebuild to fix linker issue.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 3.1.2-3
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-1
- 3.1.2

* Thu Dec 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-3
- Require redhat-rpm-config.

* Wed Dec 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-2
- Conditionalize json-c for EL-7.

* Wed Dec 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-1
- 3.1.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7.rc1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-7.rc1
- Re-add libxml2, specify optional flags.

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-6.rc1
- License, BuildRequire tweaks.

* Fri Jul 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-5.rc1
- Enable ppc64le, NIST tests.

* Thu Jul 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-4.rc1
- 3.1 rc1

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-3
- Review fixes.

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-2
- Review fixes.

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-1
- 3.1 nightly.

* Mon Apr 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0-0.rc1.1
- Initial release, adapted from open-cobol spec.
