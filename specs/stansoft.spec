Name:           stansoft
Version:        11.0
Release:        1%{?dist}
Summary:        Standard Accounting Software

License:        AGPL-3.0-or-later
URL:            https://www.stansoft.org
Source0:        https://download.stansoft.org/files/%{name}-%{version}.tar.bz2
# Filter false-positive rpmlint errors and warnings
# explicit-lib-dependency libpq
#   false-positive on anything with lib in the package name
#   See https://bugzilla.redhat.com/show_bug.cgi?id=790869
# non-standard-uid, non-standard-gid /var/lib/stansoft
#   User stansoft owns the PostgreSQL database so must own this directory
Source1:        https://download.stansoft.org/files/%{name}.rpmlintrc

# Only build on the required primary architectures.
# https://fedoraproject.org/wiki/Architectures#Structure
ExclusiveArch:  x86_64 aarch64

BuildRequires:  aubit4gl-devel
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
BuildRequires:  systemd-rpm-macros

Requires:       aubit4gl
# rpmlint gives false-positive explicit-lib-dependency libpq, needed at runtime
Requires:       libpq
Requires:       postgresql-server

Provides:  user(%{name})
Provides:  group(%{name})


%description
Stansoft is a comprehensive double-entry financial accounting system.
It includes payroll for both the U.S. and UK. It is HMRC-recognised
for UK PAYE RTI payroll and MTD VAT returns.


%prep
%autosetup


%build
%if "%{getenv:AUBITDIR}" == ""
export AUBITDIR=%{_libdir}/aubit4gl
%endif

%configure
# The database must exist to compile so create it
%make_build createdb
# It does not compile with multiple threads
%make_build -j1
# Stop the database engine
%make_build stopdb


%install
rm -rf %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%make_install

# Install the libraries into the system library directory
# Do not include unversioned libraries in non-devel package
cp -d %{buildroot}%{_libdir}/%{name}/lib/lib%{name}.so.* %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_libdir}/%{name}/lib

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
# Create a link to the startup script since it references the install dir
ln -sf ../..%{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

# Fixup the path in the systemd file
sed -i 's:/opt:%{_libdir}:g' %{buildroot}%{_libdir}/%{name}/etc/%{name}.service

# Move the systemd file into place
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_libdir}/%{name}/etc/%{name}.service %{buildroot}%{_unitdir}

# Create the database directory
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

# Fixup the environment file with the correct path to the data directory
sed -i 's:$SSDIR/data:%{_sharedstatedir}/%{name}/data:g' %{buildroot}%{_libdir}/%{name}/etc/postgres.sh 

# Do not let the Stansoft install script change ownership or permissions
sed -i 's/\(chmod 775 "\$ssdir"\)/#\1/;
        s/\(chown -R stansoft:stansoft "\$ssdir"\)/#\1/' \
        %{buildroot}%{_libdir}/%{name}/installss

# docs are installed in the system location
rm -f %{buildroot}%{_libdir}/%{name}/README
rm -f %{buildroot}%{_libdir}/%{name}/changelog
rm -f %{buildroot}%{_libdir}/%{name}/COPYING
# Not including the pdf manual or fedora-review complains about size
# The man page has a web link to the manual
rm -rf %{buildroot}%{_libdir}/%{name}/doc


%pre
getent group %{name} >/dev/null || groupadd -f %{name} >/dev/null 2>&1 || :
getent passwd %{name} >/dev/null || useradd -g %{name} -m \
       -s /bin/bash %{name} >/dev/null 2>&1 || exit 0


%post
%systemd_post %{name}.service
semanage fcontext -a -t postgresql_db_t '%{_sharedstatedir}/%{name}(/.*)?'
restorecon %{_sharedstatedir}/%{name}


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service
semanage fcontext -d -t postgresql_db_t '%{_sharedstatedir}/%{name}(/.*)?'


%check
make check


%files
%license COPYING
%doc README changelog doc/USERDOC doc/PASSPORT doc/INFORMIX doc/FAQ
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}
%dir %{_libdir}/%{name}/bin
%{_libdir}/%{name}/bin/*
%dir %{_libdir}/%{name}/etc
%{_libdir}/%{name}/etc/*
%{_libdir}/%{name}/installss
%dir %{_libdir}/%{name}/newdb
%{_libdir}/%{name}/newdb/*
%dir %{_libdir}/%{name}/pytax
%{_libdir}/%{name}/pytax/*
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1*
%attr(700,%{name},%{name}) %{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service


%changelog
* Thu Jan 22 2026 Chad Lemmen <rpm@stansoft.org> - 11.0-1
- initial Fedora RPM packaging

