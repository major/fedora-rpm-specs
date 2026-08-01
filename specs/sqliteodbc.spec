Name:		sqliteodbc
Version:	0.99991
Release:	11%{?dist}
Summary:	SQLite ODBC Driver

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.ch-werner.de/sqliteodbc
Source:		http://www.ch-werner.de/sqliteodbc/%{name}-%{version}.tar.gz
Source1:	10-sqlite.ini
Patch0:		sqliteodbc-0.99991-Fix-too-many-args-to-gpps-compilation-error.patch
Patch1:		sqliteodbc-0.99991-Fix-incompatible-pointer-compilation-error.patch

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	libxml2-devel
BuildRequires:	sqlite-devel
BuildRequires:	sqlite2-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/iconv



%description
ODBC driver for SQLite interfacing SQLite 2.x and/or 3.x using the
unixODBC or iODBC driver managers. For more information refer to:
- http://www.sqlite.org    -  SQLite engine
- http://www.unixodbc.org  -  unixODBC Driver Manager
- http://www.iodbc.org     -  iODBC Driver Manager


%prep
%autosetup -p1
# correct EOL
for i in README; do
	sed 's#\r##g' $i > $i.tmp && \
	touch -r $i $i.tmp && \
	mv $i.tmp $i
done

# Convert encoding to UTF-8
for i in ChangeLog; do
	iconv -f ISO-8859-1 -t UTF-8 -o $i.tmp $i && \
	touch -r $i $i.tmp && \
	mv $i.tmp $i
done


%build
%configure --with-odbc=$(pkg-config --variable=prefix odbc)
make %{_smp_mflags}


%install
mkdir -p %{buildroot}%{_libdir}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libsqliteodbc*.{a,la}
rm -f %{buildroot}%{_libdir}/libsqlite3odbc*.{a,la}
rm -f %{buildroot}%{_libdir}/libsqlite3_mod_*.{a,la}
# Move ODBC driver plugins to a dedicated subdirectory (rhbz#2453060)
mkdir -p %{buildroot}%{_libdir}/odbc
mv %{buildroot}%{_libdir}/libsqliteodbc*.so* %{buildroot}%{_libdir}/odbc/
mv %{buildroot}%{_libdir}/libsqlite3odbc*.so* %{buildroot}%{_libdir}/odbc/
# install example file
cat > odbc.ini.sample <<- 'EOD'
	# ~/.odbc.ini example file
	[mysqlitedb]
	Description=My SQLite3 test database
	Driver=SQLite3
	Database=/home/user_name/Documents/databases/testdb.sqlite
	# optional lock timeout in milliseconds
	# Timeout=2000
	# StepAPI = No|Yes
	# ShortNames = No|Yes
	# FKSupport = No|Yes
	# SyncPragma = NORMAL|OFF|FULL
	# JournalMode = WAL|MEMORY|TRUNCATE|OFF|PERSIST|DELETE
	# BigInt = No|Yes
EOD

# ODBC driver registration drop-in snippet
mkdir -p %{buildroot}%{_prefix}/lib/odbc/odbcinst.d
install -m644 %{SOURCE1} %{buildroot}%{_prefix}/lib/odbc/odbcinst.d/


%files
%license license.terms
%doc README ChangeLog odbc.ini.sample
%dir %{_libdir}/odbc
%{_libdir}/odbc/libsqliteodbc*.so*
%{_libdir}/odbc/libsqlite3odbc*.so*
%{_libdir}/libsqlite3_mod_*.so*
%dir %{_prefix}/lib/odbc
%dir %{_prefix}/lib/odbc/odbcinst.d
%{_prefix}/lib/odbc/odbcinst.d/10-sqlite.ini


%changelog
* Mon Jul 20 2026 Michal Schorm <mschorm@redhat.com> - 0.99991-11
- Ship drop-in snippet for ODBC driver self-registration

* Fri Jul 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.99991-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Mar 30 2026 Michal Schorm <mschorm@redhat.com> - 0.99991-9
- Move ODBC driver plugins to %%{_libdir}/odbc/ (rhbz#2453060)

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.99991-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99991-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu May 15 2025 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.99991-6
- Fix flatpak build

* Tue Jan 21 2025 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.99991-5
- Fix FTBFS on F42.

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99991-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.99991-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99991-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.99991-1
- Update to latest available version
- Drop sqliteodbc-configure-c99.patch

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Florian Weimer <fweimer@redhat.com> - 0.9996-13
- Port configure script to C99 (#2165021)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9996-6
- Fix CVE-2020-12050 (use mktemp(1) for temp. file name creation)
- Use absolute paths for binaries

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9996-1
- Update to the latest available version.

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9995-5
- Add missing BR (gcc)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9995-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9995-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9995-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9995-1
- Update to the latest available version.
- Start using %%license

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9994-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9994-1
- Update to the latest available version.

* Tue Sep 23 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.999-1
- Initial package.
