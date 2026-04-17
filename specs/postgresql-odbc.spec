%bcond_without check

%global upstream_name psqlodbc

Name: postgresql-odbc
Summary: PostgreSQL ODBC driver
Version: 16.00.0000
Release: 9%{?dist}
License: LGPL-2.0-or-later
URL: https://odbc.postgresql.org/

Source0: https://ftp.postgresql.org/pub/odbc/versions/src/%{upstream_name}-%{version}.tar.gz

Patch0: postgresql-odbc-09.06.0200-revert-money-fix.patch
Patch1: postgresql-odbc-09.05.0400-revert-money-testsuite-fix.patch
Patch2: postgresql-odbc-endianity-test-fix.patch

BuildRequires: make
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
%autosetup -p1 -n %{upstream_name}-%{version}

cat <<EOF >README.rpmdist
The upstream psqlodbc testsuite is distributed in '%{name}-tests'
(sub)package.
EOF

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure --with-unixodbc --disable-dependency-tracking --libdir=%{_libdir}/odbc
# GCC 10 defaults to -fno-common
# https://gcc.gnu.org/gcc-10/changes.html (see C section)
%make_build CFLAGS="%{optflags} -fcommon -std=gnu17"


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

%if %{with check}
%check
%postgresql_tests_run

# make sure that we are testing aginst expected output "utf8" case
mv test/expected/wchar-char_1.out test/expected/wchar-char.out
rm -rf test/expected/wchar-char_2.out
rm -rf test/expected/wchar-char_3.out

cd test && make installcheck %{_smp_mflags} CFLAGS="%{optflags} -fcommon -std=gnu17" || {
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


%files tests
%doc license.txt
%dir %{testsuitedir}
%defattr(-,postgres,postgres)
%{testsuitedir}/test


%changelog
%autochangelog
