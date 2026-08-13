%bcond   gui_related_parts 1

Name:    unixODBC
Version: 2.3.14
Release: %{autorelease}

# See README: Programs are GPL, libraries are LGPL
# News Server library (Drivers/nn/yyparse.c) is GPLv3+
# (but that one is not compiled nor shipped)
License: GPL-2.0-or-later AND LGPL-2.1-or-later

Summary: A complete ODBC driver manager for Linux
URL:     http://www.unixODBC.org/

Source:  http://www.unixODBC.org/%{name}-%{version}.tar.gz
Source2: odbcinst-generate
Source3: odbcinst-generate.1

Patch8:  so-version-bump.patch

BuildRequires: make automake autoconf libtool libtool-ltdl-devel bison flex
BuildRequires: readline-devel
%{!?rhel:BuildRequires: multilib-rpm-config}

# ODBC driver packages
Suggests: freetds
Suggests: mariadb-connector-odbc
Suggests: mdbtools-odbc
Suggests: mysql-connector-odbc
Suggests: postgresql-odbc
Suggests: sqliteodbc

# GUI management tool
Suggests: unixODBC-gui-qt

Requires: odbcinst-generate = %{version}-%{release}

%description
Install unixODBC if you want to access databases through ODBC.
You will also need the mariadb-connector-odbc package if you want to access
a MySQL or MariaDB database, and/or the postgresql-odbc package for PostgreSQL.

%package -n odbcinst-generate
Summary: Drop-in snippet generator for ODBC driver registration
BuildArch: noarch
Requires(post): coreutils

%description -n odbcinst-generate
Assembles /etc/odbcinst.ini from per-driver drop-in snippets shipped by
ODBC driver packages.  Used by both unixODBC and iODBC driver managers.

%package devel
Summary: Development files for programs which will use the unixODBC library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The unixODBC package can be used to access databases through ODBC
drivers. If you want to develop programs that will access data through
ODBC, you need to install this package.


%prep
%setup -q
%patch -P8 -p1 -b .soname-bump

autoreconf -vfi

%build
%configure \
  --with-gnu-ld=yes \
  --enable-threads=yes \
  --enable-fastvalidate \
  --enable-drivers=no \
  --with-odbc-driver-path=%{_libdir}/odbc \
%if %{with gui_related_parts}
  --enable-driver-config=yes
%else
  --enable-driver-config=no
%endif

# Get rid of the rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install

# Drop-in directory infrastructure for ODBC driver registration
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/odbc/odbcinst.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/odbc/odbcinst.d
install -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/odbcinst-generate
install -m644 -D %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1/odbcinst-generate.1

# Create %ghost file so RPM tracks ownership of the generated config
touch $RPM_BUILD_ROOT%{_sysconfdir}/odbcinst.ini

%if %{undefined rhel}
%multilib_fix_c_header --file %{_includedir}/unixODBC/unixodbc_conf.h
%multilib_fix_c_header --file %{_includedir}/unixodbc.h
%endif

# Directory for ODBC connector/driver plugins
mkdir -p $RPM_BUILD_ROOT%{_libdir}/odbc

# copy text driver documentation into main doc directory
# currently disabled because upstream no longer includes text driver
# mkdir -p doc/Drivers/txt
# cp -pr Drivers/txt/doc/* doc/Drivers/txt

# don't want to install doc Makefiles as docs
find doc -name 'Makefile*' | xargs rm

# we do not want to ship static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libltdl.*
rm -rf $RPM_BUILD_ROOT%{_datadir}/libtool

# initialize lists of .so files
find $RPM_BUILD_ROOT%{_libdir} -name "*.so.*" | sed "s|^$RPM_BUILD_ROOT||" > base-so-list
find $RPM_BUILD_ROOT%{_libdir} -name "*.so"   | sed "s|^$RPM_BUILD_ROOT||" > devel-so-list


%files -f base-so-list
%license COPYING
%doc README AUTHORS ChangeLog
%if %{with gui_related_parts}
%doc doc
%endif

%config(noreplace) %{_sysconfdir}/odbc.ini

%{_bindir}/odbcinst
%{_bindir}/isql
%{_bindir}/dltest
%{_bindir}/iusql
%{_bindir}/odbc_config
%{_bindir}/slencheck
%{_mandir}/man*/*
%exclude %{_mandir}/man1/odbcinst-generate.1*
# ODBC connector/driver plugins are placed here
%dir %{_libdir}/odbc

# Save user-modified odbcinst.ini before the %ghost transition removes it.
# RPM does not create .rpmsave when a file changes from %config to %ghost.
# Only run on first upgrade: skip if the drop-in directory already exists.
#
# To avoid nagging users who never customized the file, we parse it for
# INI section headers: if every [Section] matches a driver shipped by Fedora,
# the file is stock and needs no backup.  Any unknown section means the user
# added a custom driver, so we preserve the file as .rpmsave.
%pretrans -p <lua>
local dropin = "/usr/lib/odbc/odbcinst.d"
if posix.stat(dropin) then
  return
end
local path = "/etc/odbcinst.ini"
if not posix.stat(path) then
  return
end
-- Drivers historically shipped by Fedora / RHEL in odbcinst.ini
local known = {
  PostgreSQL = true,
  MySQL = true,
  ["MySQL-5"] = true,
  FreeTDS = true,
  MariaDB = true,
  MDBTools = true,
  SQLITE = true,
  SQLITE3 = true,
}
local custom = false
local f = io.open(path, "r")
if f then
  for line in f:lines() do
    -- Strip leading whitespace without Lua patterns (the "%%"
    -- escape needed for Lua character classes conflicts with RPM
    -- macro syntax in spec files, so we avoid patterns entirely).
    local s = line
    while s:sub(1,1) == " " or s:sub(1,1) == "\t" do
      s = s:sub(2)
    end
    if s:sub(1,1) == "[" then
      local close = s:find("]", 2, true)
      if close and close > 2 then
        local sect = s:sub(2, close - 1)
        if not known[sect] then
          custom = true
          break
        end
      end
    end
  end
  f:close()
end
-- Only save the file when it contains user-added driver sections
if custom then
  local save = path .. ".rpmsave"
  if not posix.stat(save) then
    os.rename(path, save)
  end
end

%post
if [ -f %{_sysconfdir}/odbcinst.ini.rpmsave ]; then
  echo "NOTE: Your previous %{_sysconfdir}/odbcinst.ini was saved as" >&2
  echo "%{_sysconfdir}/odbcinst.ini.rpmsave" >&2
  echo "Driver registration is now handled by drop-in snippets." >&2
  echo "To preserve custom drivers, copy their [sections] into files" >&2
  echo "under %{_sysconfdir}/odbc/odbcinst.d/ and run:" >&2
  echo "  odbcinst-generate" >&2
fi


%files -n odbcinst-generate
%license exe/COPYING
%{_bindir}/odbcinst-generate
%{_mandir}/man1/odbcinst-generate.1*
%ghost %{_sysconfdir}/odbcinst.ini
%dir %{_prefix}/lib/odbc
%dir %{_prefix}/lib/odbc/odbcinst.d
%dir %{_sysconfdir}/odbc
%dir %{_sysconfdir}/odbc/odbcinst.d

%post -n odbcinst-generate
odbcinst-generate || :

# Regenerate odbcinst.ini when driver packages install drop-in snippets
%transfiletriggerin -n odbcinst-generate -- %{_prefix}/lib/odbc/odbcinst.d %{_sysconfdir}/odbc/odbcinst.d
odbcinst-generate || :

# Regenerate after driver packages are removed
%transfiletriggerpostun -n odbcinst-generate -- %{_prefix}/lib/odbc/odbcinst.d %{_sysconfdir}/odbc/odbcinst.d
odbcinst-generate || :


%files devel -f devel-so-list
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
