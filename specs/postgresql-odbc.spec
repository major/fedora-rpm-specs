%bcond_without check

%global upstream_name psqlodbc
%global upstream_tag  REL-18_00_0006

Name: postgresql-odbc
Summary: PostgreSQL ODBC driver
Version: 18.00.0006
Release: 1%{?dist}
License: LGPL-2.0-or-later
URL: https://odbc.postgresql.org/

Source0: https://github.com/postgresql-interfaces/%{upstream_name}/archive/refs/tags/%{upstream_tag}.tar.gz
Source3: 10-postgresql.ini

Patch0: postgresql-odbc-09.06.0200-revert-money-fix.patch
Patch1: postgresql-odbc-09.05.0400-revert-money-testsuite-fix.patch
Patch2: postgresql-odbc-endianity-test-fix.patch

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires:  gcc
BuildRequires: unixODBC-devel
BuildRequires: pkgconfig(libpq)

%if %{with check}
BuildRequires: postgresql-test-rpm-macros
%endif

Provides: %upstream_name = %version-%release

# This spec file and ancillary files are licensed in accordance with
# the psqlodbc license.

%description
This package includes the driver needed for applications to access a
PostgreSQL system via ODBC (Open Database Connectivity).


%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_tag}
autoreconf -fi

cat <<EOF >README.rpmdist
The upstream psqlodbc testsuite is distributed in '%{name}-tests'
(sub)package.
EOF

%build
%configure --with-unixodbc --disable-dependency-tracking --libdir=%{_libdir}/odbc
%make_build


%install
%make_install

%global testsuitedir %{_libdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/%{testsuitedir}
cp -R test $RPM_BUILD_ROOT/%{testsuitedir}
sed -i 's~^drvr=.*~drvr=%{_libdir}/odbc/psqlodbc~' $RPM_BUILD_ROOT/%{testsuitedir}/test/odbcini-gen.sh

# Provide the old library name "psqlodbc.so" as a symlink,
# and remove the rather useless .la files
pushd ${RPM_BUILD_ROOT}%{_libdir}/odbc
	ln -s psqlodbcw.so psqlodbc.so
	rm psqlodbcw.la psqlodbca.la
popd

# ODBC driver registration drop-in snippet
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/odbc/odbcinst.d
install -m644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_prefix}/lib/odbc/odbcinst.d/

%if %{with check}
%check
%postgresql_tests_run

# make sure that we are testing aginst expected output "utf8" case
mv test/expected/wchar-char_1.out test/expected/wchar-char.out
rm -rf test/expected/wchar-char_2.out
rm -rf test/expected/wchar-char_3.out

cd test && make installcheck %{_smp_mflags} || {
	echo "=== trying to find all regression.diffs files in build directory ==="
	find -name regression.diffs | while read line; do
		cat "$line"
	done
	false
}
%endif



%package tests
Summary: Testsuite files for psqlodbc
Requires: postgresql-test
Requires: %{name} = %{version}-%{release}
# Those are requires to successful testsuite run
Requires: gcc make unixODBC-devel


%description tests
The postgresql-odbc-tests package contains files needed for various tests for
the PostgreSQL unixODBC driver.


%files
%dir %{_libdir}/odbc
%{_libdir}/odbc/psqlodbc.so
%{_libdir}/odbc/psqlodbca.so
%{_libdir}/odbc/psqlodbcw.so
%doc license.txt readme.txt docs/* README.rpmdist
%dir %{_prefix}/lib/odbc
%dir %{_prefix}/lib/odbc/odbcinst.d
%{_prefix}/lib/odbc/odbcinst.d/10-postgresql.ini


%files tests
%doc license.txt
%dir %{testsuitedir}
%defattr(-,postgres,postgres)
%{testsuitedir}/test


%changelog
* Tue Nov 17 2026 Michal Schorm <mschorm@redhat.com> - 18.00.0006-1
- Update to 18.00.0006
- Security fixes: 12 CVEs (CVE-2026-109448, CVE-2026-120057 through CVE-2026-120067)
- Source URL changed from ftp.postgresql.org to GitHub archive
- Added BuildRequires: autoconf, automake, libtool (GitHub tarballs lack pre-generated autotools files)
- Dropped '-fcommon' and '-std=gnu17' compiler flags — no longer needed

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 16.00.0000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

%autochangelog
